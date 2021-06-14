pipeline {
    agent any
    stages {
        stage('INIT') {
            steps {
                script {
                    build = load "scripted/build.groovy"
                    build()
                }
                script {
                    deploy = load "scripted/deploy.groovy"
                    deploy()
                }
            }
        }
        stage('CONTINUE') {
            echo 'Continue...'
        }
    }
}