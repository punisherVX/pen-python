Using a Config File
=======================

The default config file (.ini format) for pen-python is the .penrc file located
in the user's home directory.  Other config files can be specified but each
class that uses this config file has it's own section in the config file.

In the case of the PSM class, it reads the information from the [PSM_API] section.
If using a config file for connecting and logging into the PSM cluster, it must
have this heading or it will not work.

Here is an example .penrc file used by the PSM class

.. code-block::

[PSM_API]
server = https://10.29.75.21
user = admin
password = Pensando0$
tenant = default




.. |br| raw:: html

   <br />
