pipeline {
    agent any
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
return this