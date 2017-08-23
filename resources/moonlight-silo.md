---
layout: default
exclude: true
---

# Installing pyvisfile on moonlight

First of all, here are the modules I have loaded:

`git, subversion, gcc, hdf5-serial, openmpi, python, user_contrib, silo/4.10.2,
boost/1.62.0`

Next, create a python 2.7 conda environment and activate it:

~~~bash
$ conda create -n py27 python=2.7 anaconda
$ source activate py27
~~~

Now, there is some mis-match of libgcc in anaconda and this version
of pyublas/boost, whatever. This can be rectified by installing/upgrading
the version of libgcc in the anaconda environment:

`$ conda install libgcc`

Next we can configure, build and test pyublas:

~~~bash
$ ./configure.py --python-exe=python \
			    --boost-inc-dir=$BOOST_INC_DIR \
			    --boost-lib-dir=$BOOST_LIB_DIR \
			    --boost-compiler=gcc \
			    --boost-python-libname=boost_python
$ make
$ make install
$ cd test
$ python test_pyublas.py
~~~

Finally, configure and build pyvisfile:

~~~bash
$ ./configure.py --use-silo \
		--silo-inc-dir=$SILO_INC_DIR \
		--silo-lib-dir=$SILO_LIB_DIR \
		--python-exe=python \
		--boost-inc-dir=$BOOST_INC_DIR \
		--boost-lib-dir=$BOOST_LIB_DIR \
		--boost-compiler=gcc \
		--boost-python-libname=boost_python
$ make
$ make install
~~~

Importing pyvisfile.silo throws an error that it cannot find
libsiloh5.so. this seems to be rectified by appending `$SILO_LIB_DIR` to your
`$LD_LIBRARY_PATH`:

`$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$SILO_LIB_DIR`
