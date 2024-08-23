# This Puppet manifest optimizes Nginx configuration for handling high 
traffic loads

# Ensure the Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
}

# Update the Nginx configuration for performance optimization
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

# Ensure the Nginx configuration directory exists
file { '/etc/nginx/conf.d':
  ensure => directory,
}

# Place your custom configuration for handling static assets and routing
file { '/etc/nginx/conf.d/default.conf':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    server_name localhost;

    # Serve static assets
    location /static/ {
        alias /path/to/web_dynamic/static/;
    }

    # Route requests to Gunicorn
    location / {
        proxy_pass http://127.0.0.1:5003;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
  ",
  notify  => Service['nginx'],
}

# Restart Nginx to apply the new configuration
exec { 'restart_nginx':
  command => '/usr/sbin/nginx -s reload',
  path    => ['/usr/sbin', '/usr/bin'],
  refreshonly => true,
  subscribe => File['/etc/nginx/nginx.conf'],
}
