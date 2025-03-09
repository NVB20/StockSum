pipeline {
    agent any
    
    environment {
        // Define Docker image information
        DOCKER_IMAGE_NAME = 'my-application'
        DOCKER_IMAGE_TAG = 'latest'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // This will check out the repository where the Jenkinsfile is located
                checkout scm
                echo 'Git repository checkout complete'
                
            }
        }
        stage('Python Install') {
            docker {
                image 'python:latest'
        }
      }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image using the Dockerfile in the repo
                    // If using a private registry, use: "${DOCKER_REGISTRY}/${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}"
                    sh "docker build -t ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} ."
                    
                    // Also tag as latest
                    sh "docker tag ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} ${DOCKER_IMAGE_NAME}:latest"
                    
                    echo 'Docker image build complete'
                }
            }
        }
           
        stage('Clean Up') {
            steps {
                // Remove local Docker images to save space
                sh "docker rmi ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}"
                sh "docker rmi ${DOCKER_IMAGE_NAME}:latest"
                
                echo 'Cleanup complete'
            }
        }
    }
    
    post {
        success {
            echo "Pipeline completed successfully. Docker image ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} was built and pushed."
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}