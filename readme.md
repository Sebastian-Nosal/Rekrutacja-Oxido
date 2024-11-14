# Dokumentacja projektu

## Instalacja

1. Pobierz zawartość repozytorium.
2. (Opcjonalnie) Stwórz środowisko virtualne
3. Zainstaluj wymagane zależności z pliku `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
4. Po zainstalowaniu zależności otwórz plik `config.json` i umieść w nim swój klucz API do OpenAI.
5. (Opcjonalnie) Dostosuj nazwy i ścieżki do plików artykułu, szablonu, wyniku oraz podglądu w `config.json`. Możesz także edytować prompt systemowy używany do komunikacji z modelem.

## Uruchomienie

Aby uruchomić aplikację, będąc w katalogu głównym projektu, wykonaj następujące polecenie:
```bash
python3 main.py
```

### Wynikowe pliki
Po uruchomieniu aplikacji, generowane są domyślnie dwa pliki:
- `artykul.html` - zawiera wygenerowany artykuł,
- `podglad.html` - podgląd artykułu w wersji responsywnej.

## Obrazki

Obrazki są generowane na podstawie atrybutów `alt` wygenerowanych przez aplikację. Wykorzystano model DALL-E 3 dostępny w darmowym planie ChatGPT do tworzenia grafik, które zostały zapisane w katalogu `img`. Mimo krótkiego, ogólnego promptu uzyskane efekty są zadowalające.

## Podgląd

Podgląd artykułu jest responsywny i prosty w formie. Elementy pojawiają się z animacją `fade-up` przy pierwszym załadowaniu. W wersji na komputery (szerokość ekranu >1280px) po lewej stronie ekranu dostępny jest zestaw przycisków nawigacyjnych, pozwalających przemieszczać się między nagłówkami artykułu.

Podgląd dostępny jest w dwóch wersjach:
- `podglad.html` - wersja standardowa,
- `podglad z obrazkami.html` - wersja zawierająca wygenerowane obrazki.
