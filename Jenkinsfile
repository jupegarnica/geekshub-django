pipeline {
    agent any
    environment {
        registry = "escarti/geekshub-django"
        registryCredential = 'docker-registry'
    }
    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Build and publish') {
            steps {
                echo 'Building..'
                docker.build registry + ":$BUILD_NUMBER"
            }
        }
        stage('Deploy to K8s') {
            steps {
                echo 'Deploying....'
            }
        }

    }
}