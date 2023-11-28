# Web Server Configuration Project

This project involves configuring a web server using Nginx. Below are the tasks and corresponding files for each task.

## Tasks

| Task | Description | File |
|------|-------------|------|
| 0 | Transfer a file to your server | [0-transfer_file](0x0C-web_server/0-transfer_file) |
| 1 | Install nginx web server | [1-install_nginx_web_server](0x0C-web_server/1-install_nginx_web_server) |
| 2 | Setup a domain name | [2-setup_a_domain_name](0x0C-web_server/2-setup_a_domain_name) |
| 3 | Redirection | [3-redirection](0x0C-web_server/3-redirection) |
| 4 | Not found page 404 | [4-not_found_page_404](0x0C-web_server/4-not_found_page_404) |

## Task Descriptions

### 0. Transfer a file to your server

Write a Bash script that transfers a file from the client to the server using `scp`.

### 1. Install nginx web server

Write a Bash script that installs Nginx on the server. Nginx should be listening on port 80 and return "Hello World!" when queried at root (/).

### 2. Setup a domain name

Provide a domain name and configure DNS records with an A entry to point to the web server's IP address.

### 3. Redirection

Configure Nginx to redirect /redirect_me to another page with a "301 Moved Permanently" status.

### 4. Not found page 404

Configure Nginx to have a custom 404 page that returns an HTTP 404 error code and contains the string "Ceci n'est pas une page."
