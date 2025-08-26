Telemetry
=========

Telemetry is used to gather metrics from PSM.

API Methods
-----------

.. automethod:: pensando.PSM.getMetrics


Data Structures
---------------

.. code-block:: json

    {
        "tenant": "string",
        "namespace": "string",
        "queries": [
            {
            "kind": "string",
            "api-version": "string",
            "name": "string",
            "selector": {
                "requirements": [
                {
                    "key": "string",
                    "operator": "string",
                    "values": [
                    "string"
                    ]
                }
                ]
            },
            "fields": [
                "string"
            ],
            "function": "string",
            "start-time": "string (date-time)",
            "end-time": "string (date-time)",
            "group-by-time": "60s",
            "group-by-field": "string",
            "pagination": {
                "offset": "integer (int32)",
                "count": "integer (int32)"
            },
            "sort-order": "string"
            }
        ]
    }


Examples
--------

Get specified metrics

.. literalinclude:: ../examples/test_metrics.py
    :language: python
    :start-after: # EXAMPLE getMetrics()
    :end-before: # END getMetrics()



Example output from dataStructure LifMetrics above

.. literalinclude:: ../examples/outputs/test_metrics.output
    :language: json
    :start-after: # EXAMPLE test_metricsOutput()
    :end-before: # END test_metricsOutput()



.. |br| raw:: html

   <br />
