# sample project

```
docker-compose run --rm testserver
docker-compose run --rm testserver bash -c "python -m pytest --cov-report term --cov-report html:coverage --cov-config setup.cfg --cov=src/ test/"
docker-compose run --rm server bash -c "python -m flake8 ./src ./test"
```
