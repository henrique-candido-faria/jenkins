pipeline {
    agent {
        label 'jenkins-slave'
    }
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
    }
}