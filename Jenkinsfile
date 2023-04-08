pipeline{
    agent any
    stages  
    {

        stage("Creating virtual  environment for App"){
                
            steps{
                sh '''
                chmod +x envsetup.sh
                ./envsetup.sh
                '''
            }
        }    
        

        stage("Setup Gunicore"){
                
            steps{
                sh '''
                chmod +x gunicorn.sh
                ./gunicore.sh
                '''
            }
        
        }

        stage("Setup Nginx Webserver")
        {
                
            steps
            {
                sh '''
                chmod +x nginx.sh
                ./nginx.sh
                '''
            }
        

        
        }
    }
}