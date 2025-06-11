import copy
from typing import TypeVar, TypeAlias, Union

from sqlalchemy import select, ColumnElement
from sqlalchemy.orm import Session, InstrumentedAttribute
from sqlalchemy.sql.elements import SQLCoreOperations, Label
from sqlalchemy.sql.roles import ExpressionElementRole

from src.utils import log_func

_T = TypeVar('_T')

Conditional: TypeAlias = list[
    Union[ColumnElement, SQLCoreOperations[bool], ExpressionElementRole[bool]]
]
Groupable: TypeAlias = list[InstrumentedAttribute[_T] | _T]
Functional: TypeAlias = list[Label]


#@log_func
def get_grouped_rolls(table: _T, where: Conditional, group_by: Groupable, functions: Functional, session: Session) -> list[_T]:
    """
    Agrupa linhas de uma tabela por condições e aplica funções.
    Ao contrário do select().all(), retorna uma lista de instâncias/objetos da tabela, e não tuplas nomeadas.
    """
    main_tables = session.execute(
        select('*')
        .where(*where)
        .group_by(*group_by)
    ).all()
    func_values = session.execute(
        select(*functions)
        .where(*where)
        .group_by(*group_by)
    ).all()

    final_tbl: list[_T] = []

    for roll, new_values in zip(main_tables, func_values):

        new_roll = copy.deepcopy(dict(roll._mapping.items()._items))
        #print(new_values)
        for key, value in new_roll.items():
            print(key, type(value))

        for key, value in new_values._mapping.items()._items:
            new_roll[key] = value
        print('\n')
        final_tbl.append(table(**new_roll))

    return final_tbl
