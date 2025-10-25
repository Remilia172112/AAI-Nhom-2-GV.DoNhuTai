# Debug helper: import the notebook module functions by executing the notebook file contents
# We'll load the notebook as text and exec code cells in order until tournament_random_vs_random is defined,
# then call it with a small number of games to reproduce the error.
import json
from pathlib import Path
nb_path = Path(r"d:\Học\TTNTNC\Lab4\assignment_connect4.ipynb")
nb = json.loads(nb_path.read_text(encoding='utf-8'))
# Execute code cells in a fresh globals
ns = {}
import numpy as np
ns['np'] = np
# we'll also import Connect4Env if present after executing earlier cells
for cell in nb['cells']:
    if cell['cell_type'] != 'code':
        continue
    src = ''.join(cell.get('source', []))
    try:
        exec(src, ns)
    except Exception as e:
        print('Exception while executing a notebook cell during load:')
        import traceback
        traceback.print_exc()
        break
# Now try to call tournament_random_vs_random if defined
if 'tournament_random_vs_random' in ns:
    import inspect
    if 'empty_board' in ns:
        try:
            print('empty_board signature:', inspect.signature(ns['empty_board']))
        except Exception:
            print('empty_board is present but signature could not be determined')
    try:
        print('Calling tournament_random_vs_random(50)')
        res = ns['tournament_random_vs_random'](50)
        print('Result:', res)
    except Exception:
        import traceback
        traceback.print_exc()
else:
    print('tournament_random_vs_random not defined in executed notebook cells')
