import os
import json
from app.api import OpenAIAPI
from app.file import File
from app.parser import HTMLParser


def main():
    config = File.read_config()
    if not config:
        print("Błąd wczytywania konfiguracji.")
        return

    source_file = config.get("source_file", "artykul.txt")
    article_text = File.read_from_file(source_file)
    if not article_text:
        print(f"Błąd odczytu artykułu z pliku: {source_file}")
        return

    api = OpenAIAPI(config["API_key"])

    prompt = config["prompt"]
    try:

        html_content = api.text_to_html(prompt, article_text)
        if not HTMLParser.check_non_content_tags(html_content):
            print("Zwrócony HTML zawiera niepożądane tagi. Zalecane uruchomienie skryptu ponownie")
            return

        output_file = config.get("out_file", "artykul.html")
        if File.save_to_file(output_file, html_content):
            print(f"Artykuł został zapisany do pliku: {output_file}")

        template_file = config.get("template_file","szablon.html")
        preview_html = HTMLParser.create_preview(html_content, File.read_from_file(template_file))

        preview_file = config.get("preview_file","podglad.html")
        if File.save_to_file(preview_file, preview_html):
            print(f"Podgląd artykułu zapisano do pliku: {preview_file}")
    except ValueError as e:
        if "Text" in e: print(f"Brak treści artykułu. Sprawdź pliki config.json oraz wybrany plik artykułu")
        if "Prompt" in e: print("Brak polecenia. Sprawdź plik config.json")


if __name__ == "__main__":
    main()
