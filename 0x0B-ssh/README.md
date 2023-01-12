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
