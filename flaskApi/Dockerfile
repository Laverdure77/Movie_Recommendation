FROM python:3.10.1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

# Update pip 
RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5100

CMD ["python", "app.py"]