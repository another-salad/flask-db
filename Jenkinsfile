node {
    checkout scm
    def customImage = docker.build("flask-db-test-env", "-f Dockerfile.tests .")
    customImage.inside {
        stage('Run tests') {
            sh 'python run_tests.py'
        }
    }
}