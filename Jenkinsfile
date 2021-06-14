pipeline {
    agent any
    stages {
        stage('INIT') {
            steps {
                script {
                    build = load "scripted/build.groovy"
                    build()
                }
            }
            steps {
                script {
                    deploy = load "scripted/deploy.groovy"
                    deploy()
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