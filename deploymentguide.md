{% include navigation.html %}

# Deployment Policy
Everyone have the assignment pushed so that the website is ready to deploy by 12:00 AM on Thursday of every week

[Deployed Website](https://hackclub.tk/)

# Deployment Manager Backup List
1. Tanay
2. Colin
3. Ritvik
4. Armaan

# Website Development Process

## AWS Setup 
__[Link to Deployment Timetable with Screenshots]()__

1. ### AWS (Amazon Web Services) or **Raspberry Pi**
Raspberry Pi costs a lot, so we are settling for AWS and its EC2 instance to deploy the website. You can use the credit card information to 
buy it for free.
   - Use EC2 services in AWS and build Ubuntu EC2 instance (a form of linux)
      - Log onto aws.amazon.com and create a free account with free tiers using personal information (deployment manager)
      - Then, click the orange button that says "Get Started With Amazon EC2"
      - Choose an Instance Type, called t2 Micro, as it is a Free Tier Eligible service. Then create instance and launch the Ubuntu Server 

   -  Configure SSH in order to run the website on Ubuntu Server: 
   - Connect to server via SSH using the key: ssh -i "Siuuu.pem" ubuntu@ec2-18-117-37-233.us-east-2.compute.amazonaws.com
      - When launching the EC2 instance for the Ubuntu Server, I had to download a .pem file and called it Siuuu.pem in order to provide a secure connection between user and website when deploying
      - Click connect under the running instance and launch the Linux Server 
        
      - Allocate an Elastic IPV4 Address by associating the ip address to it 
    


     - Launch Linux server through Ubuntu 
  


2. ### Install Pip packages
   - Run command to make sure python3 is installed on Linux in terminal:
$ python3 --version
     - Must make sure Python Version 3 exists on the console



   - Run command to make sure pip is installed: 
$ pip3 --version

   - Pip3 was not installed, and I used command : "$ sudo apt install python3-pip" but it did not work.



   - Next, add team Siuuu user: sudo adduser Siuuuu
   - Update: sudo apt-get update and sudo apt-get upgrade 
   - Install python3 and nginx combined with command: sudo apt-get install python3-pip nginx git
      - Sudo apt install to install packages involving python and for configuring nginx

      
      

3. ### Setup Github Repository Environment 
   - Check Git version using command: git --version
      - Output: git version 2.24.3

   
   - Configure the Github name and email address so that everytime we do a commit, it updates the website through the domain
      - Command: git config --global user.name "Tanay Rayavarapu"
git config --global user.email "tanayrayavarapu@domain.com"



   - Clone Github Repo: 
&nbsp;
 cd ~ git clone https://github.com/KoolKidKai/Siuuuu.git

   - Then, open up repo in files:  
ls -al
cd Siuuuu

4. ### Setup Virtual Environment for Python
   - Create a seperate directory to store files using command:  mkdir flask-gunicorn
   - Install flask and gunicorn packages 
       - Use command: ~/flask-gunicorn$ pip3 install flask gunicorn
   
   

5. ### Establish a Service File
    - Change user to ubuntu, and create homesite.service file in Gunicorn: 
     sudo nano /etc/systemd/system/teamsiuuuu.service

6. ### Configure Nginx builds a reverse proxy
    - can allow you to run multiple web servers on deployment services like raspberry pi

Check deployed website: [Team Siuuuu](https://hackclub.tk/)

7. ### HTTP is unsecure
    - HTTPS is secure; unsecure site can be 
    - Go back to teams: **pull from github**; **check or update the dependencies**; **restart service file** 
    - Activate HTTPS and certbot and the website should be good to go!
    

8. ### Update Website 
     - Pull from Github Repository and Update website every Week
     - cd into folder/directory: cd ~/siuuuu 
     - Then, git pull
     - Next, type in command source homesite/bin/activate
     - pip install -r requirements.txt
     - sudo systemctl restart homesite.service
     - Website should be updated with the most recent commit from the repository for Team Siuuuu


