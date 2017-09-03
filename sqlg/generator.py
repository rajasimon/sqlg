"""
SQL Data Generator module.
"""
# Python module
import json
import logging

# Third party module
import sqlite3
from sqlite3 import OperationalError

# Data Generator Utility module
from sqlg.utility import process_data

# Process
from sqlg.process import Process

# Database Cursor
DB = sqlite3.connect('test.sqlite3')

CURSOR = DB.cursor()

# Range without zero
RANGE1 = lambda start, end: range(start, end+1)


class Generator(object):
    """ Data Generator class """

    def __init__(self, folderpath, filename):
        self.folderpath = folderpath
        self.filename = filename

    def read_file(self, filename=None):
        """ Returns json object from the json file """
        if filename:
            return json.loads(open(filename).read())
        return json.loads(open(self.filename).read())

    def process_data(self):
        """ Takes data as input and will return important values from file """

        # Get data from the json file
        data = self.read_file()

        # Table Name from Json file
        table_name = data['table_name']

        # No of Column
        column_count = data['column_count']

        # No of Row
        row_count = data['row_count']

        # Table columns schema from Json file
        column_properties = data['column_properties']

        # Get the row row_properties
        row_properties = data['row_properties']
        return table_name, column_count, row_count, column_properties, row_properties

    def create_table_query(self):
        """ Function used to create Table name in the given database """

        # Get data from the json file
        data = self.read_file()

        table_name, column_count, _, column_properties, _ = process_data(data)

        # Declaration
        statementlist = []

        # Loop through to no_of_column and create the schema for this table
        for column_key in RANGE1(1, column_count):

            # Process each column to get the Name and types
            row_name = column_properties["col_{}".format(column_key)]['row_name']
            col_type = column_properties["col_{}".format(column_key)]['col_type']

            # Skip the step where Foreign Key
            if not col_type == 'foreign_key':

                # Checkpoint to check foreign_key
                innner_statement = "`{}` {}".format(row_name, col_type)
                statementlist.append(innner_statement)

        # Joining and forming statement
        statement = ", ".join(statementlist)

        # Query to create table
        table_query = "CREATE TABLE {} ({})".format(table_name, statement)
        return table_query


    def create_row_query(self):
        """ Takes data and loop through column to create rows """

        table_name, column_count, _, _, _ = process_data(self.read_file())

        # Declaration
        values = []

        # Now create rows
        # Loop through to no_of_column and create the schema for this table
        for column_key in RANGE1(1, column_count):

            # From this generator run through the each column and rows
            # When finishing each itration value should be append to values

            row = "row_{}".format(column_key)
            column = "col_{}".format(column_key)

            col_type = self.read_file()['column_properties']["{}".format(column)]['col_type']

            # Processing
            process = Process(row, column, self.read_file())
            value = process.handler()
            values.append(value)

        valuesset = '", "'.join(str(v) for v in values)

        # Query to insert values
        row_query = 'INSERT INTO {} VALUES("{}")'.format(
            table_name, valuesset
        )
        # print(row_query)
        return row_query

    def execute_commit(self, statement):
        """
        Takes query statement and do the action and commit those chnages
        """

        # It's safe to exeucte in try! If thorws logger will emit those messages
        try:
            CURSOR.execute(statement)
        except OperationalError as error_message:
            logging.error(error_message)

        # Save those changes, Return same statement this function receives
        DB.commit()
        return statement

    def handler(self):
        """ Generator Handler """
        # Create Table and column
        create_table_query = self.create_table_query()

        # Execute function call
        self.execute_commit(create_table_query)

        # Number of rows to be generated
        data = self.read_file()
        row_count = data['row_count']

        for _ in range(row_count):

            # Create Rows
            create_row_query = self.create_row_query()

            # Execute function call
            self.execute_commit(create_row_query)