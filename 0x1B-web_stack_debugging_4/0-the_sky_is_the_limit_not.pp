# File: 0-the_sky_is_the_limit_not.pp

# Ensure Nginx package is installed
package { 'nginx':
  ensure => 'installed',
}

service {'nginx':
	ensure    => 'running',
	enable    => true,
	subscribe => File['/etc/nginx/nginx.conf'],
}

file {'/etc/nginx/nginx.conf':
	ensure  => 'file',
	content => template('nginx/nginx.conf.erb'),
	notify  => Service['nginx'],
}

exec {'optimize_nginx':
	command     => '/usr/sbin/nginx -s reload',
	path        => '/usr/bin:/usr/sbin:/bin:/sbin',
	refreshonly => true,
	subscribe   => File['/etc/nginx/nginx.conf'],
}
