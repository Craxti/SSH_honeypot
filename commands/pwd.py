# commands/pwd.py
from commands.base_command import BaseCommand

class PwdCommand(BaseCommand):
    """
    Command class for the 'pwd' command.

    This command displays the current working directory.
    """

    def execute(self, args):
        """
        Display the current working directory.

        Args:
            args: This command doesn't require arguments.

        Returns:
            str: Current working directory.
        """
        return "/home/user"
