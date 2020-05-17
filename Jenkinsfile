#!/usr/bin/env groovy


pipeline {                  // Jenkinsfile (Declarative Pipeline)
  agent any                // Isso define onde executar o código em qual máquina ou pipeline{agent{node{label'labelName'}}}
  stages {                // Cada seção do estágio tem etapas e comandos diferentes a serem seguidos
    stage('Stage 1') {
      steps {
        // sh 'ssh -tt ip172-18-0-42-br0i4liosm4g00b70ql0@direct.labs.play-with-docker.com'
        // sh 'ssh -o StrictHostKeyChecking=no ip172-18-0-8-br0nbqqosm4g008cp8fg@direct.labs.play-with-docker.com uptime'
        sh 'cd /'
        sh 'ls'
        sh 'ssh -tt ip172-18-0-8-br0nbqqosm4g008cp8fg@direct.labs.play-with-docker.com'
      }
    }
  }
}

// https://www.jenkins.io/doc/book/installing/#debianubuntu
// https://www.eficode.com/blog/jenkins-groovy-tutorial