FROM python:3.7.6

WORKDIR /opt/

COPY . /opt/

RUN pip install -r /opt/requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "/opt/app.py" ]
