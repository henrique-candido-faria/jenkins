pipeline {
    agent master
    stages {
        stage('INIT') {
            steps {
                script {
                    build = load "scripted/build.groovy"
                }
                script {
                    build()
                }
            }
        }
        stage('CONTINUE') {
            steps {
                echo 'Continue...'
            }
        }
    }
}