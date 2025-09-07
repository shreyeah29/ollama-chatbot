# Use Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy requirements if you have it, else install manually later
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
