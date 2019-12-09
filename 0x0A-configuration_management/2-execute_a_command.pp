# kill a process
exec { 'killmenow':
path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
command => 'pkill "killmenow"'
}