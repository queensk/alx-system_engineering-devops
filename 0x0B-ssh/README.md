# 0x0B. SSH

To connect to a remote host using an SSH RSA key pair, you will need to do the following:

1. Generate an RSA key pair on your local machine by using the command ssh-keygen -t rsa

```
ssh-keygen -t rsa -b 4096
```

2. Copy the public key to the remote host by using the command

```
ssh-copy-id user@remote_host
```

or
create a file and save it in

```
/.ssh/filename
```

change the filename mode to

```
chmod 600 filename
```

3. Connect to the remote host using the private key by using the command

```
ssh name@ipaddress -i ~/.ssh/filename
```

The command you provided is used to connect to a remote server with the IP address using the SSH protocol. The user specified is "name" and the private key used for authentication is located at ~/.ssh/school.

The "-i" option is used to specify the private key file to use for authentication.

This command will prompt for the password of the user ubuntu on the remote host if the key pair is not added to the authorized_keys file on the remote host or if the key is not accepted by the remote host.

Note that if the private key is protected by a passphrase, you will be prompted to enter the passphrase before the connection can be established.

Also make sure that you have the right permissions to access the private key file and the ssh directory.

## Create an SSH key pair

```
ssh-keygen -t rsa -b 4096 -P betty -f school
```

This command is used to generate an RSA key pair with the name "school" and a key size of 4096 bits, protected by the passphrase "betty".

The ssh-keygen command is a command-line utility for generating new SSH key pairs. The options used in this command are as follows:

    -t specifies the type of key to create. In this case, it is set to rsa.
    -b specifies the number of bits in the key. In this case, it is set to 4096.
    -P sets the passphrase for the key. In this case, it is set to "betty".
    -f specifies the file name of the key. In this case, it is set to "school"

The command will create both the private and the public key, the private key is going to be stored in the file "school" and the public key in "school.pub"

It is important to keep your private key secure, and not to share it with anyone. Always make sure to use a strong passphrase to protect your private key.

Also make sure that you have the right permissions to access the directory where the files will be created and to create new files in it.

Also, to use the key pair to connect to remote servers, you'll need to copy the content of the public key (school.pub) file to the authorized_keys file on the remote server.

## Add the SSH public

To add more SSH keys for authorization on an Ubuntu machine, you can follow these steps:

Open the authorized_keys file in a text editor:

```
nano ~/.ssh/authorized_keys
```

Add a new line to the file and paste in the additional SSH key(s) you want to add. Each key should be on its own line.
Save and close the file.
