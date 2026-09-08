---
date: 2026-09-08
description: Erfahren Sie, wie Sie Einheiten definieren und eine Szene in Java mit
  Aspose.3D nach FBX exportieren. Diese Schritt‑für‑Schritt‑Anleitung zeigt, wie man
  den Anwendungsnamen, die Maßeinheiten festlegt und 3D‑Szeneninformationen abruft.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Wie man FBX speichert und 3D‑Szeneninformationen in Java abruft
og_description: Erfahren Sie, wie Sie Einheiten definieren und eine Szene in Java
  mit Aspose.3D nach FBX exportieren. Der Leitfaden behandelt das Festlegen des Anwendungsnamens,
  der Maßeinheiten und das Abrufen von 3D‑Szeneninformationen in wenigen Schritten.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Wie man Einheiten definiert und eine Szene nach FBX in Java exportiert
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Wie man Einheiten definiert und eine Szene nach FBX in Java exportiert
url: /de/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man Einheiten definiert und eine Szene nach FBX in Java exportiert

## Einführung

Wenn Sie nach einer klaren, praxisnahen Anleitung suchen, **wie man Einheiten definiert** und **eine Szene nach FBX exportiert**, während Sie nützliche Metadaten aus Ihren 3D‑Szenen extrahieren, sind Sie hier genau richtig. In diesem Tutorial führen wir Sie Schritt für Schritt mit der **Aspose.3D for Java**‑Bibliothek: vom Erstellen einer Szene, **Festlegen des Anwendungsnamens**, **Definieren von Maßeinheiten**, bis zum **Export der Szene nach FBX**. Am Ende haben Sie eine einsatzbereite FBX‑Datei, die die Asset‑Informationen enthält, die Sie für nachgelagerte Pipelines benötigen.

## Schnelle Antworten
- **Was ist das Hauptziel?** Exportieren Sie eine Szene nach FBX, die benutzerdefinierte Asset‑Informationen enthält.  
- **Welche Bibliothek wird verwendet?** Aspose.3D for Java.  
- **Brauche ich eine Lizenz?** Eine kostenlose Testversion funktioniert für die Entwicklung; für die Produktion ist eine kommerzielle Lizenz erforderlich.  
- **Kann ich die Maßeinheiten ändern?** Ja – verwenden Sie `setUnitName` und `setUnitScaleFactor`.  
- **Wo wird die Ausgabe gespeichert?** Im Pfad, den Sie in `scene.save(...)` angeben.  

## Voraussetzungen

Bevor wir beginnen, stellen Sie sicher, dass Sie Folgendes haben:

- Ein fundiertes Verständnis der grundlegenden Java‑Syntax.  
- **Aspose.3D for Java** heruntergeladen und Ihrem Projekt hinzugefügt (Sie können es von der offiziellen) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Ihre bevorzugte Java‑IDE (IntelliJ IDEA, Eclipse, NetBeans usw.) korrekt konfiguriert.

## Pakete importieren

In Ihrer Java‑Quelldatei importieren Sie die Aspose.3D‑Klassen, die die Szenenverwaltung und Dateiformatunterstützung bereitstellen.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro Tipp:** Halten Sie die Importliste minimal, um unnötige Abhängigkeiten zu vermeiden und die Kompilierzeit zu verkürzen.

## Wie ist der Prozess zum Speichern einer FBX‑Datei?

Um eine Szene als FBX‑Datei zu speichern, erstellen Sie ein `Scene`, setzen gewünschte Asset‑Metadaten, definieren die Maßeinheit und rufen dann `scene.save(path, FileFormat.FBX7500ASCII)` auf. Diese Sequenz schreibt Geometrie, Materialien und Metadaten in ein ASCII‑FBX, das von nachgelagerten Tools inspiziert oder importiert werden kann.

### Schritt 1: Initialisieren einer 3D‑Szene

Die Klasse `Scene` ist der Top‑Level‑Container von Aspose.3D, der eine komplette 3D‑Szene darstellt, einschließlich Geometrie, Lichtern, Kameras und Metadaten. Erstellen Sie zunächst ein leeres `Scene`‑Objekt. Dieses wird der Container für alle Geometrien, Lichter, Kameras und Asset‑Metadaten sein.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Wie man den Anwendungsnamen in Java festlegt

Das Objekt `AssetInfo` speichert Metadaten wie Anwendungsname, Anbieter und Version für die Szene. Das Hinzufügen benutzerdefinierter Metadaten hilft nachgelagerten Tools, die Quelle der Datei zu identifizieren. Verwenden Sie das `AssetInfo`‑Objekt, um **den Anwendungsnamen** (und den Anbieter) festzulegen, bevor Sie die Datei speichern.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Warum das wichtig ist:** Viele Pipelines filtern oder markieren Assets basierend auf der Ursprung‑Anwendung, wodurch dieser Schritt für große Projekte unverzichtbar wird.

### Schritt 3: Maßeinheiten definieren

