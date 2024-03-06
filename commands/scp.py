# commands/scp.py
from commands.base_command import BaseCommand

class ScpCommand(BaseCommand):
    """
    Command class for the 'scp' command.

    This command simulates copying a file.
    """

    def execute(self, args):
        """
        Simulate copying a file.

        Args:
            args: This command doesn't require arguments.

        Returns:
            str: Copying file message.
        """
        return "Copying file..."
