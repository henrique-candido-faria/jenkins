pipeline {
    agent {
        label 'jenkins-slave'
    }
    stages {
        stage('INIT') {
            checkout scm
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