pipeline {
  environment{
    customimage = ''
	registry = "adriangp/tfm"
	registryCredential = 'DockerHub-Cred'
  }
  agent any
    stages {
	  stage('Checkout') {
	    steps {
		  sh 'echo "Obteniendo última versión de la aplicación"'
		  checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'http://github.com/adriangp/UNIR-TFM.git']]])
	      sh 'ls -lart'
		}
	  }
	  stage('Build') {
	    steps {
	      sh 'echo "Contruyendo imagen de MongoDB"'
	      customimage = docker.build registry + ":$BUILD_NUMBER"
		}
	  }
	  stage('Test'){
	    steps {
	      sh 'Testeando imagenes'
		}
	  }
	  stage('Publish'){
	    steps {
	      sh 'echo "Publicando imagenes en DockerHub"'
          docker.withRegistry('https://registry.hub.docker.com', 'DockerHub-Cred') {
            docker.push("${env.BUILD_NUMBER}")
            docker.push("latest")
          }
		}
	  }
	}
}	