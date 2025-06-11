from typing import Optional

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.core.base import Base
from src.utils.cast_to_table import cast_to_table


class TabelaISS(Base):
    __tablename__ = 'tbl_iss'

    seq: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    nome_tabela: Mapped[str]
    instituicao: Mapped[str]
    ano: Mapped[int]
    mes: Mapped[int]

    uf: Mapped[str] = mapped_column(nullable=True)
    cidade: Mapped[str] = mapped_column(nullable=True)
    valor_unitario: Mapped[float]
    iss: Mapped[float]
    pis: Mapped[float]
    cofins: Mapped[float]
    ir: Mapped[float]

    linha: Mapped[str]

    def __init__(self, **kw):
        new_params = cast_to_table(TabelaISS, **kw)
        super().__init__(**new_params)
