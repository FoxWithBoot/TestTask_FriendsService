# FROM python:3.10-alpine
#
# RUN mkdir -p /usr/src/app
# WORKDIR /usr/src/app/
#
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
#
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt
#
# COPY . .

FROM python:3.9.12-slim
WORKDIR /app/
COPY . .
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install -r requirements.txt
