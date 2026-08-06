pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest'
            }
        }

        stage('Code Quality') {
            steps {
                sh 'flake8 .'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-flask-devops:${BUILD_NUMBER} .'
            }
        }
    }
}
