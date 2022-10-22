run:
	docker compose up -d

build:
	docker compose build

down:
	docker compose down

# .PHONY: logindocker
# logindocker:
# 	docker compose exec mysql /bin/bash

.PHONY: login
login:
	mysql -u root -h 127.0.0.1 -P 4306 -p

.PHONY: logs
logs:
	docker compose logs -ft
