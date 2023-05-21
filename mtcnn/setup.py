import sys
from setuptools import setup, setuptools

if sys.version_info < (3, 4, 1):
    sys.exit('Python < 3.4.1 is not supported!')

setup(name='mtcnn',
      description='Multi-task Cascaded Convolutional Neural Networks for Face Detection, based on TensorFlow',
      url='http://github.com/ipazc/mtcnn',
      packages=setuptools.find_packages(exclude=["tests.*", "tests"]),
      install_requires=[
          "keras>=2.0.0",
          "opencv-python>=4.1.0"
      ],
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      keywords="mtcnn face detection tensorflow pip package",
      zip_safe=False)
