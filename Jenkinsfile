node(){
  stage('cloning the code'){
  checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/csenapati12/calling-py-jenkinsfile.git']]])
  }
stage('Calling Python'){
sh "python callpython.py"
}
  
  stage('python with para'){
  sh "python hello.py 23 445"
}
}
