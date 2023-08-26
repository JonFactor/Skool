### imports
import os, pathlib
from pathlib import Path
### parameter
user = 'jonfa'
### code
## paths
strpathParent = f'C:\\Users\{user}\Desktop\\Stocks'
pathParent = Path(strpathParent)
pathData = Path(f'{strpathParent}\\data\\')
pathResult = Path(f'{strpathParent}\\result\\')

paths = [pathParent, pathData, pathResult]

## make paths
for path in paths:
    path.mkdir(parents=True, exist_ok=True)
