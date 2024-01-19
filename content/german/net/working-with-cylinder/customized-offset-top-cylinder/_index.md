---
title: Maßgeschneiderter, oben versetzter Zylinder
linktitle: Maßgeschneiderter, oben versetzter Zylinder
second_title: Aspose.3D .NET API
description: Entdecken Sie die Wunder der 3D-Grafik mit Aspose.3D für .NET. Erfahren Sie, wie Sie mühelos individuelle Zylinder mit versetztem Oberteil herstellen. Steigern Sie jetzt Ihr Programmiererlebnis!
type: docs
weight: 11
url: /de/net/working-with-cylinder/customized-offset-top-cylinder/
---
## Einführung
Willkommen in der Welt der 3D-Grafikbearbeitung mit Aspose.3D für .NET! In diesem Tutorial führen wir Sie durch den Prozess der Erstellung eines benutzerdefinierten Zylinders mit versetztem Oberteil mithilfe von Aspose.3D, einer leistungsstarken Bibliothek für die Arbeit mit 3D-Szenen, Objekten und Formaten in .NET-Anwendungen.
## Voraussetzungen
Bevor wir uns mit dem Tutorial befassen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:
- Grundkenntnisse der Programmiersprache C#.
- Visual Studio ist auf Ihrem Computer installiert.
- Aspose.3D für .NET-Bibliothek heruntergeladen und in Ihrem Projekt referenziert.
Beginnen wir nun mit der Schritt-für-Schritt-Anleitung!
## Namespaces importieren
Stellen Sie zunächst sicher, dass Sie die erforderlichen Namespaces in Ihren C#-Code importieren:
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
## Schritt 1: Erstellen Sie eine Szene
```csharp
// Erstellen Sie eine Szene
Scene scene = new Scene();
```
Dadurch wird eine neue 3D-Szene mit Aspose.3D initialisiert.
## Schritt 2: Initialisieren Sie den Zylinder
```csharp
// Zylinder initialisieren
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
Hier erstellen wir einen Zylinder mit spezifischen Parametern wie Radius, Höhe und Scheiben.
## Schritt 3: Legen Sie OffsetTop für den ersten Zylinder fest
```csharp
// OffsetTop festlegen
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
Dadurch wird ein individueller Versatz oben für den ersten Zylinder festgelegt.
## Schritt 4: Erstellen Sie ChildNode für den ersten Zylinder
```csharp
// Erstellen Sie einen ChildNode
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
Wir fügen der Szene den ersten Zylinder als untergeordneten Knoten hinzu und passen seine Position an.
## Schritt 5: Initialisieren Sie den zweiten Zylinder
```csharp
//Zweiten Zylinder ohne angepasstes OffsetTop initialisieren
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
Ein zweiter Zylinder wird ohne angepasstes Offset-Oberteil initialisiert.
## Schritt 6: Erstellen Sie einen ChildNode für den zweiten Zylinder
```csharp
// Erstellen Sie einen ChildNode
scene.RootNode.CreateChildNode(cylinder2);
```
Wir fügen der Szene den zweiten Zylinder als untergeordneten Knoten hinzu.
## Schritt 7: Speichern Sie die Szene
```csharp
// Speichern
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
Dadurch wird die 3D-Szene, einschließlich des angepassten versetzten oberen Zylinders, im Wavefront OBJ-Format gespeichert.
Jetzt haben Sie mit Aspose.3D für .NET erfolgreich einen benutzerdefinierten Zylinder mit versetztem oberen Ende erstellt!
## Abschluss
In diesem Tutorial haben wir die Grundlagen der Arbeit mit Aspose.3D für .NET erkundet, um einen benutzerdefinierten Zylinder mit versetztem oberen Ende zu erstellen. Diese Bibliothek eröffnet endlose Möglichkeiten für die 3D-Grafikbearbeitung in Ihren .NET-Anwendungen.
## FAQs
### F: Wo finde ich die Dokumentation für Aspose.3D für .NET?
 A: Die Dokumentation ist verfügbar[Hier](https://reference.aspose.com/3d/net/).
### F: Wie kann ich Aspose.3D für .NET herunterladen?
 A: Sie können es herunterladen[Hier](https://releases.aspose.com/3d/net/).
### F: Gibt es eine kostenlose Testversion für Aspose.3D für .NET?
 A: Ja, Sie können eine kostenlose Testversion erhalten[Hier](https://releases.aspose.com/).
### F: Wo erhalte ich Unterstützung für Aspose.3D für .NET?
 A: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) zur Unterstützung.
### F: Kann ich eine temporäre Lizenz für Aspose.3D für .NET erhalten?
 A: Ja, Sie können eine temporäre Lizenz erhalten[Hier](https://purchase.aspose.com/temporary-license/).