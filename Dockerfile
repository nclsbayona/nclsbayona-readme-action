FROM python:3

COPY . /readme_action

WORKDIR /readme_action

RUN chmod +x ./main.py

RUN python -m pip install --upgrade pip wheel setuptools

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
