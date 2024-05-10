run: 
	cd src && \
	uvicorn main:app --host 0.0.0.0 --port 8000

build:
	pip install -r requirements.txt