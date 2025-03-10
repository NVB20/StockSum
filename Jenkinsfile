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
                sh 'ls -la'
                
            }
        }
        
    post {
        success {
            echo "Pipeline completed successfully. Docker image was built and pushed."
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}