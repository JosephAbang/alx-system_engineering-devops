## 0x14. MySQL

- [Description](#description)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. Install MySQL](#0-install-mysql)
  - [1. Let us in!](#1-let-us-in)
  - [2. If only you could see what I've seen with your eyes](#2-if-only-you-could-see-what-ive-seen-with-your-eyes)
  - [3. Quite an experience to live in fear, isn't it?](#3-quite-an-experience-to-live-in-fear-isnt-it)
  - [4. Setup a Primary-Replica infrastructure using MySQL](#4-setup-a-primary-replica-infrastructure-using-mysql)
  - [5. MySQL backup](#5-mysql-backup)

## Description

This project involves setting up a MySQL database with a primary-replica infrastructure and implementing backup strategies.

## Requirements

- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- The first line of all Bash scripts should be \`#!/usr/bin/env bash\`
- The second line of all Bash scripts should be a comment explaining the script's purpose

## Tasks

### 0. Install MySQL

Install MySQL on both web-01 and web-02 servers. MySQL distribution must be 5.7.x.

### 1. Let us in!

Create a MySQL user named \`holberton_user\` on both web-01 and web-02 with the host name set to \`localhost\` and the password \`projectcorrection280hbtn\`. Grant \`holberton_user\` permission to check the primary/replica status of the databases.

### 2. If only you could see what I've seen with your eyes

Create a database named \`tyrell_corp\` on web-01, and within it, create a table named \`nexus6\` with at least one entry.

### 3. Quite an experience to live in fear, isn't it?

On web-01, create a new user named \`replica_user\` for the replica server with \`%\` as the host name and grant appropriate permissions.

### 4. Setup a Primary-Replica infrastructure using MySQL

Setup replication for the MySQL database named \`tyrell_corp\`. The primary MySQL server must be hosted on web-01 and the replica on web-02.

### 5. MySQL backup

Write a Bash script that generates a MySQL dump named \`backup.sql\` containing all MySQL databases. Compress this dump to a tar.gz archive with the format \`day-month-year.tar.gz\`.

## Author
abangjosef@gmail.com
