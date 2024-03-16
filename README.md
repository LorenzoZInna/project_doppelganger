# Project Doppelganger

Project Doppelganger is a data science project that utilizes facial recognition technology to analyze facial expressions and predict emotions. Based on the detected emotion, the application matches the user with a song from a curated playlist on Spotify that reflects their mood.

<img src="https://i.ibb.co/N9zL3dB/pixlr-image-generator-87f2b805-7f1c-4295-ab97-78fff6e53dbd.png" width="700px;"/>



## Features
- **Facial Emotion Analysis**: Utilizes machine learning algorithms to analyze facial expressions and predict the user's emotion.
  
- **Spotify Integration**: Matches the user's emotion with a song from a curated playlist on Spotify that corresponds to their mood.

- **User Interaction**: Users can upload their photos and receive personalized song recommendations based on their facial expression.

- **Feedback Loop**: Allows users to rate the accuracy of the emotion prediction and provide feedback on the recommended songs. 
<img src="https://i.ibb.co/Df607BN/pixlr-image-generator-eda7a538-ed68-4f21-8a85-41ec80ba191b.png" width="700px;"/>


## Technology Used
- **Facial Recognition**: OpenCV, DLib, TensorFlow for facial feature detection and emotion analysis
  
- **Machine Learning**: Python libraries such as scikit-learn, TensorFlow for training emotion recognition models
  
- **Integration**: Spotify API for retrieving song recommendations based on user emotion
  

  

## Clone the project
To run the project locally, follow these steps:
Clone the project:
  ```bash
   git clone https://github.com/LorenzoZInna/project_doppelganger.git


   cd project_doppelganger
   ```
## Installation
Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
## Startup the project
Run the application using the Makefile:

 **Build Container Locally**: This target builds the Docker container locally.

   ```bash
   make build_container_local
   ```

 **Run Container Locally**: This target runs the Docker container locally.

   ```bash
   make run_container_local
   ```

Access the application in your web browser at `http://localhost:8000`.

### Building and Deploying Docker Image to Google Cloud Run

To deploy your application to Google Cloud Run, you can follow these steps:

1. **Authenticate Docker with Google Cloud Registry:**

   Before pushing the Docker image to Google Cloud Registry, you need to authenticate Docker with Google Cloud. Run the following command:

   ```bash
   make allow_docker_push
   ```

2. **Create Artifacts Repository:**

   You need to create an artifacts repository on Google Cloud to store your Docker images. Run the following command:

   ```bash
   make create_artifacts_repo
   ```

3. **Build Docker Image for Production:**

   Build the Docker image for production using the following command:

   ```bash
   make build_for_production
   ```

   This command will build the Docker image with the tag `$$GCP_REGION-docker.pkg.dev/$$GCP_PROJECT/$$ARTIFACTSREPO/$$IMAGE:prod`.

4. **Push Docker Image to Google Cloud Registry:**

   Push the Docker image to Google Cloud Registry using the following command:

   ```bash
   make push_image_production
   ```

   This command will push the Docker image to Google Cloud Registry.





## Contributors

<img src="https://github.com/LorenzoZInna.png" width="100px;"/>
<img src="https://github.com/Nil-Barcons.png" width="100px;"/> 
<img src="https://github.com/nmatalka.png" width="100px;"/> 
<img src="https://github.com/danecks.png" width="100px;"/> 
<img src="https://github.com/jb-paris.png" width="100px;"/>



