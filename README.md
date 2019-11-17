# MPharma CRUD

This is CRUD Restful API written in Python, using the Flask web micro-framework and a SQLite database.

## Dependencies

Dependencies are managed with Pipenv.

First, create a Pipenv shell with the command `pipenv shell` at the root of the folder and use `pipenv install` to install all dependencies.

## Database Setup

Run the following commands to create the migrations folder, migrate the db and populate the database.

```
python migrate.py db init
python migrate.py db migrate
python migrate.py db upgrade
```

## Starting the app and API endpoints

Start the app with `python migrate.py runserver`. Below are the available endpoints and the **cURL** commands to test them:

### POST *http://127.0.0.1:5000/api/diagnosis*

```
curl -X POST -H "Content-Type: application/json" -d '{"category_code":"A0", "diagnosis_code":"1234", "full_code":"A01234", "abbreviated_description":"Comma-ind anal ret", "full_description":"Comma-induced anal retention", "category_title":"Malignant neoplasm of anus and anal canal"}' http://127.0.0.1:5000/api/diagnosis
```

### GET *http://127.0.0.1:5000/api/diagnosis*

```
curl -X GET http://127.0.0.1:5000/api/diagnosis
```

### DELETE *http://127.0.0.1:5000/api/diagnosis*

```
curl -X DELETE -H "Content-Type: application/json" -d '{"id": "1", "category_code":"A0", "diagnosis_code":"1234", "full_code":"A01234", "abbreviated_description":"Comma-ind anal ret", "full_description":"Comma-induced anal retention", "category_title":"Malignant neoplasm of anus and anal canal"}' http://127.0.0.1:5000/api/diagnosis
```

### PUT *http://127.0.0.1:5000/api/diagnosis*

```
curl -X PUT -H "Content-Type: application/json" -d '{"id": "1", "category_code":"A0", "diagnosis_code":"1234", "full_code":"A01234", "abbreviated_description":"Comma-ind anal rets", "full_description":"Comma-induced anal retention", "category_title":"Malignant neoplasm of anus"}' http://127.0.0.1:5000/api/diagnosis
```

## Author

Oyekunle Oloyede
