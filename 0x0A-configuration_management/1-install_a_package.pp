# File: 1-install_a_package.pp

# Ensure the flask pakage is installed
package{'install-flask':
  command  => '/usr/bin/pip3 install flask=2.1.0',
  path     => '/usr/bin',
  unless   => '/usr/bin/pip3 show flask } grep -q "Version: 2.1.0"',
}
