#!/usr/bin/env groovy


pipeline {                  // Jenkinsfile (Declarative Pipeline)
  agent any                // Isso define onde executar o código em qual máquina ou pipeline{agent{node{label'labelName'}}}
  stages {                // Cada seção do estágio tem etapas e comandos diferentes a serem seguidos
    stage('Stage 1') {
      steps {
        echo 'Hello world!'
        ssh "ip172-18-0-23-br02sttim9m000ci9vp0@direct.labs.play-with-docker.com"
      }
    }
  }
}