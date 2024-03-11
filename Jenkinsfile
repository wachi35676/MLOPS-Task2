pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/wachi35676/MLOPS-Task2.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'python -m pytest test.py'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    def branchName = env.GIT_BRANCH.split('/').last()
                    if (branchName == 'main') {
                        echo "Deploying to production"
                    } else {
                        echo "Deploying to UAT"
                    }
                }
            }
        }
    }
}