pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Mustafeez1/Pipeline_Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('titanic-app')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.image('titanic-app').run('-d')
                }
            }
        }
    }
}
