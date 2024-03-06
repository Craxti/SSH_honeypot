# commands/ls.py
from commands.base_command import BaseCommand

class LsCommand(BaseCommand):
    """
    Command class for the 'ls' command.

    This command lists files and directories in the current directory.
    """

    def execute(self, args):
        """
        List files and directories in the current directory.

        Args:
            args: This command doesn't require arguments.

        Returns:
            str: List of files and directories.
        """
        return "file1.txt file2.txt folder/"
