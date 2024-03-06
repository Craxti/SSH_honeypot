# server/sessions/fake_ssh_session.py
from thrussh import Session
from server.shells.fake_ssh_shell import FakeSSHShell

class FakeSSHSession(Session):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def shell_requested(self):
        return FakeSSHShell(self)
