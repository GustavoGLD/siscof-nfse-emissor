import pathlib

from config.paths import db_url
from config.paths import InputFiles
from config.paths import OutputFolders
from config.impostos import Impostos


diretorios: list[str] = [
    value
    for key, value in OutputFolders.__dict__.items()
    if not key.startswith('__')
]

for d in diretorios:
    if not pathlib.Path(d).exists():
        pathlib.Path(d).mkdir(parents=True)
