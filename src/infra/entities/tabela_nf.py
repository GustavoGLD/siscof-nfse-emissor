from typing import Any

from sqlalchemy import String, Float, Index, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.core.base import Base
from src.utils.cast_to_table import cast_to_table


class TabelaNf(Base):
    __tablename__ = "tabela_nf"
    seq: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    nome_tabela: Mapped[str]
    instituicao: Mapped[int]
    ano: Mapped[int]
    mes: Mapped[int]
    linha: Mapped[str]

    def __init__(self, **kw):
        new_params = cast_to_table(TabelaNf, **kw)
        super().__init__(**new_params)


Index("itabela_nf", TabelaNf.nome_tabela, TabelaNf.instituicao, TabelaNf.ano)

# Base.metadata.create_all(engine)
