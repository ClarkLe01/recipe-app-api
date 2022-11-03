# recipe-app-api
#### B1 - check run flake8 to check pep 8: docker-compose run --rm app sh -c "flake8" to check pep8 
#### B2 - Init project: docker-compose run --rm app sh -c "django-admin startproject app ."
#### B3 - create app: docker-compose run --rm app sh -c "python manage.py startapp core" 
#### B4 - Set db, test, command: docker-compose run --rm app sh -c "python manage.py test"
#### B5 - test and check flake8: docker-compose run --rm app sh -c "python manage.py wait_for_db && flake8"
