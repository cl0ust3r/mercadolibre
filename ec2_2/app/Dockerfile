FROM python:3.6.4-slim
RUN apt-get update && apt-get install -y telnet curl
WORKDIR /app
ADD . /app
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
CMD ["python", "service.py"]
