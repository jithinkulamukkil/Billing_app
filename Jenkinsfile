pipeline {
    agent any

    stages {
        stage('Clean Workspace & Checkout Code') {
            steps {
                script {
                    // Clean workspace to avoid merge/divergent issues
                    deleteDir()
                }
                git branch: 'main',
                    credentialsId: 'jithin-gh-token',
                    url: 'https://github.com/jithinkulamukkil/Billing_app.git'
            }
        }

       stage('Deploy to Host Docker') {
            steps {
                script {
                    sh '''
                        echo "Stopping any running containers..."
                        docker compose -f ./docker-compose.yml down || true

                        echo "Starting application with updated code..."
                        docker compose -f ./docker-compose.yml up -d
                    '''
                }
            }
        }
    }
}