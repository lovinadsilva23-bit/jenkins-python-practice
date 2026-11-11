
pipeline {
    agent any

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['QA', 'PROD'],
            description: 'Select environment'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'GitHub source code checkout'
            }
        }

        stage('Build') {
            steps {
                echo 'Starting Python Build'
                bat '"C:\\Users\\NEW\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" hello.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running application tests'
                bat 'echo Tests completed'
            }
        }

        stage('QA Deployment') {
            when {
                expression {
                    params.ENVIRONMENT == 'QA'
                }
            }
            steps {
                echo 'QA deployment check completed'
            }
        }

        stage('PROD Deployment') {
            when {
                expression {
                    params.ENVIRONMENT == 'PROD'
                }
            }
            steps {
                echo 'PROD deployment check completed'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed'
        }
        success {
            echo 'Pipeline SUCCESS'
        }
        failure {
            echo 'Pipeline FAILURE'
        }
    }
}
