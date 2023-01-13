## 0x0C. Web server

## [0-transfer_file](./0-transfer_file)

The script you provided is a Bash script that is designed to transfer a file from the local machine to a remote machine via SCP (secure copy). The script takes four parameters as inputs:

1. PATH_TO_FILE: The path of the file on the local machine that you want to transfer
2. IP: The IP address of the remote machine
3. USERNAME: The username of the remote machine
3. PATH_TO_SSH_KEY (Optional): The path of the SSH key that should be used for the connection.

The script first checks if the number of arguments passed to it is less than 3, if it is then it will print a usage message telling the user the proper format of the command.

If the number of arguments passed to it is at least 3, then it will use the scp command to transfer the file. The -o StrictHostKeyChecking=no option is used to disable strict host key checking, allowing the script to connect to the remote machine without requiring manual confirmation.

If the number of arguments passed to the script is 4, it will also include the -i "$4" option in the scp command, specifying the path to the SSH key that should be used for the connection.

## Install nginx web server

The -y option in the apt-get -y install command is used to automatically answer yes to any prompts that would otherwise be displayed during the installation process.

When you run apt-get install command, apt package manager will prompt you with a message asking if you want to continue the installation process, the -y option is used to automatically confirm that you want to continue without being prompted.

The -y option is useful when you want to run the command in a script or automated process, where you don't want to be prompted for input. It also saves time when you are installing multiple packages and don't want to manually confirm each one.


1. apt-get update - This command updates the package lists to ensure that the latest versions of packages are available.

2. apt-get -y install nginx - This command installs the Nginx package and its dependencies. The -y option automatically answers "yes" to any prompts that would otherwise be displayed during the installation process.

3. ufw allow 'Nginx HTTP' - This command allows incoming traffic on port 80, which is the default port for HTTP traffic. It allows Nginx HTTP traffic via ufw (uncomplicated firewall)

4. echo 'Hello World!' > /var/www/html/index.html - This command creates a new file called index.html in the /var/www/html directory and writes the text "Hello World!" to the file. This file will be served as the default page for the web server.

5. service nginx start - This command starts the Nginx service.
