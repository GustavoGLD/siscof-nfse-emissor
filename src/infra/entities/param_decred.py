from typing import Optional

from sqlalchemy import Integer, String, Date, Numeric, create_engine
from sqlalchemy.orm import Mapped, mapped_column

from config import db_url
from src.utils.cast_to_table import cast_to_table

engine = create_engine(db_url)

from src.infra.core.base import Base


class ParamDecred(Base):
    __tablename__ = "param_decred"

    cod_empresa              : Mapped[Optional[int]  ] = mapped_column(Integer, primary_key=True)
    cnpj_empresa             : Mapped[Optional[str]  ] = mapped_column(String(15))
    razao_social_sefaz       : Mapped[Optional[str]  ] = mapped_column(String(50))
    municipio_sefaz          : Mapped[Optional[str]  ] = mapped_column(String(30))
    endereco                 : Mapped[Optional[str]  ] = mapped_column(String(50))
    numero                   : Mapped[Optional[int]  ] = mapped_column(Integer)
    complemento              : Mapped[Optional[str]  ] = mapped_column(String(30))
    bairro                   : Mapped[Optional[str]  ] = mapped_column(String(30))
    cidade                   : Mapped[Optional[str]  ] = mapped_column(String(100))
    cep                      : Mapped[Optional[int]  ] = mapped_column(Integer)
    uf                       : Mapped[Optional[str]  ] = mapped_column(String(2))
    empresa_email            : Mapped[Optional[str]  ]
    empresa_tel              : Mapped[Optional[str]  ]
    incricao_municipal       : Mapped[Optional[str]  ] = mapped_column(String(20))
    fax                      : Mapped[Optional[str]  ] = mapped_column(String(10))
    celular                  : Mapped[Optional[str]  ] = mapped_column(String(20))
    cargo_diretor            : Mapped[Optional[str]  ] = mapped_column(String(50))
    email_diretor            : Mapped[Optional[str]  ] = mapped_column(String(100))
    contato                  : Mapped[Optional[str]  ] = mapped_column(String(100))
    representante_legal_nome : Mapped[Optional[str]  ] = mapped_column(String(60))
    representante_legal_cpf  : Mapped[Optional[str]  ]
    representante_legal_ddd  : Mapped[Optional[int]  ] = mapped_column(Integer)
    representante_legal_fone : Mapped[Optional[int]  ] = mapped_column(Integer)
    representante_legal_ramal: Mapped[Optional[int]  ] = mapped_column(Integer)
    representante_legal_email: Mapped[Optional[str]  ] = mapped_column(String(256))
    responsavel_dados_nome   : Mapped[Optional[str]  ] = mapped_column(String(60))
    responsavel_dados_cpf    : Mapped[Optional[str]  ]
    responsavel_dados_ddd    : Mapped[Optional[int]  ] = mapped_column(Integer)
    responsavel_dados_fone   : Mapped[Optional[int]  ] = mapped_column(Integer)
    responsavel_dados_ramal  : Mapped[Optional[int]  ] = mapped_column(Integer)
    responsavel_dados_email  : Mapped[Optional[str]  ] = mapped_column(String(256))
    responsavel_dados_cargo  : Mapped[Optional[str]  ] = mapped_column(String(50))
    nome_tec1                : Mapped[Optional[str]  ] = mapped_column(String(50))
    cargo_tec1               : Mapped[Optional[str]  ] = mapped_column(String(50))
    telefone_tec1            : Mapped[Optional[str]  ] = mapped_column(String(50))
    email_tec1               : Mapped[Optional[str]  ] = mapped_column(String(50))
    nome_tec2                : Mapped[Optional[str]  ] = mapped_column(String(50))
    cargo_tec2               : Mapped[Optional[str]  ] = mapped_column(String(50))
    telefone_tec2            : Mapped[Optional[str]  ] = mapped_column(String(50))
    email_tec2               : Mapped[Optional[str]  ] = mapped_column(String(50))
    valor_sel_pessoa_fisica  : Mapped[Optional[float]] = mapped_column(Numeric)
    valor_sel_pessoa_juridica: Mapped[Optional[float]] = mapped_column(Numeric)
    semestre                 : Mapped[Optional[int]  ] = mapped_column(Integer)
    ano                      : Mapped[Optional[int]  ] = mapped_column(Integer)
    tipo_declaracao          : Mapped[Optional[int]  ] = mapped_column(Integer)
    nome_diretorio           : Mapped[Optional[str]  ] = mapped_column(String(100))
    valor_lancamento_perdas  : Mapped[Optional[float]] = mapped_column(Numeric)
    iof_41                   : Mapped[Optional[float]] = mapped_column(Numeric)
    iof_38                   : Mapped[Optional[float]] = mapped_column(Numeric)
    concessao_minima         : Mapped[Optional[float]] = mapped_column(Numeric)
    financ_iof               : Mapped[Optional[str]  ]
    org_adm                  : Mapped[Optional[int]  ] = mapped_column(Integer)
    org_fin                  : Mapped[Optional[int]  ] = mapped_column(Integer)
    last_rot_diaria          : Mapped[Optional[Date] ] = mapped_column(Date)
    last_closed_contabil     : Mapped[Optional[Date] ] = mapped_column(Date)
    sg_interface_contabil    : Mapped[Optional[str]  ] = mapped_column(String(10))
    dt_inclusao              : Mapped[Optional[Date] ] = mapped_column(Date)
    ano_deban                : Mapped[Optional[int]  ] = mapped_column(Integer)
    trimestre_deban          : Mapped[Optional[int]  ] = mapped_column(Integer)
    mes_sefaz                : Mapped[Optional[int]  ] = mapped_column(Integer)
    ano_sefaz                : Mapped[Optional[int]  ] = mapped_column(Integer)
    nat_sefaz                : Mapped[Optional[str]  ]
    fanalidade_arq_sefaz     : Mapped[Optional[str]  ]
    nome_arquivo_envio       : Mapped[Optional[str]  ] = mapped_column(String(500))
    inicio_h_verao           : Mapped[Optional[Date] ] = mapped_column(Date)
    fim_h_verao              : Mapped[Optional[Date] ] = mapped_column(Date)
    dif_h                    : Mapped[Optional[int]  ] = mapped_column(Integer)
    ir_auto_retencao         : Mapped[Optional[float]]
    pct_iss                  : Mapped[Optional[float]]
    pct_pis                  : Mapped[Optional[float]]
    pct_cofins               : Mapped[Optional[float]]
    dt_contabil              : Mapped[Optional[Date] ] = mapped_column(Date)
    taxa_pan                 : Mapped[Optional[float]] = mapped_column(Numeric)
    pct_iss_serv             : Mapped[Optional[float]] = mapped_column(Numeric)
    cdi_ano                  : Mapped[Optional[float]] = mapped_column(Numeric)
    cdi_dia                  : Mapped[Optional[float]] = mapped_column(Numeric)
    custo_oportunidade       : Mapped[Optional[float]] = mapped_column(Numeric)
    custo_dinheiro           : Mapped[Optional[float]] = mapped_column(Numeric)
    ispb_dev                 : Mapped[Optional[str]  ] = mapped_column(String(8))
    agencia                  : Mapped[Optional[str]  ] = mapped_column(String(4))
    conta                    : Mapped[Optional[str]  ] = mapped_column(String(12))
    digito_cc                : Mapped[Optional[str]  ] = mapped_column(String(4))
    resp_ir                  : Mapped[Optional[str]  ] = mapped_column(String(50))
    inscricao_estadual       : Mapped[Optional[str]  ] = mapped_column(String(14))
    dt1                      : Mapped[Optional[Date] ] = mapped_column(Date)
    dt2                      : Mapped[Optional[Date] ] = mapped_column(Date)
    usuario_sqlldr           : Mapped[Optional[str]  ] = mapped_column(String(100))
    senha_sqlldr             : Mapped[Optional[str]  ] = mapped_column(String(100))
    listar_decred            : Mapped[Optional[str]  ]
    exec_dimp                : Mapped[Optional[str]  ]
    hora_movimento           : Mapped[Optional[str]  ] = mapped_column(String(6))
    sucursal                 : Mapped[Optional[int]  ] = mapped_column(Integer)
    comercio                 : Mapped[Optional[int]  ] = mapped_column(Integer)
    cod_conglomerado         : Mapped[Optional[str]  ] = mapped_column(String(10))
    nome_conglomerado        : Mapped[Optional[str]  ] = mapped_column(String(100))
    inscricao_municipal      : Mapped[Optional[str]  ] = mapped_column(String(20))
    data_dirf                : Mapped[Optional[int]  ] = mapped_column(Integer)
    data_dirff               : Mapped[Optional[int]  ] = mapped_column(Integer)
    data_iss                 : Mapped[Optional[int]  ] = mapped_column(Integer)
    versao_dimp              : Mapped[Optional[int]  ] = mapped_column(Integer)
    new_dcx_car              : Mapped[Optional[str]  ]
    dt_dimp_ini              : Mapped[Optional[int]  ] = mapped_column(Integer)
    dt_dimp_fim              : Mapped[Optional[int]  ] = mapped_column(Integer)
    uf_dimp                  : Mapped[Optional[str]  ] = mapped_column(String(2))
    mes_i                    : Mapped[Optional[int]  ] = mapped_column(Integer)
    mes_f                    : Mapped[Optional[int]  ] = mapped_column(Integer)

    data_nf                  : Mapped[Optional[Date] ] = mapped_column(Date)

    def __init__(self, **kw):
        new_params = cast_to_table(ParamDecred, **kw)
        super().__init__(**new_params)
