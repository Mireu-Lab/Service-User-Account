FROM python:3

RUN mkdir API
WORKDIR /API
COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 80
CMD [ "python3", "main.py" ]