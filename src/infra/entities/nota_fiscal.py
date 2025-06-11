from typing import Optional, Any

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

import datetime

from src.infra.core.base import Base
from src.utils.cast_to_table import cast_to_table


# simplificar a classe NotaFiscal herdando TblDirf
class NotaFiscal(Base):
    __tablename__ = 'notas_fiscais'
    nr_previa: Mapped[int] = mapped_column(primary_key=True)

    codigo_emissor_nota         : Mapped[str]
    data_emissao                : Mapped[datetime.date]
    codigo_tomador_servico      : Mapped[str]
    cnpj_tomador_servico        : Mapped[str]
    nome_tomador_servico        : Mapped[str]
    cidade                      : Mapped[str] = mapped_column(nullable=True)
    cep                         : Mapped[str] = mapped_column(nullable=True)
    indicador_cnpj_cpf          : Mapped[str]
    data_vencimento             : Mapped[datetime.date]
    obs                         : Mapped[str]
    tipo_servico                : Mapped[str]
    descricao_servico_prestado  : Mapped[str] = mapped_column(default="Prestação de Serviços")
    quantidade                  : Mapped[int]
    descricao                   : Mapped[str]
    valor_unitario              : Mapped[float]
    valor_compra                : Mapped[float]
    iss                         : Mapped[float]
    pis                         : Mapped[float]
    cofins                      : Mapped[float]
    uf                          : Mapped[str] = mapped_column(nullable=True)
    inscricao_estadual          : Mapped[str] = mapped_column(nullable=True)
    tipo_endereco               : Mapped[str]           = mapped_column(default='')
    valor_deducao               : Mapped[float]         = mapped_column(default=0.0)
    ir                          : Mapped[float]         = mapped_column(default=0.0)
    mensagem_ir                 : Mapped[str]           = mapped_column(default='')
    endereco                    : Mapped[str]           = mapped_column(default='')
    numero                      : Mapped[int] = mapped_column(nullable=True)
    bairro                      : Mapped[str] = mapped_column(nullable=True)
    ano                         : Mapped[int]
    mes                         : Mapped[int]

    def __init__(self, **kw):
        new_params = cast_to_table(NotaFiscal, **kw)
        super().__init__(**new_params)
