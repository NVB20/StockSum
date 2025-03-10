pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git repository
                checkout scm
                
                // Print information about the checked out repository
                sh "git log -1"
                sh "git branch"
                sh "ls -la"
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo "Building the Docker Image..."
                sh 'docker build -t testerying .'
            }
        }
        
        stage('Test') {
            steps {
                echo "Running tests..."
                // Add your test commands here
            }
        }
        
        stage('Cleanup') {
            steps {
                script {
                    sh 'docker rmi -f $IMAGE_NAME || true'
                }
            }
        }
    }
    
    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline execution failed!"
        }
    }
}