node('jenkins-slave') {
    stage('ENVIRONMENT') {
        steps {
            checkout([
            $class: "GitSCM",
            branches: [[name: "master"]],
            doGenerateSubmoduleConfigurations: false,
            extensions: [[$class: "RelativeTargetDirectory", relativeTargetDir: "tmp_git_app"]],
            submoduleCfg: [],
            userRemoteConfigs: [[credentialsId: "bitbucket", url: "https://github.com/henrique-candido-faria/python"]]
            ])
        }
    }
}