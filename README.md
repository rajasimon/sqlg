# sqlg
Standardized Query Language Generator.

Documentation, installation and getting started instructions are at [https://sqlg.readthedocs.io](https://channels.readthedocs.io)


### How to use

### Integer and String configuration is quite same.

    bigint
        row_type: fixed
        value: int(???)

        row_type: random
            method: from_any
            length: int(?)

            method: from_list
            length: [???]

    varchar
        row_type: fixed
        value = str(??)

        row_type: random
            method: from_any
            length: int(?)

            method: from_list
            length: [???]

### Datetime configuration from_any only support now

    datetime
        row_type: fixed
        value = datetime()

        row_type: date_now

        row_type: date_between
        value_1: datetime()
        value_2: datetime()

### Column properties


    key: col_1
    value: col_type & row_name & file_name ( optional for foreign_key type )