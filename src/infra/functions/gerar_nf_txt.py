from sqlalchemy import select
from sqlalchemy.orm import Session

from src.infra.entities.tabela_nf import TabelaNf
from src.infra.entities.nota_fiscal import NotaFiscal
from src.infra.functions.structures.__make_wsaida__ import __make_wsaida__

from src.infra.functions.structures.__nome_tabela import __NomeTabela

from config import OutputFolders
from src.utils import log_func


@log_func
def gerar_nf_txt(nfs: list[NotaFiscal], session: Session) -> None:
    """
    Gera um arquivo texto de todas as notas fiscais de um mês.
    Obs.: certificar se todas as notas fiscais são do mesmo mês.
    :param nfs: Lista de Notas fiscais a serem geradas.
    :param session: Sessão SQLAlchemy do banco de dados.
    """

    try:
        v_qtd_registros = len(nfs)

        v_total_servicos_prestados = 0.0

        wnome_tabela = __NomeTabela(
            tipo_nota='NFSE',
            codigo_emissor_nota=nfs[0].codigo_emissor_nota,
            mes=nfs[0].mes,
            ano=nfs[0].ano,
            recibo_tipo='A',
            formato_arquivo='txt'
        ).to_string()

        for nf in nfs:
            v_total_servicos_prestados += nf.valor_compra

            wsaida = __make_wsaida__(nf)

            session.add(
                TabelaNf(
                    nome_tabela=wnome_tabela,
                    instituicao=nf.codigo_emissor_nota,
                    ano=nf.ano,
                    mes=nf.mes,
                    linha=wsaida
                )
            )
            session.commit()

        if v_qtd_registros > 0:
            wsaida = ('9' +
                      str(v_qtd_registros).rjust(7, '0') +
                      str(int(v_total_servicos_prestados * 100)).rjust(15, '0') +
                      '0' * 15)
            session.add(
                TabelaNf(
                    nome_tabela=wnome_tabela,
                    instituicao=nfs[0].codigo_emissor_nota,
                    ano=nfs[0].ano,
                    mes=nfs[0].mes,
                    linha=wsaida
                )
            )
            session.commit()

        with open(f'{OutputFolders.log_nf}/{wnome_tabela}', 'w') as file:
            a = session.execute(
                select(TabelaNf.linha)
                .filter(
                    TabelaNf.nome_tabela == wnome_tabela
                )
                .order_by(TabelaNf.linha)
            ).all()
            a = [i[0] for i in a]
            a = "\n".join(a)

            file.write(a)

    except IndexError as exception:
        raise IndexError("Não há notas fiscais para gerar") from exception
