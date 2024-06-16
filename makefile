default:
    @cat makefile

env:
    python3 -m venv env; . env/bin/activate; pip install --upgrade pip

.PYONY: update
update: env
    . env/bin/activate; pip install -r requirements.txt

.PHONY: clean
    rm -rf .ipynb_checkpoints/

