FROM python:latest

RUN pip install pytest pytest-cov

cmd [ 'sleep', 'infinity' ]