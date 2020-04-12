FROM python:latest

WORKDIR /app

COPY app/requirements.txt /app
RUN pip3 install -r requirements.txt

COPY app ./app

# HERE copy your react-app into the 
#COPY --from=react-builder /app/build ./app/dilcms/serve-folder

CMD ["python3", "./app/index.py"]
