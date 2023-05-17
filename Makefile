up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs app -f

migrate-alembic:
	docker compose exec app alembic revision --autogenerate
	docker compose exec app alembic upgrade head