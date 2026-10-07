install:
	pip install -r requirements.txt

test:
	pytest -q

run:
	uvicorn app.main:app --reload

docker-build:
	docker build -t dockerized-cicd-app:local .

docker-run:
	docker run --rm -p 8000:8000 dockerized-cicd-app:local

compose-up:
	docker compose up --build
