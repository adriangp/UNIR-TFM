pipeline {
  agent any
  environment{
    customimage = ''
	registry = "adriangp/tfm"
	registryCredential = 'DockerHub-Cred'
  }

    stages {
	   stage('Initialize'){
         script {
		   def dockerHome = tool 'myDocker'
           env.PATH = "${dockerHome}/bin:${env.PATH}"
		 }
      }
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
		  sh 'docker -version' 
	      //script{
		  //  customimage = docker.build registry, "./Docker/mongo/"
	      //}
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
          //docker.withRegistry('https://registry.hub.docker.com', 'DockerHub-Cred') {
          //  docker.push("${env.BUILD_NUMBER}")
          //  docker.push("latest")
          //}
		}
	  }
	}
}	