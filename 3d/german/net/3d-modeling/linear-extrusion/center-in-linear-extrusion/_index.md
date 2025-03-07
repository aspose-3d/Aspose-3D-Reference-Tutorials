---
title: Zentrum in der linearen Extrusion
linktitle: Zentrum in der linearen Extrusion
second_title: Aspose.3D .NET API
description: Entdecken Sie die Welt der 3D-Modellierung mit Aspose.3D für .NET. Zentrieren Sie lineare Extrusionstechniken, erstellen Sie atemberaubende Designs und lassen Sie Ihrer Kreativität freien Lauf.
weight: 10
url: /de/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Zentrum in der linearen Extrusion

## Einführung

Willkommen zu diesem umfassenden Leitfaden zur Beherrschung der linearen Extrusion mit Aspose.3D für .NET. Wenn Sie Ihre 3D-Modellierungsfähigkeiten verbessern und atemberaubende Extrusionen erstellen möchten, sind Sie hier richtig. In diesem Tutorial befassen wir uns mit der linearen Extrusionstechnik und konzentrieren uns dabei insbesondere auf den Zentrieraspekt, um Ihre Designs auf ein völlig neues Niveau zu bringen.

## Voraussetzungen

Bevor wir uns auf diese spannende Reise begeben, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

- Grundlegendes Verständnis der Programmiersprache C#.
- Visual Studio ist auf Ihrem Computer installiert.
-  Aspose.3D für .NET-Bibliothek, die Sie von der herunterladen können[Aspose.3D .NET-Dokumentation](https://reference.aspose.com/3d/net/).
-  Stellen Sie sicher, dass Sie Zugriff darauf haben[Aspose.3D .NET-Dokumentation](https://reference.aspose.com/3d/net/) als Referenz im gesamten Tutorial.

## Namespaces importieren

Zum Auftakt importieren wir die erforderlichen Namespaces. Diese werden den Grundstein für unser Meisterwerk der 3D-Modellierung legen.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Schritt 1: Initialisieren Sie das Basisprofil

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Schritt 2: Erstellen Sie eine 3D-Szene

```csharp
Scene scene = new Scene();
```

## Schritt 3: Erstellen Sie linke und rechte Knoten

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Schritt 4: Führen Sie eine lineare Extrusion am linken Knoten durch

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Schritt 5: Grundebene als Referenz festlegen

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Schritt 6: Führen Sie eine lineare Extrusion am rechten Knoten durch

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Schritt 7: Grundebene als Referenz festlegen (rechter Knoten)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Schritt 8: 3D-Szene speichern

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Abschluss

Glückwunsch! Sie haben die Kunst der linearen Extrusion mit Zentrierung mit Aspose.3D für .NET erfolgreich gemeistert. Experimentieren Sie ruhig mit verschiedenen Parametern und erkunden Sie die enormen Möglichkeiten, die diese Technik bietet.

## FAQs

### F1: Kann ich Aspose.3D für .NET mit anderen Programmiersprachen verwenden?

A1: Aspose.3D unterstützt hauptsächlich .NET-Sprachen wie C# und VB.NET.

### F2: Wo finde ich Unterstützung für Aspose.3D-bezogene Abfragen?

 A2: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für engagierte Unterstützung und Diskussionen.

### F3: Gibt es eine kostenlose Testversion für Aspose.3D für .NET?

 A3: Ja, Sie können auf die kostenlose Testversion zugreifen[Hier](https://releases.aspose.com/).

### F4: Wie kann ich eine temporäre Lizenz für Aspose.3D für .NET erhalten?

 A4: Sie können eine temporäre Lizenz erwerben[Hier](https://purchase.aspose.com/temporary-license/).

### F5: Wo kann ich die Aspose.3D für .NET-Lizenz erwerben?

 A5: Kaufen Sie Ihre Lizenz[Hier](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
