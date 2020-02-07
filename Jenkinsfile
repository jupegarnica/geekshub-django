pipeline {
    agent any
    triggers {
        pollSCM('* * * * */1')
    }
    environment {
        registry = "escarti/geekshub-django"
        registryCredential = 'docker-registry'
        apiServer = "https://192.168.99.101:8443"
        devNamespace = "default"
        minikubeCredential = 'minikube-auth-token'
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
                    dockerImage = docker.build(registry + ":$GIT_BRANCH" + "_$BUILD_NUMBER","--network host .")
                }
            }
        }
        stage('Deploy Image') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy to K8s') {
            when {
                expression { env.GIT_BRANCH == 'develop' }
            }
            steps{
                withKubeConfig([credentialsId: minikubeCredential,
                                serverUrl: apiServer,
                                namespace: devNamespace
                               ]) {
                    sh 'kubectl set image deployment/django django="$registry:$BUILD_NUMBER" --record'
                }
            }
        }
    }
}