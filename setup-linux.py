from setuptools import setup

def readme():
    with open("README.rst") as f:
        README = f.read()
    return README

setup(
    name='CrawlerCodePythonTools-Linux',
    version='1.1.6',
    packages=['pythontools.core', 'pythontools.identity', 'pythontools.sockets', 'pythontools.telegrambot', 'pythontools.dev'],
    url='',
    license='',
    author='CrawlerCode',
    author_email='',
    description='',
    long_description=readme(),
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=["colorama", "telegram", "python-telegram-bot", "cloudpickle"]
)