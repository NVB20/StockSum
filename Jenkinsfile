pipeline {
    agent any

    environment {
        // Add any environment variables you need here
        VIRTUAL_ENV = 'venv'
    }

    stages {
        stage('Install Python') {
            steps {
                script {
                    // Install Python if it's not already installed
                    def pythonInstalled = sh(script: "which python3", returnStatus: true)
                    if (pythonInstalled != 0) {
                        echo "Python 3 not found, installing..."
                        sh '''
                            apt-get install -y sudo
                            sudo apt-get update
                            sudo apt-get install -y python3 python3-pip python3-venv
                        '''
                    } else {
                        echo "Python 3 is already installed."
                    }
                }
            }
        }
        stage('Setup') {
            steps {
                script {
                    // Create a virtual environment if it doesn't exist
                    if (!fileExists(VIRTUAL_ENV)) {
                        sh 'python3 -m venv venv'
                    }
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
                    // Example: for a Flask app, you might use Docker or a custom build script
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
