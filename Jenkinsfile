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

        		sh '''
            		docker --version

            		docker build -t python-flask-devops:${BUILD_NUMBER} .
        		'''

   		    }

	    }

	    stage('Push Image to ECR') {

        steps {

            withCredentials([
                usernamePassword(
                    credentialsId: 'aws-ecr-credentials',
                    usernameVariable: 'AWS_ACCESS_KEY_ID',
                    passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                )
            ]) {

                sh '''
                    export AWS_DEFAULT_REGION=ap-south-1

                    aws --version

                    aws ecr get-login-password --region ap-south-1 | \
                    docker login \
                        --username AWS \
                        --password-stdin 959015414867.dkr.ecr.ap-south-1.amazonaws.com

                    docker tag \
                        python-flask-devops:${BUILD_NUMBER} \
                        959015414867.dkr.ecr.ap-south-1.amazonaws.com/python-flask-devops:${BUILD_NUMBER}

                    docker push \
                        959015414867.dkr.ecr.ap-south-1.amazonaws.com/python-flask-devops:${BUILD_NUMBER}
                '''

                }

            }

        }
    }
}
