pipeline {
   agent any

   stages {
      stage("Git Checkout") {
          steps {
              script {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: "https://github.com/AyushiSinglaPrsnl/Assignment2.git"]]])
              }
          }
      }

      stage('Build') {      
        steps{
          script{
                sh """
                sh script.sh
                """
        }  
      }                   
      }
   }
   post {
       always {
           cleanWs()
       }
   }
}
