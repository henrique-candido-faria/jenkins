pipeline {
    agent any
    stages {
        stage{
            when { changeset "readme.md" }
        }
        steps{
            echo 'Deploying'
        }
    }
}