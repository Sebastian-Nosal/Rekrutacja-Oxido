import os
import json

class File:
    @staticmethod
    def read_from_file(path: str) -> str:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Plik {path} nie został znaleziony.")
            return ""
        except IOError as e:
            print(f"Nie udało się odczytać pliku {path}: {e}")
            return ""

    @staticmethod
    def read_config() -> dict:
        config_path = os.path.join(os.getcwd(), 'config.json')
        try:
            with open(config_path, 'r', encoding='utf-8') as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            print(f"Plik konfiguracyjny {config_path} nie został znaleziony.")
            return {}
        except json.JSONDecodeError:
            print(f"Błąd w pliku konfiguracyjnym {config_path}.")
            return {}
        except IOError as e:
            print(f"Nie udało się odczytać pliku {config_path}: {e}")
            return {}

    @staticmethod
    def save_to_file(path: str, content: str) -> bool:
        try:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
            return True
        except IOError as e:
            print(f"Nie udało się zapisać do pliku {path}: {e}")
            return False