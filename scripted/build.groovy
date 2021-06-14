node("jenkins-slave") {
    stage("BUILD") {
        echo 'Building...'
        echo 'Deploying'
    }
    stage('DEPLOY') {
        echo 'Deploying'
    }
}