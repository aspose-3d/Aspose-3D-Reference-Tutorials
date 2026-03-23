---
date: 2026-03-23
description: Erfahren Sie, wie Sie lineare Extrusion mit Scheiben mithilfe von Aspose.3D
  für .NET durchführen. Erstellen Sie detaillierte 3D‑Modelle mit Schritt‑für‑Schritt‑Codebeispielen.
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: Wie man lineare Extrusion mit Schnitten mit Aspose.3D für .NET durchführt
url: /de/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man lineare Extrusion mit Scheiben mit Aspose.3D für .NET durchführt

## Einführung

Willkommen in der Welt des 3D-Designs mit Aspose.3D für .NET! In diesem Tutorial entdecken Sie **wie man lineare Extrusion** mit Scheiben durchführt, eine Technik, die Ihnen ermöglicht, den Detailgrad Ihrer Modelle zu steuern. Egal, ob Sie ein erfahrener Entwickler sind oder gerade erst anfangen, wir führen Sie durch jeden Schritt, erklären das Warum hinter jeder Aktion und geben Ihnen praktische Tipps, die Sie sofort anwenden können.

## Schnelle Antworten
- **Was ist lineare Extrusion mit Scheiben?** Es ist eine Methode, ein 2D‑Profil in 3D zu erweitern, wobei angegeben wird, wie viele Zwischen‑Querschnitte (Scheiben) erzeugt werden.  
- **Warum Scheiben verwenden?** Mehr Scheiben erzeugen eine glattere Krümmung; weniger Scheiben halten das Mesh leichtgewichtig.  
- **Voraussetzungen?** Aspose.3D für .NET, eine .NET‑kompatible IDE und Grundkenntnisse in C#.  
- **Typische Laufzeit?** Das Beispiel läuft in weniger als einer Sekunde auf einem modernen PC.  
- **Ausgabeformat?** Das Beispiel speichert im Wavefront OBJ-Format, aber Aspose.3D unterstützt viele Formate.

## Was ist lineare Extrusion mit Scheiben?

Lineare Extrusion nimmt eine 2‑D‑Form (ein Profil) und streckt sie entlang einer geraden Linie, um einen 3‑D‑Körper zu erzeugen. Die **Slices**‑Eigenschaft bestimmt, wie viele Zwischen‑Querschnitte zwischen dem Anfang und Ende der Extrusion eingefügt werden, was die Glätte und die Polygonanzahl beeinflusst.

## Warum Scheiben bei linearer Extrusion verwenden?

- **Mesh-Dichte steuern:** Feinabstimmung des Gleichgewichts zwischen visueller Qualität und Dateigröße.  
- **Leistung optimieren:** Verwenden Sie weniger Scheiben für Echtzeitanwendungen, mehr für hochauflösende Renderings.  
- **Kreative Flexibilität:** Kombinieren Sie unterschiedliche Scheibenzahlen bei separaten Objekten, um die Designabsicht hervorzuheben.

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie folgendes haben:

