FROM python:3.6.6-alpine 
COPY backbone /app 
WORKDIR /app 
RUN pip3 install -r requirements.txt
EXPOSE 3002
ENTRYPOINT ["python3"] 
CMD ["backbone.py"]