//jenkins file template
pipeline {
    agent none 
    options {
      timeout(time: 1, unit: 'HOURS') 
    }
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
        stage('SAST with SONARQUBE') {
         agent { label 'master' }
         steps{             
            
             script{
                 scannerHome = tool 'sonar-scanner';
             }
            withSonarQubeEnv('sonarqube') {
                //sh "${scannerHome}/sonar-scanner"
                sh "sonar-scanner"
            }
         }
        }
        stage("Quality Gate") {
            agent none
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
                    // true = set pipeline to UNSTABLE, false = don't
                    // Requires SonarQube Scanner for Jenkins 2.7+
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        stage('Website rating test from Mozilla') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'pip install httpobs-cli'
                sh 'httpobs http://www.google.com'
            }            
        }
        stage('SSL labs from Qualys') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'pip install requests'
                sh 'python runssllabs.py'                
            } 
        }
        stage('Mandatory headers checking with mozilla observatory'){
            agent {
                docker {
                    image 'node:8.16.0-jessie' 
                }
            }
            steps {
                sh 'npm install -g observatory-cli'
                //sh 'observatory www.maersk.com --format=json --min-grade B+'
                sh 'observatory www.google.com --format=json'
            }
        }
        stage('DAST with OWASP ZAP') {
            agent {
                docker {
                    image 'owasp/zap2docker-weekly' 
                     args '-v /Users/maersk_mtc03/jenkins_home/:/zap/wrk/:rw'
                }
            }
            steps {
                script {
                    sh 'zap-baseline.py -t https://www.google.com -r zapreport.html'
                }
            }            
        }
    }  
}
