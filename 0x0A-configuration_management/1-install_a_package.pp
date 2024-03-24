#!/usr/bin/pup
# File: 1-install_a_package.pp

# Ensure the flask pakage is installed
package{'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
