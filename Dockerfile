# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only necessary files (this can help with better caching during builds)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files (including templates and static files)
COPY . /app

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
