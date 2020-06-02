#!/usr/bin/env groovy

// https://www.jenkins.io/doc/book/installing/#debianubuntu
// https://www.eficode.com/blog/jenkins-groovy-tutorial
// https://medium.com/@marcosnils/pwd-ssh-c12080ea11d1
// https://medium.com/lucjuggery/now-a-pwd-driver-for-docker-machine-54c672d69e56
// https://github.com/play-with-docker/docker-machine-driver-pwd/releases

// cat /var/lib/jenkins/secrets/initialAdminPassword

pipeline {                  // Jenkinsfile (Declaração de Pipeline)
  agent any                // Isso define onde executar o código em qual máquina ou pipeline {agent{node{label'labelName'}}}
  stages {                // Cada seção do estágio tem etapas e comandos diferentes a serem seguidos
    stage('Stage 1') {
      steps {
        sh 'cd docker/'
        sh 'sh docker.sh'
      }
    }
  }
}