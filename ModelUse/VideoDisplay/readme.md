# Nutzung der Videoanalyse

Um die Videoanalyse durchzuführen, befolgen Sie die folgenden Schritte:
1.  Laden Sie den Ordner "VideoDisplay" herunter. Stellen Sie sicher, dass der Ordner folgende Dateien enthält:
   - `videoShow.py`
   - requirements.txt - Python Module 
   - `tfModel` (Ordner) - Enthält das eingesetzte Modell zur Analyse der Bilder
   - `videos` (Ordner) - Enthält die Videos, die analysiert werden sollen

2. Übertragen Sie beliebig viele Videos in den Ordner "videos". Bitte stellen Sie sicher, dass alle Videos im MP4-Format vorliegen.

3. Öffnen Sie ein neues Terminal und navigieren Sie zu dem Speicherort des Ordners "VideoDisplay" mithilfe des folgenden Befehls:

    ```
    cd "path/to/directory"
    ```
    Ersetzen Sie "Pfad/zum/Verzeichnis" durch den tatsächlichen Pfad zu dem Ordner "VideoDisplay" auf Ihrem System.

4. Installieren Sie mit pip die Requirements aus der requirements.txt:

    ```
    pip install -r requirements.txt
    ```

5. Führen Sie die Datei videoShow.py aus, indem Sie den folgenden Befehl eingeben:

    ```
    python videoShow.py
    ```
    Dadurch wird das Programm gestartet und die Videoanalyse beginnt.

    Bitte stellen Sie sicher, dass Sie alle erforderlichen Abhängigkeiten installiert haben, bevor Sie das Programm ausführen. Eventuell müssen Sie zusätzliche Python-Pakete installieren, falls noch nicht vorhanden.

    Folgen Sie diesen Schritten, um die Videoanalyse erfolgreich durchzuführen