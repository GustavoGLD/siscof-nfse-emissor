from sqlalchemy import select, func
from sqlalchemy.orm import Session

from src.infra.entities import NotaFiscal
from src.infra.entities.tbl_iss import TabelaISS

from config import OutputFolders
from src.utils import log_func


@log_func
def gera_iss_txt(nfs: list[NotaFiscal], session: Session) -> None:
    """
    Adiciona os registros na tabela TabelaISS
    Gera o arquivo ISS_<UF>_<CIDADE>_<ANO><MES>.TXT
    :param nfs:
    :param session:
    :return:
    """

    registros = session.execute(
        select(
            NotaFiscal.uf,
            NotaFiscal.cidade,
            NotaFiscal.mes,
            NotaFiscal.ano,
            func.sum(NotaFiscal.valor_unitario).label('valor_unitario'),
            func.sum(NotaFiscal.iss).label('iss'),
            func.sum(NotaFiscal.pis).label('pis'),
            func.sum(NotaFiscal.cofins).label('cofins'),
            func.sum(NotaFiscal.ir).label('ir')
        )
        .group_by(
            NotaFiscal.uf,
            NotaFiscal.cidade,
            NotaFiscal.data_vencimento,
            NotaFiscal.mes,
            NotaFiscal.ano,
        )
        .order_by(
            NotaFiscal.uf,
            NotaFiscal.cidade,
            NotaFiscal.data_vencimento
        )
    ).all()

    for i in registros:  # type: NotaFiscal
        wnome_tabela = f"ISS_{i.uf}_{(i.cidade or 'None').replace(' ', '_')}_{i.ano}{str(i.mes).zfill(2)}.TXT"

        linha = f"{i.uf}" \
                f"{i.cidade.upper().strip().replace(' ', '').translate(str.maketrans('áéíóúâêîôûãẽĩõũç', 'aeiouaeiouaeiouc')) if i.cidade else ' ': <100}" \
                f"{i.ano}{i.mes}" \
                f"{int(i.valor_unitario * 100):0>12}" \
                f"{int(i.iss * 100):0>8}" \
                f"{int(i.pis * 100):0>8}" \
                f"{int(i.cofins * 100):0>8}" \
                f"{int(i.ir * 100):0>8}"

        session.add(
            TabelaISS(
                nome_tabela=wnome_tabela,
                instituicao=1,
                ano=i.ano,
                mes=i.mes,
                uf=i.uf,
                cidade=i.cidade,
                valor_unitario=i.valor_unitario,
                iss=i.iss,
                pis=i.pis,
                cofins=i.cofins,
                ir=i.ir,
                linha=linha
            )
        )
        session.commit()

        with open(f'{OutputFolders.iss_txt}/{wnome_tabela}', 'w') as file:
            file.write(linha)
