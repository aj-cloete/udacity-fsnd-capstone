build:
	docker-compose build

.PHONY: upgrade
upgrade:
	docker-compose run --rm app flask db upgrade

.PHONY: migrate
migrate:
	make upgrade; \
	docker-compose run --rm app flask db migrate -m "$(m)"

.PHONY: up
up:
	make upgrade; \
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

.PHONY: test-upgrade
test-upgrade:
	docker-compose -f docker-compose-testing.yml up -d --remove-orphans --build test_pg; \
	docker-compose -f docker-compose-testing.yml run --rm test-app flask db upgrade; \
	docker-compose -f docker-compose-testing.yml stop

.PHONY: test
test:
	@-make down-test
	@-make test-upgrade
	docker-compose -f docker-compose-testing.yml up --remove-orphans --build test-app

.PHONY: test-db
test-db:
	docker-compose -f docker-compose-testing.yml up --remove-orphans test_pg

.PHONY: down-test
down-test:
	docker-compose -f docker-compose-testing.yml down --remove-orphans

.PHONY: tests
tests:
	@-make down-test
	@-make test-upgrade
	docker-compose -f docker-compose-testing.yml up -d --remove-orphans --build test-app
	pytest -vv

.PHONY: prune
prune:
	docker system prune -f

.PHONY: flask
flask:
	make db-d && flask run
