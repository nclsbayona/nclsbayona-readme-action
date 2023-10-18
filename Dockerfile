#### 
FROM debian:12
RUN apt-get update
RUN apt-get install python3 python-is-python3 python3-full python3-pip -y
####

ADD main.py /main.py

ADD directory_file /directory_file

ADD requirements.txt /requirements.txt

RUN chmod +x /main.py

# RUN python -m pip install --upgrade pip wheel setuptools

RUN python -m pip install --no-cache-dir --requirement requirements.txt

ENTRYPOINT [ "python", "/main.py" ]
