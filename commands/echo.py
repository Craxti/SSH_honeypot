# commands/echo.py
from commands.base_command import BaseCommand

class EchoCommand(BaseCommand):
    """
    Command class for the 'echo' command.

    This command echoes back the provided arguments.
    """

    def execute(self, args):
        """
        Echo back the provided arguments.

        Args:
            args (list): List of arguments to echo.

        Returns:
            str: Concatenated arguments as a single string.
        """
        return " ".join(args)
