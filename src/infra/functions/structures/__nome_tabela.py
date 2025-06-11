from dataclasses import dataclass
from typing import Literal

from src.utils import log_func


@dataclass
class __NomeTabela:
    tipo_nota: Literal['NFSE']
    codigo_emissor_nota: int
    mes: int
    ano: int
    recibo_tipo: Literal['A', 'B']
    formato_arquivo: Literal['txt', 'xml']

    @log_func
    def to_string(self) -> str:
        tipo_nota = self.tipo_nota.upper()
        codigo_emissor_nota = str(self.codigo_emissor_nota).zfill(11)
        # data_emissao = str(self.data_emissao).replace('-', '')
        mes = str(self.mes).zfill(2)
        tipo_arquivo = self.formato_arquivo.lower()
        recibo_tipo = self.recibo_tipo.upper()

        return (
            f'{tipo_nota}'
            f'_'
            f'{codigo_emissor_nota}'
            f'_'
            f'{mes}{self.ano}'
            f'_'
            f'{recibo_tipo}'
            f'.'
            f'{tipo_arquivo}'
        )