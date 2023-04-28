# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='virtualenv',
    version='20.21.1',
    description='Virtual Python Environment builder',
    maintainer_email='Bernat Gabor <gaborjbernat@gmail.com>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],
    install_requires=[
        'distlib<1,>=0.3.6',
        'filelock<4,>=3.4.1',
        'importlib-metadata>=4.8.3; python_version < "3.8"',
        'platformdirs<4,>=2.4',
    ],
    extras_require={
        'docs': [
            'furo>=2022.12.7',
            'proselint>=0.13',
            'sphinx-argparse>=0.4',
            'sphinx>=6.1.3',
            'sphinxcontrib-towncrier>=0.2.1a0',
            'towncrier>=22.12',
        ],
        'test': [
            'covdefaults>=2.2.2',
            'coverage-enable-subprocess>=1',
            'coverage>=7.1',
            'flaky>=3.7',
            'packaging>=23',
            'pytest-env>=0.8.1',
            'pytest-freezegun>=0.4.2',
            'pytest-mock>=3.10',
            'pytest-randomly>=3.12',
            'pytest-timeout>=2.1',
            'pytest>=7.2.1',
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
            'cpython2-mac-arm-framework = virtualenv.create.via_global_ref.builtin.cpython.mac_os:CPython2macOsArmFramework',
            'cpython2-mac-framework = virtualenv.create.via_global_ref.builtin.cpython.mac_os:CPython2macOsFramework',
            'cpython2-posix = virtualenv.create.via_global_ref.builtin.cpython.cpython2:CPython2Posix',
            'cpython2-win = virtualenv.create.via_global_ref.builtin.cpython.cpython2:CPython2Windows',
            'cpython3-mac-framework = virtualenv.create.via_global_ref.builtin.cpython.mac_os:CPython3macOsFramework',
            'cpython3-posix = virtualenv.create.via_global_ref.builtin.cpython.cpython3:CPython3Posix',
            'cpython3-win = virtualenv.create.via_global_ref.builtin.cpython.cpython3:CPython3Windows',
            'pypy2-posix = virtualenv.create.via_global_ref.builtin.pypy.pypy2:PyPy2Posix',
            'pypy2-win = virtualenv.create.via_global_ref.builtin.pypy.pypy2:Pypy2Windows',
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
        'virtualenv.create.via_global_ref.builtin.python2',
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
