pipeline {
    agent any
    stages {
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
        when { changeset "https://github.com/henrique-candido-faria/python/readme.md" }
            steps {
                echo 'Deploying'
            }
        }
    }
}