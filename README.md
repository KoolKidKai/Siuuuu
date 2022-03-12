# Siuuuu
We love diversity and also girls in comp sci, but we don't have any girls unfortunately. But we do have diversity. Go NightHawks!

## Project Description
Our project is dedicated to the learning, improvement, and utmost enjoyment of coding! We aspire to help beginners improve their coding ability by implementing a series of levels that increase difficulty as they complete the tasks. By the end, they should see themselves as better programmers than before while also having enjoyed the journey. We are Team Siuuuu and are sponsored by Hackclub, a group of coders hoping to teach beginner coders.

### [Group Policies](https://github.com/KoolKidKai/Siuuuu/wiki/Policies)

![ronaldo-siu-ronaldo-siuuu](https://user-images.githubusercontent.com/60719508/157750787-d3631b6d-3c34-4032-b246-b4c1392acc22.gif)

### Project Sponsors

Rishi and Arnav --> HackClub

What is HackClub?
- This is a club on campus that helps students find their interest in coding, and overall become more passionate in the field. 

## Plans & Policies

## Issues Policies
- Ideas are to be made into issues, placed in the to-do list and discussed
- Rejected ideas are to be placed in archive
- Approved ideas are to be placed in progress and assigned 
- Once completed, review with team and either keep in progress or move to completed by the person assigned

## Contributing Policies
- If .gitignore does not contain the following on your local: .idea, *.xml, *.iws, *.iml, *.ipr, then please add before committing/pushing
- Never push a file you did not create or edit that you know of. If you are unsure, don't do it!
- If you do get one, talk with team and add to .gitignore as needed
- Always pull at the start of the day to avoid merge conflicts
- Always pull before a push to avoid merge conflicts
- Pull requests/branches as of now will not be used but may be potentially incorporated in the future depending on the project

# Deployment
## Deployment system

- Deployment will be run by Raspberry Pi
- All files and commands have been added to the raspberry pi terminal
- Raspberry Pi can be accessed through Virtual-Network-Computing View and will be shared by email
## Updating Code
- Once on Raspberry Pi, open the terminal
- Type in "git pull" to pull the code(make sure you have "/PARK-tech" before it)
- If something was added to requirements.txt type in "sudo pip install -r requirements.txt"
- Lastly, restart service with "sudo systemctl restart homesite.service"

### Details
- All code before the end of class on Thursdays are to be pushed collectively.
- You may work afterwards individually, but have distinct deadline:
- DEADLINE: Every Thursday at 6pm (push code)
- Once proper commits are pushed, close and move appropriate issues and scrumboard tasks.
- Update README and Timebox
- Review Ticket to be updated with what's completed as final update, then send to teacher for live review with runtime link.

### Screenshot of HTTPS nginx config file for reference: 
<img width="683" alt="httpsscreen" src="https://cdn.discordapp.com/attachments/749509501773807677/921201293039648768/Screen_Shot_2021-12-16_at_4.43.11_PM.png">

### Screenshot of Service file for reference:
<img width="668" alt="serviceconfig" src="https://cdn.discordapp.com/attachments/749509501773807677/921201340724703272/Screen_Shot_2021-12-16_at_4.43.53_PM.png">

### Procedures

# Push/Pull Procedure
**Important - Make sure code works between each step**
1. Give proper name/description to commits
2. Commit changes to local branch
3. Pull from origin main
4. Push commit to origin(branch)
5. Push commit origin main
6. Go to Github and look for pull request, or create a new one.
7. Ensure that the head repository is KoolKidKai/Siuuuu
8. Accept and merge the pull request if it allows, or fix the conflict if there is one.
9. Pull the origin/main into your local branch again

# Fork and Commit Procedure
When committing, use your personal branch until your feature is complete and working. Once it is complete, follow the push/pull procedure above to add your feature to the origin/main branch.

## [Scrum Board](https://github.com/KoolKidKai/Siuuuu/projects/1)

## Web Project

## Description
Our project is dedicated to the learning, improvement, and utmost enjoyment of coding! We aspire to help beginners improve their coding ability by implementing a series of levels that increase difficulty as they complete the tasks. By the end, they should see themselves as better programmers than before while also having enjoyed the journey. We are Team Siuuuu and are sponsored by Hackclub, a group of coders hoping to teach beginner coders.



## Plans/Ideas/Wires
### Ideas
- Goal is to have the user interact with the website frequently
- Beginner coders must be entertained and attracted to the website; needs to be nicely designed
- Coders will get tasks to complete
- As they complete tasks, they will move up to different levels of difficulty; almost like a ranking system
- Each level has harder and harder tasks to complete
- Option of adding a score for each user as they move up levels
 
### Plans
- Use different APIs to make levels of code
- Use a google search bar for prizes and different fun gifs
- Have a music theme playing in the background after completing each level
- Design a nice and appealing website for everyone to read easily
### [Wireframe](https://docs.google.com/drawings/d/1UfPqEDXEEcWHStgHxJzHTTz78GcYTPCZ8vMpj08az-s/edit?usp=sharing)
<img width="936" alt="Screen Shot 2022-03-11 at 1 49 33 PM" src="https://user-images.githubusercontent.com/60719508/157975270-60091694-33cc-4b86-96df-5b34e672d345.png">

### Beginner Level
<img width="838" alt="Screen Shot 2022-03-11 at 2 02 47 PM" src="https://user-images.githubusercontent.com/89277945/157976571-60d6ed15-2571-4d8d-a9ed-980d1b90a81e.png">


### Intermediate Level 
<img width="861" alt="Screen Shot 2022-03-11 at 2 00 56 PM" src="https://user-images.githubusercontent.com/60719508/157976369-4dfac059-fb48-41a2-be5d-94465d7affa9.png">


### Hard Level
![image](https://user-images.githubusercontent.com/89219486/157976238-8e720aac-2049-4001-b1fc-0f1649d8317d.png)


## [Time Box](https://github.com/KoolKidKai/Siuuuu/blob/main/README.md)

## Weekly TPT's
### Week 0 TPT

# Week 0 TPT Notes

## Computing
- Can be harmful due to dopamine addiction --> Results in lack of desire to complete important things
- Example of Anthony Rosner and addiction to World of Warcraft; depleted him of real world skills and made him lazy

## Digital Divide
- A division in access of technology; CSP brings technology people together
- Degree in computer science can help get jobs and big companies; technology is the future
- Barriers or red tape restrictions on digital usage; different barriers in different places (ie. Del Norte# )




Week 0
=======
Setup roles for team members.

Role | Person | Description 
 ------- | ----- | ----------- |
Scrum Master | Colin |  Ensure roles are assigned.  Build Scrum Board. 
Github Admin | Colin | Setup Project in Git.  Integrate any starter code from Trimester 1.  Build policies for Fork and Pull requests.
Primary Designer | Armaan | Primary Designer and Layout manager.  Organize Jinja2 Enabled Templates, ensure usage of Bootstrap (minimize CSS customization per page).  Establish plan for overrides on each of the User Pages.
Deployment Manager | Tanay | (RPi or AWS).  Deploy Web site.  Establish policy and frequency for updates.  Ensure site is not broken and always alive for reviews.
Technical Officer | Ritvik | Works with Teacher, Classroom TOs, and BOF TO's to form TPT lessons and Tech Talk Topics for Trimester.  Also, facilitates learning of Technical Concepts within Scrum Team.






