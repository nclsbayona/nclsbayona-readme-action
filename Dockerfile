#### 
FROM docker.io/debian:12
RUN apt-get update
RUN apt-get install python3 python-is-python3 python3-full python3-pip -y
####

# Set the Working directory
WORKDIR /

# Copy the main.py file to the root directory of the container
COPY main.py /main.py

# Copy the directory_file directory to the root directory of the container
COPY directory_file /directory_file

# Copy the requirements.txt file to the root directory of the container
COPY requirements.txt /requirements.txt

# Make the main.py file executable
RUN chmod +x /main.py

# Set environment variables for API keys
ENV WAKATIME_API_KEY=0
ENV NASA_KEY=0
ENV GH_TOKEN=0
# ENV NEWS_API_KEY=0

# Install Python dependencies from requirements.txt without caching
RUN python -m venv .venv && .venv/bin/pip install --no-cache-dir --requirement requirements.txt

# Specify the entry point for the container
ENTRYPOINT [ "/.venv/bin/python", "/main.py" ]
