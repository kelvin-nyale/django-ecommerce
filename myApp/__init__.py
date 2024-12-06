import os
import glob

for filepath in glob.glob('./*/migrations/*.py'):
    if not filepath.endswith('__init__.py'):
        os.remove(filepath)
        print(f"Deleted: {filepath}")


