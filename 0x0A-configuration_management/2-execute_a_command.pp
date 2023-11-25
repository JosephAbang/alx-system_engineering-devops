# puppet kills a process

exec { 'killmenow':
    command => 'pkill -f killmenow',
    onlyif  => 'pgrep -f killmenow',
}