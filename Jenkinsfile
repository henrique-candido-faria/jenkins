pipeline {
    agent any
    stages {
        stage("git") {
            steps {
                checkout([
                $class: "GitSCM",
                branches: [[name: "dev"]],
                doGenerateSubmoduleConfigurations: false,
                extensions: [[$class: "RelativeTargetDirectory", relativeTargetDir: "tmp_git_app"]],
                submoduleCfg: [],
                userRemoteConfigs: [[credentialsId: "github", url: 'https://github.com/henrique-candido-faria/python.git']]
                ])
            }
        }
    }
}