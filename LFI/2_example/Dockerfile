FROM ubuntu:latest


RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean


RUN python3 -m venv /venv


ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


RUN pip install Flask


WORKDIR /app


COPY .. /app

EXPOSE 5000

CMD ["python", "main.py"]