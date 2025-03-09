pipeline {
    agent any

    environment {
        IMAGE_NAME = 'stock-docker'
        CONTAINER_NAME = 'stock-docker-container'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${IMAGE_NAME} .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run the container with the image and execute the test
                    sh """
                        docker run --rm -v \$(pwd)/tests:/app/tests ${IMAGE_NAME} python3 /app/tests/flask_test.py
                    """
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker containers/images if necessary
            sh 'docker system prune -f'
        }
    }
}
