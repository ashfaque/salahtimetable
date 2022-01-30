# docker build --tag salahbackend:1.0 .
# docker build --tag salahtimetable_salahbackend:latest .
# docker run --publish 8000:8000 salahtimetable_salahbackend
# sudo docker run -it salahtimetable_salahbackend sh
# To remove dangling <none> images use -----> docker rmi $(docker images -f "dangling=true" -q)
# ---------------------------------------------------------------------------------------------

# Build the application.
FROM python:3.6-alpine3.15

# Set the current working directory inside the image.
WORKDIR /app

RUN python3 -m pip install --upgrade pip

# To install GCC. This will run in terminal.
RUN apk add build-base

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

# Copy requirements.txt to the image.
COPY requirements.txt requirements.txt

# Install Python packages.
RUN pip3 install -r requirements.txt

# Copy all django files from present HOST dir to current working dir (/app) of docker image.
COPY . .

# Run this command in linux terminal.
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
# RUN chmod +x pythonscript.sh
# CMD ["./pythonscript.sh"]