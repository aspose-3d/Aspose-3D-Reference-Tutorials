---
date: 2025-12-17
description: Erfahren Sie, wie Sie die Lizenz in Aspose.3D für Java festlegen und
  wie Sie öffentliche und private Schlüssel für die nutzungsbasierte Lizenzierung
  verwenden.
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Wie man die Lizenz in Aspose.3D für Java festlegt – Vollständige Anleitung
url: /de/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man eine Lizenz in Aspose.3D für Java festlegt

## Einführung

Willkommen! In diesem Schritt‑für‑Schritt‑Tutorial erfahren Sie **wie man eine Lizenz** für Aspose.3D in einer Java‑Anwendung festlegt und lernen **wie man öffentliche und private Schlüssel** für die Metered‑Lizenzierung verwendet. Aspose.3D ist eine leistungsstarke Java‑Bibliothek, die die Arbeit mit 3D‑Dateiformaten vereinfacht, und eine gültige Lizenz schaltet den vollen Funktionsumfang frei. Am Ende dieses Leitfadens können Sie die Lizenzierung nahtlos in jedes Java‑Projekt integrieren.

## Kurze Antworten
- **Was ist der primäre Weg, eine Lizenz festzulegen?** Verwenden Sie die `License`‑Klasse und rufen Sie `setLicense` mit einem Dateipfad oder Stream auf.  
- **Kann ich die Lizenz aus einem Stream laden?** Ja – ein `FileInputStream` funktioniert einwandfrei.  
- **Wofür dienen öffentliche/ private Schlüssel?** Sie ermöglichen die Metered‑Lizenzierung über die `Metered`‑Klasse.  
- **Brauche ich eine Lizenz für die Entwicklung?** Eine temporäre oder Testlizenz reicht für Tests aus; für die Produktion ist eine Voll‑Lizenz erforderlich.  
- **Welche Java‑Versionen werden unterstützt?** Aspose.3D funktioniert mit Java 6 und höher.

## Voraussetzungen

Bevor wir beginnen, stellen Sie sicher, dass Sie:

- Ein grundlegendes Verständnis der Java‑Programmierung.
- Die Aspose.3D‑Bibliothek zu Ihrem Projekt hinzugefügt. Laden Sie sie von der [Release‑Seite](https://releases.aspose.com/3d/java/) herunter.
- Eine gültige `.lic`‑Datei oder Ihre öffentlichen und privaten Metered‑Schlüssel.

## Pakete importieren

Fügen Sie die erforderlichen Importe zu Ihrer Java‑Quelldatei hinzu. Stellen Sie sicher, dass das Aspose.3D‑JAR im Klassenpfad liegt.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Wie man Lizenz mit einer Datei festlegt

### Schritt 1: Lizenzobjekt erstellen

Instanziieren Sie die `License`‑Klasse – dieses Objekt enthält die Lizenzinformationen.

```java
License license = new License();
```

### Schritt 2: Lizenz aus Datei setzen

Geben Sie den relativen oder absoluten Pfad zu Ihrer `.lic`‑Datei an und wenden Sie sie an.

```java
license.setLicense("Aspose._3D.lic");
```

> **Pro Tipp:** Bewahren Sie die Lizenzdatei außerhalb Ihres Source‑Control‑Verzeichnisses auf, um ein versehentliches Offenlegen zu vermeiden.

## Wie man Lizenz mit einem Stream festlegt

### Schritt 1: Lizenzobjekt erstellen

Wie zuvor starten Sie mit einer neuen `License`‑Instanz.

```java
License license = new License();
```

### Schritt 2: Lizenz aus einem Stream setzen

Lesen Sie die Lizenzdatei in einen `FileInputStream` ein und übergeben Sie den Stream an `setLicense`. Der try‑with‑resources‑Block sorgt dafür, dass der Stream automatisch geschlossen wird.

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## Wie man öffentliche und private Schlüssel für Metered‑Lizenzierung verwendet

### Schritt 1: Metered‑Lizenzobjekt initialisieren

Erstellen Sie eine Instanz der `Metered`‑Klasse, die die Metered‑(Pay‑as‑you‑go‑)Lizenzierung verwaltet.

```java
Metered metered = new Metered();
```

### Schritt 2: Öffentliche und private Schlüssel setzen

Geben Sie die Schlüssel an, die Sie von Aspose erhalten haben. Diese Schlüssel ermöglichen es der Bibliothek, die Nutzung an den Lizenz‑Server zurückzumelden.

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

> **Warnung:** Kodieren Sie Ihren privaten Schlüssel niemals fest in ein öffentlich verteiltes JAR. Laden Sie ihn lieber aus einem sicheren Speicherort oder einer Umgebungsvariable.

## Gemeinsame Anwendungsfälle

- **Enterprise‑3D‑Rendering‑Pipelines** – schalten Sie Hochleistungs‑APIs frei, nachdem die Lizenz gesetzt wurde.
- **Automatisierte Testumgebungen** – verwenden Sie eine temporäre Lizenz (siehe FAQ), um die Funktionalität zu prüfen, ohne eine Voll‑Lizenz zu kaufen.
- **Metered‑SaaS‑Lösungen** – integrieren Sie öffentliche/ private Schlüssel, um Kunden basierend auf tatsächlicher Nutzung abzurechnen.

## Fazit

Herzlichen Glückwunsch! Sie wissen jetzt **wie man eine Lizenz** für Aspose.3D in Java mithilfe einer Datei, eines Streams festlegt und **wie man öffentliche private Schlüssel** für die Metered‑Lizenzierung verwendet. Mit diesen Schritten können Sie Aspose.3D sicher in jede Java‑Anwendung integrieren und die vollen Möglichkeiten der 3D‑Verarbeitung nutzen.

## Häufig gestellte Fragen

**F1: Ist Aspose.3D mit allen Java‑Versionen kompatibel?**  
A1: Ja, Aspose.3D funktioniert mit Java 6 und späteren Versionen.

**F2: Wo finde ich zusätzliche Dokumentation?**  
A2: Sie können die Dokumentation [hier](https://reference.aspose.com/3d/java/) einsehen.

**F3: Kann ich Aspose.3D vor dem Kauf testen?**  
A3: Ja, Sie können eine kostenlose Testversion [hier](https://releases.aspose.com/) ausprobieren.

**F4: Wie erhalte ich Support für Aspose.3D?**  
A4: Besuchen Sie das [Aspose.3D‑Forum](https://forum.aspose.com/c/3d/18) für Community‑ und offiziellen Support.

**F5: Benötige ich eine temporäre Lizenz für Tests?**  
A5: Ja, erhalten Sie eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-17  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

---