pipeline {
    agent any
    stages {
        stage("git") {
            steps {
                git credentialsId: 'git_credentials', url 'https://github.com/henrique-candido-faria/python.git'
            }
        }
    }
}