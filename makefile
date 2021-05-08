ENV=development
REQUIREMENTS=requirements/development.txt


all: clean install load
dev: test lint


run:
	python manage.py


clean:
	rm -rf venv
	rm -Rf .pytest_cache
	rm -Rf __pycache__
	rm -Rf */*/__pycache__
	find tests -type f -name "*-test.json" -delete
	find . -type f -name "*.pyc" -delete


coverage:
	coverage run --omit 'venv/*' -m pytest tests/ -v
	make test-report


test-report:
	coverage report -m
	coverage html


lint:
	flake8 --exclude=venv


lint-statistics:
	flake8 . --exclude=venv --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --exclude=venv --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics


load:
ifeq ($(ENV), development)
	bash -c "source venv/bin/activate"
endif


install-dev:
	python -m virtualenv venv
	chmod +x venv/bin/activate
	make load && ./venv/bin/pip install -r requirements/development.txt


install-prod:
	pip install -r requirements/production.txt

install-test:
	pip install -r requirements/test.txt


install:
ifeq ($(ENV), development)
	make install-dev
endif
ifeq ($(ENV), production)
	make install-prod
endif
ifeq ($(ENV), test)
	make install-test
endif
ifeq ($(ENV), undefined)
	make install-dev
endif


unit-test:
	python -m unittest discover -v -s tests/unit


integration-test:
	python -m unittest discover -v -s tests/integration


test:
ifeq ($(ENV), development)
	make unit-test
endif
ifeq ($(ENV), local)
	make unit-test
endif
ifeq ($(ENV), test)
	make unit-test
	make integration-test
endif
ifeq ($(ENV), undefined)
	make unit-test
endif
