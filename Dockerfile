FROM python:3

COPY . /readme_action

WORKDIR /readme_action

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]