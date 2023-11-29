"""
Summary
"""

import os
from pathlib import Path

project_path = Path(__file__).parent
post_path = project_path / 'collections' / '_posts'

if not post_path.is_dir():
    raise Exception(f'{post_path} is not a directory')

list_ipynb = list(post_path.rglob('*/*.ipynb'))

for ipynb in list_ipynb:
    print(ipynb)


print('Helloooooo')
