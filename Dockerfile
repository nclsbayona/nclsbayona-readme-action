FROM docker.io/python:3

COPY main.py /main.py

COPY directory_file /directory_file

COPY requirements.txt /requirements.txt

RUN chmod +x /main.py

RUN python -m pip install --upgrade pip wheel setuptools

ENV WAKATIME_API_KEY = 0
ENV NASA_KEY = 0
ENV GH_TOKEN = 0

RUN pip install --no-cache-dir --requirement requirements.txt

ENTRYPOINT [ "python", "/main.py" ]
