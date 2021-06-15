pipeline {
    agent {
        label 'jenkins-slave'
    }
    stages {
        stage('INIT') {
            steps {
                checkout scm
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