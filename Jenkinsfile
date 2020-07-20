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
	      sh 'echo "Contruyendo imagen de MongoDB" '
	      script{
		    customimage = docker.build registry + ":$BUILD_NUMBER", "./Docker/mongo/"
	      }
		}
	  }
	  stage('Test'){
	    steps {
	      sh 'echo "Testeando imagenes"'
		}
	  }
	  stage('Publish'){
	    steps {
	      sh 'echo "Publicando imagenes en DockerHub"'
		  script {
            docker.withRegistry('https://registry.hub.docker.com', 'DockerHub-Cred') {
              customimage.push("${env.BUILD_NUMBER}")
              customimage.push("latest")
		    }
          }
		}
	  }
	}
}	