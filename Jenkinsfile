pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }

    environment {
        VIRTUAL_ENV = 'venv'
    }

    stages {
        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Create virtual environment
                    sh 'python3 -m venv venv'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Activate the virtual environment and install dependencies
                    sh '. ${VIRTUAL_ENV}/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    // Run the unit tests using unittest
                    sh '. ${VIRTUAL_ENV}/bin/activate && python -m unittest discover -s tests -p "flask_test.py"'
                }
            }
        }

        stage('Build Project') {
            steps {
                script {
                    // Build your project (e.g., using a build tool or custom command)
                    echo "Building project..."
                }
            }
        }
    }

    post {
        success {
            echo "Build and tests passed successfully!"
        }
        failure {
            echo "Build or tests failed."
        }
    }
}
