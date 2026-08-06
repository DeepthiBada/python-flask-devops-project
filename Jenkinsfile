pipeline {
    agent any

    stages {

        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m venv .venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '.venv/bin/python -m pip install --upgrade pip'
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '.venv/bin/python -m pytest'
            }
        }

        stage('Code Quality') {
            steps {
                sh '.venv/bin/flake8 . --exclude=.venv'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-flask-devops:${BUILD_NUMBER} .'
            }
        }
    }
}
