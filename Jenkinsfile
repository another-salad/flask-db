node {
    checkout scm;
    def customImage = docker.build('flask-db-test-env', '-f Dockerfile.tests .');
    customImage.inside {
        try {
            stage('Run tests') {
                sh 'python /tests/run_tests.py';
            }
        } catch (e) {
            currentBuild.result = 'FAILED';
            throw e;
        } finally {
            stage('Notify') {
                if (currentBuild.result == 'FAILURE') {
                    postNotification();
                }
            }
        }
    }
}

void postNotification() {
    lock(label: 'piHat', variable: 'resource_name') {
        sh """\
            curl -X POST -H "Content-Type: application/json" -d \
            '{"text_str": "FLASK-DB TEST FAILURE", "text_color": [0, 50, 50],"back_color": [150, 50, 0],"scroll": 0.1}' \
            ${env.resource_name}\
            """;
    }
}