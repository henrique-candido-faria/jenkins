pipeline {
    agent master
    stages {
        stage('BUILD') {
            steps {
                script {
                    node = load "scripted/node.groovy"
                    node()
                }
            }
        }
    }
}