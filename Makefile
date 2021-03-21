build:
	docker-compose build

.PHONY: up
up:
	docker-compose up --remove-orphans app

.PHONY: db
db:
	docker-compose up --remove-orphans postgres


.PHONY: db-d
db-d:
	docker-compose up -d --remove-orphans postgres

.PHONY: down
down:
	docker-compose down

.PHONY: test
test:
	docker-compose -f docker-compose-testing.yml up

.PHONY: test-db
test-db:
	docker-compose -f docker-compose-testing.yml up test_pg

.PHONY: down-test
down-test:
	docker-compose -f docker-compose-testing.yml down --remove-orphans

.PHONY: prune
prune:
	docker system prune -f

.PHONY: flask
flask:
	make db-d && flask run

.PHONY: upgrade
upgrade:
	make db-d; \
	flask db upgrade;

.PHONY: migrate
migrate:
	make upgrade; \
	flask db migrate -m "$(m)";
