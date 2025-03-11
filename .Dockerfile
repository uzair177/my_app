#Use python latest as base image
FROM python:3.9-slim

#Set working directory in the container
WORKDIR /app

#Copy requirements file in the container 
COPY requirements.txt .

#Install any needed packgae mention in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
