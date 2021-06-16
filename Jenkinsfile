pipeline {
    // agent { dockerfile true }
    agent { any }
    stages {
        stage('INIT') {
            steps {
                // build = load "pipeline/scripted/build.groovy"
                // build()
                sh """
                    docker build -t teste:teste -f Dockerfile .
                """
            }
        }
    }
}