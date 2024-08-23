# Ensure that the nginx service is installed, configured, and running

class { 'nginx':
  package_ensure => 'present',
  service_ensure => 'running',
  service_enable => true,
}

file { '/etc/nginx/nginx.conf':
  ensure  => 'file',
  content => template('nginx/conf.d/nginx.conf.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure     => 'running',
  enable     => true,
  require    => File['/etc/nginx/nginx.conf'],
  provider   => 'systemd',
}
