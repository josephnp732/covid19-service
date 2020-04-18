FROM python:3.6.6-alpine 
COPY all /app 
WORKDIR /app 
RUN pip3 install -r requirements.txt
EXPOSE 3001
ENTRYPOINT ["python3"] 
CMD ["all.py"]