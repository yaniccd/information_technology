# Git introduction
Git is a distributed version control system (DVCS) designed to track changes in source code during software development. In this tutorial, I assume that `Github` is being used as the hosting plateform. I will also assume that either `WSL` or `Linux` is being used.

## Table of Contents
- [Creating a SSH key](#creating_ss_key)
- [Clone a Github repo with SSH](#Cloning_github)

## Creating a SSH key
An SSH key, or Secure Shell key, is a pair of cryptographic keys used to establish secure, encrypted communication between two parties over an insecure network. In our case, it is used to make the connection between a PC/laptop and our online Github account. Any repository for which you have acces through your Github account can be cloned on the linked machine without having to generate a new token (password equivalent) each time you want to work on your projects.

In your shell, type the following to generate a new SSH key.
```
ssh-keygen
```
You can simply press enter through every question to leave the default saving parameters and to not have a password for the key. In my case, this password is not particularly useful since no one else then me uses my laptop. 

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

## Clone a Github repo with SSH