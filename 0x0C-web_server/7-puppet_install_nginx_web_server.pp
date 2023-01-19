# Puppet manifest to install nginx
package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
        listen 80 default_server;
        server_name _;
        root /var/www/html;
        index index.html;

        server_name _;
        error_page 404 /custom_404.html;
        location = /custom_404.html {
        root /usr/share/nginx/html;
        internal;
        }
        
        location / {
                try_files $uri $uri/ /index.html;
        }

        location /redirect_me/ {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        add_header Content-Length 193;
        }
}',
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
