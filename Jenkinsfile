pipeline {
  agent any
  environment{
    customimage = ''
	registry = "adriangp/tfm"
	registryCredential = 'DockerHub-Cred'
  }

    stages {
	  stage('Checkout') {
	    steps {
		  sh 'echo "Obteniendo ultima version de la aplicacion"'
		  checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'http://github.com/adriangp/UNIR-TFM.git']]])
	      sh 'ls -lart'
		}
	  }
	  stage('Build') {
	    steps {
	      sh 'echo "Contruyendo imagen de MongoDB"'
	      //customimage = docker.build registry + ":$BUILD_NUMBER"
		}
	  }

	}
}	