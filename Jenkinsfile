pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-stock'
        CONTAINER_NAME = 'stock-cont'
    }
    
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
                sh 'docker build -t $IMAGE_NAME .'
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    sh "docker run --rm --name $CONTAINER_NAME $IMAGE_NAME pytest tests/flask_test.py --junitxml=results.xml"
                }
            }
        }
        
        stage('Cleanup') {
            steps {
                script {
                    echo "Cleaning up!"
                    sh 'docker rmi -f $IMAGE_NAME || true'
                }
            }
        }
    }
    
    post {
        success {
            echo "Pipeline executed successfully!"
            jiraAddComment comment: 'mission executed successfully!', issueKey: 'CPG-8'
        }
        failure {
            echo "Pipeline execution failed!"
            jiraAddComment comment: 'mission failed', issueKey: 'CPG-8'
        }
    }
}