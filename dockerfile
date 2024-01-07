# Using a python image
FROM python:3.8

# Setting the working dir
WORKDIR /usr/src/app

# Copy the python script to working dir
COPY ./python_task/ .

# Command to run when container starst
CMD ["python", "./python_script.py"]
