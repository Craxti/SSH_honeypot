# main.py
from server.fake_ssh_server import FakeSSHServer
from utils.config import SERVER_HOST, SERVER_PORT

def run_server():
    server = FakeSSHServer()
    server.load_host_keys(HOST_KEY_PATH)
    server.listen(SERVER_HOST, SERVER_PORT)
    print(f"Fake SSH server is listening on {SERVER_HOST}:{SERVER_PORT}")
    server.run()

if __name__ == '__main__':
    run_server()
