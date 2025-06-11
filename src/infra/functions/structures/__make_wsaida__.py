import datetime
from dataclasses import dataclass
from typing import Literal

from src.infra.entities import NotaFiscal
from src.utils import log_func


@dataclass
class __SaidaNF:
    tipo_registro: Literal['1']
    versao_arquivo: Literal['001']

    data_inicial: datetime.date
    """data inicio do período transferido no arquivo"""

    data_final: datetime.date
    """data final do período transferido no arquivo"""

    inscricao_municipal: str
    """Inscrição Municipal do prestador de serviços."""

    def to_string(self) -> str:
        tipo_registro = self.tipo_registro
        versao_arquivo = self.versao_arquivo
        data_inicial = str(self.data_inicial).replace('-', '')
        data_final = str(self.data_final).replace('-', '')
        incricao_municipal = str(self.inscricao_municipal).zfill(8)

        return (
            f'{tipo_registro} '
            f'{versao_arquivo} '
            f'{incricao_municipal} '
            f'{data_inicial} '
            f'{data_final} '
            #f' '
        )

    def __str__(self) -> str:
        return self.to_string()


@log_func
def __make_wsaida__(nf: NotaFiscal) -> str:
    wsaida = __SaidaNF(
        tipo_registro='1',
        versao_arquivo='001',
        data_inicial=nf.data_emissao,
        data_final=nf.data_vencimento,
        inscricao_municipal=nf.codigo_emissor_nota
    ).to_string()

    wsaida += ('2' + 'RPS  ' + 'A' * 5)

    wsaida += str(nf.nr_previa).zfill(12)

    wsaida += nf.data_emissao.strftime('%Y%m%d')

    wsaida += 'T'
    # wsaida := wsaida ||'T' ;

    wsaida += str(nf.codigo_tomador_servico).zfill(8)

    wsaida += str(int(nf.valor_compra * 100)).rjust(15, '0')
    # wsaida := wsaida ||lpad(to_char(nf.valor_servico*100,'fm000000000000000'),15,'0') ;

    wsaida += '0' * 15 + '05820' + '0200' + '2'
    # wsaida := wsaida ||lpad('0',15,'0')|| '05820'|| '0200'|| '2';

    wsaida += nf.indicador_cnpj_cpf
    # wsaida := wsaida ||nf.INDICADOR_CNPJ_CPF ;

    wsaida += str(nf.cnpj_tomador_servico).rjust(
        14, '0'
    )
    # wsaida := wsaida ||lpad(nvl(pck_utils.so_numero(nf.cnpj),0),14,'0');

    wsaida += '0' * 12
    # wsaida := wsaida ||lpad('0',12,'0');

    wsaida += '0' * 12
    # wsaida := wsaida ||lpad('0',12,'0');

    # por que não o nome do começo?
    # wsaida += nota_fiscal.nome_tomador_servico[10:].ljust(75, ' ')
    wsaida += nf.nome_tomador_servico.ljust(75, ' ')
    # wsaida := wsaida ||rpad(SubStr(nf.nome_tomador_servico,11),75,' ') ;

    wsaida += (nf.tipo_endereco or ' ').ljust(3, ' ')
    # wsaida := wsaida ||rpad(nvl(nf.tipo_endereco,' '),3,' ');

    wsaida += (nf.endereco or '').ljust(50, ' ')
    # wsaida := wsaida ||rpad(nf.endereco,50,' ');

    wsaida += str(nf.numero).rjust(10)
    # wsaida := wsaida ||rpad(nvl(nf.numero,' '),10,' ');

    wsaida += ' ' * 30
    # wsaida := wsaida ||rpad(' ',30,' ' );

    wsaida += (nf.bairro or '').rjust(30)
    # wsaida := wsaida ||rpad(nvl(nf.bairro,' '),30,' ');

    wsaida += (nf.cidade or '').rjust(50)
    # wsaida := wsaida ||rpad(nvl(nf.cidade,' '),50,' ');

    wsaida += (nf.uf or '').rjust(2)
    # wsaida := wsaida ||rpad(nvl(nf.uf,' '),2,' ');

    wsaida += (nf.cep or '').rjust(8, '0')
    # wsaida := wsaida ||lpad(nvl(nf.cep,' '),8,'0');

    wsaida += ' ' * 75
    # wsaida := wsaida ||rpad(' ',75,' ');

    wsaida += nf.descricao_servico_prestado
    # wsaida := wsaida ||nf.descricao_servico_prestado

    wsaida += nf.descricao + '|' + \
              'Lei Federal 12.741/12; CF/88  Artigo 150 §5º:' + '|' \
                                                                      'Tributos informados para atendimento à legislação mencionada, NÃO devendo ser pagos e nem retidos.' + '|  ' + \
              f'|ISS:-----  2,00% R${nf.iss:.2f}' + '|' + \
              f'PIS:-----  1,65% R${nf.pis:.2f}' + '|' + \
              f'COFINS:--  7,60% R${nf.cofins:.2f}' + '| ' + \
              f'|IR auto retenção Instrução Normativa SRF nº 153/1987' + '|' + \
              f'Tributos informados para atendimento à legislação mencionada, NÃO devendo ser pagos e nem retidos.' + '| ' + \
              f'|IR:------  1,50% R${nf.ir:.2f}' + '| ' \
              f'| |***OBS: Esta nota fiscal é para simples conferência e NÃO deve ser paga conforme os termos do contrato de serviço.' + '| '+ \
              f'|Att.,' + '| ' + \
              f'|' + nf.mensagem_ir

    return wsaida