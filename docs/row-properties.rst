Row Properties
=================

Integer
-------

bigint::
    
    row_type: fixed
    value: int(???)

    row_type: random
        method: from_any
        length: int(?)

        method: from_list
        length: [???]

varchar::
    
    row_type: fixed
    value = str(??)

    row_type: random
        method: from_any
        length: int(?)

        method: from_list
        length: [???]

datetime::
    
    row_type: fixed
    value = datetime()

    row_type: date_now

    row_type: date_between
    value_1: datetime()
    value_2: datetime()
