ckanext-dev
===========

CKAN extension that provides various development tools :

- An IPython shell, run within the CKAN environment, started as a paster script ;
- A configuration option to start PyCharm remote debugger session

Setup
------

To enable the remote debugger session, you need:

- Install the pycharm-debug.egg package on the remote machine (this file is part of the PyCharm
  distribution, see http://www.jetbrains.com/pycharm/webhelp/remote-debugging.html)

- Add the line 'debug.enabled = True' to your configuration file

- Setup a Remote Debugger within PyCharm, using port 8888 (or as defined by debug.host.port).

You may optionally define:
- debug.host.ip for the host IP (defaults to 10.0.2.2 which is the default host IP when using Vagrant) ;
- debug.host.port for the host port (defaults to 8888; it needs to match the setting in PyCharm) ;
- debug.output.stdout_to_server to send stdout to the debugging host (defaults to True) ;
- debug.output.stderr_to_server to send stderr to the debugging host (defaults to True)


Usage
-----

To use the paster launched shell do:

paster --plugin=ckanext-dev shell -c &lt;path to your config file&gt;