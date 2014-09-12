from distutils.core import setup

setup(
    name='HappyCowler',
    version='0.1',
    author='Peter Wittek',
    author_email='peterwittek@users.noreply.github.com',
    packages=['happycowler'],
    url='http://peterwittek.github.io/happycowler/',
    keywords=[
        'vegan',
        'vegetarian',
     'happycow.net',
     'crawler',
     'kml'],
    license='LICENSE',
    description='Crawl the HappyCow database to KML files for offline use.',
    long_description=open('README.rst').read(),
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
         'Operating System :: OS Independent',
         'Intended Audience :: End Users/Desktop',
         'Development Status :: 3 - Alpha',
         'Programming Language :: Python'
    ],
    install_requires=[
        "beautifulsoup >= 4"
    ],
)