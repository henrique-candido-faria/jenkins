pipeline {
    agent any
    stages {
        stage("repository") {
            steps {
                git credentialsId: 'git_credentials', url https://github.com/henrique-candido-faria/python.git
            }
        }
    }
}