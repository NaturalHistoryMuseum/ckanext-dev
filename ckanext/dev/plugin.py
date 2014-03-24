import logging

import ckan.plugins as p

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
        true_string = ['yes', 'Yes', 'true', 'True', '1']
        debug = config.get('debug.enabled', 'False')  in true_string
        host_ip = config.get('debug.host.ip', '10.0.2.2')
        host_port = config.get('debug.host.port', '8888')
        stdout = config.get('debug.output.stdout_to_server', 'True') in true_string
        stderr = config.get('debug.output.stderr_to_server', 'True') in true_string
        suspend = config.get('debug.suspend', 'False') in true_string
        if debug:
            # We don't yet have a translator, so messages will be in english only.
            log.info("Initiating remote debugging session to {}:{}".format(host_ip, host_port))
            try:
                pydevd.settrace(host_ip, port=int(host_port), stdoutToServer=stdout, stderrToServer=stderr, suspend=suspend)
            except NameError:
                log.warning("debug.enabled set to True, but pydevd is missing.")
            except SystemExit:
                log.warning("Failed to connect to debug server; is it started?")
