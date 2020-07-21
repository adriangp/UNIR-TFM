pipeline {
  agent any
  environment{
	versionBD = "1.1"
	versionAPP = "1.1"
    customimageBD = ''
	customimageAPP = ''
	registryBD = "adriangp/tfm-bd"
	registryAPP = "adriangp/tfm-app"
	registryCredential = 'DockerHub-Cred'
	projectId = "unir-tfm-283117"
	clusterName = "cluster-tfm"
	clusterLocation = "europe-west1-d"
	gkeCredential = 'Google-Cred'
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
		    customimageBD = docker.build registryBD + ":$versionBD", "./Docker/mongo/"
	      }
		  sh 'echo "Contruyendo imagen de Aplicacion" '
	      script{
		    customimageAPP = docker.build registryAPP + ":$versionAPP", "./Docker/python/"
	      }
		}
	  }
	  stage('Test'){
	    steps {
	      sh 'echo "Testeando imagenes"'
		}
	  }
	  stage('Publish image'){
	    steps {
	      sh 'echo "Publicando imagenes en DockerHub"'
		  script {
            docker.withRegistry('https://registry.hub.docker.com', 'DockerHub-Cred') {
              customimageBD.push("${versionBD}")
              customimageBD.push("latest")
			  customimageAPP.push("${versionAPP}")
              customimageAPP.push("latest")
		    }
          }
		}
	  }
	  stage('Deploy in GKE'){
	    steps{
		   step([$class: 'KubernetesEngineBuilder', projectId: "${projectID}", clusterName: "${clusterName}", location: ${clusterLocation}", manifestPattern: './Kubernetes/mongo.yaml', credentialsId: "${gkeCredential}", verifyDeployments: true])
		   //step([$class: 'KubernetesEngineBuilder', projectId: $projectID, $clusterName: $clusterName, location: $clusterLocation, manifestPattern: './Kubernetes/python.yaml', credentialsId: $gkeCredential, verifyDeployments: true])
           //step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'deployment.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])

		}
	  }
	}
}	