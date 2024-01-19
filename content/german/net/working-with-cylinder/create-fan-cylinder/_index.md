---
title: Lüfterzylinder erstellen
linktitle: Lüfterzylinder erstellen
second_title: Aspose.3D .NET API
description: Entdecken Sie die Welt des 3D-Designs mit Aspose.3D für .NET! Erstellen Sie mühelos atemberaubende Lüfter- und Nichtlüfterzylinder. Laden Sie jetzt Ihre Testversion herunter.
type: docs
weight: 10
url: /de/net/working-with-cylinder/create-fan-cylinder/
---
## Einführung
Willkommen in der Welt der 3D-Modellierung und Visualisierung mit Aspose.3D für .NET! In dieser Schritt-für-Schritt-Anleitung erfahren Sie, wie Sie mit Aspose.3D für .NET einen faszinierenden Lüfterzylinder erstellen. Aspose.3D ist eine leistungsstarke Bibliothek, die umfassende Funktionen für die Arbeit mit 3D-Inhalten in .NET-Anwendungen bietet.
## Voraussetzungen
Bevor wir in die spannende Welt der 3D-Modellierung eintauchen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:
- Ein grundlegendes Verständnis der .NET-Programmierung.
- Visual Studio ist auf Ihrem Computer installiert.
-  Aspose.3D für .NET-Bibliothek, die Sie herunterladen können[Hier](https://releases.aspose.com/3d/net/).
- Ein echtes Interesse daran, Ihrer Kreativität durch 3D-Design freien Lauf zu lassen.
## Namespaces importieren
Beginnen wir mit dem Importieren der erforderlichen Namespaces, um die Aspose.3D-Funktionalität in Ihrem .NET-Projekt verfügbar zu machen.
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Importieren Sie Aspose.3D-Namespaces
```
Nachdem wir nun alle Vorbereitungen getroffen haben, unterteilen wir den Prozess der Erstellung eines Lüfterzylinders in überschaubare Schritte.
## Schritt 1: Erstellen Sie eine Szene
```csharp
// Erstellen Sie eine Szene
Scene scene = new Scene();
```
Beginnen Sie mit der Initialisierung einer neuen 3D-Szene. Dies dient als Leinwand, auf der unser Lüfterzylinder zum Leben erweckt wird.
## Schritt 2: Erstellen Sie einen Lüfterzylinder
```csharp
// Erstellen Sie einen Zylinder
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
Definieren Sie die Eigenschaften Ihres Lüfterzylinders und geben Sie Parameter wie Radius, Höhe und Auflösung an.
## Schritt 3: Passen Sie die Eigenschaften des Lüfterzylinders an
```csharp
// Setzen Sie GenerateFanCylinder auf true
fan.GenerateFanCylinder = true;
// Legen Sie ThetaLength fest
fan.ThetaLength = MathUtils.ToRadian(270);
```
Passen Sie Ihren Lüfterzylinder an, indem Sie die Generierung des Lüfterteils aktivieren und den Winkeldurchlauf mit ThetaLength anpassen.
## Schritt 4: Positionieren Sie den Lüfterzylinder in der Szene
```csharp
// Erstellen Sie einen ChildNode
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
Fügen Sie den Lüfterzylinder als untergeordneten Knoten zum Wurzelknoten der Szene hinzu und positionieren Sie ihn im 3D-Raum.
## Schritt 5: Erstellen Sie einen Zylinder ohne Lüfter
```csharp
// Erstellen Sie einen Zylinder ohne Lüfter
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
Entdecken Sie die Flexibilität von Aspose.3D, indem Sie einen Zylinder ohne Lüfterteil erstellen.
## Schritt 6: Passen Sie die Eigenschaften des Zylinders ohne Lüfter an
```csharp
// Setzen Sie GenerateFanCylinder auf „false“.
nonfan.GenerateFanCylinder = false;
// Legen Sie ThetaLength fest
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
Unterscheiden Sie den Zylinder ohne Lüfter, indem Sie die Erzeugung des Lüfterteils deaktivieren.
## Schritt 7: Positionieren Sie den Zylinder ohne Lüfter in der Szene
```csharp
// Erstellen Sie einen ChildNode
scene.RootNode.CreateChildNode(nonfan);
```
Fügen Sie auf ähnliche Weise den Nicht-Lüfter-Zylinder als untergeordneten Knoten zum Wurzelknoten der Szene hinzu.
## Schritt 8: Speichern Sie die Szene
```csharp
// Szene speichern
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
Speichern Sie Ihr Meisterwerk im gewünschten Format und Ort. Jetzt haben Sie mit Aspose.3D für .NET erfolgreich einen Lüfter- und einen Nicht-Lüfterzylinder erstellt!
## Abschluss
Herzlichen Glückwunsch zum Abschluss dieser praktischen Anleitung zur 3D-Modellierung mit Aspose.3D für .NET! Sie haben Ihrer Kreativität im digitalen Bereich freien Lauf gelassen und mit Leichtigkeit Lüfter- und Nicht-Lüfterzylinder hergestellt.
## Häufig gestellte Fragen
### Kann ich Aspose.3D für .NET mit anderen .NET-Frameworks verwenden?
Ja, Aspose.3D ist mit verschiedenen .NET-Frameworks kompatibel und bietet so Vielseitigkeit in Ihren Entwicklungsprojekten.
### Gibt es eine kostenlose Testversion für Aspose.3D für .NET?
 Ja, Sie können eine kostenlose Testversion ausprobieren[Hier](https://releases.aspose.com/).
### Wo finde ich eine ausführliche Dokumentation zu Aspose.3D für .NET?
 Die Dokumentation ist verfügbar[Hier](https://reference.aspose.com/3d/net/).
### Wie erhalte ich Unterstützung für Aspose.3D für .NET?
 Besuchen Sie das Support-Forum[Hier](https://forum.aspose.com/c/3d/18)für die Unterstützung durch die Community und Aspose-Experten.
### Sind temporäre Lizenzen für Aspose.3D für .NET verfügbar?
 Ja, temporäre Lizenzen können erworben werden[Hier](https://purchase.aspose.com/temporary-license/).