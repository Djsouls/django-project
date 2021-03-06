# Django tutorial project
This project was made following the [Django tutorial](https://docs.djangoproject.com/pt-br/3.2/intro/tutorial01/). Besides the `mysite`, an app for polls (conveniently called `polls`) is also available.

The purpose here is to learn about the Django core in practice, while giving my own twists to the project.

## Running
Currently you have two options for running the project, either locally or via `docker` container.

### Locally
Run `pip install -r requirements.txt` to install the dependencies to you local machine, or create a virtual environment and run the same command in the virtual environment shell.

After installing the dependencies, just run:
```
python manage.py runserver
```

And the app should be accessible via `localhost:8000`.

### Docker
Make sure you have `docker` installed in you machine and run:
```
docker build . -t django-project
```
Here `django-project` is just a placeholder for your image name, you can put whatever you want. Then, after the building is complete, run the container:
```
docker run -p 8000:8000 django-project
```

And it's done, after the running process is complete, the app should be accessible via `localhost:8000`.

## About .env file
This file should NOT be here, the only reason he's in the upstream repo is for facilitating a quick approach to run and test the application. Ideally, every deploy of the project should have it's own .env file with the respectives environment variables, following the [12 factor philosophy](https://12factor.net/config).

## Testing
As for now, testing is only available locally, but later on it will also be containerized.

### Preparing
Before running the tests, we need to make sure that Django will be able to construct a temporary database for our testing data, the way we do this is providing our app some `migrations`. Run `python manage.py makemigrations` and the magic is done, what this command will do is creating `.py` files describing our database structure, based on the `models` provided. A `db.sqlite3` will also be created at the root of the project, don't worry about it now.

If you want more information about this structure, run `python manage.py sqlmigrate <migration_id>` and the SQL used to create the tables will be outputed in the terminal (since this is probably your first migration, `<migration_id>` likely is going to be `0001`). 

### Running
Now that Django know's how to create our test database all we gotta do is execute:
```
python manage.py test polls
```

And the tests for our `polls` application will run.
