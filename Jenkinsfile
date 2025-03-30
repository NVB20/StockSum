pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-stock'
        CONTAINER_NAME = 'stock-cont'
        ISSUE_KEY = sh(script: 'cat ./issue_key.txt', returnStdout: true).trim()
        SITE_NAME = 'Jira-Stock'
        TRANSITION_NAME = 'Done'
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
        stage('Get Jira Transitions') {
            steps {
                script {
                    def transitions = jiraGetIssueTransitions(
                        idOrKey: env.ISSUE_KEY, 
                        site: $SITE_NAME
                    )
                    echo "Available transitions: ${transitions}"
                    
                    def doneTransitionId = null
                    transitions.data.transitions.each { transition ->
                        if (transition.name == '$TRANSITION_NAME') {
                            doneTransitionId = transition.id
                        }
                    }
                    
                    env.DONE_TRANSITION_ID = doneTransitionId
                    
                    echo "Done transition ID: ${doneTransitionId}"
                }
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
                    sh "docker run --rm --name $CONTAINER_NAME $IMAGE_NAME pytest tests --junitxml=results.xml"
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
            jiraComment body: 'Pipeline executed successfully', issueKey: env.ISSUE_KEY
            jiraTransitionIssue idOrKey: env.ISSUE_KEY, 
                                  site: $SITE_NAME, 
                                  input: [
                                      transition: [
                                          id: env.DONE_TRANSITION_ID 
                                      ]
                                  ]
        }
        failure {
            echo "Pipeline execution failed!"
            jiraAddComment comment: 'Pipeline execution failed', idOrKey: env.ISSUE_KEY, site: $SITE_NAME
        }
    }
}