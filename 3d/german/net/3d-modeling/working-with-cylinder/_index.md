---
title: Maßgeschneiderter Scherbodenzylinder
linktitle: Maßgeschneiderter Scherbodenzylinder
second_title: Aspose.3D .NET API
description: Erfahren Sie mit unserer detaillierten Schritt-für-Schritt-Anleitung, wie Sie mit Aspose.3D für .NET maßgeschneiderte Scherbodenzylinder erstellen. Verbessern Sie noch heute Ihre 3D-Modellierungsfähigkeiten!
weight: 12
url: /de/net/3d-modeling/working-with-cylinder/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Maßgeschneiderter Scherbodenzylinder

## Einführung
Willkommen zu unserem umfassenden Leitfaden zum Erstellen eines benutzerdefinierten Zylinders mit Aspose.3D für .NET. Wenn Sie Ihre 3D-Modellierungsfähigkeiten verbessern und Ihren Projekten einzigartige Funktionen hinzufügen möchten, sind Sie hier richtig. In diesem Tutorial führen wir Sie mit klaren Erklärungen und Codeausschnitten Schritt für Schritt durch den Prozess.
## Voraussetzungen
Bevor wir uns mit dem Tutorial befassen, stellen Sie sicher, dass Sie über Folgendes verfügen:
- Grundlegendes Verständnis der C#- und .NET-Programmierung.
-  Aspose.3D für .NET-Bibliothek installiert. Sie können es herunterladen[Hier](https://releases.aspose.com/3d/net/).
- Eine für die .NET-Programmierung eingerichtete Entwicklungsumgebung.
## Namespaces importieren
Beginnen Sie in Ihrem C#-Code mit dem Importieren der erforderlichen Namespaces:
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
Beginnen Sie mit der Erstellung einer 3D-Szene mit Aspose.3D:
```csharp
Scene scene = new Scene();
```
## Schritt 2: Zylinder 1 erstellen
Erzeugen Sie den ersten Zylinder und legen Sie seine Eigenschaften fest:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Schritt 3: Scherboden für Zylinder 1 anpassen
Bringen Sie einen maßgeschneiderten Scherboden am ersten Zylinder an:
```csharp
//Scherung 47,5 Grad in der xy-Ebene (z-Achse)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Setzen Sie GenerateFanCylinder auf true
cylinder1.GenerateFanCylinder = true;
// Legen Sie ThetaLength fest
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// OffsetTop festlegen
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
## Schritt 4: Zylinder 1 zur Szene hinzufügen
Fügen Sie der Szene den ersten Zylinder hinzu und legen Sie seine Übersetzung fest:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Schritt 5: Zylinder 2 erstellen
Erzeugen Sie einen zweiten Zylinder mit ähnlichen Eigenschaften:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Schritt 6: Zylinder 2 zur Szene hinzufügen
Fügen Sie der Szene den zweiten Zylinder ohne benutzerdefinierte Parameter hinzu:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Schritt 7: Speichern Sie die Szene
Speichern Sie die Szene als Wavefront-OBJ-Datei in Ihrem Dokumentverzeichnis:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Abschluss
Glückwunsch! Sie haben mit Aspose.3D für .NET erfolgreich einen benutzerdefinierten Scherbodenzylinder erstellt. Dieses Tutorial soll eine Schritt-für-Schritt-Anleitung für Benutzer mit unterschiedlichem Fachwissen in der 3D-Modellierung und -Programmierung bieten.
## Häufig gestellte Fragen
### Ist Aspose.3D für .NET für Einsteiger geeignet?
Absolut! Aspose.3D für .NET bietet eine benutzerfreundliche Oberfläche, die es sowohl für Anfänger als auch für erfahrene Entwickler zugänglich macht.
### Kann ich Zylinder mit unterschiedlichen Scherwinkeln versehen?
Ja, Sie können den Scherboden für jeden Zylinder individuell anpassen und so einzigartige Effekte erzielen.
### Gibt es eine Testversion?
 Ja, Sie können die kostenlose Testversion ausprobieren[Hier](https://releases.aspose.com/).
### Wo finde ich zusätzliche Unterstützung?
 Besuche den[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für Community-Unterstützung und Diskussionen.
### Wie kann ich eine temporäre Lizenz erhalten?
 Holen Sie sich Ihre temporäre Lizenz[Hier](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
