// pipeline {
//     agent {
//         label 'jenkins-slave'
//     }
//     stages {
//         stage('INIT') {
//             steps {
//                 script {
//                     build = load "pipelines/scripted/build.groovy"
//                 }
//                 script {
//                     build()
//                 }
//             }
//         }
//     }
// }
pipeline {
    agent {
        docker { image 'node:14-alpine' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}