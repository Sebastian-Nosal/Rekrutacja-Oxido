import unittest
from unittest.mock import patch, mock_open
from app.file import File
import os
import json

class TestFile(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="Sample file content")
    def test_read_from_file_successful(self, mock_file):
        result = File.read_from_file("dummy_path.txt")
        self.assertEqual(result, "Sample file content")
        mock_file.assert_called_once_with("dummy_path.txt", 'r', encoding='utf-8')

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_from_file_not_found(self, mock_file):
        result = File.read_from_file("nonexistent.txt")
        self.assertEqual(result, "")
        mock_file.assert_called_once_with("nonexistent.txt", 'r', encoding='utf-8')

    @patch("builtins.open", side_effect=IOError("Read error"))
    def test_read_from_file_io_error(self, mock_file):
        result = File.read_from_file("dummy_path.txt")
        self.assertEqual(result, "")
        mock_file.assert_called_once_with("dummy_path.txt", 'r', encoding='utf-8')

    @patch("os.path.join", return_value="mocked_config_path.json")
    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    def test_read_config_successful(self, mock_file, mock_path_join):
        result = File.read_config()
        self.assertEqual(result, {"key": "value"})
        mock_path_join.assert_called_once_with(os.getcwd(), 'config.json')
        mock_file.assert_called_once_with("mocked_config_path.json", 'r', encoding='utf-8')

    @patch("os.path.join", return_value="mocked_config_path.json")
    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_config_not_found(self, mock_file, mock_path_join):
        result = File.read_config()
        self.assertEqual(result, {})
        mock_path_join.assert_called_once_with(os.getcwd(), 'config.json')
        mock_file.assert_called_once_with("mocked_config_path.json", 'r', encoding='utf-8')

    @patch("os.path.join", return_value="mocked_config_path.json")
    @patch("builtins.open", new_callable=mock_open, read_data='Invalid JSON')
    def test_read_config_json_decode_error(self, mock_file, mock_path_join):
        result = File.read_config()
        self.assertEqual(result, {})
        mock_path_join.assert_called_once_with(os.getcwd(), 'config.json')
        mock_file.assert_called_once_with("mocked_config_path.json", 'r', encoding='utf-8')

    @patch("builtins.open", new_callable=mock_open)
    def test_save_to_file_successful(self, mock_file):
        result = File.save_to_file("dummy_path.txt", "New content")
        self.assertTrue(result)
        mock_file.assert_called_once_with("dummy_path.txt", 'w', encoding='utf-8')
        mock_file().write.assert_called_once_with("New content")

    @patch("builtins.open", side_effect=IOError("Write error"))
    def test_save_to_file_io_error(self, mock_file):
        result = File.save_to_file("dummy_path.txt", "New content")
        self.assertFalse(result)
        mock_file.assert_called_once_with("dummy_path.txt", 'w', encoding='utf-8')

if __name__ == "__main__":
    unittest.main()
