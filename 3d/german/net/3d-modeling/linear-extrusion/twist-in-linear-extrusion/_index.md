---
title: Verdrehen in der linearen Extrusion
linktitle: Verdrehen in der linearen Extrusion
second_title: Aspose.3D .NET API
description: Entdecken Sie die faszinierende Welt der 3D-Grafik mit Aspose.3D für .NET. Lernen Sie Schritt für Schritt die lineare Extrusion mit einem Twist.
weight: 14
url: /de/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Verdrehen in der linearen Extrusion

## Einführung

In der sich ständig weiterentwickelnden Welt der .NET-Entwicklung ist die Nutzung der Leistungsfähigkeit von 3D-Grafiken ein spannendes Unterfangen. Aspose.3D für .NET erweist sich als wertvolles Toolkit, das Entwicklern die nahtlose Erstellung immersiver und visuell beeindruckender Anwendungen ermöglicht. In diesem umfassenden Leitfaden befassen wir uns mit einer faszinierenden Funktion – der linearen Extrusion mit einem Twist. Dieses Tutorial führt Sie Schritt für Schritt durch den Prozess und erschließt das Potenzial von Aspose.3D für .NET.

## Voraussetzungen

Bevor wir uns auf diese 3D-Reise begeben, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

-  Aspose.3D für .NET: Stellen Sie sicher, dass Sie die Aspose.3D-Bibliothek installiert haben. Wenn nicht, können Sie es herunterladen[Hier](https://releases.aspose.com/3d/net/).

- Grundlegende .NET-Entwicklungskenntnisse: Dieses Tutorial setzt grundlegende Kenntnisse der .NET-Entwicklung voraus.

## Namespaces importieren:

In jedem .NET-Projekt ist die ordnungsgemäße Verwendung von Namespaces von entscheidender Bedeutung. Beginnen Sie mit dem Importieren der erforderlichen Namespaces, um die Funktionen von Aspose.3D effektiv nutzen zu können. Hier ist ein Ausschnitt zur Orientierung:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Lassen Sie uns nun den faszinierenden Prozess der linearen Extrusion mit einem Twist unter Verwendung von Aspose.3D für .NET in leicht verständliche Schritte unterteilen:

## Schritt 1: Initialisieren Sie das Basisprofil

```csharp
// Initialisieren Sie das zu extrudierende Basisprofil
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Beginnen Sie mit dem Einrichten des Basisprofils für die Extrusion. In diesem Beispiel verwenden wir eine Rechteckform mit einem angegebenen Rundungsradius.

## Schritt 2: Erstellen Sie eine 3D-Szene

```csharp
// Erstellen Sie eine Szene
Scene scene = new Scene();
```

Erstellen Sie eine 3D-Szene, in der die ganze Magie stattfinden wird. Dies dient als Leinwand für unser 3D-Meisterwerk.

## Schritt 3: Erstellen Sie linke und rechte Knoten

```csharp
// Linken Knoten erstellen
var left = scene.RootNode.CreateChildNode();
// Erstellen Sie den rechten Knoten
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

Erzeugen Sie linke und rechte Knoten innerhalb der Szene. Passen Sie die Übersetzung des linken Knotens an, um ihn richtig zu positionieren.

## Schritt 4: Führen Sie eine lineare Extrusion mit Drehung am linken Knoten durch

```csharp
// Die Eigenschaft „Drehung“ definiert den Grad der Drehung beim Extrudieren des Profils
//Führen Sie eine lineare Extrusion am linken Knoten mithilfe der Eigenschaft „Verdrehen“ und „Scheiben“ durch
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

Hier geschieht die Magie. Führen Sie eine lineare Extrusion am linken Knoten aus und integrieren Sie die Drehungseigenschaft, um den Grad der Drehung zu definieren. Passen Sie die Anzahl der Slices an, um feinere Details zu erhalten.

## Schritt 5: Führen Sie eine lineare Extrusion mit Drehung am rechten Knoten durch

```csharp
// Führen Sie eine lineare Extrusion am rechten Knoten mithilfe der Twist- und Slices-Eigenschaft durch
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

Spiegeln Sie den Prozess am rechten Knoten und experimentieren Sie mit verschiedenen Verdrehungswerten, um die Variationen in der Extrusion zu beobachten.

## Schritt 6: Speichern Sie die 3D-Szene

```csharp
// 3D-Szene speichern
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Speichern Sie abschließend Ihr 3D-Meisterwerk im gewünschten Ausgabeverzeichnis. Passen Sie den Dateinamen nach Ihren Wünschen an.

## Abschluss

In diesem Tutorial haben wir die faszinierende Welt der linearen Extrusion mit einem Twist mithilfe von Aspose.3D für .NET erkundet. Diese Funktion öffnet Türen zu kreativen Möglichkeiten und ermöglicht es Entwicklern, mühelos dynamische visuelle Elemente in ihre Anwendungen einzubauen.

## FAQs

### F1: Kann ich die lineare Extrusion mit Drehung auf andere Formen anwenden?

A1: Auf jeden Fall! Sie können mit verschiedenen Basisprofilen über Rechtecke hinaus experimentieren und so eine Vielzahl von Gestaltungsmöglichkeiten erschließen.

### F2: Welche Rolle spielt die Eigenschaft „Twist“ bei der linearen Extrusion?

A2: Die Eigenschaft „Twist“ bestimmt den Grad der Drehung während des Extrusionsprozesses und beeinflusst die endgültige 3D-Form.

### F3: Gibt es Leistungsaspekte bei der Verwendung einer großen Anzahl von Slices?

A3: Eine höhere Anzahl an Slices fügt zwar mehr Details hinzu, kann sich jedoch auf die Leistung auswirken. Finden Sie eine Balance basierend auf den Anforderungen Ihrer Anwendung.

### F4: Kann ich lineare Extrusion mit anderen Aspose.3D-Funktionen kombinieren?

A4: Auf jeden Fall! Aspose.3D bietet zahlreiche Funktionen. Für komplexere Designs können Sie Linear Extrusion gerne mit anderen Funktionen kombinieren.

### F5: Gibt es eine Community für Aspose.3D-Support und Diskussionen?

 A5: Ja, treten Sie der Aspose.3D-Community bei[Aspose-Forum](https://forum.aspose.com/c/3d/18) für die Unterstützung und die spannenden Diskussionen.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
