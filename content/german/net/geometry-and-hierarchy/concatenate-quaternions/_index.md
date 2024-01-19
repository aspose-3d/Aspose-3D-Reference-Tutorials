---
title: Verketten von Quaternionen in 3D-Szenen
linktitle: Verketten von Quaternionen in 3D-Szenen
second_title: Aspose.3D .NET API
description: Entdecken Sie die Leistungsfähigkeit der Quaternion-Manipulation in 3D-Szenen mit Aspose.3D für .NET. Lernen Sie Schritt für Schritt, Quaternionen für immersive Transformationen zu verketten.
type: docs
weight: 11
url: /de/net/geometry-and-hierarchy/concatenate-quaternions/
---
## Einführung

Willkommen zu diesem umfassenden Tutorial zum Verketten von Quaternionen in 3D-Szenen mit Aspose.3D für .NET! Wenn Sie Entwickler oder 3D-Enthusiast sind und Ihre Fähigkeiten in der Quaternion-Manipulation verbessern möchten, sind Sie hier richtig. Dieses Tutorial führt Sie Schritt für Schritt durch den Prozess und sorgt für ein reibungsloses Lernerlebnis.

## Voraussetzungen

Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

-  Aspose.3D für .NET-Bibliothek: Laden Sie die Bibliothek von herunter und installieren Sie sie[Aspose-Website](https://releases.aspose.com/3d/net/).
- Entwicklungsumgebung: Stellen Sie sicher, dass Sie über eine funktionierende Entwicklungsumgebung für .NET verfügen.

## Namespaces importieren

Fügen Sie in Ihr .NET-Projekt die erforderlichen Namespaces ein, um die Leistungsfähigkeit von Aspose.3D zu nutzen:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
```

## Schritt 1: Erstellen Sie eine Szene

Beginnen Sie mit der Erstellung einer 3D-Szene mithilfe der Aspose.3D-Bibliothek. Die Szene dient als Leinwand für die Quaternion-Manipulation.

```csharp
Scene scene = new Scene();
```

## Schritt 2: Quaternionen definieren

 Definieren Sie drei Quaternionen,`q1`, `q2` , Und`q3`, die jeweils eine bestimmte Drehung darstellen.

```csharp
Quaternion q1 = Quaternion.FromEulerAngle(Math.PI * 0.5, 0, 0);
Quaternion q2 = Quaternion.FromAngleAxis(-Math.PI * 0.5, Vector3.XAxis);
Quaternion q3 = q1.Concat(q2);
```

## Schritt 3: Zylinder erstellen

Erstellen Sie drei Zylinder, die jeweils ein Quaternion darstellen. Legen Sie die Rotations- und Translationseigenschaften basierend auf den definierten Quaternionen fest.

```csharp
Node cylinder = scene.RootNode.CreateChildNode("cylinder-q1", new Cylinder(0.1, 1, 2));
cylinder.Transform.Rotation = q1;
cylinder.Transform.Translation = new Vector3(-5, 2, 0);

// Wiederholen Sie dies für q2 und q3
```

## Schritt 4: In Datei speichern

Speichern Sie die Szene in einer Datei und geben Sie dabei das Ausgabeformat und den Dateinamen an.

```csharp
var output = "Your Output Directory" + "test_out.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```

## Schritt 5: Erfolgsmeldung anzeigen

Drucken Sie eine Erfolgsmeldung zusammen mit dem Dateipfad, sobald die Quaternionen verkettet und die Datei gespeichert ist.

```csharp
Console.WriteLine("\nQuaternions concatenated successfully.\nFile saved at " + output);
```

## Abschluss

Glückwunsch! Sie haben erfolgreich gelernt, wie Sie mit Aspose.3D für .NET Quaternionen in 3D-Szenen verketten. Experimentieren Sie mit verschiedenen Quaternion-Kombinationen, um in Ihren Projekten einzigartige Transformationen zu erzielen.

## FAQs

### F1: Was sind Quaternionen in 3D-Grafiken?

A1: Quaternionen sind mathematische Einheiten, die zur Darstellung von Rotationen im 3D-Raum verwendet werden und Vorteile gegenüber anderen Rotationsdarstellungen bieten.

### F2: Kann ich Aspose.3D für .NET mit anderen .NET-Bibliotheken verwenden?

A2: Ja, Aspose.3D für .NET ist so konzipiert, dass es nahtlos mit anderen .NET-Bibliotheken zusammenarbeitet.

### F3: Gibt es eine kostenlose Testversion für Aspose.3D für .NET?

 A3: Ja, Sie können auf eine kostenlose Testversion zugreifen[Hier](https://releases.aspose.com/).

### F4: Wie erhalte ich Unterstützung für Aspose.3D für .NET?

 A4: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für Community-Unterstützung und Diskussionen.

### F5: Kann ich eine temporäre Lizenz für Aspose.3D für .NET verwenden?

 A5: Ja, Sie können eine temporäre Lizenz erhalten[Hier](https://purchase.aspose.com/temporary-license/).