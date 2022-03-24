{% include navigation.html %}

{% include sponsornavbar.html %}

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
