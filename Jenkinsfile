pipeline {
    agent any
    stages {
        stage("repository") {
            steps {
                checkout([
                $class: "GitSCM",
                branches: [[name: "main"]],
                doGenerateSubmoduleConfigurations: false,
                extensions: [[$class: "RelativeTargetDirectory", relativeTargetDir: "repository"]],
                submoduleCfg: [],
                userRemoteConfigs: [[credentialsId: "github", url: 'https://github.com/henrique-candido-faria/python.git']]
                ])
            }
        }
    }
}