FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /haute_hiker
WORKDIR /haute_hiker
COPY requirements.txt /haute_hiker/
RUN pip install -r requirements.txt
COPY . /haute_hiker/
