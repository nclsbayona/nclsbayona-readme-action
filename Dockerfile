FROM python:3

COPY . /readme_action

WORKDIR /readme_action

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x ./main.py

CMD [ "python", "./main.py" ]