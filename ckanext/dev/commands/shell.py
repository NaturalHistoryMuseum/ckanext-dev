import ckan.lib.cli as cli
from IPython import embed
import logging

log = logging.getLogger(__name__)


class ShellCommand(cli.CkanCommand):
    """
    Commands:
        paster --plugin=ckanext-dev shell -c <config> [-a <action>]

    Where:
        <config> = path to your ckan config file
        <action> = Specify an action (as a URL path) to have the shell open in
                   the context of the associated controller. If this is not
                   defined, the shell opens in the context of the plugin.
    """

    summary = __doc__.split('\n')[0]
    usage = __doc__
    context = None

    def command(self):
        '''
        Parse command line arguments and call appropriate method.
        '''
        self._load_config()
        embed()
        # type('NewClassName', (BaseClass,), {'a_func': a_func})