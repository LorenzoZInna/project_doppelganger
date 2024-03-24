# Project Doppelganger
![bg](https://github.com/MunawarJohar/project_doppelganger/assets/106137102/41618950-72be-4e81-b623-eba7b4f6498f)


Project Doppelganger is a data science project that utilizes facial recognition technology to analyze facial expressions and predict emotions. Based on the detected emotion, the application matches the user with a song from a curated playlist on Spotify that reflects their mood.


## Features
- **Facial Emotion Analysis**: Utilizes machine learning algorithms to analyze facial expressions and predict the user's emotion.
  
- **Spotify Integration**: Matches the user's emotion with a song from a curated playlist on Spotify that corresponds to their mood.

- **User Interaction**: Users can upload their photos and receive personalized song recommendations based on their facial expression.

- **Feedback Loop**: Allows users to rate the accuracy of the emotion prediction and provide feedback on the recommended songs. 

![features](https://github.com/MunawarJohar/project_doppelganger/assets/106137102/a3faa81b-eb84-4e27-a163-fdff05af6168)


## Technology Used
- **Facial Recognition**: OpenCV, DLib, TensorFlow for facial feature detection and emotion analysis
  
- **Machine Learning**: Python libraries such as scikit-learn, TensorFlow for training emotion recognition models
  
- **Integration**: Spotify API for retrieving song recommendations based on user emotion
  


## Contributors
This project was created by the following contributors as a part of Le Wagon Data Science #1455:

- [Daniel Alejandro Bernal Eckstein](https://github.com/danecks)
- [Jean-Baptiste](https://github.com/jb-paris)
- [Lorenzo Zinna](https://github.com/LorenzoZInna)
- [Nil Barcons](https://github.com/Nil-Barcons)
- [Noor Matalka](https://github.com/nmatalka)
![contribute](https://github.com/MunawarJohar/project_doppelganger/assets/106137102/1b2c97c7-789f-4558-8773-1f829692ffa2)

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
  


## Install
Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
Clone the project and install it:
To run the project locally, follow these steps:
Clone the project:
  ```bash
   git clone https://github.com/LorenzoZInna/project_doppelganger.git


