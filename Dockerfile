FROM python:3
ADD . /server
WORKDIR /server
RUN python -m pip install -r ./requirements.txt
ENTRYPOINT ["python"]
CMD [python -m ./src/app.py]
