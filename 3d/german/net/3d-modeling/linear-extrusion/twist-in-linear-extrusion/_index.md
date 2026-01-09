---
date: 2026-01-09
description: Erfahren Sie, wie Sie in .NET mit Aspose.3D eine 3D‑Szene erstellen,
  und entdecken Sie, wie Sie Extrusion mit linearen Extrusions‑Drehtechniken verdrehen.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: 3D‑Szene erstellen .NET – Drehung bei linearer Extrusion
url: /de/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D‑Szene .NET erstellen – Drehung bei linearer Extrusion

## Einleitung

## Schnelle Antworten
- **Was bedeutet „create 3d scene .net“?** Es bezieht sich auf das programmgesteuerte Erstellen einer 3‑D‑Szene mit der Aspose.3D‑Bibliothek in einer .NET‑Umgebung.  
- **Wie füge ich einer Extrusion eine Drehung hinzu?** Setzen Sie die `Twist`‑Eigenschaft eines `LinearExtrusion`‑Objekts; der Wert ist der Rotationswinkel in Grad.  
- **Benötige ich eine Lizenz für Aspose.3D?** Eine kostenlose Testversion ist für die Evaluierung ausreichend; für den Produktionseinsatz ist eine kommerzielle Lizenz erforderlich.  
- **Welche .NET‑Versionen werden unterstützt?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6 und später.  
- **Welche Auswirkung hat der `Slices`‑Wert?** Mehr Slices ergeben eine glattere Drehung, erhöhen jedoch Speicher- und Verarbeitungszeit.

## Was ist lineare Extrusion mit Twist?
Linear extrusion sweeps a 2‑D profile along a straight path, while the **twist** property rotates the profile gradually, producing a helical effect. This technique is perfect for modeling springs, twisted columns, or decorative elements.

## Warum Aspose.3D für diese Aufgabe verwenden?
- **Einfach zu nutzende API** – intuitive Klassen wie `LinearExtrusion` und `RectangleShape`.  
- **Vollständige .NET‑Integration** – funktioniert nahtlos mit C#, VB.NET und F#.  
- **Plattformübergreifende Ausgabe** – Export nach OBJ, STL, FBX und vielen anderen Formaten.

## Voraussetzungen

Bevor wir diese 3D‑Reise beginnen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllt haben:

- Aspose.3D for .NET: Stellen Sie sicher, dass Sie die Aspose.3D‑Bibliothek installiert haben. Falls nicht, können Sie sie [hier](https://releases.aspose.com/3d/net/) herunterladen.
- Basic .NET Development Knowledge: Dieses Tutorial setzt Grundkenntnisse in .NET‑Entwicklung voraus.

## Namespaces importieren

In jedem .NET‑Projekt ist die korrekte Verwendung von Namespaces entscheidend. Beginnen Sie damit, die erforderlichen Namespaces zu importieren, um die Funktionalitäten von Aspose.3D effektiv zu nutzen. Hier ein Code‑Snippet zur Orientierung:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Wie man eine 3D‑Szene .NET mit Linear Extrusion Twist erstellt

Im Folgenden finden Sie eine Schritt‑für‑Schritt‑Anleitung, die genau zeigt, wie man **eine 3D‑Szene .NET** erstellt und einer linearen Extrusion eine Drehung hinzufügt.

### Schritt 1: Basisprofil initialisieren

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Wir beginnen mit der Definition eines Rechteckprofils. Passen Sie `RoundingRadius` an, um die Ecken bei Bedarf abzurunden.

### Schritt 2: 3D‑Szene erstellen

```csharp
// Create a scene 
Scene scene = new Scene();
```

Das `Scene`‑Objekt dient als Leinwand, auf der alle 3‑D‑Objekte platziert werden.

### Schritt 3: Linke und rechte Nodes erstellen

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

Nodes sind Container für Geometrie. Wir erstellen zwei Nodes, um eine nicht‑gedrehte Extrusion (links) mit einer gedrehten (rechts) zu vergleichen. Der linke Node wird um 15 Einheiten entlang der X‑Achse verschoben, um eine visuelle Trennung zu erzielen.

### Schritt 4: Lineare Extrusion mit Twist am linken Node ausführen

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

Hier ist `Twist` auf **0°** gesetzt, was eine gerade Extrusion erzeugt. Der `Slices`‑Wert von **100** liefert eine glatte Oberfläche.

### Schritt 5: Lineare Extrusion mit Twist am rechten Node ausführen

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

Durch Setzen von `Twist = 90` wird das Profil über die Extrusionslänge um volle 90 Grad gedreht, wodurch eine deutliche Helix entsteht.

### Schritt 6: 3D‑Szene speichern

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Die Szene wird als OBJ‑Datei exportiert, die Sie in den meisten 3‑D‑Betrachtern öffnen oder in andere Pipelines importieren können.

## Häufige Probleme und Lösungen

| Problem | Warum es passiert | Wie zu beheben |
|---------|-------------------|----------------|
| **Twist sieht flach aus** | `Slices` ist zu niedrig, was zu grober Geometrie führt. | Erhöhen Sie `Slices` (z. B. 200) für glattere Drehungen. |
| **Leistung sinkt bei hohem `Slices`** | Mehr Polygone benötigen mehr Speicher/CPU. | Verwenden Sie das niedrigste `Slices`, das noch die gewünschte Bildqualität liefert, oder aktivieren Sie die Geometrie‑Vereinfachung nach der Extrusion. |
| **Datei beim Speichern nicht gefunden** | Der Pfad des Ausgabeverzeichnisses ist ungültig. | Geben Sie einen vollständigen absoluten Pfad an oder stellen Sie sicher, dass das Verzeichnis existiert, bevor Sie `Save` aufrufen. |

## Häufig gestellte Fragen

**F: Kann ich lineare Extrusion mit Twist auf andere Formen anwenden?**  
A: Auf jeden Fall! Sie können mit verschiedenen Basisprofilen jenseits von Rechtecken experimentieren und damit zahlreiche Gestaltungsmöglichkeiten erschließen.

**F: Welche Rolle spielt die 'Twist'-Eigenschaft bei der linearen Extrusion?**  
A: Die 'Twist'-Eigenschaft bestimmt den Rotationsgrad während des Extrusionsvorgangs und beeinflusst damit die endgültige 3D‑Form.

**F: Gibt es Leistungsaspekte bei Verwendung einer hohen Anzahl von Slices?**  
A: Obwohl eine höhere Anzahl von Slices mehr Details liefert, kann sie die Leistung beeinträchtigen. Finden Sie ein Gleichgewicht, das den Anforderungen Ihrer Anwendung entspricht.

**F: Kann ich lineare Extrusion mit anderen Aspose.3D‑Funktionen kombinieren?**  
A: Natürlich! Aspose.3D bietet einen umfangreichen Funktionsumfang. Kombinieren Sie gerne lineare Extrusion mit anderen Funktionen für komplexere Designs.

**F: Gibt es eine Community für Aspose.3D‑Support und Diskussionen?**  
A: Ja, treten Sie der Aspose.3D‑Community im [Aspose Forum](https://forum.aspose.com/c/3d/18) bei für Support und anregende Diskussionen.

---

**Zuletzt aktualisiert:** 2026-01-09  
**Getestet mit:** Aspose.3D 24.11 für .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}