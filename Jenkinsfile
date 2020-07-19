pipeline {
  agent any
    stages {
	  stage('checkout'){
	    steps{
			checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'http://git-server/adriangp/UNIR-TFM.git']]])
		}
	  }
      stage('Build') {
	    steps {
	      sh 'ls -lart'
	    }
	  }
	}
}	