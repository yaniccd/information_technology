# Linux installation and Setting up a Working Environment
The following is a guide to set up a solid work environment on Ubuntu. With this guide, we will install VSCode, Git and more, set up virtual environments for coding and install matematica. 

## Table of Contents
- [Ubuntu Installation](#ubuntu_installation)
- [Setting Up a Working Environment](#setting_up_a_working_environment)
- [Python Environments](#python_environments)
- [Mathematica](#mathematica)
- [Mount a Formatted Disk](#mount_a_formatted_disk)

## Ubuntu Installation
To reboot your machine with the latest version of Ubuntu, follow the steps on [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview).

Once Ubuntu is opened on your machine, you can always type `CTRL`+`ALT`+`T` to open a terminal. You can see the content of the current folder with `ls`. Use `cd` with the path to navigate in your folders. `~/` to write app path from the home trajectory. `..` will bring you back one folder. Use the command `mkdir` with the path and the name to create a folder. `mv old_folder_name new_folder_name` to rename a folder. `rmdir folder_name` to delete an empty folder and `rm -r folder_name` to delete a folder with stuff in it.

You can also always look for Ubuntu updates with `sudo apt-get update`.

## Setting Up a Working Environment
We can then start install stuff on our machine. 
* Python3 is preinstalled on the machine. In the terminal we can always type `python3` to acces a Python interpreter. 
* VSCode can be installed directly from the App Center. `code .` to open VSCode from the terminal. In order to run python in VSCode, you'll have to download the python extension direction from VSCode. You can also download the Jupyter extension to create Jupyter notebooks. To create a notebook, simply create a file with extension `.ipynb`.

Then, in a terminal,
* `sudo apt install pip` to install pip. Used to install python packages.
* `sudo apt-get install git` to install git.
* `pip install virtualenv` to install a package for virtual environments. For some reason, there has been a bug on Ubuntu 23.10 that forced me to use `sudo apt install python3-virtualenv` to install packages.

## Python Environments
After the installation of virtualenv, you can create an environement with `virtualenv path/name`. Then, you can activate the environment with `source path/name/bin/activate`. Example : `source ~/venv/radar/bin/activate`. You can always `deactivate` the environment. `sudo snap install jupyter` to install jupyter. You can then always open a Jupyter notebook with the command `jupyter notebook`. You can always close the instance from the terminal with `CTRL`+`C`.

## Matehmatica
I used the following [Mathematica engine installation](https://nicoguaro.github.io/posts/wolfram_jupyter/) tutorial, but it only worked to install the engine. To execute the download file, `sh path/WolframEngine_14.0.0_LINUX.sh`. For some reason, on VSCode and Jupterlab, the kernel was not able to connect. So I had to used this [Mathematica engine front-end](https://mathematica.stackexchange.com/questions/198839/how-to-add-a-front-end-to-the-free-wolfram-engine) tutorial to be able to use Mathematica in Jypter.

You can always, from the terminal, open Mathematica with `wolframscript`, and use `CTRL`+`D` to exit the script.

## Mount a Formatted Disk
After you plugged in the formatted disk:
* `mdkir ~/usb` to create a folder if you don't already have one.
* `lsblk` to find the name of disk. If the disk is called `sdb1`
* `sudo mount dev/sdb1 ~/usb` to mount the disk.
