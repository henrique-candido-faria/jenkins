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
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
                sh 'svn --version'
            }
        }
    }
}