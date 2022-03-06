# To remove dangling <none> images use -----> docker rmi $(docker images -f "dangling=true" -q)
# Python versions for, bullseye ---> 3.9, buster ---> 3.7, stretch ---> 3.5.3
# ---------------------------------------------------------------------------------------------

# Build the application.
FROM redis:6.2.6-buster AS redis5-debian10

RUN \
    apt update \
    && apt install python3-dev -y \
    && apt install python3-pip -y \
    && python3 -m pip install --upgrade pip setuptools wheel

# Set the current working directory inside the image.
WORKDIR /root

# Copy requirements.txt to the image.
COPY ./email_requirements.txt /root/email_requirements.txt

# Install Python packages.
RUN pip3 install --no-cache-dir -r /root/email_requirements.txt

COPY ./email_service.py /root/email_service.py

RUN mkdir /root/salahtimetable

COPY ./salahtimetable/settings.py /root/salahtimetable/settings.py

WORKDIR /data

RUN \
    rm -rf /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Kolkata /etc/localtime

# --save(snapshotting RDB): saves snapshots of the dataset on disk, in a binary file called dump.rdb every 10 seconds if there is atleast 1 changes in the datasets. --appendonly(AOF): Every time Redis receives a command that changes the dataset (e.g. SET) it will append it to the AOF. When you restart Redis it will re-play the AOF to rebuild the state. [debug: (a lot of information, useful for development/testing)], [verbose: (includes information not often needed, but logs less than debug)], [notice: (moderately verbose, ideal for production environments)], [warning: (only very important / critical messages are logged)]
CMD [ "redis-server", "--save", "10", "1", "--appendonly", "yes", "--loglevel", "debug", "--requirepass", "zUXY8FuZppzQHDPntNwxQVga9pTe5f74" ]
