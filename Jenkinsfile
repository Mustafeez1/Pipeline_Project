pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/opt/homebrew/bin:/bin:/usr/bin:/usr/sbin:/sbin"
    }

    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Mustafeez1/Pipeline_Project.git'
            }
        }

        stage('Sanity Check') {
            steps {
                sh '/bin/sh -c "echo Shell OK && which docker && docker --version"'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '/bin/sh -c "docker build -t titanic-app ."'
            }
        }

        stage('Remove Existing Container') {
            steps {
                sh '''
                    if [ "$(docker ps -aq -f name=titanic_prediction_container)" ]; then
                        echo "Removing existing container..."
                        docker rm -f titanic_prediction_container
                    else
                        echo "No existing container to remove."
                    fi
                '''
            }
        }

        stage('Find Available Port') {
            steps {
                script {
                    // Find the first available port starting from 5000
                    def port = 5000
                    def maxPort = 5100
                    while (port <= maxPort) {
                        def result = sh(script: "lsof -ti :${port}", returnStatus: true)
                        if (result != 0) {
                            echo "Port ${port} is available."
                            env.FLASK_PORT = port.toString()
                            break
                        } else {
                            echo "Port ${port} is in use, trying next one."
                            port++
                        }
                    }

                    // If all ports are occupied, fail the build
                    if (port > maxPort) {
                        error "No available ports between 5000 and 5100"
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    echo "Starting container on port ${FLASK_PORT}"
                    docker-compose -f docker-compose.yml up -d
                '''
            }
        }
    }
}
