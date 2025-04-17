# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only necessary files (this can help with better caching during builds)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . /app

# Expose the specific port (e.g., 8080)
EXPOSE 8080

# Run the application on port 8080
CMD ["python", "app.py"]
