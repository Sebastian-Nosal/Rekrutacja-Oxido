import unittest
from app.parser import HTMLParser

class TestHTMLParser(unittest.TestCase):

    # Testy dla metody check_non_content_tags
    def test_check_non_content_tags_with_html_tags(self):
        html_with_structure_tags = "<!DOCTYPE HTML><html><head><title>Test</title></head><body>Content</body></html>"
        result = HTMLParser.check_non_content_tags(html_with_structure_tags)
        self.assertFalse(result)

    def test_check_non_content_tags_without_html_tags(self):
        html_without_structure_tags = "<p>This is a paragraph.</p>"
        result = HTMLParser.check_non_content_tags(html_without_structure_tags)
        self.assertTrue(result)

    def test_check_non_content_tags_with_script_tag(self):
        html_with_script_tag = "<script>alert('Hello');</script><p>Content</p>"
        result = HTMLParser.check_non_content_tags(html_with_script_tag)
        self.assertFalse(result)

    def test_check_non_content_tags_mixed_case(self):
        html_mixed_case = "<Html><BoDy><P>Content</P></BoDy></Html>"
        result = HTMLParser.check_non_content_tags(html_mixed_case)
        self.assertFalse(result)

    # Testy dla metody create_preview
    def test_create_preview_with_valid_body(self):
        html_content = "<p>This is a preview content.</p>"
        template = "<html><head></head><body></body></html>"
        result = HTMLParser.create_preview(html_content, template)
        expected_result = "<html><head></head><body> \n \t<p>This is a preview content.</p></body></html>"
        self.assertEqual(result, expected_result)

    def test_create_preview_empty_html(self):
        empty_html_content = ""
        template = "<html><head></head><body></body></html>"
        result = HTMLParser.create_preview(empty_html_content, template)
        self.assertEqual(result, template)

    def test_create_preview_no_body_tag(self):
        html_content = "<p>This is a preview content.</p>"
        template = "<html><head></head></html>"
        result = HTMLParser.create_preview(html_content, template)
        self.assertEqual(result, template)

    def test_create_preview_case_insensitive_body_tag(self):
        html_content = "<p>This is a preview content.</p>"
        template = "<html><head></head><BODY></BODY></html>"
        result = HTMLParser.create_preview(html_content, template)
        expected_result = "<html><head></head><body> \n \t<p>This is a preview content.</p></body></html>"
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
