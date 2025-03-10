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
        
        stage('Build') {
            steps {
                echo "Building the project..."
                // Add your build commands here
            }
        }
        
        stage('Test') {
            steps {
                echo "Running tests..."
                // Add your test commands here
            }
        }
        
        stage('Deploy') {
            steps {
                echo "Deploying the application..."
                // Add your deployment commands here
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