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
                sh 'docker build -t titanic-app .'
            }
        }
        
        stage('Run Docker Container') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
