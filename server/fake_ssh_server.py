# server/fake_ssh_server.py
import thrussh
from server.sessions.fake_ssh_session import FakeSSHSession

class FakeSSHServer(thrussh.Server):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def connection_made(self, connection):
        super().connection_made(connection)
        print(f"Connection from {connection.peer[0]}:{connection.peer[1]}")

    def session_requested(self):
        return FakeSSHSession()
