# fixing the user files limit

exec {'replace-1':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile unlimited/" /etc/security/limits.conf',
  before   => Exec['replace-2'],
}

exec {'replace-2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile unlimited/" /etc/security/limits.conf',
}
