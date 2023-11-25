# Create a file

file {'/tmp/school':
    ensure  => file,
    path    => '/tmp/school',
    mode    => '0744',
    owner   => 'www-data',
    content => 'I love Puppet',
}