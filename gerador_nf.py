import datetime
import inspect
import sys

from loguru import logger
from sqlalchemy import Connection, text
from sqlalchemy.orm import Session

import pandas as pd

from src.infra.core.connection import engine

from src.infra.entities.log_nf import LogNf

from src.infra.functions import gerar_nf_txt
from src.infra.functions import gera_iss_txt
from src.infra.functions import gerar_nf

from config import OutputFolders, InputFiles

from src.utils import log_func

logger.remove()
logger.add(sys.stdout, level="WARNING")

@log_func  # Remove o argumento do decorador
def gerar_log_nf(session: Session) -> None:
    """
    Gera o arquivo de log_nf.csv
    """
    (
        pd
        .read_sql(
            session.query(LogNf).statement,
            session.bind
        )
        .to_csv(
            f'{OutputFolders.log_nf}/log_nf.csv',
            index=False,
            sep=';',
        )
    )


with Connection(engine) as conn, Session(engine) as session:
    nfs = gerar_nf(
        pacquirer_id=1,
        session=session
    )

    gerar_nf_txt(nfs, session)

    gera_iss_txt(nfs, session)

    gerar_log_nf(session)
