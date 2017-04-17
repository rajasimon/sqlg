""" Data Generator Process Module """
import random
from datetime import datetime

# Utility Module
from sqlg.utility import id_generator, random_date, random_integer


class Process(object):
    """ Process class function """

    def __init__(self, current_row, current_column, data):
        self.data = data
        self.current_row = current_row
        self.current_column = current_column
        # import pdb; pdb.set_trace()
        self.row_properties = self.data['row_properties']
        self.column_properties = self.data['column_properties']


    def process_integer(self):
        """ Integer found, It's Integer and check the method """
        row_type = self.row_properties["{}".format(self.current_row)]['row_type']
        method = self.row_properties["{}".format(self.current_row)].get('method')

        # Process by row type
        if row_type == 'fixed':
            return self.row_properties["{}".format(self.current_row)]['value']

        elif row_type == 'random':
            if method == 'from_any':
                # Any random value between 1 to 9
                length = self.row_properties["{}".format(self.current_row)].get('length')
                return random_integer(length)

            elif method == 'from_list':
                # Any value between the list
                value_list = self.row_properties["{}".format(self.current_row)]['value']
                return random.choice(value_list)


    def process_varchar(self):
        """ Varchar found, It's string and check the method. """
        row_type = self.row_properties["{}".format(self.current_row)]['row_type']
        method = self.row_properties["{}".format(self.current_row)].get('method')

        # Processing by row type
        if row_type == 'fixed':
            return self.row_properties["{}".format(self.current_row)]['value']

        elif row_type == 'random':
            if method == 'from_any':
                # Any random value between a to z and 1 to 9
                length = self.row_properties["{}".format(self.current_row)].get('length')
                return id_generator(length)

            elif method == 'from_list':
                # Any value between the list
                value_list = self.row_properties["{}".format(self.current_row)]['value']
                return random.choice(value_list)


    def process_datetime(self):
        """
        When this function executed assumes this row datatype is datetime
        """
        row_type = self.row_properties["{}".format(self.current_row)]['row_type']
        method = self.row_properties["{}".format(self.current_row)].get('method')

        # Check current date time
        if row_type == 'fixed':
            if method == 'date_now':
                return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            else:
                # Fixed values doesn't change, so take the value
                return self.row_properties["{}".format(self.current_row)]['value']

        elif row_type == 'random':

            if method == 'date_between':
                # Random Date Generator
                value_1 = self.row_properties["{}".format(self.current_row)]['value_1']
                value_2 = self.row_properties["{}".format(self.current_row)]['value_2']
                return random_date(value_1, value_2, random.random())

    def handler(self):
        """ Running this process """
        # Empty Value declaration
        value = None

        # Column Type
        col_type = self.column_properties["{}".format(self.current_column)]['col_type']

        # Processing with col type
        if col_type.startswith('bigint'):
            # Execute the processor
            value = self.process_integer()

        elif col_type.startswith('varchar'):
            # Execute the processor
            value = self.process_varchar()

        elif col_type.startswith('datetime'):
            # Execute the datetime processor
            value = self.process_datetime()

        return value