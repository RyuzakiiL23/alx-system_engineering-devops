# Convert task 0 to puppet

class nginx_example {
  package { 'nginx':
    ensure => 'installed',
  }

  service { 'nginx':
    ensure => 'running',
    enable => true,
  }

  file { '/var/www/html/index.nginx-debian.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => file,
    content => "server {\n  add_header X-Served-By $hostname;\n}\n",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  exec { 'ufw_allow_nginx':
    command     => '/usr/sbin/ufw allow "Nginx HTTP"',
    path        => ['/usr/sbin', '/usr/bin'],
    unless      => '/usr/sbin/ufw status | grep "Nginx HTTP"',
    subscribe   => Package['nginx'],
  }
}
