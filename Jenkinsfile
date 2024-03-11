pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/revolutionarybukhari/StudentsInMLOps'
            }
        }

        stage('Set up Python') {
            steps {
                // Download Python installer
                bat 'curl -o python-installer.exe https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe'
                // Install Python
                bat 'python-installer.exe /quiet InstallAllUsers=1 PrependPath=1'
                // Remove Python installer
                bat 'del python-installer.exe'
            }
        }
        
        stage('Install dependencies') {
            steps {
                // Install Python dependencies
                bat 'pip install -r requirements.txt'
                bat 'pip install pytest'
            }
        }
        
        stage('Run tests') {
            steps {
                // Run tests using full path to pytest executable
                bat 'python3 test.py'
            }
        }
    }
}

