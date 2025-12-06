---
date: 2025-12-06
description: Erfahren Sie, wie Sie FBX‑Dateien speichern und Szeneninformationen mit
  Aspose.3D für Java abrufen. Diese Schritt‑für‑Schritt‑Anleitung behandelt das Festlegen
  des Anwendungsnamens, das Definieren von Maßeinheiten und das Exportieren der Szene
  nach FBX.
language: de
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: Wie man FBX speichert und 3D‑Szeneninformationen in Java abruft
url: /java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man FBX speichert und 3D‑Szeneninformationen in Java abruft

## Einführung

Wenn Sie nach einer klaren, praxisnahen Anleitung suchen, **wie man FBX**‑Dateien speichert und dabei nützliche Metadaten aus Ihren 3D‑Szenen extrahiert, sind Sie hier genau richtig. In diesem Tutorial führen wir Sie Schritt für Schritt mit der **Aspose.3D Java**‑Bibliothek durch: vom Erstellen einer Szene, **Festlegen des Anwendungsnamens**, **Definieren der Maßeinheiten** bis hin zum **Exportieren der Szene nach FBX**. Am Ende haben Sie eine einsatzbereite FBX‑Datei, die die Asset‑Informationen enthält, die Sie für nachgelagerte Pipelines benötigen.

## Schnelle Antworten
- **Was ist das Hauptziel?** Eine FBX‑Datei speichern, die benutzerdefinierte Asset‑Informationen enthält.  
- **Welche Bibliothek wird verwendet?** Aspose.3D für Java.  
- **Brauche ich eine Lizenz?** Eine kostenlose Testversion reicht für die Entwicklung; für die Produktion ist eine kommerzielle Lizenz erforderlich.  
- **Kann ich die Maßeinheiten ändern?** Ja – verwenden Sie `setUnitName` und `setUnitScaleFactor`.  
- **Wo wird die Ausgabe gespeichert?** An dem Pfad, den Sie in `scene.save(...)` angeben.

## Voraussetzungen

Bevor wir beginnen, stellen Sie sicher, dass Sie folgendes haben:

