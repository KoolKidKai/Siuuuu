{% include navigation.html %}

# Deployment Policy
Everyone have the assignment pushed so that the website is ready to deploy by 12:00 AM on Thursday of every week

[Deployed Website]()

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
   - Connect to server via SSH using the key: ssh -i "teamfood.pem" ubuntu@ec2-18-117-37-233.us-east-2.compute.amazonaws.com
      - When launching the EC2 instance for the Ubuntu Server, I had to download a .pem file and called it teamfood.pem in order to provide a secure connection between user and website when deploying
      - Click connect under the running instance and launch the Linux Server 
        <img width="882" alt="Screen Shot 2021-12-02 at 2 03 02 PM" src="https://user-images.githubusercontent.com/60719508/144511102-3f77abcb-9ee5-4e92-9154-9f9d6545de8e.png">
        <img width="634" alt="Screen Shot 2021-12-02 at 2 19 33 PM" src="https://user-images.githubusercontent.com/60719508/144512484-9cf120f2-28cd-4154-aa74-63197ece4d86.png">


      - Allocate an Elastic IPV4 Address by associating the ip address to it 
      <img width="622" alt="Screen Shot 2021-12-02 at 2 22 44 PM" src="https://user-images.githubusercontent.com/60719508/144512779-4a35104a-1717-4afa-b76c-7bd12eef1b5d.png">
      <img width="590" alt="Screen Shot 2021-12-02 at 2 25 28 PM" src="https://user-images.githubusercontent.com/60719508/144513143-3fff310b-5afb-423e-8965-9c0a3a6fcbde.png">



     - Launch Linux server through Ubuntu 
     <img width="626" alt="Screen Shot 2021-12-02 at 2 27 56 PM" src="https://user-images.githubusercontent.com/60719508/144513780-e61fb2c1-9d8b-416b-b35a-17bb7135b412.png">


2. ### Install Pip packages
   - Run command to make sure python3 is installed on Linux in terminal:
$ python3 --version
     - Must make sure Python Version 3 exists on the console

     ![Screen Shot 2021-12-02 at 2 03 00 PM](https://user-images.githubusercontent.com/89223703/144510767-529ec603-fe31-4ab0-a536-7fc41d910ebd.png)


   - Run command to make sure pip is installed: 
$ pip3 --version

   - Pip3 was not installed, and I used command : "$ sudo apt install python-pip" but it did not work.
   - As of 12/1/21, the pip3 installed using the code. Had to replace python with python3, the latest version 

   <img width="1091" alt="Screen Shot 2021-12-02 at 2 34 58 PM" src="https://user-images.githubusercontent.com/60719508/144514124-d7c53426-29f8-410b-b8e7-7c9575685ee7.png">

   - Next, add team food user: sudo adduser teamfood
   - Update: sudo apt-get update and sudo apt-get upgrade 
   - Install python3 and nginx combined with command: sudo apt-get install python3-pip nginx git
      - Sudo apt install to install packages involving python and for configuring nginx

      
      

3. ### Setup Github Repository Environment 
   - Check Git version using command: git --version
      - Output: git version 2.24.3

   
      <img width="601" alt="Screen Shot 2021-12-02 at 2 43 15 PM" src="https://user-images.githubusercontent.com/60719508/144515510-0edc1c7e-ef92-4f98-bd88-92f7d3dd5372.png">

   - Configure the Github name and email address so that everytime we do a commit, it updates the website through the domain
      - Command: git config --global user.name "Tanay Rayavarapu"
git config --global user.email "tanayrayavarapu@domain.com"

    
    <img width="597" alt="Screen Shot 2021-12-02 at 2 54 36 PM" src="https://user-images.githubusercontent.com/60719508/144516067-1c2ffd08-6a2e-42b2-b0f7-28f6c9ef9210.png">


   - Clone Github Repo: 
&nbsp;
 cd ~ git clone https://github.com/KoolKidKai/Siuuuu.git

   - Then, open up repo in files:  
ls -al
cd teamfood

4. ### Setup Virtual Environment for Python
   - Create a seperate directory to store files using command:  mkdir flask-gunicorn
   - Install flask and gunicorn packages 
       - Use command: ~/flask-gunicorn$ pip3 install flask gunicorn
   
![Screen Shot 2021-12-02 at 2 08 46 PM](https://user-images.githubusercontent.com/89223703/144511096-79395488-f9bf-4c70-be67-ba80e1f9d15c.png)
   

5. ### Establish a Service File
    - Change user to ubuntu, and create homesite.service file in Gunicorn: 
     sudo nano /etc/systemd/system/homesite.service

6. ### Configure Nginx builds a reverse proxy
    - can allow you to run multiple web servers on deployment services like raspberry pi

Check deployed website: [Team Siuuuu]()

7. ### HTTP is unsecure
    - HTTPS is secure; unsecure site can be 
    - Go back to teams: **pull from github**; **check or update the dependencies**; **restart service file** 
    - Activate HTTPS and certbot and the website should be good to go!
    
     ![Screen Shot 2021-12-15 at 5 32 24 PM](https://user-images.githubusercontent.com/60719508/146291565-cd7805a5-2db0-4930-86f2-f1a5444b8eef.png)

8. ### Update Website 
     - Pull from Github Repository and Update website every Week
     - cd into folder/directory: cd ~/siuuuu 
     - Then, git pull
     - Next, type in command source homesite/bin/activate
     - pip install -r requirements.txt
     - sudo systemctl restart homesite.service
     - Website should be updated with the most recent commit from the repository for Team Siuuuu
# Process to perform an update
1. ![image (1)](https://user-images.githubusercontent.com/89223703/146321852-b6c0736c-a85c-4cf0-9b24-b20f4a4266a6.png)
2. ![image](https://user-images.githubusercontent.com/89223703/146321860-82acf748-dcbc-4649-a701-2c14a6a27c02.png)
3. ![image (2)](https://user-images.githubusercontent.com/89223703/146321870-55a64858-376a-4cb7-98b6-24284d0f981f.png)

