# Convert task 0 to puppet

class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => file,
    content => "server {
                  listen 80 default_server;
                  listen [::]:80 default_server;
									add_header X-Served-By \$hostname;
                  root /var/www/html;
                  index index.html index.htm index.nginx-debian.html;
                  server_name _;
                }",
    notify  => Service['nginx'],
  }
}
