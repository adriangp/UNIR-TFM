pipeline {
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
	    sh 'echo "Contruyendo imagen de MongoDB"'
	    docker-image = docker.build("adriangp/tfm-mongo","./Docker/mongo/Dockerfile")
	  }
	  stage('Test'){
	    sh 'Testeando imagenes'
	  }
	  stage('Publish'){
	    sh 'echo "Publicando imagenes en DockerHub"'
        docker.withRegistry('https://registry.hub.docker.com', 'DockerHub-Cred') {
          docker-image.push("${env.BUILD_NUMBER}")
          docker-image.push("latest")
        }
	  }
	}
}	