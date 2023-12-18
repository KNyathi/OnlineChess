FROM python:3.11

MAINTAINER ChessTeamBVT2201

ENV ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE chess_project.settings
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /chessapp

#COPY ./entrypoint.sh .

WORKDIR /chessapp/chess_project
ENTRYPOINT ["sh", "/chessapp/entrypoint.sh"]

