pipeline {
    agent any
    triggers {
        pollSCM('* * * * */1')
    }
     options {
        disableConcurrentBuilds()
    }
    environment {
        registry = "escarti/geekshub-django"
        registryCredential = 'docker-registry'
        apiServer = "https://192.168.99.101:8443"
        devNamespace = "default"
        minikubeCredential = 'minikube-auth-token'
        imageTag = "${env.GIT_BRANCH + '_' + env.BUILD_NUMBER}"
        developDeployRepo = "https://github.com/escarti/geekshub-django-deployment.git"
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
                    dockerImage = docker.build(registry + ":$imageTag","--network host .")
                }
            }
        }
        stage('Upload to registry') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Update deployment file') {
            when {
                expression { env.GIT_BRANCH == 'develop' }
            }
            steps{
                script {
                    dir('deployment') {
                        git branch: 'master',
                        credentialsId: 'Git',
                        url: developDeployRepo

                        sh "echo \"spec:\n  template:\n    spec:\n      containers:\n        - name: django\n          image: $imageTag\" > patch.yaml"
                        sh "kubectl patch --local -o yaml -f django-deployment.yaml -p \"\$(cat patch.yaml)\" > new-deploy.yaml"
                        sh "mv new-deploy.yaml django-deployment.yaml"
                        sh "rm patch.yaml"
                        sh "git add ."
                        sh "git commit -m\"Patched deployment for $imageTag\""

                        withCredentials([usernamePassword(credentialsId: 'Git-Encoded', usernameVariable: 'username', passwordVariable: 'password')]){
                            sh "git push https://$username:$password@github.com/escarti/geekshub-django-deployment.git"
                        }
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
                    sh 'kubectl apply -f deployment/django-deployment.yaml'
                }
            }
        }
    }
}