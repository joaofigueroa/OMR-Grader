# OMR Grader

Grader for bubble sheet multiple choice tests using Optical Mark Recognition, Python, and OpenCV. Test images should be 300 dpi or greater.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisities

* Python 3
* OpenCV 3.4.3 or later
* NumPy
* imutils

### Installing on Mac/Linux
To install the libraries, run the following commands:
```
$ brew install python3
$ pip install opencv-python
$ pip install numpy
$ pip install imutils
```

### Installing on Windows Subsystem for Linux
To install the libraries, run the following commands:
```
$ apt install python3
$ apt install python3-opencv
$ apt install python3-pip
$ pip3 install numpy
$ pip3 install scipy
$ pip3 install imutils
```

## Running

`$ python grader.py --image [path to image]`

## Acknowledgements
Adrian Rosebrock's OMR tutorial "Bubble sheet multiple choice scanner and test grader using OMR, Python, OpenCV"
Daniel Van Beurden
