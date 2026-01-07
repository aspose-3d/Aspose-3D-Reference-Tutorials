---
date: 2026-01-07
description: Erfahren Sie, wie Sie ein 2D‑Profil linear extrudieren und das 3D‑Modell
  im OBJ‑Format mit Aspose.3D für .NET exportieren. Dieses Tutorial zur linearen Extrusion
  führt Sie Schritt für Schritt.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Wie man lineare Extrusion mit Aspose.3D für .NET durchführt
url: /de/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# How to Linear Extrude mit Aspose.3D für .NET

## Einführung

Willkommen zu unserem **linear extrusion tutorial**! In diesem Leitfaden erfahren Sie **wie man linear extrude** ein 2‑D‑Profil und es in ein vollwertiges 3‑D‑Objekt mit Aspose.3D für .NET verwandelt. Egal, ob Sie eine CAD‑ähnliche Anwendung bauen oder einfach **export 3d model obj**‑Dateien für die Weiterverarbeitung benötigen, diese Schritt‑für‑Schritt‑Anleitung gibt Ihnen das Vertrauen, leistungsstarke Geometrieerstellung in Ihre Projekte zu integrieren.

## Schnellantworten
- **Was ist linear extrusion?** Ein 2‑D‑Form wird entlang einer geraden Linie zu einem 3‑D‑Körper erweitert.  
- **Welche Bibliothek verwenden wir?** Aspose.3D für .NET.  
- **Brauche ich eine Lizenz?** Eine temporäre Lizenz reicht für Tests; für die Produktion ist eine Voll‑Lizenz erforderlich.  
- **Kann ich nach OBJ exportieren?** Ja – die finale Szene wird als Wavefront‑OBJ‑Datei gespeichert.  
- **Wie viele Code‑Zeilen?** Unter 30 Zeilen C# plus erläuternde Kommentare.

## Was ist Linear Extrusion?

Linear extrusion nimmt ein flaches Profil (z. B. ein Rechteck oder einen Kreis) und schwenkt es entlang einer geraden Linie, optional mit Drehungen, Skalierungen oder Versätzen. Das Ergebnis ist ein Festkörper, der gerendert, bearbeitet oder für andere 3‑D‑Tools exportiert werden kann.

## Warum Aspose.3D für Linear Extrusion verwenden?

* **Zero‑dependency:** Keine externen CAD‑Kerne nötig.  
* **Vollständige .NET‑Unterstützung:** Funktioniert mit .NET Framework, .NET Core und .NET 5/6+.  
* **Export‑Flexibilität:** Direktes Speichern nach OBJ, STL, FBX und vielen anderen Formaten.  
* **Umfangreiche API:** Steuern Sie Slices, Twist und Offsets mit nur wenigen Eigenschaften.

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie Folgendes haben:

