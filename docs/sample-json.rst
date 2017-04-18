Sample Json
===========

This will create a test table in the mention database::

    {
        "table_name": "test",
        "column_count": 5,
        "column_properties": {
            "col_1": {
                "row_name": "device_id", 
                "col_type": "bigint(20)"
            },
            "col_2": {
                "row_name": "start",
                "col_type": "varchar(20)"
            },
            "col_3": {
                "row_name": "start_time",
                "col_type": "datetime"
            },
            "col_4": {
                "row_name": "finish",
                "col_type": "varchar(20)"
            },
            "col_5": {
                "row_name": "finish_time",
                "col_type": "datetime"
            }
        },
        "row_count": 1,
        "row_properties": {
            "row_1": {
                "row_type": "random",
                "method": "from_any",
                "length": 3
            },
            "row_2": {
                "row_type": "fixed",
                "value": "YES"
            },
            "row_3": {
                "row_type": "fixed",
                "method": "date_now"
            },
            "row_4": {
                "row_type": "fixed",
                "value": "YES"
            },
            "row_5": {
                "row_type": "random",
                "method": "date_between",
                "value_1": "2018-08-21 14:11:09",
                "value_2": "2020-08-21 14:11:09"
            }

        }
    }