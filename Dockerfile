FROM python:3

COPY . /readme_action

WORKDIR /readme_action

RUN chmod +x ./main.py

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