1. **Aspose.3D installiert** – laden Sie es von [hier](https://releases.aspose.com/3d/net/) herunter.  
2. **Zugriff auf die Dokumentation** – folgen Sie dem Setup‑Guide [hier](https://reference.aspose.com/3d/net/).  
3. Eine .NET‑Entwicklungsumgebung (Visual Studio, VS Code oder Rider) mit den erforderlichen Namespaces.

## Namespaces importieren

Binden Sie die wesentlichen Namespaces ein, um die Funktionalität von Aspose.3D zu nutzen:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Diese Namespaces geben Ihnen Zugriff auf `Scene`, `LinearExtrusion`, `RectangleShape` und Hilfsklassen wie `Vector3`.

## Linear Extrusion durchführen

Im Folgenden finden Sie den kompletten Workflow. Jeder Schritt wird in einfacher Sprache erklärt, bevor der zugehörige Codeblock folgt, sodass Sie ohne Rätselraten dem Code folgen können.

### Schritt 1: Basis‑Profil initialisieren

Zuerst erstellen Sie die 2‑D‑Form, die extrudiert werden soll. In diesem Beispiel verwenden wir ein Rechteck mit einem kleinen Rundungsradius.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*Warum das wichtig ist:* Das Profil definiert den Querschnitt des finalen 3‑D‑Objekts. Passen Sie `RoundingRadius`, Breite oder Höhe an, um unterschiedliche Silhouetten zu erhalten.

### Schritt 2: Linear Extrusion anwenden

Jetzt schwenken wir das Profil 10 Einheiten entlang der Z‑Achse, fügen 100 Slices für Glätte hinzu, zentrieren die Geometrie und wenden einen vollen 360°‑Twist mit einem Offset an.

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*Pro‑Tipp:* Spielen Sie mit `Slices`, um das Verhältnis von Performance zu visueller Qualität zu balancieren, und experimentieren Sie mit `Twist` für Spiral‑Effekte.

### Schritt 3: Szene erstellen

Eine `Scene` fungiert als Container für alle 3‑D‑Entitäten – denken Sie an eine Leinwand.

```csharp
Scene scene = new Scene();
```

### Schritt 4: Extrusion zur Szene hinzufügen

Binden Sie die extrudierte Geometrie an den Root‑Node der Szene, damit sie Teil der renderbaren Hierarchie wird.

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### Schritt 5: 3‑D‑Modell speichern

Abschließend exportieren Sie die Szene in eine weit verbreitete OBJ‑Datei. Dies demonstriert die **export 3d model obj**‑Fähigkeit von Aspose.3D.

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Wenn Sie die resultierende `LinearExtrusion.obj` in einem beliebigen 3‑D‑Viewer öffnen, sehen Sie ein verdrehtes rechteckiges Prisma – genau das, was der Code beschreibt.

## Häufige Stolperfallen & Tipps

| Problem | Warum es passiert | Lösung |
|---------|-------------------|--------|
| **Profil nicht sichtbar** | Vergessen, die Extrusion zur Szene hinzuzufügen. | Sicherstellen, dass `CreateChildNode` aufgerufen wird. |
| **Twist wirkt flach** | `Slices` zu niedrig, wodurch grobe Geometrie entsteht. | `Slices` erhöhen (z. B. 200) für einen glatteren Twist. |
| **Export schlägt fehl** | Ausgabeverzeichnis existiert nicht oder fehlende Schreibrechte. | `RunExamples.GetOutputFilePath` verwenden oder das Verzeichnis manuell erstellen. |
| **Unerwartete Skalierung** | `Center` ist auf `false` gesetzt und verschiebt die Geometrie. | `Center = true` setzen, sofern kein Offset gewünscht ist. |

## Häufig gestellte Fragen

### Q1: Ist Aspose.3D für Anfänger geeignet?

A1: Absolut! Aspose.3D bietet eine benutzerfreundliche API, und dieses Tutorial führt Sie durch die Grundlagen von linear extrusion.

### Q2: Kann ich Aspose.3D für kommerzielle Projekte nutzen?

A2: Ja, Aspose.3D bietet Lizenzoptionen für sowohl private als auch kommerzielle Nutzung. Details finden Sie [hier](https://purchase.aspose.com/buy).

### Q3: Wie bekomme ich temporäre Lizenzen für Tests?

A3: Besuchen Sie [diesen Link](https://purchase.aspose.com/temporary-license/), um temporäre Lizenzen für Testzwecke zu erhalten.

### Q4: Wo finde ich Community‑Support?

A4: Treten Sie dem [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) bei, um sich mit einer lebendigen Community zu vernetzen und Hilfe zu erhalten.

### Q5: Gibt es eine kostenlose Testversion?

A5: Natürlich! Laden Sie die kostenlose Testversion [hier](https://releases.aspose.com/) herunter, um die Fähigkeiten von Aspose.3D selbst zu erleben.

---

**Zuletzt aktualisiert:** 2026-01-07  
**Getestet mit:** Aspose.3D 24.11 für .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}