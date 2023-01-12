## 0x0C. Web server

## [0-transfer_file](./0-transfer_file)

The script you provided is a Bash script that is designed to transfer a file from the local machine to a remote machine via SCP (secure copy). The script takes four parameters as inputs:

PATH_TO_FILE: The path of the file on the local machine that you want to transfer
IP: The IP address of the remote machine
USERNAME: The username of the remote machine
PATH_TO_SSH_KEY (Optional): The path of the SSH key that should be used for the connection.
The script first checks if the number of arguments passed to it is less than 3, if it is then it will print a usage message telling the user the proper format of the command.

If the number of arguments passed to it is at least 3, then it will use the scp command to transfer the file. The -o StrictHostKeyChecking=no option is used to disable strict host key checking, allowing the script to connect to the remote machine without requiring manual confirmation.

If the number of arguments passed to the script is 4, it will also include the -i "$4" option in the scp command, specifying the path to the SSH key that should be used for the connection.

##
