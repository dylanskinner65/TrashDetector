FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy only the TrashDetector directory from your local machine to the /app directory in the container
COPY TrashDetector/ /app/

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "/app/TrashDetector/app.py", "--server.port=8501", "--server.address=0.0.0.0"]

