
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Java application'
                bat 'javac app.java'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Java application'
                bat 'java app'
            }
        }

        stage('Run Application') {
            steps {
                bat 'java app'
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully'
        }
        failure {
            echo 'CI Pipeline failed'
        }
    }
}

          
