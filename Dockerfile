FROM python:3.11-slim

# Set working directory
WORKDIR /app
RUN chmod +x /run.sh
# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the app code
COPY . /app/

# Expose port for the UI
EXPOSE 8080

# Run the application
CMD ["bash", "/app/run.sh"]
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the app code
COPY . /app/

# Expose port for the UI
EXPOSE 8080

# Run the application
CMD ["bash", "/app/run.sh"]
