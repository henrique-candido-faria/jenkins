pipeline {
    // agent { dockerfile true }
    agent { label 'jenkins-slave' }
    stages {
        stage('INIT') {
            steps {
                // build = load "pipeline/scripted/build.groovy"
                // build()
                sh """
                    ls -l
                    docker build -t teste:teste -f Dockerfile .
                """
            }
        }
    }
}