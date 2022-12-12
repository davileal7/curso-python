import os
import pathlib
from pathlib import Path

if os.path.isdir('diretório'):
    print('existe')
else:
    print('não existe')

if Path('diretório').is_dir():
    print('o diretório existe')
else:
    print('diretório NÃO existe')