# Linux installation and Setting up a Working Environment
The following is a guide to set up a solid work environment on Ubuntu. With this guide, we will install VSCode, Git and more, set up virtual environments for coding and install matematica. 

## Table of Contents
- [Ubuntu Installation](#ubuntu_installation)
- [Working Setup](#working_setup)
- [Python Virtual Environments](#python_virtual_environments)
- [Julia](#julia)
- [Mathematica](#mathematica)
- [Mount a Formatted Disk](#mount_a_formatted_disk)
- [Shell Scripting](#shell_scripting)
- [Install Zotero](#install_zotero)
- [Download Fonts](#download-fonts)

## Ubuntu Installation
To reboot your machine with the latest version of Ubuntu, follow the steps on [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview).

Once Ubuntu is opened on your machine, you can always type `CTRL`+`ALT`+`T` to open a terminal. You can see the content of the current folder with `ls`. Use `cd` with the path to navigate in your folders. `~/` to write app path from the home trajectory. `..` will bring you back one folder. Use the command `mkdir` with the path and the name to create a folder. `mv old_folder_name new_folder_name` to rename a folder. `rmdir folder_name` to delete an empty folder and `rm -r folder_name` to delete a folder with stuff in it or to delete specific files. `touch file_name` can be used to create a file. `mv old_name new_name` to rename a file.

You can also always look for Ubuntu updates with `sudo apt-get update`.

## Working Setup
We can then start install stuff on our machine. 
* Python3 is preinstalled on the machine. In the terminal we can always type `python3` to acces a Python interpreter. 
* VSCode can be installed directly from the App Center. `code .` to open VSCode from the terminal. In order to run python in VSCode, you'll have to download the python extension direction from VSCode. You can also download the Jupyter extension to create Jupyter notebooks. To create a notebook, simply create a file with extension `.ipynb`.

Then, in a terminal,
* `sudo apt install pip` to install pip. Used to install python packages.
* `sudo apt-get install git` to install git.
* `pip install virtualenv` to install a package for virtual environments. For some reason, there has been a bug on Ubuntu 23.10 that forced me to use `sudo apt install python3-virtualenv` to install packages.

## Python Virtual Environments
After the installation of virtualenv, you can create an environement with `virtualenv path/name`. Then, you can activate the environment with `source path/name/bin/activate`. Example : `source ~/venv/radar/bin/activate`. You can always `deactivate` the environment. The `pip install jupyterlab` or `sudo snap install jupyter` to install jupyter. You can then always open a Jupyter notebook with the command `jupyter lab` (or `jupyter notebook` for previous version). You can always close the instance from the terminal with `CTRL`+`C`.

If you are working in a project with a `requirements.txt` file with the required packages needed to work on the projet, you simply have to run `pip install -r requirements.txt` to install the packages on your activated virtual environment.

## Julia
To install Julia, simply run `curl -fsSL https://install.julialang.org | sh` in a terminal or follow these (instructions)[https://julialang.org/downloads/]. This command doesn't seem to work too well with the snap installation of curl. If you get an error saying that curl wasn't able to find a path, you can remove the snap version and install the apt version. 
```
sudo snap remove curl
sudo apt install curl
```
Then, `sudo snap install julia` will allow you to simply type `julia` in a terminal to run it. In order to run Julia in a Jupyter notebook, you'll have to install the IJulia package. To do so, in a terminal,
```
julia
using Pkg
Pkg.add("IJulia")
``` 
You should know have acces to the Julia kernel in your notebooks.

## Mathematica
I used the following [Mathematica engine installation](https://nicoguaro.github.io/posts/wolfram_jupyter/) tutorial, but it only worked to install the engine. To execute the download file, `sh path/WolframEngine_14.0.0_LINUX.sh`. For some reason, on VSCode and Jupterlab, the kernel was not able to connect. So I had to used this [Mathematica engine front-end](https://mathematica.stackexchange.com/questions/198839/how-to-add-a-front-end-to-the-free-wolfram-engine) tutorial to be able to use Mathematica in Jypter.

You can always, from the terminal, open Mathematica with `wolframscript`, and use `CTRL`+`D` to exit the script.

## Mount a Formatted Disk
After you plugged in the formatted disk:
* `mdkir ~/usb` to create a folder if you don't already have one.
* `lsblk` to find the name of disk. If the disk is called `sdb1`
* `sudo mount /dev/sdb1 ~/usb` to mount the disk.

To unmount the usb stick,
* `sudo umount ~/usb`

## Shell Scripting
[automate](https://blog.stackademic.com/automating-tasks-in-linux-using-cron-jobs-and-shell-scripting-6d23651b3c2c)


## Install Zotero
Zotero is a reference management tool. To install it on Ubuntu, start by downloading the tarball from [Zotero](https://www.zotero.org/download/) website. Then from your download folder, extract its content
```
tar -xjf Zotero-7.0.2_linux-x86_64.tar.bz2
```
Move to a proper apt folder. Then, from this folder, update `.desktop` file for the location and create a symbolic link in the local applications directory
```
mv Zotero_linux-x86_64 /opt/zotero
cd /opt/zotero
set_launcher_icon
ln -s /opt/zotero/zotero.desktop ~/.local/share/applications/zotero.desktop
```
Zotero should then be accessible through the application launcher. YOu can then add the [Zotero connector](https://www.zotero.org/download/) for Firefox in order to upload papers online directly to Zotero.

## Download Fonts
A lot of different fonts can be download directly from [Google Fonts](https://fonts.google.com/), but extra steps are needed to have acces to these fonts on other softwar. Once you have picked and download the desired font, unzip the download file and move the `.ttf` file(s) into the font folders. For example, I create a folder called `google` within my font folder. In order to move the files,
```
sudo cp ~/Downloads/Sulphur_Point/SulphurPoint-Regular.ttf  /usr/share/fonts/truetype/google/
```
Then, update the cache
```
sudo fc-cache -f -v
```
You can then make sure your new font as been properly added to the font list
```
fc-list | grep "Sulphur Point"
```
You should now have acces to the font through all apts.