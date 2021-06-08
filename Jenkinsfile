// pipeline {
//     agent any
//     parameters {
//         choice(name: 'BRANCH', choices: ['beta', 'prod'], description: '')
//     }
//     stages {
//         stage('CHECKOUT'){
//             steps {
//                 checkout([
//                 $class: "GitSCM",
//                 branches: [[name: "${BRANCH}"]],
//                 doGenerateSubmoduleConfigurations: false,
//                 extensions: [[$class: "RelativeTargetDirectory", relativeTargetDir: "tmp_git_app"]],
//                 submoduleCfg: [],
//                 userRemoteConfigs: [[url: "https://github.com/henrique-candido-faria/python"]]
//                 ])
//             }
//         }
//         stage('BUILD'){
//             agent {
//                 docker {
//                     image 'python:3.7-slim'
//                     // Run the container on the node specified at the top-level of the Pipeline, in the same workspace, rather than on a new node entirely:
//                     reuseNode true
//             }
//         }
//     }
// }
pipeline {
    agent any
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'gradle:6.7-jdk11'
                    // Run the container on the node specified at the top-level of the Pipeline, in the same workspace, rather than on a new node entirely:
                    reuseNode true
                }
            }
            steps {
                sh 'gradle --version'
            }
        }
    }
}