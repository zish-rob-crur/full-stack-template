import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent))

from backend_app.cli.main import app

if __name__ == "__main__":
    app()
