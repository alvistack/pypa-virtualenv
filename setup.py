# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='virtualenv',
    version='20.24.2',
    description='Virtual Python Environment builder',
    maintainer_email='Bernat Gabor <gaborjbernat@gmail.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    install_requires=[
        'distlib<1,>=0.3.7',
        'filelock<4,>=3.12.2',
        'importlib-metadata>=6.6; python_version < "3.8"',
        'platformdirs<4,>=3.9.1',
    ],
    extras_require={
        'docs': [
            'furo>=2023.5.20',
            'proselint>=0.13',
            'sphinx-argparse>=0.4',
            'sphinx>=7.0.1',
            'sphinxcontrib-towncrier>=0.2.1a0',
            'towncrier>=23.6',
        ],
        'test': [
            'covdefaults>=2.3',
            'coverage-enable-subprocess>=1',
            'coverage>=7.2.7',
            'flaky>=3.7',
            'packaging>=23.1',
            'pytest-env>=0.8.2',
            'pytest-freezer>=0.4.8; platform_python_implementation == "PyPy"',
            'pytest-mock>=3.11.1',
            'pytest-randomly>=3.12',
            'pytest-timeout>=2.1',
            'pytest>=7.4',
            'setuptools>=68',
            'time-machine>=2.10; platform_python_implementation == "CPython"',
        ],
    },
    entry_points={
        'console_scripts': [
            'virtualenv = virtualenv.__main__:run_with_catch',
        ],
        'virtualenv.activate': [
            'bash = virtualenv.activation.bash:BashActivator',
            'batch = virtualenv.activation.batch:BatchActivator',
            'cshell = virtualenv.activation.cshell:CShellActivator',
            'fish = virtualenv.activation.fish:FishActivator',
            'nushell = virtualenv.activation.nushell:NushellActivator',
            'powershell = virtualenv.activation.powershell:PowerShellActivator',
            'python = virtualenv.activation.python:PythonActivator',
        ],
        'virtualenv.create': [
            'cpython3-mac-framework = virtualenv.create.via_global_ref.builtin.cpython.mac_os:CPython3macOsFramework',
            'cpython3-posix = virtualenv.create.via_global_ref.builtin.cpython.cpython3:CPython3Posix',
            'cpython3-win = virtualenv.create.via_global_ref.builtin.cpython.cpython3:CPython3Windows',
            'pypy3-posix = virtualenv.create.via_global_ref.builtin.pypy.pypy3:PyPy3Posix',
            'pypy3-win = virtualenv.create.via_global_ref.builtin.pypy.pypy3:Pypy3Windows',
            'venv = virtualenv.create.via_global_ref.venv:Venv',
        ],
        'virtualenv.discovery': [
            'builtin = virtualenv.discovery.builtin:Builtin',
        ],
        'virtualenv.seed': [
            'app-data = virtualenv.seed.embed.via_app_data.via_app_data:FromAppData',
            'pip = virtualenv.seed.embed.pip_invoke:PipInvoke',
        ],
    },
    packages=[
        'virtualenv',
        'virtualenv.activation',
        'virtualenv.activation.bash',
        'virtualenv.activation.batch',
        'virtualenv.activation.cshell',
        'virtualenv.activation.fish',
        'virtualenv.activation.nushell',
        'virtualenv.activation.powershell',
        'virtualenv.activation.python',
        'virtualenv.app_data',
        'virtualenv.config',
        'virtualenv.config.cli',
        'virtualenv.create',
        'virtualenv.create.via_global_ref',
        'virtualenv.create.via_global_ref.builtin',
        'virtualenv.create.via_global_ref.builtin.cpython',
        'virtualenv.create.via_global_ref.builtin.pypy',
        'virtualenv.discovery',
        'virtualenv.discovery.windows',
        'virtualenv.run',
        'virtualenv.run.plugin',
        'virtualenv.seed',
        'virtualenv.seed.embed',
        'virtualenv.seed.embed.via_app_data',
        'virtualenv.seed.embed.via_app_data.pip_install',
        'virtualenv.seed.wheels',
        'virtualenv.seed.wheels.embed',
        'virtualenv.util',
        'virtualenv.util.path',
        'virtualenv.util.subprocess',
    ],
    package_dir={'': 'src'},
)
