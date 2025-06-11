import datetime
from typing import Optional

from sqlalchemy import Column, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.core.base import Base
from src.utils.cast_to_table import cast_to_table


class TblDirf(Base):
    __tablename__    = "tbl_dirf"

    id: Mapped[int] = mapped_column(primary_key=True)

    no_instituicao    : Mapped[int] = mapped_column(nullable=True)
    cnpj_loja         : Mapped[str] = mapped_column(nullable=True)
    loja              : Mapped[str] = mapped_column(nullable=True)
    nome              : Mapped[str] = mapped_column(nullable=True)
    cidade            : Mapped[str] = mapped_column(nullable=True)
    indicador_cnpj_cpf: Mapped[str] = mapped_column(nullable=True)
    dt_operacao       : Mapped[datetime.date] = mapped_column(nullable=True)
    funcao_cartao     : Mapped[str] = mapped_column(nullable=True)
    forma_captura     : Mapped[int] = mapped_column(nullable=True)
    vl_operacao       : Mapped[float] = mapped_column(nullable=True)
    interchange       : Mapped[float] = mapped_column(nullable=True)
    refnum_bandeira   : Mapped[str] = mapped_column(nullable=True)
    mdr               : Mapped[float] = mapped_column(nullable=True)
    mdr_liquido       : Mapped[float] = mapped_column(nullable=True)
    uf                : Mapped[str] = mapped_column(nullable=True)
    ano               : Mapped[int] = mapped_column(nullable=True)
    mes               : Mapped[int] = mapped_column(nullable=True)
    cep               : Mapped[str] = mapped_column(nullable=True)
    email_cont        : Mapped[str] = mapped_column(nullable=True)
    endereco          : Mapped[str] = mapped_column(nullable=True)
    numero            : Mapped[str] = mapped_column(nullable=True)
    nm_complemento    : Mapped[str] = mapped_column(nullable=True)
    nm_bairro         : Mapped[str] = mapped_column(nullable=True)

    def __init__(self, **kw):
        new_params = cast_to_table(TblDirf, **kw)
        super().__init__(**new_params)

#Index("itbl_dirf", tbl_dirf.acquirer_id, tbl_dirf.comercio, tbl_dirf.sucursal, tbl_dirf.fecha_presentacion)

#Base.metadata.create_all(engine)
