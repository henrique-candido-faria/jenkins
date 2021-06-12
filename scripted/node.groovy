import hudson.model.Build

node("jenkins-slave") {
    stage("One"){
        echo 'hello'
    }
}