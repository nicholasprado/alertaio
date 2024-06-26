from setuptools import find_packages, setup

version = '5.5.2'

setup(
    name='alerta-slack',
    version=version,
    description='Alerta plugin for Slack',
    url='https://github.com/nicholasprado/alertaio/alerta-contrib',
    license='MIT',
    author='Nick Satterly',
    author_email='nick.satterly@theguardian.com',
    packages=find_packages(),
    py_modules=['alerta_slack'],
    install_requires=[
        'requests'
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.plugins': [
            'slack = alerta_slack:ServiceIntegration'
        ]
    }
)
