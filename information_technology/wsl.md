# WSL installation and configuration walkthrough
WSL (Windows subsystem for Linux) allows you to install and use Linux applications directly on Windows without the overhead of a traditional virtual machine or dualboot setup.

## Table of Contents
- [Install WSL](#install_wsl)
- [Install Anaconda](#install_anaconda)
- [Configure Git](#configure_git)
- [Clone a Git repo](#clone_git)
- [Create a conda environnement for your git projet](#conda_env)
- [Open a git repo stored on your WSL using VScode](#open_vscode)
- [Jyputer notebook in WSL VS Code](#jupyter_notebook)

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
6. A clone of the repo should now be in your Git folder.

## Create a conda environnement for your git projet
It is best practice to have a different python environnement for every different git projet so that you only use the
specifed libraries of the projet.
1. Open your Linux shell.
2. Most git repos will specify the Python version to use in the Readme.md file. If you don't specify the Python version, the latest Python version will automatically be applied to your environment
```
conda create -n [name of your environnement] python=[Python version]
```
3. To change from the base environnement to your new environnement, type
```
conda activate [name of your environnement]
```
4. Use the `cd` command to go into the folder where the requirements file is. Most repos will have a requirements file with the list of librairies to install in order to work with the Git project.
5. To add the Python libraries specified in the requirements file to your actvated conda environnement, type (requirements files might have a different name)
```
pip install -r requirements.txt
```
6. Come back at the head of your repo directory using `cd ..` if need be.
7. To root your environnement at the head of the repo (that tells Python where to look for the import functions) type
```
pip install -e . –user
```
8. It should not be the case, but if you get an error message saying something like `pip is not reconize as an internal command`. Type `conda install pip`

## Open a git repo stored on your WSL using VScode
Finally, you can run VScode directly form your Linux environment. To do so
1. Open VScode, search for `WSL` in the vscode extension section on the left and install it.
2. In your Linux shell, type `code .` to open VS Code in your current folder. If that doesn’t work, it might be because VS Code (and thus the command `code`) is not in your Linux PATH variable (tells Linux where to look for commands). So you would then have to had it manually. To do so
    * Locate where your VS Code bin folder is saved on your laptop/PC and copy that path. Mine was in `c/Users/yanic/AppData/Local/Programs/Microsoft VS Code/bin/`
    * In your Linux shell, type `echo $PATH` and make sure this path is not already in the variable. If it is, your problem comes from somewhere else. At that point, I can’t help anymore...
    * `echo 'export PATH=\$PATH:"/mnt/[past path to bin folder]"' >> ~/.bashrc`
    * The command `echo` makes your previous changes permanent so be careful what you do. If you would like to test if modifying your PATH variable fixes your problem before making the changes permanent, only type `export PATH=\$PATH:"/mnt[past path to bin folder]` and try to open VS Code again using `code .` If it works, use the previous line to make the change permanent.

## Jyputer notebook in WSL VS Code
The following steps will allow you to run Jyputer notebooks from VS Code in you Linux environment
1. In a VS Code instence open from your Linux shell, install the extension name "Jupyter". Make sur to select "install for WSL".
2. You can now create files with the `ipynb`
3. In the top left corner of VS Code, Select Kernel
4. Import python environnements