import datetime
from typing import Optional, List, Type

from dateutil.relativedelta import relativedelta
from loguru import logger
from sqlalchemy import select, Result, func, and_
from sqlalchemy.orm import Session

from src.infra.entities import ParamDecred, TblDirf
from src.infra.entities.tbl_dirf import TblDirf

from config import Impostos
from src.utils import get_grouped_rolls, log_func


@log_func
def __get_selected_param_decred__(session: Session, pacquirer_id: int) -> ParamDecred:
    """
    Retorna o registro de ParamDecred selecionado para o pacquirer_id.
    """
    param_decred: Optional[ParamDecred] = session.scalars(
        select(ParamDecred)
        .where(
            ParamDecred.cod_empresa == pacquirer_id
        )
    ).first()

    assert param_decred is not None, f'Não foi encontrado o registro de ParamDecred para o pacquirer_id {pacquirer_id}'
    return param_decred


@log_func
def __get_impostos_pct__(param_decred: ParamDecred) -> tuple[float, float, float]:
    """
    Retorna a porcentagem dos impostos a serem aplicados sobre o valor da nota fiscal.
    Se não estiver definido em param_decred, retorna o valor padrão.
    :return: (pct_iss, pct_cofins, pct_pis)
    """
    print(param_decred.pct_iss, param_decred.pct_cofins, param_decred.pct_pis)
    return (
        param_decred.pct_iss or Impostos.PCT_ISS,
        param_decred.pct_cofins or Impostos.PCT_COFINS,
        param_decred.pct_pis or Impostos.PCT_PIS
    )


@log_func
def __get_tbl_dirf__(session: Session, p_datai: datetime.date) -> list[Type[TblDirf]]:

    """
    Retorna os registros de TblDirf que serão utilizados para gerar as notas fiscais.
    """
    dirfs = session.execute(
        select(
            TblDirf.no_instituicao,
            TblDirf.nome,
            TblDirf.loja,
            TblDirf.cidade,
            TblDirf.uf,
            TblDirf.indicador_cnpj_cpf,
            TblDirf.cnpj_loja,
            TblDirf.forma_captura,
            TblDirf.ano,
            TblDirf.mes,
            TblDirf.cep,
            TblDirf.email_cont,
            TblDirf.endereco,
            TblDirf.numero,
            TblDirf.nm_complemento,
            TblDirf.nm_bairro,
            func.sum(TblDirf.vl_operacao).label('vl_operacao'),
            func.sum(TblDirf.mdr).label('mdr'),
            func.sum(TblDirf.mdr_liquido).label('mdr_liquido'),
        )
        .where(
            and_(p_datai <= TblDirf.dt_operacao, TblDirf.dt_operacao <= p_datai + relativedelta(day=31))
        )
        .group_by(
            TblDirf.loja,
            TblDirf.nome,
            TblDirf.cnpj_loja,
            TblDirf.cidade,
            TblDirf.ano,
            TblDirf.mes,
            TblDirf.cep,
            TblDirf.email_cont,
            TblDirf.endereco,
            TblDirf.numero,
            TblDirf.nm_complemento,
            TblDirf.nm_bairro,
            TblDirf.uf,
            TblDirf.indicador_cnpj_cpf,
            TblDirf.forma_captura,
            TblDirf.no_instituicao,
        )
    ).all()

    assert dirfs, logger.exception(f'Não foram encontrados registros de TblDirf para o mês {p_datai}')

    return dirfs


@log_func
def __calc_impostos__(vl_operacao: float, pct_iss: float, pct_cofins: float, pct_pis: float) -> tuple[
    float, float, float]:
    """
    Calcula os impostos a serem aplicados sobre o valor da nota fiscal.
    :return: (iss, cofins, pis)
    """
    return (
        round(pct_iss * vl_operacao / 100, 2),
        round(pct_cofins * vl_operacao / 100, 2),
        round(pct_pis * vl_operacao / 100, 2)
    )
