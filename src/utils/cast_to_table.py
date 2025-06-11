import datetime
from typing import Any, TypeVar

from loguru import logger
from sqlalchemy.orm import Mapped

from src.utils import log_func

_T = TypeVar('_T')


@log_func
def cast_to_table(tbl: _T, **params: Any) -> dict[str, Any]:
    """
    Transforma os valores para os tipos das colunas da tabela.
    """
    # `self._sa_instance_state.key[0].__annotations__` para substituir o parâmetro `tbl: _T` por `self`

    with logger.contextualize(user=f'cast_to_table-{tbl.__name__}'):

        # remove os parâmetros que não são colunas da tabela
        params: dict[str, Any] = {
            key: value
            for key, value in params.items()
            if not key.startswith('_') and key not in ['self', 'kw']
        }

        new_params: dict[str, Any] = {}
        for key, value in params.items():
            try:
                # se o tipo da coluna for datetime.date e o valor for str, converte para datetime.date
                if type(value) == str and tbl.__annotations__[key].__args__[0] is datetime.date:
                    new_params[key] = datetime.datetime.strptime(value, '%Y-%m-%d').date()
                    logger.debug(f"Strptime cast {value} to {new_params[key]} - {tbl.__name__}.{key}")

                # se os tipos da coluna e do valor diferirem e o valor não for None, converte para o tipo da coluna
                elif type(value) is not tbl.__annotations__[key].__args__[0] and value is not None:
                    new_params[key] = tbl.__annotations__[key].__args__[0](value)
                    logger.debug(f"Converted {value} ({type(value)}) to {new_params[key]} ({type(new_params[key])}) - {tbl.__name__}.{key}")

                # se os tipos da coluna e do valor forem iguais, mantém o valor
                else:
                    new_params[key] = value

            except (TypeError, ValueError):
                new_params[key] = None
                logger.warning(
                    f"Impossible to convert '{value}' {type(value)} to {tbl.__annotations__[key].__args__[0]} "
                    f"in {tbl.__name__}.{key}"
                )

        return new_params

