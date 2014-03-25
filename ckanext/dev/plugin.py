import logging

import ckan.plugins as p
from paste.deploy.converters import asbool

try:
    import pydevd
except ImportError:
    pass

log = logging.getLogger(__name__)


class DevPlugin(p.SingletonPlugin):
    """Development plugin.

    This plugin provides:
    - Start remote debugger (if correct library is present) during update_config call
    """
    p.implements(p.IConfigurer)

    def update_config(self, config):
        self._start_debug_client(config)

    def _start_debug_client(self, config):
        debug = asbool(config.get('debug.remote', 'False'))
        host_ip = config.get('debug.remote.host.ip', '10.0.2.2')
        host_port = config.get('debug.remote.host.port', '8888')
        stdout = asbool(config.get('debug.remote.stdout_to_server', 'True'))
        stderr = asbool(config.get('debug.remote.stderr_to_server', 'True'))
        suspend = asbool(config.get('debug.remote.suspend', 'False'))
        if debug:
            # We don't yet have a translator, so messages will be in english only.
            log.info("Initiating remote debugging session to {}:{}".format(host_ip, host_port))
            try:
                pydevd.settrace(host_ip, port=int(host_port), stdoutToServer=stdout, stderrToServer=stderr, suspend=suspend)
            except NameError:
                log.warning("debug.enabled set to True, but pydevd is missing.")
            except SystemExit:
                log.warning("Failed to connect to debug server; is it started?")
