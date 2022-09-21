# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

#set work directory
WORKDIR /project

# RUN ls .

RUN python -m pip install --upgrade pip

COPY /hello-django /project

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


VOLUME /project

EXPOSE 8080
EXPOSE 8000

# CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]