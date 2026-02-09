import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Ensure src modules can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from server import server

class TestServer(unittest.TestCase):
    @patch('server.server.socket')
    @patch('builtins.print')
    @patch('builtins.input')
    def test_server_startup_and_exit(self, mock_input, mock_print, mock_socket):
        """
        Test that server binds to port 4444 and exits gracefully when 'exit' is typed.
        """
        # Setup mocks
        mock_socket_instance = MagicMock()
        mock_socket.socket.return_value = mock_socket_instance
        
        # Mock connection accept
        mock_conn = MagicMock()
        mock_addr = ('127.0.0.1', 12345)
        mock_socket_instance.accept.return_value = (mock_conn, mock_addr)

        # Mock user input sequence: "unknown_cmd", then "exit"
        mock_input.side_effect = ["whoami", "exit"]
        
        # Mock connection recv for the "whoami" command response
        mock_conn.recv.return_value = b"root"

        # Run main
        server.main()

        # Assertions
        mock_socket_instance.bind.assert_called_with(("0.0.0.0", 4444))
        mock_socket_instance.listen.assert_called_with(1)
        mock_conn.send.assert_any_call(b"whoami")
        mock_conn.close.assert_called()
        print("Server test passed!")

if __name__ == '__main__':
    unittest.main()
