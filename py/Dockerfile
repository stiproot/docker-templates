FROM python:3.11.4-alpine3.18 as base
  RUN apk update && apk add nginx
  COPY nginx.conf /etc/nginx/http.d/default.conf

FROM base as requirements
  RUN mkdir /app
  COPY requirements.txt /app/
  RUN pip install --no-cache-dir -r /app/requirements.txt

FROM requirements as app
  COPY app/ /app/
  COPY entrypoint.sh /
  RUN chmod +x /entrypoint.sh

FROM app as final
  EXPOSE 8080
  WORKDIR /
  CMD ["/bin/sh", "entrypoint.sh"]
