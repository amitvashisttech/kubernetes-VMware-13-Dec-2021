# Base Image 
FROM python:2.7-slim

# Work DIR 
WORKDIR /app

# Copy all the config
ADD . /app

# Install Packages via PIP 
RUN pip install --trusted-host pypi.python.org -r req.txt 

# Expose on Port 
EXPOSE 8081

# Bring Up my App 
CMD ["python", "app.py"]
