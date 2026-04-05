---
date: 2026-03-26
description: Erfahren Sie, wie Sie mit Aspose.3D für .NET einen Zylinder erstellen
  und eine OBJ-Datei exportieren. Dieser einsteigerfreundliche Leitfaden behandelt
  die Einrichtung einer 3D‑Szene und den OBJ‑Export.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Wie man einen Zylinder mit Scherboden erstellt – Aspose.3D für .NET
url: /de/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# So erstellen Sie einen Zylinder mit Scherunterseite – Aspose.3D für .NET

## Einführung
Wenn Sie sich fragen, **wie man Zylinder**‑Objekte mit einer angepassten Scherunterseite in einer .NET‑Umgebung erstellt, sind Sie hier genau richtig. In diesem Tutorial führen wir Sie Schritt für Schritt durch den gesamten Prozess – vom Einrichten einer 3‑D‑Szene bis zum Export des fertigen Modells als OBJ‑Datei – damit Sie Ihre *Anfänger‑3D‑Modellierungs*‑Fähigkeiten mit **Aspose.3D für .NET** verbessern können.

## Schnelle Antworten
- **Welche Hauptklasse startet ein 3D‑Modell?** `Scene` erzeugt den Wurzel‑Container für alle Geometrien.  
- **Welche Methode exportiert das Modell nach OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Benötige ich eine Lizenz für Tests?** Eine kostenlose Testversion ist verfügbar — siehe den Testlink im FAQ.  
- **Kann ich den Scherwinkel ändern?** Ja, passen Sie `ShearBottom` mit einem `Vector2`‑Wert an.  
- **Ist das für Anfänger geeignet?** Absolut; die API abstrahiert die Low‑Level‑Mesh‑Verarbeitung.

## Was ist eine 3D‑Szene?
Eine *3D‑Szene* ist ein hierarchischer Container, der alle geometrischen Entitäten, Lichter, Kameras und Transformationen enthält. In Aspose.3D bietet die Klasse `Scene` eine klare Möglichkeit, Ihre Modelle zu organisieren und später zu exportieren.

## Warum OBJ exportieren?
OBJ ist ein weit verbreitetes, textbasiertes Format, das von vielen 3‑D‑Anwendungen (Blender, Maya, Unity) importiert werden kann. Der Export nach OBJ ermöglicht es Ihnen, Ihre Zylindermodelle außerhalb von .NET zu teilen oder weiter zu bearbeiten.

## Voraussetzungen
Bevor wir starten, stellen Sie sicher, dass Sie Folgendes haben:

- Grundkenntnisse in C# und .NET‑Entwicklung.  
- **Aspose.3D für .NET** installiert – Sie können es **[hier](https://releases.aspose.com/3d/net/)** herunterladen.  
- Eine .NET‑IDE (Visual Studio, Rider oder VS Code) bereit zum Coden.

## Namespaces importieren
Zuerst bringen wir die benötigten Namespaces in den Gültigkeitsbereich, damit die API‑Typen erkannt werden.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Schritt 1: Eine 3D‑Szene erstellen
Das `Scene`‑Objekt fungiert als Wurzel Ihrer Modell‑Hierarchie.

```csharp
Scene scene = new Scene();
```

## Schritt 2: Zylinder 1 erstellen
Wir erzeugen den ersten Zylinder mit einem Radius von 2, einer Höhe von 10 und 20 radialen Segmenten.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Schritt 3: Scherunterseite für Zylinder 1 anpassen
Wenden Sie eine Scher‑Transformation an, aktivieren Sie die Fan‑Cylinder‑Erzeugung und passen Sie weitere Eigenschaften an, um die gewünschte Form zu erreichen.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Schritt 4: Zylinder 1 zur Szene hinzufügen
Platzieren Sie den ersten Zylinder an einer geeigneten Position mittels einer Translations‑Transformation.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Schritt 5: Zylinder 2 erstellen
Ein zweiter Zylinder wird mit denselben Grundmaßen, jedoch ohne benutzerdefiniertes Scheren, erstellt – ideal für einen Seiten‑zu‑Seiten‑Vergleich.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Schritt 6: Zylinder 2 zur Szene hinzufügen
Wir hängen den zweiten Zylinder einfach an den Szenen‑Graphen an.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Schritt 7: Die Szene als OBJ‑Datei exportieren
Abschließend speichern wir die gesamte Szene in einer OBJ‑Datei, sodass sie in jedem gängigen 3‑D‑Viewer geöffnet werden kann.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Häufige Probleme und Lösungen
| Problem | Warum es passiert | Lösung |
|---------|-------------------|--------|
| **OBJ‑Datei ist leer** | Die Szene enthält keine Geometrie. | Stellen Sie sicher, dass beide Zylinder zu `scene.RootNode` hinzugefügt wurden. |
| **Scherung sieht falsch aus** | `ShearBottom` erwartet den Tangens des Winkels. | Verwenden Sie `Math.Tan(winkelInRadiant)` oder den bereitgestellten Wert `0.83` für ca. 47,5°. |
| **Dateipfad‑Fehler** | Ungültiges oder fehlendes Verzeichnis. | Nutzen Sie `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## Häufig gestellte Fragen
### Ist Aspose.3D für .NET für Anfänger geeignet?
Absolut! Aspose.3D für .NET bietet eine High‑Level‑API, die die mathematisch intensiven Teile der 3‑D‑Modellierung abstrahiert und damit für Entwickler jeder Erfahrungsstufe zugänglich ist.

### Kann ich unterschiedliche Scherwinkel für Zylinder anwenden?
Ja, jede `Cylinder`‑Instanz besitzt ihre eigene `ShearBottom`‑Eigenschaft, sodass Sie jedem Objekt einen individuellen Winkel zuweisen können.

### Gibt es eine Testversion?
Ja, Sie können die kostenlose Testversion **[hier](https://releases.aspose.com/)** ausprobieren.

### Wo finde ich zusätzlichen Support?
Besuchen Sie das **[Aspose.3D‑Forum](https://forum.aspose.com/c/3d/18)** für Community‑Hilfe, Code‑Beispiele und Diskussionen.

### Wie erhalte ich eine temporäre Lizenz?
Holen Sie Ihre temporäre Lizenz **[hier](https://purchase.aspose.com/temporary-license/)**.

**Zusätzliche Fragen & Antworten**

**F: Wie exportiere ich das Modell in ein anderes Format, z. B. STL?**  
A: Ersetzen Sie `FileFormat.WavefrontOBJ` durch `FileFormat.STL` im Aufruf von `scene.Save`.

**F: Kann ich die Zylinder nach der Erstellung animieren?**  
A: Ja, Sie können Schlüsselbild‑Animationen zu Knoten‑Transformationen hinzufügen, indem Sie die von Aspose.3D bereitgestellten `Animation`‑Klassen nutzen.

**F: Unterstützt die API .NET Core?**  
A: Die Bibliothek ist vollständig kompatibel mit .NET Core, .NET 5+ und .NET 6+.

---

**Zuletzt aktualisiert:** 2026-03-26  
**Getestet mit:** Aspose.3D für .NET (neueste Version)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}