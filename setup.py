from distutils.core import setup

setup(
    name='cankan.vip.worker',
    version='1.0',
    packages=[],
    url='',
    license='',
    author='FIRAT',
    author_email='muratf@gmail.com',
    description='',
    scripts=['AppRun.py'],
    install_requires=["flask",
                      "pymongo",
                      "gevent",
                      "MongoEngine",
                      "apscheduler"],
    package_data={
        'data': ['config.json'],
    }
)
