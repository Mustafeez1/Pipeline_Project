pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin/docker"  // Add Docker's path here
    }

    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Mustafeez1/Pipeline_Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '/bin/sh -c "docker build -t titanic-app ."'  // Use the full path to bash or sh
            }
        }
        
        stage('Run Docker Container') {
            steps {
                sh '/bin/sh -c "docker-compose up -d"'  // Same here
            }
        }
    }
}
