# Git introduction
Git is a distributed version control system (DVCS) designed to track changes in source code during software development. In this tutorial, I assume that `Github` is being used as the hosting plateform. I will also assume that either `WSL` or `Linux` is being used.

## Table of Contents
- [Creating a SSH key](#creating_ss_key)
- [Git Configuration](#git_configuration)
- [Clone a Github repo with SSH](#Cloning_github)
- [Creating a new branch](#branch)
- [Push and Pull](#push_pull)
- [Track a specific branch from the repo](#track-a-specific-branch-from-the-repo)
- [Resolve merge conflicts by given priority to modifications on the main](#resolve-merge-conflicts-by-given-priority-to-modifications-on-the-main)
- [Pull changes made on the main onto your own branch](#pull-changes-made-on-the-main-onto-your-own-branch)

## Creating a SSH key
An SSH key, or Secure Shell key, is a pair of cryptographic keys used to establish secure, encrypted communication between two parties over an insecure network. In our case, it is used to make the connection between a PC/laptop and our online Github account. Any repository for which you have acces through your Github account can be cloned on the linked machine without having to generate a new token (password equivalent) each time you want to work on your projects. Reference : [Github Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

In your shell, type the following to generate a new SSH key.
```
ssh-keygen
```
You can simply press enter through every question to leave the default saving parameters and to not have a password for the key. In my case, this password is not particularly useful since no one else then me uses my laptop. In Linux, I actually used the command `ssh-keygen -o -t -C "yanic.cardin.1@gmail.com"`.

Now that the key has been generated, we will need to copy its content to link it to a Github account. Usually, the key should have been saved in a folder named `.ssh` in your home directory. To copy the containt of the key (change key name for actual key name on your machine) use the `clip` command from Linux
```
clip.exe < id_rsa.pub
```
Or you can simply open the file to copy its content manually
```
cat id_rsa.pub
```

Then, on your Github account clic on your profil image in the top right corner and go into
* Settings
* SSH and GPG keys
* New SSH key

Then give a name to your key and past the content of your clipboard to link your machine to you Github account.

## Git Configuration
In a terminal, in order to configure git on your machine
```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

## Clone a Github repo with SSH
1. I personally like to create a Git folder where I store all my Git projects. To do so, use the `cd` command to reach the folder where you would want to greate your git folder. To create a folder called git, type
```
mkdir git
```
2. Then you can acces your folder
```
cd git
```
3. From the Github website of the repo you are trying to clone, copy the SSH link (click on the `<> Code` button and copy the link)
4. Back in you shell, type
```
git clone <past HTTPS link>
```
5. A clone of the repo should now be in your Git folder.

## Creating a new branch
To see the list of available branches
```
git branch
```
To create a new branch
```
git branch <new_branch_name>
```
To checkout to a branch
```
git checkout <branch_name>
```
The new branch is a copy of the branch you are currently on. To branchout of your `main` branch, make sure you use `git checkout main` before creating the new branch. You can also create a new branch and automatically checkout to it.
```
git checkout -b <new_branch_name>
```
In order to be able to work from your new branch and push its content onto your online repo, it first has to be set upstream (push the new branch to your online repo). To do so
```
git push --set-upstream origin <new_branch_name>
```
or, in short,
```
git push -u origin <new_branch_name>
```

## Push and Pull
To pull the latest changes from your online repo to your local machine, in your repo folder, type
```
git pull
```
The pulled branched is by default the currently checked-out one. To pull from another branch, do
```
git pull origin <branch_name>
```
Then, you will make some changes to your branch and eventually, you will want to push it back to your online repo. Here's how to do it. 

0. The command `git status` allows you to see the modified files that have or have not yet been commited.

1. You first have to stage the modified files. Staging is the process of selecting specific changes to be part of the next commit.
```
git add <file1> <file2> ...
```
You can also stage all modified files at once
```
git add --all
```
2. Then, you need to commit the changes. This commit is only local. 
```
git commit -m 'Your commit message.'
```
3. Finally, you can push the changes to the remote repository.
```
git push
```
It is sometimes necessary to specify both the remote repository and the branch to be pushed.
```
git push origin branch_name
```

## Track a specific branch from the repo
To pull a specific branch from the repo, `git checkout --track origin/branch_name`. Alternatively,
```
git fetch origin
git checkout branch_name
```
Other alternative
```
git checkout -b branch_name origin/branch_name
```
## Resolve merge conflicts by given priority to modifications on the main
First, make sure you have the lastest modifications to the main branch.
```
git checkout main
git pull origin main
```
Then switch to your branch and merge the main unto it by specifing with the strategy `theirs` that you want to give priority to the main whenever their is a conflict.
```
git checkout your_branch
git merge main --strategy-option=theirs
```
Then you can commit the changes to the your branch
```
git commit -m 'your message'
git push
```
Then the pull request can be made from Github. Their should not be any conflicts anymore.

## Pull changes made on the main onto your own branch
```
git fetch origin
git checkout your_branch
git merge origin/main
```
Alternative
```
git checkout main
git git pull
git checkout your_branch && git merge main
```
I believe there might be a better way to do that using `base` or `rebase`.