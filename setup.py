from setuptools import setup, find_packages

setup(
    name='my_inventree_plugin',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,  # Stellt sicher, dass Templates und Static-Dateien aufgenommen werden
    description='Ein einfaches InvenTree Plugin zur Navigation und Testseite',
    author='Jan Schüler',
    author_email='Jandeluxe96@gmail.com',
    url='https://example.com/',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
