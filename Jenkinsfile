node(){
  def listIps =["172.11.45.1","172.11.45.2","172.11.45.3"]
  stage('cloning the code'){
  checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/csenapati12/calling-py-jenkinsfile.git']]])
  }
//stage('Calling Python'){
//sh "python callpython.py"
//}
  
 // stage('python with para'){
 // sh "python hello.py 23 445"
//}
  
stage('Calling IPs'){
  for(int i=0;i<listIps.size();i++){
  sh "python getKeyClockToken.py $listIps[i]"
  }
}
}
