redis-subschat
========

A multi-tematic, content based, web-chat implemented with Redis Pub/Sub.

Requirements
------------

- Redis: http://redis.io/download
- redis-py: https://github.com/andymccurdy/redis-py
- PyQt4: https://www.riverbankcomputing.com/software/pyqt/download

Installation tips
-----------------
Under the file **settings.py** you can see that the web-chat client is setup to
work using a Redis instance running on the local machine on port 6379 (the default one):

.. code-block:: python
	
	import redis

	config = {
		'host': 'localhost',
		'port': 6379,
		'db': 0,
	}

	r = redis.StrictRedis(**config)
	
the **config** dict can be configured according the desired specification.
To get additional informations, consult the official redis-py repository
and its documentation at https://redis-py.readthedocs.org/.

Usage
-----

Once you have setup the **settings.py** according to the preferred specification
and the StrictRedis object is connected to an active Redis Server Instance, from shell:

.. code-block:: bash

	$ python redis_web-chat.py
	
this will pop out the user interface of the application.
Once the user interface is displayed, directly interact with it.
