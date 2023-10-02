# Convert task 0 to puppet

exec {'update':
  provider => shell,
  command  => 'sudo apt-get update -y',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get install nginx -y',
  before   => Exec['add_header'],
}

exec { 'add_header':
  provider    => shell,
  environment => ["MYNAME=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\default;/include \/etc\/nginx\/sites-enabled\/\default;\n\tadd_header X-Served-By \"$MYNAME\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
