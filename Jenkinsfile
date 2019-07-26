pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py' 
            }
        }
        stage('Security Test Zap') {
            agent {
                docker {
                    image 'owasp/zap2docker-stable' 
                     args '-v /var/jenkins_home/workspaces/samplepython:/zap/wrk/:rw'
                }
            }
            steps {
                script {
                    sh 'zap-baseline.py -t https://www.google.com -r testreport.html'
                }
            }            
        }
        stage('httpobs test') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'pip install httpobs-cli'
                sh 'httpobs www.google.com'
            }            
        }
        stage('Security Test observatory'){
            agent {
                docker {
                    image 'node:8.16.0-jessie' 
                }
            }
            steps {
                sh 'npm install -g observatory-cli'
                sh 'observatory www.google.com'
            }
        }
    }  
}