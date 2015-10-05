# Python Of War

**Dependencies:**

Python 3.4+ and PyGame

* python3
* python3-dev
* python3-numpy
* python3-simplejson
* python3-easygui
* python3-tk

```sh
$ sudo apt-get install python3-tk python3-easygui python3-simplejson
```

>Ubuntu Dependencies
```sh
$ sudo apt-get install build-essential
```


# PyGame for Python3 in Virtualenv

**PySDL**

```sh
$ sudo apt-get install python3-dev python3-numpy libav-tools libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev  libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev
```

**Freetype**

```sh
$ sudo apt-get install libfreetype6
```

**PIP**

```sh
$ sudo apt-get install python-pip
```

**Mercurial clone ('$hg clone'... Similar '$git clone')**

```sh
$ sudo apt-get install mercurial meld
```

**Virtualenv/VirtualenvWrapper**

```sh
$ sudo apt-get install virtualenvwrapper
```


> Note: Run the following command, only once
```sh
$ source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
```

> Create a new Virtualenv
```sh
$ mkvirtualenv --python=/usr/bin/python3 NAME_VENV
```

> Activate Virtualenv

```sh
$ workon NAME_VENV
```

> Install pygame for python3 in Virtualenv

```sh
(NAME_VENV)$ sudo pip install hg+http://bitbucket.org/pygame/pygame
```
