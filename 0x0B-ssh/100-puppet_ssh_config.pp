#set up client SSH configuration to connect without typing password
include stdlib

file_line { 'No password':
  ensure => present,
  path   => '/home/yourusername/.ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Identity file':
  ensure => present,
  path   => '/home/yourusername/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}
