# README

### Python Toolkit

PyKit is a Python wrapper for [DB2Sock](https://bitbucket.org/litmis/db2sock).

> As of major version zero, PyKit only supports an HTTP REST transport. Before
trying to use PyKit, please be sure to have DB2Sock up and running with an HTTP
transport available. Follow the
[DB2Sock Instlalation Instructions](https://bitbucket.org/litmis/db2sock#markdown-header-yips-pre-compiled-test-vesion)
and
[setup](https://bitbucket.org/litmis/db2sock/src/8361279737df4f9a7cffe02fa164ad21f1d0c2b0/toolkit/fastcgi/?at=master)
either nginx or apache.

### PyKit Setup

PyKit is not an official Python Package quite yet, so install it like any
package that is in development.

#### Clone repository

You'll need the PyKit source to install

```commandline
$ git clone git@github.com:Club-Seiden/pykit.git
```

#### Use pip3 to install PyKit

PyKit uses Python 3, so be sure to use `pip3` when installing.

```commandline
$ cd pykit
$ pip3 install ./pykit
```

> If you're having trouble installing a new version of PyKit, try running
install with `--upgrade`

```commandline
$ pip3 install --upgrade ./pykit
```

### Testing PyKit

Unit tests are in place for PyKit. To run them, use the normal command.

```commandline
$ cd /path/to/source/of/pykit/
$ python3 -m unittest
```

> PyKit requires the transport information be setup to run tests. These are
setup with bash environment variables. If you're running the test for the 
first time and don't have the bash variables defined somewhere, you'll
probably need to do something like:

```commandline
$ export PK_DB2SOCK_URL='http://127.0.0.1:8088/db2json.db2'; export PK_DB2SOCK_USER=db2_user; export PK_DB2SOCK_PASS=db2_password;
$ cd /path/to/source/of/pykit
$ python3 -m unittest
```
