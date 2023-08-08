install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py
lint:
	pylint --disable=R,C,W1203,W0703 *.py
test:
	python -m pytest -vv --cov=app test_app.py