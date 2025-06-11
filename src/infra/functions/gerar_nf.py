import datetime
from io import StringIO
from typing import Literal

from dateutil.relativedelta import relativedelta
from loguru import logger
from sqlalchemy.orm import Session

from src.infra.entities import NotaFiscal, ParamDecred, LogNf, TblDirf
from src.infra.functions.structures.__gera_nf import __get_selected_param_decred__, __get_impostos_pct__, \
    __get_tbl_dirf__, __calc_impostos__
from src.utils import log_func, LogBufferHandler


@log_func
def gerar_nf(session: Session, pacquirer_id: int, p_datai: datetime.date | Literal['auto'] = 'auto') -> list[NotaFiscal]:
    """
    Gera as notas fiscais do Mês para ID de emissor e data informados.
    :param pacquirer_id: ‘ID’ do emissor.
    :param p_datai: Mês das notas fiscais a serem geradas.
    :param session: Sessão do banco de dados.
    :return: Lista de notas fiscais geradas.
    """

    # definir parâmetros conforme o pacquirer_id
    param_decred: ParamDecred = __get_selected_param_decred__(session, pacquirer_id)

    if p_datai == 'auto':
        p_datai = param_decred.data_nf

    # definir porcentagem dos impostos de acordo os parâmetros definidos
    pct_iss, pct_cofins, pct_pis = __get_impostos_pct__(param_decred)

    # buscar registros
    dirfs = __get_tbl_dirf__(session, p_datai)

    # gerar nota fiscal para cada registro
    nfs: list[NotaFiscal] = []
    for dirf in dirfs:

        with LogBufferHandler(level='WARNING', format="{extra[user]} {message}") as nf_log_buffer:

            wiss, wcofins, wpis = __calc_impostos__(dirf.vl_operacao, pct_iss, pct_cofins, pct_pis)

            nf = NotaFiscal(
                codigo_emissor_nota=dirf.no_instituicao,
                data_emissao=p_datai + relativedelta(day=31),
                codigo_tomador_servico=dirf.loja,
                cnpj_tomador_servico=dirf.cnpj_loja,
                nome_tomador_servico=dirf.nome,
                cidade=dirf.cidade,
                indicador_cnpj_cpf=1 if dirf.indicador_cnpj_cpf == 'F' else 2,
                data_vencimento=p_datai + relativedelta(day=31),
                obs="Esta NF é para simples conferência, não deve ser paga, o valor é descontado em seus recebíveis",
                tipo_servico='05820',
                descricao_servico_prestado='Prestação de Serviços',
                quantidade=1,
                descricao='Compra com cartão de credito',
                valor_unitario=round(dirf.vl_operacao, 2),
                valor_compra=round(dirf.vl_operacao, 2),
                iss=wiss,
                pis=wpis,
                cofins=wcofins,
                uf=dirf.uf,
                ir=dirf.mdr,
                inscricao_estadual=param_decred.inscricao_estadual,
                endereco=dirf.endereco,
                numero=dirf.numero,
                bairro=dirf.nm_bairro,
                cep=dirf.cep,
                ano=dirf.ano,
                mes=dirf.mes,
            )
            nfs.append(nf)

            session.add(nf)
            session.commit()

            vmsg = f"loja = {str(dirf.loja)} - {nf_log_buffer.getvalue() or 'Ok'}"
            session.add(
                LogNf(
                    procedure_name='Proc-gera_nf',
                    filename=f'dataI = {str(p_datai)}',
                    process_date=datetime.datetime.now(),
                    success=not bool(nf_log_buffer.getvalue()),
                    msg_carga=vmsg,
                )
            )
            session.commit()

    return nfs
