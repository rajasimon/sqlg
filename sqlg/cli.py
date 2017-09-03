"""
Command Line Interface
"""
import os
import sys
import argparse
import logging
from sqlg.generator import Generator

logger = logging.getLogger(__name__)


class CommandLineInterface(object):
    
    description = "Standardized Query Language Generator"

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self.description)
        self.parser.add_argument(
            '-i',
            dest='filename',
            help='Please give a model file name',
            default=None
        )
        self.parser.add_argument(
            '-v',
            '--verbosity',
            type=int,
            help='How verbose to make the output',
            default=1,
        )

    @classmethod
    def entrypoint(cls):
        """
        Main entrypoint for external starts.
        """
        cls().run(sys.argv[1:])

    def run(self, args):
        """
        Pass in raw argument list and it will decode them
        and run the server
        """
        # Decode args
        args = self.parser.parse_args(args)
        # Set up logging
        logging.basicConfig(
            level={
                0: logging.WARN,
                1: logging.INFO,
                2: logging.DEBUG,
            }[args.verbosity],
            format="%(asctime)-15s %(levelname)-8s %(message)s",
        )

        logger.info('Starting sql...')
        filename = args.filename
        filepath = os.getcwd() + '/{}'.format(filename)
        folderpath = "/".join(filepath.split("/")[:-1])

        # Check folder exists
        if os.path.isdir(folderpath):
            generator = Generator(folderpath, filepath)
            generator.handler()

        else:
            raise ValueError("Please give correct folder name")
