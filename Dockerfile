
# Install Python 3 in Docker image
FROM python:3

# Add Project files to Docker image
ADD scripts /
ADD requirements.txt /

# install project depandencies in Docker image
RUN pip install -r requirements.txt

# Run the project in Docker image
CMD [ "python", "./scripts/main.py" ]
