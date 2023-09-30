# UEP-Schedule-Importer
Krok 1: Utwórz nowy projekt w Google Cloud Console

    - Przejdź do strony https://console.cloud.google.com/ i zaloguj się na swoje konto Google.

    - Kliknij w menu po lewej stronie, a następnie wybierz "Projekty".

    - Kliknij na przycisk "Utwórz projekt" i postępuj zgodnie z instrukcjami, aby utworzyć nowy projekt.

    - Po utworzeniu projektu przejdź do karty "Uprawnienia" i dodaj dostęp do API. Wybierz "Konta usług" i dodaj nowe konto usługi, aby wygenerować identyfikator usługi. Nadaj mu odpowiednie uprawnienia, takie jak dostęp do Google Calendar API.

Krok 2: Pobierz credentials.json i umieść plik w projekcie

    - Po wygenerowaniu identyfikatora usługi zostaniesz przekierowany na stronę konfiguracji tego identyfikatora. Na tej stronie pobierz plik JSON z danymi uwierzytelniającymi (credentials.json). Pamiętaj, aby zachować ten plik w bezpiecznym miejscu.

    - W Twojej aplikacji powinieneś mieć folder "resources". Wklej do niego pobrany wcześniej plik.

Krok 3: Uruchom aplikację

    - Teraz możesz uruchomić aplikację. Otwórz projekt w swoim środowisku programistycznym.

    - Jeśli trzeba pobierz wymagane paczki.

    - Zlokalizuj skrypt main.py i go uruchom.

    - Postepuj zgodnie z intrukcjami wyświetlanymi na ekranie.
