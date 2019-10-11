default:
	python3 extract.py

install:
	pip3 install -r requirements.txt

clear:
	rm -rf convert_todoist2markdown/__pycache__
