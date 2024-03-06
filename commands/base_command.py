# commands/base_command.py
from utils.logger import logger

class BaseCommand:
    """
    Base class for SSH commands.

    Subclasses of this class should implement the execute() method.
    """

    def execute(self, args):
        """
        Execute the command with the given arguments.

        Args:
            args (list): List of arguments for the command.

        Returns:
            str: Result of executing the command.
        """
        pass
