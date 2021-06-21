pipeline {
    agent {
        docker { image 'ubuntu:20.10' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}