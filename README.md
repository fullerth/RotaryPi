# Virtual Environment
`.gitignore` will ignore a virtual environment folder named `pirot_venv/`

The python bindings for dbus cannot be installed into a virtual environment via 
pip as it [does not have a `setup.py`](
https://abdealiik.wordpress.com/2015/06/09/python-dbus-and-continuous-integration/)
Install the python dbus bindings package: `apt-get install python3-dbus`. Create 
the virtual environment using the [`--system-site-packages` option](
http://stackoverflow.com/questions/13365697/install-python-dbus-in-virtualenv#answer-13367493)

# Testing
Since the code relies on RPi.GPIO it must be tested using `sudo`
