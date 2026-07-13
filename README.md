# Restaurant-Tischreservierung

Dieses Projekt ist eine einfache Verwaltungssoftware für Restaurant-Tischreservierungen. Mitarbeitende können Tische anlegen, Reservierungen erstellen, vorhandene Reservierungen anzeigen und Reservierungen stornieren.

Die Anwendung wird mit Python umgesetzt und über Streamlit visualisiert. Der Fokus liegt auf objektorientierter Programmierung mit mehreren Klassen, Vererbung bei Tischarten und einer zentralen Verwaltungsklasse für die Reservierungslogik.

## Funktionen

* Innen- und Außentische anlegen
* Tische mit Eigenschaften speichern
* Tische aktivieren, deaktivieren und löschen
* Reservierungen mit Kundendaten erstellen
* passenden Tisch automatisch suchen
* Reservierungen anzeigen
* Reservierungen stornieren
* grundlegende Tests für die Klassen ausführen

## Klassenübersicht

Das Projekt nutzt folgende zentrale Klassen:

* `Table`: Oberklasse für allgemeine Tische
* `IndoorTable`: Unterklasse für Innentische
* `OutdoorTable`: Unterklasse für Außentische
* `Customer`: speichert Kundendaten
* `Reservation`: speichert eine Reservierung
* `ReservationSystem`: verwaltet Tische und Reservierungen

## Projektstruktur

```text
tischreservierung-restaurant/
├── README.md
├── requirements.txt
├── start_app.py
│
└── src/
    ├── main/
    │   ├── app.py
    │   ├── table.py
    │   ├── indoor_table.py
    │   ├── outdoor_table.py
    │   ├── customer.py
    │   ├── reservation.py
    │   └── reservation_system.py
    │
    └── test/
        ├── test_table.py
        ├── test_indoor_table.py
        ├── test_outdoor_table.py
        ├── test_customer.py
        ├── test_reservation.py
        └── test_reservation_system.py
```

## Installation

Zuerst sollten die benötigten Pakete installiert werden:

```bash
python -m pip install -r requirements.txt
```

## Anwendung starten

Die Streamlit-App kann über die Datei `start_app.py` gestartet werden:

```bash
python start_app.py
```

Alternativ kann Streamlit direkt gestartet werden:

```bash
python -m streamlit run src/main/app.py
```

## Tests ausführen

Die Tests können mit folgendem Befehl ausgeführt werden:

```bash
python -m pytest src/test
```

## Hinweise

Die Daten werden aktuell nur während der Laufzeit gespeichert. Wenn die Anwendung geschlossen wird, gehen angelegte Tische und Reservierungen verloren. Eine dauerhafte Speicherung über eine Datei oder Datenbank ist bewusst noch nicht umgesetzt und könnte später ergänzt werden.

Reservierungen für vergangene Zeitpunkte werden aktuell nicht blockiert. Diese Entscheidung ist bewusst getroffen, da ein Restaurant bei der Einführung der Software eventuell bereits bestehende oder alte Reservierungen nachtragen muss.

Das Projekt ist als Lernprojekt aufgebaut. Der Fokus liegt daher auf der objektorientierten Struktur, der Trennung von Klassen und Oberfläche sowie auf einfachen Tests der Kernlogik.

## KI-Unterstützung

Bei der Entwicklung wurde KI unterstützend eingesetzt, zum Beispiel zur Strukturierung des Codes, zur Fehlersuche und für Formulierungsvorschläge. Die Umsetzung, Anpassung und fachliche Entscheidung über die Funktionen wurden eigenständig vorgenommen.