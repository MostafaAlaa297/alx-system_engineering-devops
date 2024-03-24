# File: 2-execute_a_command.pp

# Define an exec resource to kill the process named "killmenow"

exec{ 'killmenow':
  command     => '/usr/bin/pkill killmenow',
  path        => '/usr/bin:/bin',
  refreshonly => true,
  logoutput   => true,
}
