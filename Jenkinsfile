pipeline {
    agent any
    stages {
        stage('VALIDATION README.MD') {
        when { changeset "readme.md" }
            steps {
                echo 'Building'
            }
        }
        stage('DOWNLOAD REPOSITORY') {
            steps {
                checkout([
                    $class: "GitSCM",
                    branches: [[name: "prod"]],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [[$class: "RelativeTargetDirectory", relativeTargetDir: "tmp_git_app"]],
                    submoduleCfg: [],
                    userRemoteConfigs: [[credentialsId: "bitbucket", url: "https://github.com/henrique-candido-faria/python"]]
                ])
            }
        }
        stage('VALIDATION README.MD'){
        when { changeset "readme.md" }
            steps {
                echo 'Deploying'
            }
        }
    }
}