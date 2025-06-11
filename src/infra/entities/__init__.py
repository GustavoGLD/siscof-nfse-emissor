from src.infra.core.connection import engine
from src.infra.core.base import Base


#tabelas a serem inicializadas em gerador_nf.py
from src.infra.entities.log_nf import LogNf
from src.infra.entities.nota_fiscal import NotaFiscal
from src.infra.entities.tabela_nf import TabelaNf
from src.infra.entities.tbl_iss import TabelaISS
from src.infra.entities.docs.doc3040 import Doc3040
from src.infra.entities.docs.doc3026 import Doc3026

Base.metadata.drop_all(bind=engine)

# tabelas a serem inicializadas em create_db.py
from src.infra.entities.param_decred import ParamDecred
from src.infra.entities.tbl_dirf import TblDirf

Base.metadata.create_all(bind=engine)
