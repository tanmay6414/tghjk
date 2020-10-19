FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /satav
COPY ./requirement.txt /requirement.txt
RUN pip install -r /requirement.txt
COPY ./satav/ ./
EXPOSE 8080

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080"]