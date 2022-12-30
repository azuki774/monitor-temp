container_name:=monitor-temp-client

.PHONY: build start stop start-client
build:
	docker build -t $(container_name) -f build/Dockerfile .

start:
	docker network create external-monitor-temp
	docker compose -f deployment/compose-local-db.yml up -d

stop:
	docker compose -f deployment/compose-local-db.yml down
	docker network rm external-monitor-temp

start-client:
	- docker stop monitor-temp-client
	docker compose -f deployment/compose-local-client.yml up -d
