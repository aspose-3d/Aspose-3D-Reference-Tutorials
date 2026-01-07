---
date: 2026-01-07
description: Erfahren Sie, wie Sie eine Grundfläche hinzufügen, während Sie lineare
  Extrusion mit Aspose.3D für .NET durchführen und Wavefront‑OBJ‑Dateien exportieren.
  Beherrschen Sie Zentrierungs‑ und Bodentechniken im 3‑D‑Modellieren.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: Grundebene und Zentrum in linearer Extrusion hinzufügen
url: /de/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Grundfläche hinzufügen und zentrieren bei linearer Extrusion

## Einführung

Willkommen zu diesem umfassenden Leitfaden, der Ihnen die lineare Extrusion mit Aspose.3D für .NET näherbringt. Wenn Sie **eine Grundfläche** zu Ihren Modellen hinzufügen und **Wavefront‑OBJ**‑Dateien exportieren möchten, während die Extrusion zentriert bleibt, sind Sie hier genau richtig. In diesem Tutorial gehen wir auf die Technik der linearen Extrusion ein, wobei wir besonders den Aspekt der Zentrierung beleuchten und zeigen, wie eine Grundfläche das Ergebnis klarer visualisiert.

## Schnellantworten
- **Was bewirkt das „Grundfläche hinzufügen“?** Sie liefert eine visuelle Referenz, die das Erkennen erleichtert, wo die Extrusion in der X‑Z‑Ebene liegt.  
- **Welches Format wird zum Exportieren des Modells verwendet?** Die Szene wird als Wavefront‑OBJ‑Datei gespeichert (`FileFormat.WavefrontOBJ`).  
- **Benötige ich eine Lizenz, um den Code auszuführen?** Eine kostenlose Testversion reicht für die Entwicklung; für den Produktionseinsatz ist eine permanente Lizenz erforderlich.  
- **Kann ich die Extrusionslänge ändern?** Ja – ändern Sie den zweiten Parameter von `LinearExtrusion`.  
- **Ist die Zentrierung optional?** Durch Setzen von `Center = true` wird die Extrusion um das Profil zentriert; `false` richtet sie an einer Seite aus.

## Voraussetzungen

Bevor wir diese spannende Reise beginnen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllt haben:

- Grundlegendes Verständnis der Programmiersprache C#.  
- Visual Studio auf Ihrem Rechner installiert.  
- Aspose.3D für .NET‑Bibliothek, die Sie von der [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) herunterladen können.  
- Stellen Sie sicher, dass Sie Zugriff auf die [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) für Referenzzwecke während des Tutorials haben.

## Namespaces importieren

Um loszulegen, importieren wir die notwendigen Namespaces. Diese bilden das Fundament für unser 3‑D‑Modellierungs‑Meisterwerk.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Schritt 1: Basisprofil initialisieren

Wir beginnen mit der Definition eines rechteckigen Profils, das extrudiert wird. Der `RoundingRadius` fügt den Ecken eine dezente Rundung hinzu.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Schritt 2: 3‑D‑Szene erstellen

Ein `Scene`‑Objekt fungiert als Container für alle Geometrien, Lichter und Kameras.

```csharp
Scene scene = new Scene();
```

## Schritt 3: Linke und rechte Knoten erstellen

Zwei Geschwister‑Knoten werden unter dem Root‑Knoten erzeugt. Einer demonstriert die Extrusion **ohne** Zentrierung, der andere **mit** Zentrierung. Wir verschieben den linken Knoten, damit sich die beiden Beispiele nicht überlappen.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Schritt 4: Lineare Extrusion am linken Knoten durchführen (Keine Zentrierung)

Hier extrudieren wir das Profil ohne Zentrierung. Beachten Sie das Flag `Center = false`.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Schritt 5: Grundfläche zur Referenz hinzufügen (Linker Knoten)

Das Hinzufügen einer dünnen Box dient als **Grundfläche**, sodass Sie klar erkennen können, wie die Extrusion auf der Basis liegt.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Schritt 6: Lineare Extrusion am rechten Knoten durchführen (Mit Zentrierung)

Jetzt extrudieren wir dasselbe Profil, jedoch mit aktivierter Zentrierung. Die Geometrie wird symmetrisch um den Ursprung des Profils platziert.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Schritt 7: Grundfläche zur Referenz hinzufügen (Rechter Knoten)

Eine zweite Grundfläche wird dem rechten Knoten hinzugefügt, um den visuellen Vergleich konsistent zu halten.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Schritt 8: Wavefront‑OBJ‑Datei exportieren

Abschließend **exportieren wir das Wavefront‑OBJ**, sodass das Ergebnis in jedem gängigen 3‑D‑Viewer geöffnet werden kann.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Warum eine Grundfläche hinzufügen?

Eine Grundfläche liefert sofortige visuelle Hinweise zur Höhe und Ausrichtung der Extrusion. Sie ist besonders hilfreich, wenn Sie zentrierte und nicht‑zentrierte Ergebnisse vergleichen möchten, wie in diesem Tutorial demonstriert.

## Häufige Probleme & Tipps

- **Grundfläche nicht sichtbar:** Stellen Sie sicher, dass die Dicke der Ebene (`0.01` im `Box`‑Konstruktor) klein genug ist, um die Extrusion nicht zu verdecken, aber groß genug, um gerendert zu werden.  
- **Export schlägt fehl:** Prüfen Sie, ob das Ausgabeverzeichnis existiert und Sie Schreibrechte besitzen.  
- **Zentrierte Extrusion erscheint versetzt:** Überprüfen Sie die Eigenschaft `Center`; `true` zentriert das Profil, `false` richtet es an einer Seite aus.

## Häufig gestellte Fragen

### Q1: Kann ich Aspose.3D für .NET mit anderen Programmiersprachen verwenden?

A1: Aspose.3D unterstützt hauptsächlich .NET‑Sprachen wie C# und VB.NET.

### Q2: Wo finde ich Support für Fragen zu Aspose.3D?

A2: Besuchen Sie das [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) für dedizierten Support und Diskussionen.

### Q3: Gibt es eine kostenlose Testversion von Aspose.3D für .NET?

A3: Ja, Sie können die kostenlose Testversion [hier](https://releases.aspose.com/) erhalten.

### Q4: Wie kann ich eine temporäre Lizenz für Aspose.3D für .NET erhalten?

A4: Eine temporäre Lizenz erhalten Sie [hier](https://purchase.aspose.com/temporary-license/).

### Q5: Wo kann ich die Aspose.3D für .NET‑Lizenz kaufen?

A5: Kaufen Sie Ihre Lizenz [hier](https://purchase.aspose.com/buy).

### Q6: Kann ich die Szene in andere Formate als OBJ exportieren?

A6: Ja, Aspose.3D unterstützt viele Formate wie STL, FBX und GLTF. Ändern Sie einfach den `FileFormat`‑Enum‑Wert in der `Save`‑Methode.

### Q7: Wie ändere ich die Anzahl der Scheiben bei der Extrusion?

A7: Passen Sie die Eigenschaft `Slices` im `LinearExtrusion`‑Konstruktor an, um die Mesh‑Dichte zu steuern.

---

**Zuletzt aktualisiert:** 2026-01-07  
**Getestet mit:** Aspose.3D für .NET neueste Version  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}