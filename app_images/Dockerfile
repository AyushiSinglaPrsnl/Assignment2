FROM python:3.6-slim
COPY . /app
WORKDIR /app
RUN pip install -r app_images/requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "src/app.py" ]