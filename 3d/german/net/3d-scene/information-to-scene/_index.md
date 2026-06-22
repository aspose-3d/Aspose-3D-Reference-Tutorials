---
date: 2026-03-26
description: Erfahren Sie, wie Sie Anbieterdaten zu einer 3D‑Szene hinzufügen und
  FBX‑Dateien mit Aspose.3D für .NET speichern. Folgen Sie dieser Schritt‑für‑Schritt‑Anleitung
  mit sofort ausführbarem Code.
linktitle: Extracting Information to Scene Assets
second_title: Aspose.3D .NET API
title: Wie man Anbieterinformationen hinzufügt und eine FBX‑Szene mit Aspose.3D speichert
url: /de/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man Anbieterinformationen hinzufügt und eine FBX‑Szene mit Aspose.3D speichert

## Einführung

Willkommen zu diesem umfassenden Tutorial, das **zeigt, wie man Anbieter**‑Details zu einer 3D‑Szene hinzufügt und anschließend **wie man FBX**‑Dateien mit Aspose.3D für .NET speichert. Egal, ob Sie architektonische Visualisierungen, Spiel‑Assets oder Ingenieur‑Modelle erstellen – das Einbetten von Anbieter‑ und Anwendungs‑Metadaten macht Ihre Szenen informativer und erleichtert die nachgelagerte Verwaltung. Lassen Sie uns den Prozess Schritt für Schritt durchgehen.

## Schnellantworten
- **Was bedeutet „Add Vendor“?** Es speichert die Anwendungs‑ und Anbieternamen im AssetInfo‑Block der Szene.  
- **Welches Format unterstützt Anbieterinformationen?** FBX (ASCII oder binär) behält die Metadaten beim Speichern bei.  
- **Wie speichere ich FBX?** Verwenden Sie `scene.Save(path, FileFormat.FBX7500ASCII)` oder das binäre Gegenstück.  
- **Benötige ich eine Lizenz?** Eine kostenlose Testversion reicht für die Entwicklung; für die Produktion ist eine kommerzielle Lizenz erforderlich.  
- **Kann ich die Maßeinheiten ändern?** Ja, setzen Sie `AssetInfo.UnitName` und `AssetInfo.UnitScaleFactor`.

## Was bedeutet „how to add vendor“ in einer 3D‑Szene?
Das Hinzufügen von Anbieterinformationen bedeutet, die `AssetInfo`‑Eigenschaften eines `Scene`‑Objekts zu befüllen. Diese Eigenschaften reisen mit der Datei und ermöglichen es jedem Empfänger der FBX‑Datei zu sehen, welche Anwendung sie erstellt hat und wer der Anbieter ist.

## Warum Anbieterinformationen hinzufügen?
- **Nachverfolgbarkeit:** Schnell die Quelle eines Modells in großen Pipelines identifizieren.  
- **Compliance:** Einige Branchen verlangen eine explizite Anbieterkennzeichnung für das Asset‑Management.  
- **Automatisierung:** Skripte können Dateien basierend auf Anbieter‑Metadaten filtern oder verarbeiten.

## Voraussetzungen

- Aspose.3D für .NET installiert. Sie können es von der [Aspose.3D für .NET‑Seite](https://releases.aspose.com/3d/net/) herunterladen.

## Namespaces importieren

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Wie man Anbieterinformationen hinzufügt

### Schritt 1: Eine 3D‑Szene initialisieren

```csharp
Scene scene = new Scene();
```

Das Erstellen einer frischen `Scene` gibt Ihnen eine saubere Arbeitsfläche.

### Schritt 2: Anwendungs‑ und Anbieterinformationen festlegen

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Hier demonstrieren wir **wie man Anbieter**‑Daten hinzufügt, indem wir sinnvolle Zeichenketten `ApplicationName` und `ApplicationVendor` zuweisen.

### Schritt 3: Maßeinheiten definieren

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Die Angabe des Einheitssystems stellt sicher, dass jeder, der die FBX‑Datei öffnet, die Abmessungen korrekt interpretiert. In diesem Beispiel entspricht ein „Pol“ 60 cm.

## Wie man die FBX‑Szene speichert

### Schritt 4: Szene speichern (how to save fbx)

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Diese Zeile zeigt **wie man fbx speichert** mit der ASCII‑Version von FBX 7.5.0. Wenn Sie das binäre Format bevorzugen, ersetzen Sie `FBX7500ASCII` durch `FBX7500Binary`.

> **Pro‑Tipp:** Halten Sie die Dateierweiterung `.fbx` konsistent mit dem gewählten Format; sonst können einige Viewer den Inhalt falsch interpretieren.

### Schritt 5: Erfolgsmeldung anzeigen

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Eine freundliche Konsolennachricht bestätigt, dass die Szene, inklusive Anbieter‑Metadaten, auf die Festplatte geschrieben wurde.

## Häufige Probleme und Lösungen

| Problem | Lösung |
|-------|----------|
| **Anbieterinformationen werden im Viewer nicht angezeigt** | Stellen Sie sicher, dass Sie die Datei als **FBX ASCII** oder **Binary** gespeichert haben; einige ältere Viewer unterstützen nur ein Format. |
| **Pfad enthält Leerzeichen** | Setzen Sie den Pfad in Anführungszeichen oder verwenden Sie `Path.Combine`, um einen sicheren Dateipfad zu erstellen. |
| **Einheitsskala sieht falsch aus** | Überprüfen Sie `UnitScaleFactor`; es ist ein Multiplikator relativ zu Metern. |
| **Lizenz‑Ausnahme** | Nutzen Sie die kostenlose Testversion zum Testen; erwerben Sie eine Voll‑Lizenz für Produktions‑Builds. |

## Häufig gestellte Fragen

**F: Kann ich Aspose.3D für .NET mit anderen Programmiersprachen verwenden?**  
A: Aspose.3D unterstützt hauptsächlich .NET‑Sprachen, aber Sie können Interoperabilitäts‑Optionen für andere Sprachen erkunden.

**F: Gibt es eine kostenlose Testversion für Aspose.3D für .NET?**  
A: Ja, Sie können die kostenlose Testversion [hier](https://releases.aspose.com/) erhalten.

**F: Wie erhalte ich Support für Aspose.3D‑bezogene Anfragen?**  
A: Besuchen Sie das [Aspose.3D‑Forum](https://forum.aspose.com/c/3d/18) für Community‑ und Support‑Hilfe.

**F: Kann ich eine temporäre Lizenz für Aspose.3D für .NET erwerben?**  
A: Ja, Sie können eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/) erwerben.

**F: Wo finde ich ausführliche Dokumentation für Aspose.3D für .NET?**  
A: Siehe die [Dokumentation](https://reference.aspose.com/3d/net/) für detaillierte Informationen.

---

**Zuletzt aktualisiert:** 2026-03-26  
**Getestet mit:** Aspose.3D 24.11 für .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}