# recipe-app-api
    - check run flake8 to check pep 8: docker-compose run --rm app sh -c "flake8" to check pep8
    - Init project: docker-compose run --rm app sh -c "django-admin startproject app ."
    - create app: docker-compose run --rm app sh -c "python manage.py startapp core" 
    - Set db, test, command: docker-compose run --rm app sh -c "python manage.py test"
    - test and check flake8: docker-compose run --rm app sh -c "python manage.py wait_for_db && flake8"
    - List volume docker: docker volume ls
    - List volume docker: docker volume rm <volume_name>"
    - wait_for_db and migrate: docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
