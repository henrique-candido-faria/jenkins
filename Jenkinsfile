pipeline {
    agent any
    stages {
        stage('BUILD') {
            step {
                script {
                    node = load "scripted/node.groovy"
                    node()
                }
            }
        }
    }
}