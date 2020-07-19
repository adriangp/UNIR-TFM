node {
  agent any
  environment{
    customimage = ''
	registry = "adriangp/tfm"
	registryCredential = 'DockerHub-Cred'
  }

    stages {
	  stage('Checkout') {
	    steps {
		  sh 'echo "Obteniendo última versión de la aplicación"'
		  checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'http://github.com/adriangp/UNIR-TFM.git']]])
	      sh 'ls -lart'
		}
	  }

	}
}	