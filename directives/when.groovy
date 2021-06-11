pipeline {
    agent any
    stages {
        stage('VALIDATION README.MD') {
        when { changeset "readme.md" }
            steps {
                echo 'Building'
            }
        }
    }
}