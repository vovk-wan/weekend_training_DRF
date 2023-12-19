up:
	docker-compose -f docker-compose.yml up -d
build:
	docker-compose -f docker-compose.yml up -d --build
down:
	docker-compose -f docker-compose.yml down
downv:
	docker-compose -f docker-compose.yml down -v
migrations:
	docker exec -it training_app python manage.py makemigrations
migrate:
	docker exec -it training_app python manage.py migrate
	sudo chown -R svv:svv .
super:
	docker exec -it training_app python manage.py createsuperuser
bash:
	docker exec -it training_app bash
shell:
	docker exec -it training_app python manage.py shell_plus
test:
	docker exec -it training_app python -m pytest
	#docker exec -it training_app python -m pytest core/tests/test_target_plan_api.py
lint:
	cd ./app && isort ./core && flake8 ./core
write_dump:
	docker exec training_db pg_dump training -U training > ./dumps/training.sql
read_dump:
	cat ./dumps/training.sql | docker exec -i training psql -U training
fixture:
	docker exec -it training_app python manage.py dumpdata --indent=2 core.disciplinemodel core.rssconfigmodel core.draftagreementstypesmodel  > ./app/fixtures/core.json
empty:
	docker exec -it training_app python manage.py makemigrations --empty core
