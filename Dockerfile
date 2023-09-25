FROM docker.io/python:3

ADD main.py /main.py

ADD directory_file /directory_file

ADD requirements.txt /requirements.txt

RUN chmod +x /main.py

RUN python -m pip install --upgrade pip wheel setuptools

ENV WAKATIME_API_KEY = 0
ENV NASA_KEY = 0
ENV GH_TOKEN = 0

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "/main.py" ]
