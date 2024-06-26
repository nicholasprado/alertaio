from setuptools import find_packages, setup

version = '5.1.2'

setup(
    name='alerta-zabbix',
    version=version,
    description='Alerta plugin for Zabbix',
    url='https://github.com/nicholasprado/alertaio/alerta-contrib',
    license='MIT',
    author='Nick Satterly',
    author_email='nick.satterly@gmail.com',
    packages=find_packages(),
    py_modules=['alerta_zabbix'],
    install_requires=[
        'pyzabbix'
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.plugins': [
            'zabbix = alerta_zabbix:ZabbixEventAck'
        ]
    }
)
