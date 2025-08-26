Monitoring
==========

Configure and manage Event, Logging, Alerts, Mirror Sessions and other monitoring policies.

*API Objects are*:
Alert AlertDestination AlertPolicy ArchiveRequest AuditPolicy EventPolicy
FlowExportPolicy FwlogPolicy MirrorSession StatsAlertPolicy TechSupportRequest TroubleshootingSession

API Methods
-----------

.. automethod:: pensando.PSM.getAlerts
.. automethod:: pensando.PSM.getAlertObject
.. automethod:: pensando.PSM.getFlowExportPolicy
.. automethod:: pensando.PSM.getFWLogPolicies
.. automethod:: pensando.PSM.getFWLogPolicy


Data Structures
---------------

None at this time

Examples
--------

Get all Firewall log policies defined in PSM

.. literalinclude:: ../examples/test_monitoring.py
    :language: python
    :start-after: # EXAMPLE getFWLogPolicies()
    :end-before: # END getFWLogPolicies()

Get all alerts in PSM

.. literalinclude:: ../examples/test_monitoring.py
    :language: python
    :start-after: # EXAMPLE getAlerts()
    :end-before: # END getAlerts()




.. |br| raw:: html

   <br />
