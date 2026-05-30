# specify the runtime environment 
FROM python:3.11-slim 

# set the initial working directory 
WORKDIR /app 

# copy dependencies and install them 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

# copy the entire project (frontend + backend) into the container 
COPY . . 

# change into the backend directory 
WORKDIR /app/backend

# expose the port the app runs on 
EXPOSE 8000 

# start the server 
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]