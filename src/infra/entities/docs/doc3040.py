from sqlalchemy.orm import mapped_column, Mapped

from src.infra.core.base import Base
from src.utils.cast_to_table import cast_to_table


class Doc3040(Base):
    __tablename__ = 'doc3040'

    seq: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome_tabela: Mapped[str]
    instituicao: Mapped[str]
    ano: Mapped[int]
    mes: Mapped[int]
    linha: Mapped[str]

    def __init__(self, nome_tabela: str, instituicao: str, ano: int, mes: int, linha: str):
        new_params = cast_to_table(Doc3040, **locals())
        super().__init__(**new_params)
