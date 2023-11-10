# WSL installation and configuration walkthrough
WSL (Windows subsystem for Linux) allows you to install and use Linux applications directly on Windows without the overhead of a traditional virtual machine or dualboot setup.

## Table of Contents
- [Install WSL](#install_wsl)
- [Install Anaconda](#install_anaconda)
- [Configure Git](#configure_git)
- [Clone a Git repo](#clone_git)

## Install WSL
Useful link : [WSL installation](https://learn.microsoft.com/en-us/windows/wsl/install)
1. Open a command prompt by typing `cmd` in the Windows start menu.
2. The following allows you to install Ubuntu. For a complet list of available Linux type `wsl --list --online`
```
wsl –install -d Ubuntu
``` 
3. Ubuntu should open by itself and ask you to create a username and a password. If you get an error `WslRegisterDistribution failed with error : 0x800701bc` then you might have to download and execute an Linux kernel update and do the previous step again. [Download the Linux kernel update package](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
4. To use the autocomplet feature, in Ubuntu Shell, type `sudo apt install bash-completion`. After closing and then reopening the window, you can use Tab to autocomplet your commands.
5. From now on, you can always open your Linux shell by typing `Ubuntu` in the Windows start menu.

## Install Anaconda
Anaconda allows you to create environments for your coding projects. It is best practice to create a different environment for every projet containing only the minimal libraries required. The environment system also allows you to use specific Python version for every project as well. To install Anaconda
1.  Copy the link to the Linux Installer in the download page of the [Anaconda](https://www.anaconda.com/download/#linux) website (both of the page).
2. Open your Linux shell and type `wget` and past the Anaconda extension. It should look something like
```
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
```
3. Run the installation script
```
bash Anaconda3-2023.09-0-Linux-x86_64.sh
```
4. Answer `yes` to both questions so that your Linux shell always show you the Anaconda environnement you are in and allow you to enter `conda` commands. Close Ubuntu and open it again. It should look something like `(base) yaniccd@DESKTOP-CU9PH0T :` since by default, your conda environnement is called `base`.

## Configure Git
```
git config –global user.email [your email]
git config –global user.name [your user name]
```

## Clone a Git repo
The following section should be modified to use SSH instead of using HTTPS links.
1. I personally like to create a Git folder where I store all my Git projects. To do so, use the `cd` command to reach the folder where you would want to greate your git folder. To create a folder called git, type
```
mkdir git
```
2. Then you can acces your folder
```
cd git
```
3. From the Github website of the repo you are trying to clone, copy the HTTPS link (click on the `<> Code` button and copy the link)
4. Back in you shell, type
```
git clone [past HTTPS link]
```
5. Github will ask you for your username and a password (Token). The create a token, on you Github profil, then
    * Settings
    * Developer Settings (at the bottom)
    * Personal access Tokens
    * Tokens (classic)
    * Generate new token
    * Generate new token (classic)
    * Setup the token then copy it, this is your password.