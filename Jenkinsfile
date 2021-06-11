pipeline {
    agent any
    stages {
        stage('BUILD') {
            node = load "scripted/node.groovy"
            node()
        }
    }
}