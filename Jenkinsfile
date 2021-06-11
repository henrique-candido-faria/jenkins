pipeline {
    agent any
    stages {
        stage('Example Hello world') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Example Repo') {
            steps {
                when {
                    changeset "readme.md"
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
        }
        stage('Exaple Deploy'){
        when { changeset "readme.md" }
            steps {
                echo 'Deploying'
            }
        }
    }
}