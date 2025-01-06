FROM python:3.11
WORKDIR /reinn
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./reinn ./reinn
COPY ./tests ./tests
CMD ["uvicorn", "reinn.__main__:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
