container_name:=monitoring-temp

.PHONY: build
build:
	docker build -t $(container_name) -f build/Dockerfile .

.PHONY: start
start:
	docker compose -f deployment/compose-local.yml up -d

.PHONY: stop
stop:
	docker compose -f deployment/compose-local.yml down
