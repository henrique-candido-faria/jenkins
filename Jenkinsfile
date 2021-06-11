pipeline {
    agent any
    stages {
        stage('Example Build') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Example Deploy') {
            checkout([
                $class: "GitSCM",
                branches: [[name: "master"]],
                doGenerateSubmoduleConfigurations: false,
                extensions: [[$class: "RelativeTargetDirectory", relativeTargetDir: "tmp_git_app"]],
                submoduleCfg: [],
                userRemoteConfigs: [[credentialsId: "bitbucket", url: "https://github.com/henrique-candido-faria/python"]]
            ])
            when { changeset "readme.md" }
            steps {
                echo 'Deploying'
            }
        }
    }
}