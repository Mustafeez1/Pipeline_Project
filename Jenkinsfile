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

        stage('Run Docker Container') {
            steps {
                sh '/bin/sh -c "docker-compose up -d"'
            }
        }
    }
}

