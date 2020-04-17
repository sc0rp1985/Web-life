FROM python:3.8

run mkdir -p /var/www/WebLife
workdir /var/www/WebLife
copy . /var/www/WebLife
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080

ENV STATIC_URL /Static
ENV STATIC_PATH /var/www/WebLife/Static
ENV MONGO_DB_NAME LifeCache

cmd ["python", "webapp.py" ]