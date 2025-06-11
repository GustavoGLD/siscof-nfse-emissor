from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.infra.core.base import Base
from src.utils.cast_to_table import cast_to_table


class Log3040(Base):
    __tablename__ = 'log_3040'

    seq: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    procedure_name: Mapped[str]
    filename: Mapped[str]
    process_date: Mapped[datetime.date]
    qtde_line_inserted: Mapped[int]
    msg_carga: Mapped[str]
    rtc: Mapped[int]

    def __init__(self, procedure_name: str, filename: str, process_date: datetime, qtde_line_inserted: int, msg_carga: str, rtc: int):
        new_params = cast_to_table(Log3040, **locals())
        super().__init__(**new_params)
