!['Workflow status'](https://github.com/KateSharkun/todo/actions/workflows/workflow.yml/badge.svg)
# CI/CD pipeline implementation
To create a CI/CD pipeline I decided to take small steps and started by establishing a ssh connection between my local pc and VPS. 
It gave a clear understanding of how the connection works and showed its benefits.
So I decided not to use premade GitHub actions like appleboy/ssh-action and found a great tutorial on creating a pure ssh connection
with VPS using alias (source:https://blog.benoitblanchon.fr/github-action-run-ssh-commands/) What it does is creates a folder on a runner and writes private key, 
stored in *secrets*, in a file within .ssh folder and permits it so the ssh connection could be established. Also, it binds an alias for VPS to simplify the next steps in a job 
performed on it.

Also, I needed to get a bit more knowledge on Git to correctly update files on VPS each time there is a push to repo. 
Had a small problem with branches and merge conflict because of that, editing the repo on github is not a good idea :) 
So the whole workflow looks next way: first I create and edit code 
on my local machine, then add-commit-push it to the GitHub repo and it triggers a workflow that automatically connects via ssh to VPs and updates code based on repo changes -
just as was requested in an assignment.

I created a new user on VPS and set up config to allow authorise with a key.

After that, everything was relatively easy besides small debugging for the wrong route in a bash script that made the pull request invalid, syntax errors in yaml file (dashes are important)
organizing steps in the right order. As jobs are executed dependently in a chain there was no need for multiple jobs with dependencies for this exercise.

