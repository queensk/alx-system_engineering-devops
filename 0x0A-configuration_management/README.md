# 0x0A. Configuration management

## [Background Context](https://twitter.com/devopsreact/status/836971570136375296)

When I was working for SlideShare, I worked on an auto-remediation tool called Skynet that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server’s hostname or any other metadata we had (server type, server environment…). At some point, a bug was present in my code that sent nil to the filter method.

There were 2 pieces of bad news:

    1. When MCollective receives nil as an argument for its filter method, it takes this to mean ‘all servers’
    2. The action I sent was to terminate the selected servers

I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare’s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoint's, and videos… Pretty bad!

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)…

Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.

## Install puppet

```
sudo apt-get install -y ruby=1:2.7+1 --allow-downgrades && sudo apt-get install -y ruby-augeas && sudo apt-get install -y ruby-shadow && sudo apt-get install -y puppet
```

## Install puppet-lint

```
sudo gem install puppet-lint
```

## Puppet

Puppet is a configuration management tool that is used to automate the deployment and management of servers. It allows you to define the desired state of your infrastructure, and then automatically enforces that state on your servers.

The core concept of Puppet is the use of "manifests" which are written in the Puppet DSL (domain-specific language). Manifests contain "resources" which are basic building blocks for your infrastructure. Each resource describes some aspect of your server, such as a file, package, service, or user.

Here is an example of a simple manifest that installs the "ntp" package and starts the "ntp" service:

```
package { 'ntp':
  ensure => installed,
}

service { 'ntp':
  ensure => running,
  enable => true,
}

```

## Writing Puppet manifests

Writing Puppet manifests is done using the Puppet Domain Specific Language (DSL), which is based on Ruby and has a simple, easy-to-read syntax.

Here are some basic concepts to help you get started writing Puppet manifests:

- Resources: Resources are the basic building blocks of Puppet manifests. A resource can be anything that can be managed on a server, such as a file, package, service, or user. Resources are declared using the resource type followed by a name in the format type { 'name':.

- Attributes: Attributes are used to set various properties of a resource. They are set using the => operator, and are separated from the resource name by a comma. For example, to ensure a package is installed, you would use ensure => installed.

- Dependencies: You can specify that one resource should be applied before another using require or before metaparameter, for example you can ensure that a service is started after a package is installed by adding require => Package['ntp'].

Classes: Classes allow you to organize resources into reusable groups. They are defined using the class keyword, and can be included in other manifests using the include keyword.

Here's an example of a simple Puppet manifest that installs the "ntp" package and starts the "ntp" service:

```
package { 'ntp':
  ensure => installed,
}

service { 'ntp':
  ensure => running,
  enable => true,
  require => Package['ntp'],
}

```

## Puppet, classes

In Puppet, classes are used to organize resources into reusable groups. Classes are defined using the class keyword, and can be included in other manifests using the include keyword.

Here's an example of a simple class called ntp:

```
class ntp {
  package { 'ntp':
    ensure => installed,
  }

  service { 'ntp':
    ensure => running,
    enable => true,
  }
}

```

This class declares a package resource for the "ntp" package and a service resource for the "ntp" service. To use this class in another manifest, you would include it like this:

```
include ntp
```

You can also pass parameters to class and use them inside, here's an example of a class that take a variable:

```
class ntp (
  $package_name = 'ntp',
  $service_name = 'ntp'
) {
  package { $package_name:
    ensure => installed,
  }

  service { $service_name:
    ensure => running,
    enable => true,
  }
}

```

you can use this class in another manifest and pass the values of the parameters:

```
class { 'ntp':
  package_name => 'ntpdate',
  service_name => 'ntp',
}

```

## create a file using Puppet file

In Puppet, you can create a file using the file resource type. The file resource allows you to manage the content, ownership, permissions, and other properties of a file on a server.

Here's an example of how you can create a file called example.txt with the contents "Hello, World!":

```
file { '/path/to/example.txt':
  ensure => file,
  content => 'Hello, World!',
}

```

In this example, the file resource is declared with a title of /path/to/example.txt. The ensure attribute is set to file, which means that Puppet will ensure that a file with this name exists. The content attribute is set to the string "Hello, World!", which will be written to the file.

If the file should be managed in a different way, you can change the value of the ensure attribute. You can use ensure => absent to remove the file, ensure => directory to make sure it's a directory and many other possibilities.

You can also set other attributes for the file, such as owner and group to set the ownership of the file and mode to set the permissions. Here's an example that sets the owner, group and mode of a file:

```
file { '/path/to/example.txt':
  ensure  => file,
  content => 'Hello, World!',
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
}

```

You can also specify a source file, which allows you to manage the file using a file on your local machine. This can be useful for deploying configuration files or scripts to servers. For example:

```
file { '/path/to/example.txt':
  ensure => file,
  source => 'puppet:///modules/mymodule/example.txt',
}

```

## Author

Queens Kisivuli <queenskisivuli@gmail.com>
