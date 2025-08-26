The PSM Class
=======================

The ``PSM`` class holds methods corresponding to all API endpoints
that the server provides. In order to get connected to a PSM server,
start by initializing a new instance of this class.

Example using the .penrc configuration file located in the users home
directory (default)

.. code-block:: python

   from psmapi import PSM

   # Log into a PSM server instance with credentials from the default .penrc file
   myPSM = PSM()


Example specifying a configuration file

.. code-block:: python

   from psmapi import PSM

   # Log into a PSM server instance with credentials from the specified config file
   myPSM = PSM(config="/home/user/my_config")


Example specifying server and login parameters

.. code-block:: python

   from psmapi import PSM

   # Log into a PSM server instance with credentials supplied
   myPSM = PSM(server="https://10.9.5.21",user='admin',password="Passw0rd!",tenant='default')


Take a look at the next few topics for information on all the methods the
``PSM`` class has available and their corresponding data structures.

Basic Methods
-------------

.. autoclass:: pensando.PSM
   :members:


.. |br| raw:: html

   <br />
