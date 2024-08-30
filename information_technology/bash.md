BASH stands for Born Again Shell. It is the language to interact with Linux' OS.

Basic commands
* `echo`
* `cd <path>` Stand for change directory. The path is stated from current path. `~` brings us to the home directory, `..` references the parent directory while `.` references the current directory.
* `pwd` returns current directory
* `ls` list the files and directory of current path.
* `sudo` super user do, allows one to run any administrator command.
* `touch <file>`
* `mkdir <path>` stands for make directoy.
* `nano <file>` opens file in text editor.
* `clear` clears the directory
* `mv <file> <path>` moves a files. Can also change the file name if we give an extension to `<new_path>`.
* `cp <file> <path>` copies a file.
* `cp -r <path1> <path2>` copies a whole directory, where `r` stands for recursive which allows use to work with the whole content of a path.
* `rm <file>` removes (deletes) a file.
* `rm -r <path>` removes (deletes) a directory.
* `cat <file>` stands for concatenate. Allows to read the content of a file.
* `head <file>` returns 5 first lines of a file. Or use `head -n 10 <file>` to specify the number of lines to display, 10 in that case.
* `tail <file>` returns 5 last lines of a file.
* `grep <"string"> <file>` returns all lines with occurence of the string in the file.
* `find <path> -name *.py` search for files or directory from a certain path. Use `find . -name *.py` to look in current directory. `*` means that you are taking all that finishes with `.py`.

More advance commands.
* `sudo apt update` to update packages on the account.
* `sudo apt insall <package>` to install a package.

## My very first BASH script
Open the text editor and create a bash script (with extension `.sh`) by typing `nano script.sh`. Then, you can write the follow where the first lines defines the type of scrpit written (telling the BASH interpreter what language to use for this script).
```BASH
#!/bin/bash
echo "I will go to sleep for 5 seconds."
sleep 5
echo "Okay, I'm awake."
```
Then `CTRL+X` to exist the script, then `Y` to save and `Enter` to finish. The script can then be ran through `bash script.sh`. Just running `./script.sh` will not work until we change the permission so that the file can be execute. The command to do so is `chmod +x script.sh`. You should see that it is now executable when running `ls -l`. The permission for that file should have changed from `-rw-r` to `-rwxr`. If the previous doesn't run, you might have your BASH saved somewhere else. To find where it is, in a terminal, write `which $SHELL`.
To turn into an executable,
