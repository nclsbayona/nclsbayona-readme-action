# Use a specific version of the Python image from Docker Hub
FROM docker.io/python:3

# Copy the main.py file to the root directory of the container
COPY main.py /main.py

# Copy the directory_file directory to the root directory of the container
COPY directory_file /directory_file

# Copy the requirements.txt file to the root directory of the container
COPY requirements.txt /requirements.txt

# Make the main.py file executable
RUN chmod +x /main.py

# Upgrade pip, wheel, and setuptools
RUN python -m pip install --upgrade pip wheel setuptools

# Set environment variables for API keys
ENV WAKATIME_API_KEY=0
ENV NASA_KEY=0
ENV GH_TOKEN=0

# Install Python dependencies from requirements.txt without caching
RUN pip install --no-cache-dir -r /requirements.txt

# Specify the entry point for the container
ENTRYPOINT ["python", "/main.py"]
