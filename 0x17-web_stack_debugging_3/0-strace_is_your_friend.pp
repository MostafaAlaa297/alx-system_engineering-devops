# Puppet manifest to fix Apache 500 error

# Ensure Apache service is running
service { 'apache2':
	ensure  => 'running',
}

# Fix Apache configuration file
file { '/etc/apache2/apache2.conf':
	ensure  => present,
	content => template('apache/apache2.conf.erb'),
	notify  => Service['apache2'],
}

# Ensure required packages are installed
package { 'apache2':
	ensure  => 'installed',
}
