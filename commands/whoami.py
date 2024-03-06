# whoami.py
from commands.base_command import BaseCommand

class WhoamiCommand(BaseCommand):
    def execute(self, args):
        return "user"
