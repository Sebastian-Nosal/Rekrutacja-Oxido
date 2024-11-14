import unittest
from unittest.mock import patch, MagicMock
from app.api import OpenAIAPI


class TestOpenAIAPI(unittest.TestCase):
    def setUp(self):
        self.api = OpenAIAPI(api_key="test_key")

    @patch("openai.ChatCompletion.create")
    def test_text_to_html_successful(self, mock_create):
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "<p>HTML content</p>"
        mock_create.return_value = mock_response

        prompt = "Please convert text to HTML."
        text = "This is a sample text."
        result = self.api.text_to_html(prompt, text)

        self.assertEqual(result, "<p>HTML content</p>")
        mock_create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text}
            ]
        )

    def test_text_to_html_empty_prompt(self):
        with self.assertRaises(ValueError) as context:
            self.api.text_to_html("", "Sample text")
        self.assertEqual(str(context.exception), "Prompt cannot be empty")

    def test_text_to_html_empty_text(self):
        with self.assertRaises(ValueError) as context:
            self.api.text_to_html("Please convert text to HTML.", "")

        self.assertEqual(str(context.exception), "Text cannot be empty")

    @patch("openai.ChatCompletion.create")
    def test_text_to_html_api_failure(self, mock_create):
        mock_create.side_effect = Exception("API Error")

        with self.assertRaises(Exception) as context:
            self.api.text_to_html("Valid prompt", "Valid text")

        self.assertEqual(str(context.exception), "API Error")
