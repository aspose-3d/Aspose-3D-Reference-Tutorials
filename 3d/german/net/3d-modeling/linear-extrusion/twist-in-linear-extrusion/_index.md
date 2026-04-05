---
date: 2026-03-23
description: Erfahren Sie, wie Sie mit Aspose.3D für .NET eine Extrusion mit einer
  Drehung erstellen. Dieser Schritt‑für‑Schritt‑Leitfaden behandelt Techniken zur
  linearen Extrusion‑Drehung.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Wie man eine Extrusion mit einer Drehung in der linearen Extrusion erstellt
url: /de/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man eine Extrusion mit einer Drehung bei linearer Extrusion erstellt

## Einleitung

Wenn Sie .NET‑Anwendungen entwickeln, die auffällige 3D‑Visualisierungen benötigen, werden Sie schnell feststellen, dass **how to create extrusion** eine grundlegende Fähigkeit ist. Aspose.3D für .NET bietet Ihnen eine saubere, hochleistungsfähige API, um einfache 2‑D‑Profile in anspruchsvolle 3‑D‑Modelle zu verwandeln – insbesondere, wenn Sie eine Drehung hinzufügen. In diesem Tutorial führen wir Sie durch jeden Schritt, vom Einrichten der Szene bis zum Speichern der finalen OBJ‑Datei, damit Sie die Kraft der linearen Extrusions‑Drehung in Aktion sehen können.

## Schnelle Antworten
- **Wie lautet die primäre Klasse für die Extrusion?** `LinearExtrusion`
- **Welche Eigenschaft fügt die Rotation hinzu?** `Twist`
- **Wie viele Slices ergeben glatte Ergebnisse?** Etwa 100 Slices (nach Bedarf anpassen)
- **Kann ich andere Formen verwenden?** Ja, jedes `IProfile` wie Kreise, Polygone oder benutzerdefinierte Kurven
- **Welches Dateiformat wird im Beispiel verwendet?** Wavefront OBJ (`.obj`)

## Voraussetzungen

Bevor wir beginnen, stellen Sie sicher, dass Sie Folgendes haben:

- Aspose.3D für .NET installiert. Wenn Sie es noch nicht heruntergeladen haben, erhalten Sie es **[hier](https://releases.aspose.com/3d/net/)**.
- Eine funktionierende .NET‑Entwicklungsumgebung (Visual Studio, VS Code oder ein beliebiges IDE Ihrer Wahl).
- Grundlegende Kenntnisse der C#‑Syntax und objektorientierter Konzepte.

## Namespaces importieren

In jedem .NET‑Projekt ist die korrekte Verwendung von Namespaces entscheidend. Beginnen Sie damit, die notwendigen Namespaces zu importieren, um die Funktionalitäten von Aspose.3D effektiv zu nutzen. Hier ein Snippet zur Orientierung:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Schritt‑für‑Schritt‑Anleitung

### Schritt 1: Basisprofil initialisieren

Wir beginnen damit, die Form zu definieren, die extrudiert werden soll. In diesem Beispiel verwenden wir ein Rechteck mit einem kleinen Abrundungsradius, um den Kanten eine dezente Krümmung zu geben.

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Schritt 2: Eine 3D‑Szene erstellen

Ein `Scene`‑Objekt fungiert als Leinwand, auf der alle 3‑D‑Entitäten leben. Denken Sie daran als die Bühne für Ihre Extrusion.

```csharp
// Create a scene 
Scene scene = new Scene();
```

### Schritt 3: Linke und rechte Knoten hinzufügen

Knoten ermöglichen es Ihnen, Objekte hierarchisch zu organisieren. Wir erstellen zwei Geschwister‑Knoten – einen für eine gerade Extrusion und einen für eine gedrehte Version.

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### Schritt 4: Lineare Extrusion mit Drehung am linken Knoten ausführen

Die `Twist`‑Eigenschaft steuert, wie stark das Profil während der Extrusion rotiert. Wird sie auf **0** gesetzt, entsteht eine klassische gerade Extrusion.

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### Schritt 5: Lineare Extrusion mit Drehung am rechten Knoten ausführen

Jetzt wenden wir eine 90‑Grad‑Drehung auf dasselbe Profil an. Dies demonstriert den **linear extrusion twist**‑Effekt deutlich.

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### Schritt 6: Die 3D‑Szene speichern

Abschließend exportieren wir die Szene in ein Format, das Sie in jedem 3‑D‑Viewer betrachten können. Das Beispiel verwendet Wavefront OBJ, aber Aspose.3D unterstützt viele weitere Formate.

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Warum lineare Extrusion mit einer Drehung verwenden?

- **Schnelles Prototyping:** 2‑D‑Skizzen in 3‑D‑Teile umwandeln, ohne manuelles Modellieren.
- **Design‑Flexibilität:** Den `Twist`‑Wert anpassen, um Spiralen, helicale Rippen oder dekorative Elemente zu erzeugen.
- **Performance‑freundlich:** Der `Slices`‑Parameter ermöglicht ein Gleichgewicht zwischen visueller Detailtreue und Laufzeitgeschwindigkeit.

## Häufige Probleme & Tipps

- **Zu viele Slices:** Obwohl 100 Slices glatt aussehen, können extrem hohe Werte das Rendering verlangsamen. Testen Sie niedrigere Werte, falls die Performance ein Problem wird.
- **Negative Twist‑Werte:** Ein negativer `Twist` dreht in die entgegengesetzte Richtung – nützlich für gespiegelte Designs.
- **Dateipfade:** Stellen Sie sicher, dass das Ausgabeverzeichnis existiert und Sie Schreibrechte haben; andernfalls wirft `scene.Save` eine Ausnahme.

## Fazit

In diesem Tutorial haben wir gezeigt **how to create extrusion** mit einer Drehung mithilfe von Aspose.3D für .NET. Durch Anpassen der `Twist`‑ und `Slices`‑Eigenschaften können Sie eine Vielzahl von Formen erzeugen, von einfachen verdrehten Stäben bis zu komplexen helicalen Strukturen, und das mit nur wenigen Codezeilen.

## Häufig gestellte Fragen

**Q: Kann ich lineare Extrusion mit einer Drehung auf andere Formen anwenden?**  
A: Absolut! Jede Klasse, die `IProfile` implementiert – wie `CircleShape`, `PolygonShape` oder eine benutzerdefinierte Spline – kann mit einer Drehung extrudiert werden.

**Q: Was stellt die `Twist`‑Eigenschaft tatsächlich dar?**  
A: Sie gibt den Gesamtdrehwinkel (in Grad) an, der über die Extrusionslänge auf das Profil angewendet wird.

**Q: Wird das Erhöhen der Anzahl von Slices den Speicherverbrauch beeinflussen?**  
A: Ja, mehr Slices erzeugen mehr Vertices und Faces, was zusätzlichen Speicher verbraucht und die Performance auf Low‑End‑Geräten beeinträchtigen kann.

**Q: Kann ich lineare Extrusion mit anderen Aspose.3D‑Funktionen kombinieren?**  
A: Definitiv. Sie können nach der Extrusion Materialien, Texturen oder sogar Boolesche Operationen anwenden, um noch reichhaltigere Modelle zu erstellen.

**Q: Wo kann ich Hilfe erhalten oder Ideen mit anderen Entwicklern diskutieren?**  
A: Treten Sie der Aspose.3D‑Community im **[Aspose Forum](https://forum.aspose.com/c/3d/18)** bei für Support, Beispiele und Diskussionen.

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}