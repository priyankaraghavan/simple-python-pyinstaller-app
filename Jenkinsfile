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
         stage('Test') { 
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
        stage('Security Test'){
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
    
        stage('Security Test Zap') {
            agent {
                docker {
                    image 'owasp/zap2docker-weekly' 
                }
            }
            steps {
                script {
                    startZap(host: "127.0.0.1", port: 9095, timeout:1500 ,zapHome:"/Applications/OWASP ZAP.app/Contents/Java") // Start ZAP at /opt/zaproxy/zap.sh, allowing scans on github.com (if allowedHosts is not provided, any local addresses will be used
                    runZapCrawler(host: "https://www.google.com")
                }
            }
            post {
                always {
                    script {
                        archiveZap(failAllAlerts: 1, failHighAlerts: 0, failMediumAlerts: 0, failLowAlerts: 0, falsePositivesFilePath: "zapFalsePositives.json")
                    }
                }
            } 
        }
    }  
}