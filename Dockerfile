#Template
FROM python:3.8.12-slim

# Grab files from folder and put into container
COPY Test_package_folder Test_package_folder
COPY requirements.txt requirements.txt
COPY models models
COPY Streamlit_Interface Streamlit_Interface

# Terminal command that we want when image is built
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Run container with the specified port
CMD uvicorn Test_package_folder.api_backend:app --host 0.0.0.0

# Run container with the specified port
#CMD uvicorn Test_package_folder.api_backend:app --host 0.0.0.0 --port $PORT
