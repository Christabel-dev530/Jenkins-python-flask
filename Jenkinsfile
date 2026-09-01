pipeline{

    agent any
    stages{
        stage("GitHub checkout....") {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/Christabel-dev530/Jenkins-python-flask.git'
                }
            }
        }
        stage("Build docker connecting....."){
            steps{
                sh 'printenv'
                sh 'git version'
                sh 'docker build . -t christyluv82/image-app1.1'
            }
        }
        stage("push image to DockerHub"){
            steps{
                script {
                    withCredentials([string(credentialsId: 'dockerID', variable: 'dockerID')]) {
                        sh 'docker login -u christyluv82 -p ${dockerID}'
                    }
                    sh 'docker push christyluv82/image-app1.1:latest'
                }
            }
        }
    }
}
