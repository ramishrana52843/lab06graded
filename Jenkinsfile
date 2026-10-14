pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/YOUR_GITHUB_USER/YOUR_REPO.git'
                sh 'docker compose down'
                sh 'docker compose pull'
                sh 'docker compose up -d'
            }
        }
    }
}
