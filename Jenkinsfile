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
    parameters {
        choice(name: 'ENVIRONMENT', choices: ['dev', 'beta', 'prod'], description: 'Escolha qual sera o ambiente')
        string(name: 'CUSTOM_BRANCH', defaultValue: '', description: 'Necessario preencher ao utilizar o ambiente de dev')
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
                        BRANCH = "${CUSTOM_BRANCH}"
                        echo 'dev'
                        echo "${CUSTOM_BRANCH}"
                    }
                }
            }
        }
    }
}