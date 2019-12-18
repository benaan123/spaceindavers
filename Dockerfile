FROM python:3.7

workdir /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "./spaceinvanders.py"]

