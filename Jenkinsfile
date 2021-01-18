pipeline {
    agent any
    stages {
        stage("git") {
            steps {
                git credentialsId: 'github', url 'https://github.com/henrique-candido-faria/python.git'
            }
        }
    }
}