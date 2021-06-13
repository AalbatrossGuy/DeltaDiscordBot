FROM python:3.9

WORKDIR /DeltaBot

COPY requirements.txt /DeltaBot/requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["./start.sh"]

