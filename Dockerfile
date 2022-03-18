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

# Upgrading pip.
RUN python3 -m pip install --upgrade pip setuptools wheel

# To install GCC. This will run in terminal.
RUN apk add build-base

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev \
    && apk add libpq jpeg-dev zlib-dev libjpeg \
    && apk add --update libffi \
    && apk add --update --no-cache g++ libxml2-dev libxslt-dev libffi-dev openssl-dev make

# Copy requirements.txt to the image.
COPY requirements.txt requirements.txt

# Install Python packages.
# RUN pip3 install -r requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all django files from present HOST dir to current working dir (/app) of docker image.
COPY . .

RUN \
    apk add tzdata \
    && cp /usr/share/zoneinfo/Asia/Kolkata /etc/localtime \
    && echo "Asia/Kolkata" >  /etc/timezone \
    && apk del tzdata

# Run this command in linux terminal.
# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

# Running project using uvicorn.
# man page: `uvicorn --help`
# CMD [ "uvicorn", "salahtimetable.asgi:application", "--host", "0.0.0.0", "--port", "8000" ]

# Running project using uvicorn with logging.
# critical/fatal: the crucial part of the application is not working, so a total failure. [OR] Severe error that will prevent the application from continuing.
# error: Error events that might still allow the application to continue running. [OR] Record of critical errors that are encountered.
# warning: Event that may result in future problems/errors.
# info: day-to-day operation as "proof" that program is performing its function as designed.
# debug: Fine-grained informational events that are most useful to debug an application. [OR] information important for troubleshooting, and usually suppressed in normal day-to-day operation.
# trace: finer-grained informational events than the DEBUG. [OR] Fine-grained debug message, typically capturing the flow through the application.

# --log-level <str>: Options: 'critical', 'error', 'warning', 'info', 'debug', 'trace'. Default: 'info'.
CMD [ "uvicorn", "salahtimetable.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--use-colors", "--log-level", "info" ]


# RUN chmod +x pythonscript.sh
# CMD ["./pythonscript.sh"]

# COPY ./entrypoint.sh /app/
# ENTRYPOINT [ "sh", "./entrypoint.sh" ]