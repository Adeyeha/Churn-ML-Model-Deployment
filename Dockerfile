FROM python
 
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY ./app /code/app

#CMD ["uvicorn", "app.main:app", "--host", "172.16.1.70", "--port", "80"]