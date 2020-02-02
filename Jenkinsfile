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
        stage('Build image') {
            steps {
                script {
                    docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy to K8s') {
            steps {
                echo 'Deploying....'
            }
        }

    }
}