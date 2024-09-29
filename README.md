# Hack Yeah 2024 | Team: Magic Lab

Głównym zadaniem konkursu była detekcja anomalii w pliku nagraniowym mówcy. Do wykonania zadania posłużono się uczeniem maszynowym i klasycznymi algorytmami. Wyniki pracy byłby widoczne na hoście, gdyby działał :)

## Spis Treści

- [Hack Yeah 2024 | Team: Magic Lab](#hack-yeah-2024--team-magic-lab)
  - [Spis Treści](#spis-treści)
  - [Installation](#installation)
  - [Run](#run)
  - [Członkowie Zespołu](#członkowie-zespołu)
  - [Szczegółowy opis projektu](#szczegółowy-opis-projektu)
  - [Użyte technologie](#użyte-technologie)
    - [Aplikacja webowa:](#aplikacja-webowa)
    - [Przetwarzanie danych / AI:](#przetwarzanie-danych--ai)
  - [Funkcjonalności](#funkcjonalności)

---

## Installation

Clone the repository:

   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

## Run

W celu uruchomienia aplikacji należy wykonać poniższe kroki:
- po lewej stronie ekranu wybrać plik do przetworzenia z dysku lokalnego
- kliknąć przycisk `Przetwórz`
- poczekać na zakończenie przetwarzania
- obserwować wyniki oraz prawą stronę ekranu, gdzie wyświetlone zostaną informacje o przetworzonym pliku

## Członkowie Zespołu

- **Nazwa zespołu**: Magic Lab
- **Członkowie**:
  - Piotr Błędowski - Computer Vision, AI - [GitHub/LinkedIn Profile]
  - Bartłomiej Kruczek - Przetwarzanie Audio, AI - [GitHub/LinkedIn Profile]
  - Lidia Moryc - UI / UX design, Przetwarzanie Języka Naturalnego, AI - [GitHub/LinkedIn Profile]
  - Max Słota - Web Development, Integration - [GitHub/LinkedIn Profile]
  - Adam Stajek - Przetwarzanie Języka Naturalnego, AI - [GitHub/LinkedIn Profile]

## Szczegółowy opis projektu

Celem projektu było wykrycie jak największej liczby anomalii z pliku nagraniowego. Cały proces podzielono na trzy etapy: przetwarzanie wideo, przetwarzanie audio oraz przetwarzanie tekstu. Do przetwarzania obrazu użyto algorytmów `Computer Vision`, do przetwarzania tekstu posłużono się algorytmami `Natural Language Processing`, a do przetwarzania dźwięku użyto klasycznych algorytmów opartych na przetwarzaniu sygnałów ze względu na ograniczenia sprzętowe. 

## Użyte technologie

### Aplikacja webowa:
  - Django, Django REST Framework (backend)
  - React.js (frontend)

### Przetwarzanie danych / AI:
  - OpenCV
  - Mediapipe
  - Ultralytics (YOLO)
  - NLTK
  - OpenAI
  - Spacey
  - Librosa

## Funkcjonalności

- generacja transkryptu wypowiedzi
- identyfikacja błędów w wypowiedzi, w zakresie wypowiadanego tekstu, sposobu mowy oraz mowy ciała
- detekcja osób nieproszonych na nagraniu
- detekcja ruchów ciała z naciskiem na obracanie się i gestykulację
- obliczanie szybkości wypowiedzi
- automatyczne wykrywanie pauz
- określanie poziomu głośności wypowiedzi na przestrzeni nagrania
- wykrywanie żargonu, powtorzeń, zmiany tematu, zbyt długich wypowiedzi
- detekcja wtrąceń słownictwa z obcego języka
- wyznaczanie błędów w słownictwie i niezgodności z transkrypcją
- używanie strony biernej
- wykrywanie niepoprawnego akcentowania w języku angielskim 
- analiza sentymentu wypowiedzi; ton, emocje, hate speech

---