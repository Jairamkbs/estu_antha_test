# Use lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Python script
COPY data_estu_hakabahudu.py .

# Run the script
CMD ["python", "data_estu_hakabahudu.py"]
