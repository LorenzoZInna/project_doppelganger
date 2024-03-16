#template
FROM python:3.8.12-slim

# Set a default port number (you can change this if needed)
ENV PORT=8504

# Grab files from folder and put into container
COPY package_folder package_folder
COPY requirements.txt requirements.txt
COPY models models
COPY Streamlit_Interface Streamlit_Interface
COPY notebooks notebooks

# Terminal command that we want when image is built
RUN pip install -r requirements.txt

# Run container with the specified port
CMD uvicorn package_folder.api_file:app --host 0.0.0.0 --port $PORT
