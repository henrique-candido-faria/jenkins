podTemplate {
    node('jenkins-slave') {
        stage('Example Build') {
            step {
                echo 'Hello World'
            }
        }
        stage('Example Deploy') {
            when {
                branch 'production'
                echo 'Deploying'
            }
        }
    }
}

