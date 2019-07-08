from distutils.core import setup

with open("README.rst", "r") as f:
    readme = f.read()

setup(name='jturtle',
      version='0.5.1',
      description='Turtles in the Jupyter Notebook',
      long_description = readme,
      author='Thomas Kluyver & Oliver Cordes',
      author_email='ocordes@astro.uni-bonn.de',
      url='https://github.com/ocordes/jturtle',
      packages=['jturtle'],
      package_data={'jturtle': ['jturtle_javascript/*.js']},
      classifiers=[
          'Framework :: IPython',
          'Intended Audience :: Education',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Artistic Software',
          'Topic :: Education',
      ],
      install_requires=['IPython', 'ipywidgets>=7.0.0'],
)
