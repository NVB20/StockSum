pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-stock'
        CONTAINER_NAME = 'stock-cont'
        ISSUE_KEY = 'CPG-8'
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
                jiraComment body: 'test form jenkins', issueKey: $ISSUE_KEY
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
            jiraComment body: 'Pipeline executed successfully', issueKey: '$ISSUE_KEY'
        }
        failure {
            echo "Pipeline execution failed!"
            jiraComment body: 'Pipeline execution failed', issueKey: '$ISSUE_KEY'
        }
    }
}