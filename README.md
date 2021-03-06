# salahtimetable
settings.py file not included in this repo. See `gist`.

### Clone this repo and navigate to the root directory of this project where the [docker-compose.yaml](docker-compose.yaml) file is located.
- Create migrations/ directory in [months](months/) app with empty [__init__.py](months/__init__.py) inside it.
- Have docker installed in your system and run this command to start the container: `docker-compose up --build`.

# Do these after first clone
- Have `docker` & `docker-compose` installed in your system.
- Create a directory called `migrations` in each & every app. In linux do give it all the necessary permissions with `chmod`. And also create an empty file called [\_\_init\_\_.py](salahtimetable/__init__.py) inside this newly created directory.
- Make two directories called `static` & `staticfiles` in [root directory of this project](/)
- Navigate to the root directory of this project in terminal & do a `docker-compose up --build`.
- Open a new terminal instance & go inside the backend container using this command ---> `docker-compose exec salahbackend sh`.
- Inside the backend container run these & do accept all the prompts.
    + `python3 manage.py makemigrations`
    + `python3 manage.py migrate`
    + `python3 manage.py createsuperuser`
    + `python manage.py collectstatic`

# Running a fresh instance of this project already running in your system
- In a new terminal instance do a `docker-compose down`.
- Delete all the contents inside all the `migrations` directory except the [\_\_init\_\_.py](salahtimetable/__init__.py) in it.
- Delete a directory called `.dbdata` in the root directory of this project.
- Run this command to see the container name ---> `docker container ls -a`.
- Run this command to delete the container ---> `docker rm <container_name>`.
- Run this command to see the image name ---> `docker images`.
- Run this command to delete the existing image ---> `docker image rm <image_name>`.
- Run this to build & run a fresh instance of the container ---> `docker-compose up --build`.
- Open a new terminal instance & go inside the backend container using this command ---> `docker-compose exec salahbackend sh`.
- Inside the backend container run these & do accept all the prompts.
    + `python3 manage.py makemigrations`
    + `python3 manage.py migrate`
    + `python3 manage.py createsuperuser`
    + `python manage.py collectstatic`

## Updating code in the server :-
- Navigate to the project [root directory](/).
- First check the branch with `git branch` then do a `git pull origin master`.
- Copy the `settings.py` file.
- Do `docker-compose down`.
- Switch to the `screen` in which this project is running.
- Then do `docker-compose up --build` in that `screen`.
- Go back to the main terminal. Go inside the backend terminal and do migrations if needed.

#### NB: If any of the docker commands throws an error run it with `sudo`.
#### NB: Starting with Docker Desktop 3.4.0, you can run Compose V2 commands. Instead of `docker-compose` you can use `docker compose` without a `-` in between. To disable Docker Compose V2 using the CLI, run: `docker-compose disable-v2`.
