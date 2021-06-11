pipeline {
    agent any
    stages {
        stage('BUILD') {
            script {
                node = load "scripted/node.groovy"
                node()
            }
        }
    }
}