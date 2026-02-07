pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-python-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Lint') {
            steps {
                sh 'pylint src/'
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('deployment') {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Deploy (Simulation)') {
            steps {
                echo 'Deploying application...'
                // Add deployment steps here
            }
        }
    }
}
