// pipeline {
//     agent {
//         label 'jenkins-slave'
//     }
//     stages {
//         stage('INIT') {
//             steps {
//                 checkout scm
//                 script {
//                     build = load "scripted/build.groovy"
//                 }
//                 script {
//                     build()
//                 }
//             }
//         }
//         stage('CONTINUE') {
//             steps {
//                 echo 'Continue...'
//             }
//         }
//     }
// }
// pipeline {
//     agent {
//         kubernetes { image 'node:14-alpine' }
//     }
//     stages {
//         stage('Test') {
//             steps {
//                 sh 'node --version'
//             }
//         }
//     }
// }
pipeline {
    agent {
        label 'jenkins-slave'
    }
    stages {
        stage('ENVIRONMENT') {
            steps {
                script { // Parametros esperados do Jenkins ENVIRONMENT, BRANCH, BUCKET, DNS
                    if (ENVIRONMENT == "prod") {
                        echo 'prod'
                    }
                    if (ENVIRONMENT == "beta") {
                        echo 'beta'
                    }
                    if (ENVIRONMENT == "dev") {
                        echo 'dev'
                    }
                }
            }
        }
    }
}