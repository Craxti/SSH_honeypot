# server/shells/fake_ssh_shell.py
from thrussh import Shell
from logging.logging_utils import log_action

class FakeSSHShell(Shell):
    def __init__(self, session):
        super().__init__(session)

    def data_received(self, data):
        command = data.decode('utf-8').strip()
        username = self.session.connection.server.username
        ip_address = self.session.connection.peer[0]

        log_action('command', username, ip_address, command)
        output = self.execute_command(command)

        self.write(output)

    def execute_command(self, command):
        command_parts = command.split()
        command_name = command_parts[0]
        args = command_parts[1:]

        return self.session.connection.server.command_dispatcher.execute(command_name, args)
