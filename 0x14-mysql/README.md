# 0x14. MySQL

The main role of a database is to provide a centralized, organized, and structured repository for storing and managing large amounts of data. It enables efficient data retrieval and manipulation through the use of query languages and indexing, and provides mechanisms for data integrity and security. Databases can be used for a wide range of applications, including financial systems, customer relationship management (CRM) systems, and e-commerce websites.

A database replica is a copy of a database that is used to provide redundancy and high availability. The replica is kept in sync with the primary database, ensuring that data remains consistent across all instances.

The purpose of a database replica is to provide a backup for the primary database in case it becomes unavailable due to a failure or outage. The replica can be used to take over the role of the primary database, allowing the application to continue functioning with minimal downtime.

Database backups need to be stored in different physical locations to protect against data loss due to physical disasters such as fires, earthquakes, and floods. In the event that one of the backup locations is affected by a disaster, the other backups can be used to recover the data. This helps ensure that the data remains available even in the face of catastrophic events.

To make sure that your database backup strategy actually works, you should regularly perform a "test restore." This involves restoring the backup to a test environment and verifying that the data can be successfully retrieved. This helps ensure that the backup is viable and can be used in the event of a real disaster. It also helps identify any potential problems with the backup process so that they can be addressed before a real emergency occurs.

## To install MySQL on your web-01 and web-02 servers, you can follow these steps:

Log in to your servers via SSH:

```
ssh username@web-01.example.com
```

Repeat this step for web-02.example.com as well.

Update the package index:

```
sudo apt update
```

Install the MySQL server package:

```
wget http://repo.mysql.com/mysql-apt-config_0.8.10-1_all.deb
```

Ubuntu bionic - Mysql server & cluster - mysql 5-7 - ok

```
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
```

Update the package index:

```
sudo apt update
```

If you see an error like this :

GPG error: http://repo.mysql.com/apt/ubuntu bionic InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 467B942D3A79BD29

Run this script :

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29
```

replace this with the code from your error

install mysql 5.7.\*

```
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
```

If you got an error again :
dpkg: dependency problems prevent configuration of mysql-server:
mysql-server depends on mysql-community-server (= 5.7.37-1ubuntu18.04); however:
Package mysql-community-server is not configured yet.

fix with this:
vi /etc/apt/preferences.d/mysql

Package: mysql-server
Pin: version 5.7\*
Pin-Priority: 1001

Package: mysql-client
Pin: version 5.7\*
Pin-Priority: 1001

Clean Setup again:
apt-get remove mysql-client mysql-common mysql-community-client mysql-community-server mysql-server
apt-get purge mysql-client mysql-common mysql-community-client mysql-community-server mysql-server

apt-get update

Install mysql again :
sudo apt install -f mysql-client mysql-community-server mysql-server

Repeat the above steps for web-02.example.com.

Once the installation is complete, you can verify that the MySQL service is running by checking its status:

```
sudo service mysql status
```

You should now have MySQL installed on both web-01 and web-02 servers.
