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
                sh 'make install'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'make test'
            }
        }
    }
}