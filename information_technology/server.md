# Connect to server from Linux
## Connecting to server
Most Poly hosted servers will require you to be on Poly's network in order to connect. You can always follow Poly's tutorial to install a Proxy and work from home. In order to connect to a server of IP adresse `000.000.00.00` for example, in a terminal type
```
ssh user_id@000.000.00.00
```
with your actual user id.

## Connect without password
You can also use an ssh key in order to note have to input your password everytime. To see if you already have an ssh key for that specific machine you are using
```
cd ~/.ssh
ls
```
in which there should be a file of the form `id_rsa.pub`. If not, you can generate one with the command
```
ssh-keygen
```
Then, to like this key to the server, from that same path, input
```
ssh-copy-id user_id@000.000.00.00
```
The server now automatically recognize your machine when connecting and doesn't prompt for a password.

## Configuration Directive
If you don't want to have to write down the IP adresse everytime you want to connect, you can add the host directive to the `config` file. Again, within the `~/.ssh` folder, create the `config` file
```
nano config
```
In which you can write something like
```
VisualHostKey=yes

Host host_config
	HostName 000.000.00.00
	User user_name
```
where you can change the variable name `host_config` for anything you'd like. Then, you can connect on the host simply by typing
```
ssh host_config
```

## Other useful tips
You can use the following from within the host.
* `who` will list the user currently connected to the server.

* `htop` Show usage of the 128 cores of the CPU. Useful to see if you can launch something or not. Simply press `q` to quit.

* `./gpuviz.sh` similar to the previous, will show the GPU usage. I believe that `ctrl+D` is used to quite.

There is also a way to run task over a long period of time without having to keep your machine open.
```
screen -R
```
will open a new terminal in which you can run the time consumming task. If you were to `exit`, that would automatically kill the task. Instead, you can `ctrl+A` then `ctrl+D` in order to detach from the current terminal without killing the task. You can come back to this terminal by doing `screen -R` again. The initial task you started should still be running if it wasn't done executing.