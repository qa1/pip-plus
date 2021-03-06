import setuptools
from setuptools import find_packages, setup
# python setup.py bdist_wheel --universal
# twine upload dist/*


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pip-plus",
    version="0.0.1.dev4",
    author="huohongming",
    author_email="gin_huo@hotmail.com",
    description="A small pip web management tool package",
    long_description=long_description,  
    long_description_content_type="text/markdown",
    url="https://github.com/hmhuo/pip-plus",    
    license='MIT',
    keywords='sample setuptools development',
    package_dir={"": "src"},
    packages=find_packages(
        where="src",
    ),

    python_requires=">=3.4",
    platforms=["windows"],
    entry_points={'console_scripts': [
        'pp = pip_plus.pip_plus:main',
    ]},

    package_data={
        # "pip_plus.html.css": ["*.css"],
        # "pip_plus.html.images": ["*.ico","*.svg"],
        # "pip_plus.html.scripts": ["*.js"],
        # "pip_plus.html": ["index.html"],
        "pip_plus":[
        "controllor/ProcessGET.py",
        "html/index.html",
        "html/css/baseStyle.css",
        "html/css/bootstrap-min.css",
        "html/css/bootstrap.min.css",
        "html/css/bootstrap.min.css.map",
        "html/css/dashboard.css",
        "html/css/fileinput.min.css",
        "html/css/jquery.loading.css",
        "html/css/jquery.loading.min.css",
        "html/images/favicon.ico",
        "html/images/white-cube.svg",
        "html/scripts/bootstrap.js",
        "html/scripts/dataHandleScript.js",
        "html/scripts/fileinput.min.js",
        "html/scripts/ie10-viewport-bug-workaround.js",
        "html/scripts/jquery-3.2.1.min.js",
        "html/scripts/jquery-3.3.1.min.js",
        "html/scripts/jquery.loading.js",
        "html/scripts/jquery.loading.min.js",
        "html/scripts/layoutScript.js",
        "html/scripts/mainScript.js",
        "html/scripts/pageHandleScript.js",
        "html/scripts/popper.min.js",
        ],

    },

    # data_files=[
    # ("", [
    #     "src/pip_plus/html/index.html",
    #     "src/pip_plus/html/css/baseStyle.css",
    #     "src/pip_plus/html/css/bootstrap-min.css",
    #     "src/pip_plus/html/css/bootstrap.min.css",
    #     "src/pip_plus/html/css/bootstrap.min.css.map",
    #     "src/pip_plus/html/css/dashboard.css",
    #     "src/pip_plus/html/css/fileinput.min.css",
    #     "src/pip_plus/html/css/jquery.loading.css",
    #     "src/pip_plus/html/css/jquery.loading.min.css",
    #     "src/pip_plus/html/images/favicon.ico",
    #     "src/pip_plus/html/images/white-cube.svg",
    #     "src/pip_plus/html/scripts/bootstrap.js",
    #     "src/pip_plus/html/scripts/dataHandleScript.js",
    #     "src/pip_plus/html/scripts/fileinput.min.js",
    #     "src/pip_plus/html/scripts/ie10-viewport-bug-workaround.js",
    #     "src/pip_plus/html/scripts/jquery-3.2.1.min.js",
    #     "src/pip_plus/html/scripts/jquery-3.3.1.min.js",
    #     "src/pip_plus/html/scripts/jquery.loading.js",
    #     "src/pip_plus/html/scripts/jquery.loading.min.js",
    #     "src/pip_plus/html/scripts/layoutScript.js",
    #     "src/pip_plus/html/scripts/mainScript.js",
    #     "src/pip_plus/html/scripts/pageHandleScript.js",
    #     "src/pip_plus/html/scripts/popper.min.js",
    #     ]),
    # ],
    # package_data={
    #     # If any package contains *.txt or *.rst files, include them:
    #     '': ['*.js', '*.css','*.html','*.svg'],
    #     # # And include any *.msg files found in the 'hello' package, too:
    #     # 'hello': ['*.msg'],
    # },


    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ),
    project_urls={
    'Documentation': 'https://github.com/hmhuo/pip-plus/wiki',
    # 'Funding': 'https://donate.pypi.org',
    # 'Say Thanks!': 'http://saythanks.io/to/example',
    'Source': 'https://github.com/hmhuo/pip-plus',
    'Tracker': 'https://github.com/hmhuo/pip-plus/issues',
},
)

