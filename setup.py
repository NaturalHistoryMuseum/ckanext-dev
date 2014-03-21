from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ckanext-dev',
    version=version,
    description="",
    long_description="""\
    """,
    classifiers=[],
    keywords='',
    author='Alice Heaton',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.dev'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[  # -*- Extra requirements: -*-
    ],
    entry_points="""
            [ckan.plugins]
                dev = ckanext.dev.plugin:DevPlugin
            [paste.paster_command]
                shell=ckanext.dev.commands.shell:ShellCommand
        """
)
