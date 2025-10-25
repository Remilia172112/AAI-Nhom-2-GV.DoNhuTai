import nbformat
import sys
from pathlib import Path
p = Path(r"d:/Học/TTNTNC/Lab4/assignment_connect4.ipynb")
nb = nbformat.read(str(p), as_version=4)
# Use Agg backend for matplotlib to avoid GUI
try:
    import matplotlib
    matplotlib.use('Agg')
except Exception:
    pass

globals_dict = {}
for i, cell in enumerate(nb.cells):
    if cell.cell_type != 'code':
        continue
    src = ''.join(cell.source)
    try:
        compiled = compile(src, f'<cell-{i}>', 'exec')
        exec(compiled, globals_dict)
    except Exception as e:
        print(f'Error in cell {i} (id={cell.get("id")}):', file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
print('Sanity check: all code cells executed without exception (in this runner).')
