# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='StyleTransferTensorFlow',
    url='https://github.com/LordHarsh/Neural_Style_Transfer',
    author='Hash Banka',
    author_email='harshbanka321@gmail.com',
    # Needed to actually package something
    packages=setuptools.find_packages(),
    # Needed for dependencies
    install_requires=['matplotlib','tensorflow','os-win','ffmpy','glob2', 'pytest-shutil', 'pytube', 'opencv-python', 'pillow', 'numpy', 'tensorflow_hub'],
    # *strongly* suggested for sharing
    version='0.1.3',
    # The license can be anything you like
    license='MIT',
    description="Package to apply style transfer on different frames of a video",
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
    python_requires='>=3.6',
)