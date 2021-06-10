// node('jenkins-slave') {
//     stage('ENVIRONMENT') {
//         // when { changeset "readme.md" }
//         when { changeset "**/*.js" }
//         steps {
//             checkout([
//             $class: "GitSCM",
//             branches: [[name: "master"]],
//             doGenerateSubmoduleConfigurations: false,
//             extensions: [[$class: "RelativeTargetDirectory", relativeTargetDir: "tmp_git_app"]],
//             submoduleCfg: [],
//             userRemoteConfigs: [[credentialsId: "bitbucket", url: "https://github.com/henrique-candido-faria/python"]]
//             ])
//         }
//     }
// }

// node('jenkins-slave') {
//     stage ("Deploy branches") {

//         when {
//             allOf {
//                 not { branch 'master' }
//                 changeset "some-directory/**"
//                 expression {  // there are changes in some-directory/...
//                     sh(returnStatus: true, script: 'git diff  origin/master --name-only | grep --quiet "^some-directory/.*"') == 0
//                 }
//                 expression {   // ...and nowhere else.
//                     sh(returnStatus: true, script: 'git diff origin/master --name-only | grep --quiet --invert-match "^some-directory/.*"') == 1
//                 }
//             }
//         }

//         steps {
//             // do stuff
//         }
//     }
// }

pipeline {
    node('jenkins-slave'){
        stages {
            stage('Example Build') {
                steps {
                    echo 'Hello World'
                }
            }
            stage('Example Deploy') {
                when {
                    branch 'master'
                }
                steps {
                    echo 'Deploying'
                }
            }
        }
    }
}