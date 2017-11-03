
# Install Python 3 Docker image
FROM python:3

# Create a work directory
WORKDIR /usr/src/app

# install project depandencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy working files to the image
COPY . .

# Run the project
CMD [ "python", "./scripts/main.py" ]
