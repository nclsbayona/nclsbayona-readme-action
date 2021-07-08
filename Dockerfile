FROM python:3

WORKDIR /readme_action

ADD main.py .

ADD directory_file .

ADD requirements.txt .

RUN chmod +x ./main.py

RUN python -m pip install --upgrade pip wheel setuptools

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
