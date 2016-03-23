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

Info
----

You can find personal information about myself in my Linkedin page:
https://it.linkedin.com/in/fabrizio-farinacci-496679116

The project was developed and has been presented within the course of "Pervasive Systems", 
held by Prof. Ioannis Chatzigiannakis within the Master of Science in Computer Science (MSE-CS),
at University if Rome "La Sapienza". Informations about the course are available in the following page:
http://ichatz.me/index.php/Site/PervasiveSystems2016

Additional informations about the project can be found in the following Slideshare presentation:
http://www.slideshare.net/FabrizioFarinacci1/redis-usability-and-use-cases.

