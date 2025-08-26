Workloads
=========

Workloads are any application/VM/container that runs on the DSC and PSM identifies
it as a workload.  These methods are used to add/del/modify workloads and their
respective attributes

API Methods
-----------

.. automethod:: pensando.PSM.addWorkloadLabel

.. automethod:: pensando.PSM.delWorkloadLabel

.. automethod:: pensando.PSM.getWorkload

.. automethod:: pensando.PSM.getWorkloadLabels

.. automethod:: pensando.PSM.getWorkloads


Data Structures
---------------

None at this time


Examples
--------
Get all workloads:

.. code-block:: python

   #!/usr/bin/env python

   import json
   from psmapi import PSM

   # Get PSM object using config parameters in default ~/.penrc file
   psm = PSM()

   workLoads = psm.getWorkloads()
      print("\n\nWORKLOADS")
      print("="*50)
      for workLoad in workLoads['items']:
            print(f"Workload Name: {workLoad['meta']['name']}")


Add a label to a workload:

.. code-block:: python

   #!/usr/bin/env python

   import json
   from psmapi import PSM

   # Get PSM object using config parameters in default ~/.penrc file
   psm = PSM()

   try:
        print("\n\nADDING LABEL TO WORKLOAD")
        labelKey = "test.label"
        labelValue = "my_label_value"
        response = psm.addWorkloadLabel("orch1--vm-90", labelKey, labelValue)
        print(f"{response}")
    except Exception as e:
        print(f"Unable to add label to workload: {e}")


.. |br| raw:: html

   <br />
