install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py mylib/*.py
lint:
	pylint --disable=R,C,W1203,W0703 *.py mylib/*.py
test:
	python -m pytest -vv --cov=mylib/calc.py --cov=cal_cli.py --cov= app.py test_calc.py test_cal_cli.py test_app.py
all: install lint test
