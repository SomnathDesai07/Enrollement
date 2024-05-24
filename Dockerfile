FROM python:3.9.13
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
COPY static/enroll_app/css /app/static/enroll_app/css
COPY static/enroll_app/js /app/static/enroll_app/js
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY .env /app
COPY . .
