import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Ensure src modules can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from server import server

class TestServer(unittest.TestCase):
    @patch('server.server.socket.socket')
    @patch('builtins.print')
    @patch('builtins.input')
    def test_server_startup_and_exit(self, mock_input, mock_print, mock_socket_class):
        """
        Test that server binds correctly and exits gracefully when 'exit' is typed.
        """
        # Setup mocks
        mock_socket_instance = MagicMock()
        mock_socket_class.return_value = mock_socket_instance
        
        # Mock connection accept
        mock_conn = MagicMock()
        mock_addr = ('127.0.0.1', 12345)
        mock_socket_instance.accept.return_value = (mock_conn, mock_addr)

        # Mock user input sequence: "whoami", then "exit"
        mock_input.side_effect = ["whoami", "exit"]
        
        # Mock connection recv for the "whoami" command response
        mock_conn.recv.return_value = b"test_user"

        # Run main
        server.main()

        # Assertions
        mock_socket_instance.bind.assert_called()
        mock_socket_instance.listen.assert_called_with(1)
        mock_conn.send.assert_any_call(b"whoami")
        mock_conn.close.assert_called()

    def test_write_file_success(self):
        """Test the file writing helper."""
        with patch('builtins.open', unittest.mock.mock_open()) as mocked_file:
            res = server.write_file("test.txt", b"content")
            self.assertEqual(res, "[+] Download complete")
            mocked_file.assert_called_once_with("test.txt", "wb")
            mocked_file().write.assert_called_once_with(b"content")

if __name__ == '__main__':
    unittest.main()
