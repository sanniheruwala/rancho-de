# install requirements

install:
	pip install -r requirements.txt

# run the app

run:
	python3 main.py

# run the app in debug mode

debug:
	python3 main.py debug

# run the tests

unit-test:
	python3 -m pytest tests/unit