- Aspose.3D for .NET Bibliothek – laden Sie sie von [hier](https://releases.aspose.com/3d/net/) herunter.  
- Eine IDE, die C# unterstützt (Visual Studio, Rider, VS Code usw.).  
- Grundlegende Kenntnisse der C#‑Syntax und objektorientierter Konzepte.  
- Neugier, mit 3‑D‑Geometrie zu experimentieren!

## Namespaces importieren

Zuerst importieren Sie die Namespaces, die Ihnen Zugriff auf die Kernklassen von Aspose.3D geben.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Schritt‑für‑Schritt‑Anleitung

### Schritt 1: Basisprofil initialisieren

Wir beginnen mit einer einfachen rechteckigen Form und geben ihr einen kleinen Abrundungsradius, sodass die Kanten nicht perfekt scharf sind.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Schritt 2: 3D‑Szene erstellen

`Scene` fungiert als Container für alle Nodes, Meshes, Lichter und Kameras.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Schritt 3: Linke und rechte Nodes hinzufügen

Wir erstellen zwei Geschwister‑Nodes unter dem Root der Szene. Der linke Node erhält eine niedrige Scheibenzahl, der rechte Node eine hohe Scheibenzahl, sodass Sie den visuellen Unterschied vergleichen können.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Schritt 4: Lineare Extrusion am linken Node durchführen (geringe Detailgenauigkeit)

Hier extrudieren wir das Rechteck mit nur **2 Scheiben**. Das erzeugt ein grobes Mesh – ideal für schnelle Vorschauen.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Schritt 5: Lineare Extrusion am rechten Node durchführen (hohe Detailgenauigkeit)

Jetzt verwenden wir **10 Scheiben** für ein deutlich glatteres Ergebnis. Beachten Sie, wie die Geometrie feiner wird.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Schritt 6: 3D‑Szene speichern

Abschließend schreiben Sie die Szene in eine OBJ‑Datei. Ersetzen Sie `"Your Output Directory"` durch einen gültigen Pfad auf Ihrem Rechner.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Häufige Probleme und Lösungen

| Problem | Warum es passiert | Lösung |
|-------|----------------|-----|
| **Keine Datei erstellt** | Ausgabepfad ist ungültig oder es fehlen Schreibrechte. | Verwenden Sie einen absoluten Pfad und stellen Sie sicher, dass der Ordner existiert. |
| **Objekt sieht flach aus** | `Slices` ist auf 1 oder 0 gesetzt. | Setzen Sie `Slices` auf mindestens 2 für eine sichtbare Extrusion. |
| **Unerwartete Geometrie** | Abrundungsradius zu groß für die Rechteckgröße. | Passen Sie `RoundingRadius` auf einen Wert an, der kleiner ist als die Hälfte der kleinsten Seite des Rechtecks. |

## Häufig gestellte Fragen

**Q:** Kann ich die Extrusionsrichtung ändern?  
**A:** Ja. Verwenden Sie die `Transform`‑Eigenschaft am Node, um die extrudierte Geometrie vor dem Speichern zu drehen oder zu verschieben.

**Q:** Unterstützt Aspose.3D andere Extrusionstypen?  
**A:** Absolut. Neben `LinearExtrusion` können Sie `RevolveExtrusion`, `SweepExtrusion` und weitere verwenden.

**Q:** In welche Dateiformate kann ich exportieren?  
**A:** Aspose.3D unterstützt OBJ, STL, FBX, 3MF, Collada und viele weitere. Ändern Sie einfach das `FileFormat`‑Enum.

**Q:** Gibt es eine Möglichkeit, programmgesteuert ein Material zu setzen?  
**A:** Ja. Nachdem Sie den Node erstellt haben, weisen Sie seiner `Entity`‑Sammlung ein `Material` zu.

**Q:** Wie wirkt sich die Scheibenzahl auf den Speicherverbrauch aus?  
**A:** Mehr Scheiben erhöhen die Anzahl von Vertices und Faces, was den Speicherverbrauch proportional steigert. Nutzen Sie Profiling, um den optimalen Wert für Ihre Zielplattform zu finden.

## Originale FAQ's

### F1: Kann ich Aspose.3D für .NET mit anderen Programmiersprachen verwenden?

A1: Aspose.3D ist hauptsächlich für .NET konzipiert, aber Sie können Interoperabilitätsoptionen mit Sprachen wie Python über .NET‑Bindings erkunden.

### F2: Wo finde ich detaillierte Dokumentation für Aspose.3D für .NET?

A2: Siehe die Dokumentation [hier](https://reference.aspose.com/3d/net/) für ausführliche Informationen zu den Fähigkeiten und der Verwendung von Aspose.3D.

### F3: Gibt es eine kostenlose Testversion für Aspose.3D für .NET?

A3: Ja, Sie können Ihre kostenlose Testversion [hier](https://releases.aspose.com/) erhalten, um die Funktionen der Bibliothek vor dem Kauf zu erkunden.

### F4: Wie kann ich technischen Support für Aspose.3D für .NET erhalten?

A4: Besuchen Sie das Aspose.3D‑Forum [hier](https://forum.aspose.com/c/3d/18), um Hilfe zu erhalten und sich mit der Community auszutauschen.

### F5: Kann ich eine temporäre Lizenz für Aspose.3D für .NET verwenden?

A5: Ja, erhalten Sie eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/) für Evaluierungszwecke.

## Fazit

Sie haben nun gesehen **wie man lineare Extrusion** mit Scheiben mit Aspose.3D für .NET durchführt, die Auswirkungen verschiedener Scheibenzahlen erkundet und gelernt, wie Sie Ihre Arbeit exportieren. Experimentieren Sie mit anderen Profilen, spielen Sie mit dem `Slices`‑Wert und integrieren Sie Materialien oder Lichter, um produktionsreife 3‑D‑Assets zu erstellen.

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}