- Ein solides Verständnis der grundlegenden Java‑Syntax.  
- **Aspose.3D für Java** heruntergeladen und Ihrem Projekt hinzugefügt (Sie erhalten es von der offiziellen [Aspose 3D download page](https://releases.aspose.com/3d/java/)).  
- Ihre bevorzugte Java‑IDE (IntelliJ IDEA, Eclipse, NetBeans usw.) korrekt konfiguriert.

## Pakete importieren

Importieren Sie in Ihrer Java‑Quelldatei die Aspose.3D‑Klassen, die die Szenenverwaltung und Dateiformatunterstützung bereitstellen.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro‑Tipp:** Halten Sie die Importliste minimal, um unnötige Abhängigkeiten zu vermeiden und die Kompilierzeit zu verkürzen.

## Wie ist der Prozess zum Speichern einer FBX‑Datei?

Im Folgenden finden Sie einen knappen, schrittweisen Leitfaden, der zeigt, **wie man Asset‑Informationen** zu einer Szene hinzufügt und dann **die Szene nach FBX exportiert**.

### Schritt 1: Eine 3D‑Szene initialisieren

Erzeugen Sie zunächst ein leeres `Scene`‑Objekt. Dieses dient als Container für alle Geometrien, Lichter, Kameras und Asset‑Metadaten.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Schritt 2: Anwendungs‑ und Herstellerinformationen festlegen

Das Hinzufügen benutzerdefinierter Metadaten hilft nachgelagerten Tools, die Quelle der Datei zu identifizieren. Hier **setzen wir den Anwendungsnamen** und den Hersteller über das `AssetInfo`‑Objekt.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Warum das wichtig ist:** Viele Pipelines filtern oder taggen Assets basierend auf der erzeugenden Anwendung, sodass dieser Schritt für große Projekte unverzichtbar ist.

### Schritt 3: Maßeinheiten definieren

Aspose.3D ermöglicht es Ihnen, das Einheitensystem Ihrer Szene festzulegen. In diesem Beispiel verwenden wir eine altägyptische Einheit namens „pole“ mit einem benutzerdefinierten Skalierungsfaktor.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tipp:** Passen Sie `unitScaleFactor` an die reale Größe Ihrer Modelle an; 1,0 entspricht einer 1‑zu‑1‑Abbildung der gewählten Einheit.

### Schritt 4: Szene nach FBX exportieren

Jetzt, wo die Asset‑Informationen angehängt sind, speichern wir die Szene als FBX‑Datei. Die Option `FileFormat.FBX7500ASCII` erzeugt ein menschenlesbares ASCII‑FBX, was für Debugging praktisch ist.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Denken Sie daran:** Ersetzen Sie `"Your Document Directory"` durch einen absoluten Pfad oder einen Pfad relativ zum Arbeitsverzeichnis Ihres Projekts.

### Schritt 5: Erfolgsmeldung ausgeben

Eine einfache Konsolenausgabe bestätigt, dass der Vorgang erfolgreich war, und gibt an, wo die Datei geschrieben wurde.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Häufige Anwendungsfälle

- **Game‑Asset‑Pipelines** – Erstellerinformationen direkt in FBX‑Dateien einbetten für Versionsnachverfolgung.  
- **Architekturvisualisierung** – Projektspezifische Einheiten speichern, um Skalierungsfehler beim Import in Rendering‑Engines zu vermeiden.  
- **Automatisierte Berichterstellung** – FBX‑Dateien on‑the‑fly generieren mit Metadaten, die nachgelagerte Analyse‑Tools auslesen können.

## Fehlersuche & Tipps

| Problem | Lösung |
|---------|--------|
| **Datei nach dem Speichern nicht gefunden** | Prüfen Sie, ob `MyDir` auf einen existierenden Ordner zeigt und ob Ihre Anwendung Schreibrechte hat. |
| **Einheiten erscheinen in externen Viewern falsch** | Überprüfen Sie `unitScaleFactor`; einige Viewer erwarten Meter als Basiseinheit. |
| **Asset‑Metadaten fehlen** | Stellen Sie sicher, dass Sie `scene.getAssetInfo()` **vor** dem Aufruf von `save()` ausführen; Änderungen nach `save()` werden nicht gespeichert. |

## FAQ's

### Q1: Ist Aspose.3D mit allen Java‑IDEs kompatibel?

A1: Ja, Aspose.3D ist so konzipiert, dass es nahtlos mit allen gängigen Java‑IDEs funktioniert.

### Q2: Kann ich Aspose.3D für kommerzielle Projekte nutzen?

A2: Absolut. Aspose.3D bietet kommerzielle Lizenzen für Entwickler, sodass Sie die Lizenzanforderungen einhalten können.

### Q3: Wo finde ich zusätzlichen Support für Aspose.3D?

A3: Für Fragen oder Unterstützung besuchen Sie das [Aspose.3D forum](https://forum.aspose.com/c/3d/18).

### Q4: Gibt es eine kostenlose Testversion von Aspose.3D?

A4: Ja, Sie können die Funktionen mit einer kostenlosen Testversion ausprobieren, die Sie [hier](https://releases.aspose.com/) finden.

### Q5: Wie erhalte ich eine temporäre Lizenz für Aspose.3D?

A5: Eine temporäre Lizenz für Testzwecke erhalten Sie [hier](https://purchase.aspose.com/temporary-license/).

## Häufig gestellte Fragen

**F: Wie ändere ich das Ausgabeformat zu binärem FBX?**  
A: Ersetzen Sie `FileFormat.FBX7500ASCII` durch `FileFormat.FBX7500`, wenn Sie `scene.save(...)` aufrufen.

**F: Kann ich benutzerdefinierte, vom Nutzer definierte Metadaten hinzufügen, die über die integrierten Asset‑Felder hinausgehen?**  
A: Ja, verwenden Sie `scene.getUserData().add("Key", "Value")`, um zusätzliche Schlüssel‑Wert‑Paare einzubetten.

**F: Unterstützt Aspose.3D andere Exportformate wie OBJ oder GLTF?**  
A: Ja. Ändern Sie einfach das `FileFormat`‑Enum zu `OBJ` oder `GLTF2`, je nach Bedarf.

**F: Welche Java‑Version wird benötigt?**  
A: Aspose.3D für Java unterstützt Java 8 und höher.

**F: Ist es möglich, ein vorhandenes FBX zu laden, dessen Asset‑Info zu ändern und erneut zu speichern?**  
A: Absolut. Laden Sie die Datei mit `new Scene("input.fbx")`, ändern Sie `scene.getAssetInfo()`, und speichern Sie anschließend.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Zuletzt aktualisiert:** 2025-12-06  
**Getestet mit:** Aspose.3D for Java 24.11  
**Autor:** Aspose