Das Einheitssystem bestimmt die reale Skalierung der Szene; Aspose.3D ermöglicht es Ihnen, einen Einheitennamen und einen Skalierungsfaktor relativ zu Metern anzugeben. In diesem Beispiel verwenden wir eine altägyptische Einheit namens „pole“ mit einem benutzerdefinierten Skalierungsfaktor.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tipp:** Passen Sie `unitScaleFactor` an die reale Größe Ihrer Modelle an; 1,0 entspricht einer 1‑zu‑1‑Abbildung mit der gewählten Einheit.

### Schritt 4: Szene nach FBX exportieren

Jetzt, da die Asset‑Informationen angehängt sind, speichern wir die Szene als FBX‑Datei. Die Option `FileFormat.FBX7500ASCII` erzeugt ein menschenlesbares ASCII‑FBX, das für Debugging praktisch ist.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Denken Sie daran:** Ersetzen Sie `"Your Document Directory"` durch einen absoluten Pfad oder einen Pfad relativ zum Arbeitsverzeichnis Ihres Projekts.

## Warum Szene mit Aspose.3D nach FBX exportieren?

Aspose.3D unterstützt **über 50 Eingabe‑ und Ausgabeformate** und kann Szenen mit mehreren hundert Seiten verarbeiten, ohne die gesamte Datei in den Speicher zu laden, wodurch Sie die volle Kontrolle über die exportierte Datei – Metadaten, Einheiten und Geometrie – ohne eine schwere 3D‑Authoring‑Anwendung erhalten. Das macht die automatisierte Asset‑Erstellung, Stapelverarbeitung und serverseitige Konvertierungen schnell und zuverlässig.

## Häufige Anwendungsfälle

- **Game‑Asset‑Pipelines** – Erstellerinformationen direkt in FBX‑Dateien einbetten für Versionsverfolgung.  
- **Architekturvisualisierung** – projektspezifische Einheiten speichern, um Skalierungsfehler beim Import in Rendering‑Engines zu vermeiden.  
- **Automatisiertes Reporting** – FBX‑Dateien on‑the‑fly mit Metadaten erzeugen, die nachgelagerte Analyse‑Tools lesen können.  
- **Cloud‑basierte 3D‑Dienste** – Szenen programmgesteuert erstellen und exportieren ohne GUI, ideal für SaaS‑Plattformen.

## Fehlerbehebung & Tipps

| Problem | Lösung |
|-------|----------|
| **Datei nach dem Speichern nicht gefunden** | Stellen Sie sicher, dass `MyDir` auf einen bestehenden Ordner verweist und dass Ihre Anwendung Schreibberechtigungen hat. |
| **Einheiten erscheinen im externen Viewer falsch** | Überprüfen Sie `unitScaleFactor` erneut; einige Viewer erwarten Meter als Basiseinheit. |
| **Asset‑Metadaten fehlen** | Stellen Sie sicher, dass Sie `scene.getAssetInfo()` **vor** dem Speichern aufrufen; Änderungen nach `save()` werden nicht gespeichert. |
| **Leistungsengpass bei großen Szenen** | `scene.optimize()` vor dem Speichern verwenden, um den Speicherverbrauch zu reduzieren. |
| **ASCII‑FBX ist zu groß** | Wechseln Sie zu binärem FBX, indem Sie `FileFormat.FBX7500` verwenden (siehe FAQ). |

## Häufig gestellte Fragen

**Q: Wie ändere ich das Ausgabeformat zu binärem FBX?**  
A: Ersetzen Sie `FileFormat.FBX7500ASCII` durch `FileFormat.FBX7500`, wenn Sie `scene.save(...)` aufrufen.

**Q: Kann ich benutzerdefinierte, vom Nutzer definierte Metadaten über die integrierten Asset‑Felder hinaus hinzufügen?**  
A: Ja, verwenden Sie `scene.getUserData().add("Key", "Value")`, um zusätzliche Schlüssel‑Wert‑Paare einzubetten.

**Q: Unterstützt Aspose.3D andere Exportformate wie OBJ oder GLTF?**  
A: Ja. Ändern Sie einfach das `FileFormat`‑Enum zu `OBJ` oder `GLTF2`, je nach Bedarf.

**Q: Welche Java‑Version wird benötigt?**  
A: Aspose.3D for Java unterstützt Java 8 und höher.

**Q: Ist es möglich, ein vorhandenes FBX zu laden, seine Asset‑Info zu ändern und erneut zu speichern?**  
A: Absolut. Laden Sie die Datei mit `new Scene("input.fbx")`, ändern Sie `scene.getAssetInfo()`, und speichern Sie anschließend.

---

**Zuletzt aktualisiert:** 2026-09-08  
**Getestet mit:** Aspose.3D for Java 24.11  
**Autor:** Aspose

## Verwandte Tutorials

- [Reduce 3D File Size – Compress Scenes with Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [How to set vector3 color java: Change Diffuse Color and Manage 3D Properties in Java Scenes using Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}