import datetime

from sqlalchemy import String, Index, Integer, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.infra.core.base import Base
from src.utils.cast_to_table import cast_to_table


class LogNf(Base):
    __tablename__ = 'log_nf'
    line_num: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    procedure_name: Mapped[str]
    filename: Mapped[str]
    process_date: Mapped[datetime.datetime]
    # qtde_line_read    : Mapped[int]   = mapped_column(Integer)
    # qtde_line_inserted: Mapped[int]   = mapped_column(Integer)
    success: Mapped[bool]
    msg_carga: Mapped[str]
    # rtc               : Mapped[str]   = mapped_column(String(3))

    def __init__(self, **kw):
        new_params = cast_to_table(LogNf, **kw)
        super().__init__(**new_params)


Index(
    'id_log_nf',
    LogNf.procedure_name,
    LogNf.filename,
    LogNf.process_date
)

# Base.metadata.create_all(engine)
