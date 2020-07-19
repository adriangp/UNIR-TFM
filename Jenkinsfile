pipeline {
  agent any
    stages {
	  
      stage('Build') {
	    steps{
			checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'http://git-server/adriangp/UNIR-TFM.git']]])
		}
        steps {
	      sh 'ls -lart'
	    }
	  }
	}
}	