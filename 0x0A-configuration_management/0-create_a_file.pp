# File: create_a_file.pp

# Define a class to create a file
#class create_a_file {
file{'/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
#}
