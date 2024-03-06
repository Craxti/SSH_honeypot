# uname.py
from commands.base_command import BaseCommand

class UnameCommand(BaseCommand):
    def execute(self, args):
        return "Linux"
