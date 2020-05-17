#!/usr/bin/env groovy


pipeline {                  // Jenkinsfile (Declarative Pipeline)
  agent any                // Isso define onde executar o código em qual máquina ou pipeline{agent{node{label'labelName'}}}
  stages {                // Cada seção do estágio tem etapas e comandos diferentes a serem seguidos
    stage('Stage 1') {
      steps {
        // sh 'ssh -tt ip172-18-0-42-br0i4liosm4g00b70ql0@direct.labs.play-with-docker.com'
        sh 'ls '
        sh 'ssh -o StrictHostKeyChecking=no ip172-18-0-23-br02sttim9m000ci9vp0@direct.labs.play-with-docker.com uptime'
        sh 'ls /'
      }
    }
  }
}

// https://www.jenkins.io/doc/book/installing/#debianubuntu
// https://www.eficode.com/blog/jenkins-groovy-tutorial