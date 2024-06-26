from setuptools import find_packages, setup

version = '0.0.1'

setup(
    name='alerta-ding',
    version=version,
    description='Example Alerta plugin for test alerts',
    url='https://github.com/nicholasprado/alertaio/alerta-contrib',
    license='Apache License 2.0',
    author='Komal Gupta',
    author_email='komalg038@gmail.com',
    packages=find_packages(),
    py_modules=['alerta_ding'],
    install_requires=[],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.plugins': [
            'dingtalk = alerta_ding:ServiceIntegration'
        ]
    }
)
