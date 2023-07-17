# Nutzung der Bildanalyse

Um die Bildanalyse durchzuführen, befolgen Sie die folgenden Schritte:

1. Laden Sie den Ordner "ImageAnalysis" herunter. Stellen Sie sicher, dass der Ordner folgende Dateien enthält:
   - imageShow.py
   - tfModel (Ordner) - Enthält das verwendete Modell zur Analyse der Bilder
   - images (Ordner) - Enthält die Bilder, die analysiert werden sollen

2. Übertragen Sie beliebig viele Bilder in den Ordner "images". Bitte stellen Sie sicher, dass alle Bilder im JPG- oder PNG-Format vorliegen.

3. Öffnen Sie ein neues Terminal und navigieren Sie zu dem Speicherort des Ordners "ImageAnalysis" mithilfe des folgenden Befehls:

    ```
    cd "Pfad/zum/Verzeichnis"
    ```
    Ersetzen Sie "Pfad/zum/Verzeichnis" durch den tatsächlichen Pfad zu dem Ordner "ImageAnalysis" auf Ihrem System.

4. Installieren Sie die erforderlichen Abhängigkeiten aus der `requirements.txt`-Datei mit dem folgenden Befehl:

    ```
    pip install -r requirements.txt
    ```

5. Führen Sie die Datei imageShow.py aus, indem Sie den folgenden Befehl eingeben:

    ```
    python imageShow.py
    ```
    Dadurch wird das Programm gestartet und die Bildanalyse beginnt.

    Bitte stellen Sie sicher, dass Sie alle erforderlichen Abhängigkeiten installiert haben, bevor Sie das Programm ausführen. Möglicherweise müssen Sie zusätzliche Python-Pakete installieren, falls sie noch nicht auf Ihrem System vorhanden sind.

Folgen Sie diesen Schritten, um die Bildanalyse erfolgreich durchzuführen.

## Tastenkürzel

Während der Bildanalyse können Sie die folgenden Tastenkürzel verwenden:

- **q**: Springen Sie zum nächsten Bild.
- **t**: Beenden Sie das Programm.
- **s**: Aktivieren/Deaktivieren Sie die Anzeige der Klassifikationsergebnisse.

Verwenden Sie diese Tastenkürzel, um die Bildanalyse nach Bedarf zu steuern.
