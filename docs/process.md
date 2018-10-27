# Learning Computer Vision
## My process

The first thing I tried to do was install SimpleCV. This turned out to be
a dead end because the library seems to have been made irrelevant by updates
to OpenCV. When SimpleCV was written, even the Python implementation of OpenCV
was complicated to work with.

I did try to port SimpleCV from Legacy Python to Modern Python, but the
OpenCV APIs had changed significantly since the latest version of SimpleCV.
OpenCV-Python uses NumPy a LOT these days.

Once I decided to scale my goal back from updating SimpleCV to rebuilding it
as an IPython terminal tutorial working with OpenCV as directly as possible,
I took stock of what changes I was making as I made them. My goal is to document
my choices to that point that each line clearly serves a purpose.

Files describing packages installed and used are in requirements.txt,
envpre.txt, & envdur.txt.

[This article](https://eev.ee/blog/2016/07/31/python-faq-how-do-i-port-to-python-3/)
has helpful information on porting from 2 to 3.

[This](https://python-packaging.readthedocs.io/en/latest/minimal.html) and
[this](https://docs.python-guide.org/writing/structure/) gave me guidance on
package structure.

[This file](https://ipython.readthedocs.io/en/stable/config/intro.html)
helped me work through reconfiguring IPython terminal setup. I double-checked
each change against the
[IPython source repo](https://github.com/ipython/ipython).

[PyTest docs](https://docs.pytest.org/en/latest/assert.html)

