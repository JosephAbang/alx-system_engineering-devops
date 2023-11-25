# Install flask using puppet

package { 'python3-pip':
    ensure => 'installed',
}

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}

# Install a compatible version of Werkzeug
package { 'Werkzeug':
    ensure   => '2.1.1',
    provider => 'pip3',
    require  => Package['python3-pip'],
}