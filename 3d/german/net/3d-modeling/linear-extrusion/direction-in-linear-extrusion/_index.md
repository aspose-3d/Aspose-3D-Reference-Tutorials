---
title: Richtung in der linearen Extrusion
linktitle: Richtung in der linearen Extrusion
second_title: Aspose.3D .NET API
description: Entdecken Sie die Welt der 3D-Modellierung mit Aspose.3D für .NET. Lernen Sie die Richtung der linearen Extrusion kennen, steigern Sie die Kreativität und erstellen Sie mühelos immersive Anwendungen.
weight: 11
url: /de/net/3d-modeling/linear-extrusion/direction-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Richtung in der linearen Extrusion

## Einführung

In der dynamischen Welt der Softwareentwicklung ist die Erstellung immersiver 3D-Modelle eine unverzichtbare Fähigkeit. Aspose.3D für .NET bietet Entwicklern eine Reihe robuster Tools, mit denen sie das Potenzial der 3D-Modellierung in ihren Anwendungen nutzen können. In diesem Tutorial tauchen wir in die faszinierende Welt der linearen Extrusion ein und erkunden die Nuancen der Funktion „Richtung bei linearer Extrusion“.

## Voraussetzungen

Bevor wir uns auf diese spannende Reise begeben, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

-  Aspose.3D für .NET: Laden Sie die Bibliothek herunter und installieren Sie sie[Aspose.3D .NET-Dokumentation](https://reference.aspose.com/3d/net/).

- Entwicklungsumgebung: Stellen Sie sicher, dass Sie eine funktionierende .NET-Entwicklungsumgebung eingerichtet haben.

## Namespaces importieren

Importieren Sie in Ihrem .NET-Projekt die erforderlichen Namespaces, um auf die Funktionalität von Aspose.3D zuzugreifen. Fügen Sie am Anfang Ihres Codes die folgenden Zeilen hinzu:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Schritt 1: Initialisieren Sie das Basisprofil

Beginnen Sie mit der Initialisierung des zu extrudierenden Basisprofils. In diesem Beispiel erstellen wir eine Rechteckform mit einem Rundungsradius von 0,3.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Schritt 2: Erstellen Sie eine 3D-Szene

Schaffen Sie die Grundlage für Ihr 3D-Meisterwerk, indem Sie eine Szene erstellen.

```csharp
Scene scene = new Scene();
```

## Schritt 3: Knoten erstellen

Generieren Sie Knoten innerhalb der Szene, um verschiedene Komponenten Ihrer 3D-Umgebung darzustellen.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## Schritt 4: Lineare Extrusion ohne Richtung

 Führen Sie mit dem eine lineare Extrusion am linken Knoten durch`Twist` Und`Slices` Eigenschaften.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Schritt 5: Lineare Extrusion mit Richtung

 Erweitern Sie die Extrusionsmöglichkeiten durch die Integration`Direction` Eigenschaft im rechten Knoten.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## Schritt 6: Speichern Sie die 3D-Szene

 Bewahren Sie Ihre Kreation, indem Sie die 3D-Szene speichern. Ersetzen`"Your Output Directory"` mit dem gewünschten Verzeichnis.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Glückwunsch! Sie haben die lineare Extrusion mit Aspose.3D für .NET erfolgreich implementiert und dabei sowohl den traditionellen als auch den gerichteten Ansatz untersucht.

## Abschluss

In diesem Tutorial haben wir uns mit Aspose.3D für .NET durch die faszinierende Welt der 3D-Modellierung bewegt. Die lineare Extrusion mit und ohne Richtung eröffnet Entwicklern, die visuell beeindruckende Anwendungen erstellen möchten, endlose Möglichkeiten. Mit Aspose.3D haben Sie die Leistungsfähigkeit der 3D-Modellierung immer zur Hand.

## FAQs

### F1: Wie kann ich eine temporäre Lizenz für Aspose.3D für .NET erhalten?

 A1: Besuchen[Stellen Sie eine temporäre Lizenz bereit](https://purchase.aspose.com/temporary-license/) um eine befristete Lizenz zu erhalten.

### F2: Wo finde ich Unterstützung für Aspose.3D?

 A2: Treten Sie dem bei[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) um Hilfe zu suchen und mit der Gemeinschaft in Kontakt zu treten.

### F3: Gibt es eine kostenlose Testversion?

 A3: Ja, entdecken Sie die Funktionen mit einer kostenlosen Testversion unter[Aspose.3D-Veröffentlichungen](https://releases.aspose.com/).

### F4: Wie kaufe ich Aspose.3D für .NET?

 A4: Navigieren Sie zu[Aspose-Kaufseite](https://purchase.aspose.com/buy) für Lizenzoptionen und Kaufdetails.

### F5: Wo finde ich eine ausführliche Dokumentation für Aspose.3D für .NET?

 A5: Sehen Sie sich die umfassende Übersicht an[Aspose.3D .NET-Dokumentation](https://reference.aspose.com/3d/net/) für ausführliche Informationen.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
