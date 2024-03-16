#template
FROM  python:3.8.12-slim

#grab files from folder and put into container
#take package folder and copy into the container
#with the same name
COPY package_folder package_folder
COPY requirements.txt requirements.txt
COPY models models
COPY Streamlit_Interface Streamlit_Interface
COPY notebooks notebooks

#terminal command that we want when image is built

RUN pip install -r requirements.txt

#run container LOCALLY
#CMD uvicorn package_folder.api_file:app --host 0.0.0.0

#run container DEPLOYED

CMD uvicorn package_folder.api_file:app --host 0.0.0.0 --port $PORT
