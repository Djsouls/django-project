# Django tutorial project
This project was made following the [Django tutorial](https://docs.djangoproject.com/pt-br/3.2/intro/tutorial01/). Besides the `mysite`, an app for polls (convenently called `polls`) is also available.

The purpose here is to learn about the Django core in practice, while giving my own twists to the project.

## Running
Currently you have two options for running the project, either locally or via `docker` container.

### Locally
Run `pip install -r requirements.txt` to install the dependencies to you local machine, or create a virtual environment and run the same command in the virtual environment shell

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
