# commands/exit.py
from commands.base_command import BaseCommand

class ExitCommand(BaseCommand):
    """
    Command class for the 'exit' command.

    This command exits the SSH session.
    """

    def execute(self, args):
        """
        Perform the exit action.

        Args:
            args: This command doesn't require arguments.

        Returns:
            str: Exit message.
        """
        return "Goodbye!"
