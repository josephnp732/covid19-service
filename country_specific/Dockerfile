FROM python:3.6.6-alpine 
COPY country /app 
WORKDIR /app 
RUN pip3 install -r requirements.txt
EXPOSE 3003
ENTRYPOINT ["python3"] 
CMD ["country_specific.py"]