//jenkins file template
pipeline {
    agent none 
    options {
      timeout(time: 1, unit: 'HOURS') 
    }
    stages {        
    /*    stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py' 
            }
        }*/
        /*stage('SAST with SONARQUBE') {
         agent { label 'master' }
         steps{             
            
             script{
                 catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
                    scannerHome = tool 'sonar-scanner';
                    echo scannerHome;
                 }
             }
            withSonarQubeEnv('sonarqube') {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){               
                    sh "pwd;ls -l ${scannerHome};${scannerHome}/sonar-scanner -X"                
                }
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
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){                
                    sh 'pip install httpobs-cli'
                    sh 'httpobs www.itsecgames.com'
                }
            }            
        }*/
        stage('SSL labs from Qualys') { 
            agent {
                docker {
                    //image 'python:2-alpine'
                    image 'python2-dev'
                     
                }
            }
            environment {
                AZUREBLOB = credentials('AZUREBLOB_CREDS')               
            }
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){                    
                    //sh 'apk add --no-cache --virtual .build-deps gcc musl-dev && pip install cython && apk del .build-deps gcc musl-dev && pip install azure-storage-blob'                   
                    //sh 'apk add --no-cache --update python3-dev  gcc build-base &&  pip install azure-storage-blob'                   
                    //sh 'apt-get install gcc'
                    sh 'pip install azure-storage-blob'
                    sh 'pip install requests'
                    sh 'pip install azure-nspkg'
                    sh 'pip install azure-common'
                    
                                                        
                    
                    //sh 'pip install azure-storage-queue'
                    //sh 'pip install azure-storage-blob'   

                    sh '''python runssllabs.py "sqlva5n7utjk3i7qwm" $AZUREBLOB_PSW "securityscanresults" "sslabs" "ssllabscans.json" "www.google.com"'''                
                }
            } 
        }
        /*stage('Mandatory headers checking with mozilla observatory'){
            agent {
                docker {
                    image 'node:8.16.0-jessie' 
                }
            }
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
                    sh 'npm install -g observatory-cli'
                    sh 'observatory www.itsecgames.com --format=json --min-grade B+'
                    //sh 'observatory www.google.com --format=json'
                }
            }
        }
        stage('DAST with OWASP ZAP') {
            agent {
                docker {
                    image 'owasp/zap2docker-weekly' 
                     args '-v /Users/maersk_mtc03/jenkins_home/workspace/samplepython/report:/zap/wrk/:rw'
                }
            }
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
                    script {
                        sh 'zap-baseline.py -t http://www.itsecgames.com/ -r JENKINS_ZAP_VULNERABILITY_REPORT.html -x JENKINS_ZAP_VULNERABILITY_REPORT.xml '
                    }
                }
            }            
        }*/
        stage("SONAR Quality Gate") {
            agent { label 'master' }
            steps {
                timeout(time: 3, unit: 'MINUTES') {
                    // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
                    // true = set pipeline to UNSTABLE, false = don't
                    // Requires SonarQube Scanner for Jenkins 2.7+
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }  
}
