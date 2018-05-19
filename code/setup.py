from distutils.core import setup

setup(name="pynimations",
      packages=["pynimations"],
      version="3.2.6",
      description="All-in-one python library for program loading animations",
      long_description="Visit https://tbhaxor.me/pynimations/",
      author_email="Gurkirat Singh <tbhaxor@gmail.com>",
      author="Gurkirat Singh",
      url="https://tbhaxor.me/pynimations/",
      download_url="https://github.com/tbhaxor/pynimations/archive/pynimations-v3.2.6.tar.gz",
      keywords="pynimations gurkirat_singh tbhaxor",
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
      license="GPL-3.0",
      python_requires='>=3',
      install_requires=["pbars", "termisize"],
      )
