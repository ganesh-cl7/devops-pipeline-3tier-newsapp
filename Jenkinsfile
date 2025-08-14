pipeline {
    agent any
    environment {
        TARGET = "local"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ganesh-cl7/devops-pipeline-3tier-newsapp.git'
            }
        }
        stage('Build and Deploy') {
            steps {
                script {
                    if (env.TARGET == 'local') {
                        sh 'docker-compose down'
                        sh 'docker-compose up -d --build'
                    } else if (env.TARGET == 'aws') {
                        sh 'ssh -i /path/to/key.pem ec2-user@AWS_PUBLIC_IP "cd /path/to/project && docker-compose down && docker-compose up -d --build"'
                    }
                }
            }
        }
    }
}
