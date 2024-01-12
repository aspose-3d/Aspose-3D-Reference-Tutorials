---
title: Verdrehungsversatz in der linearen Extrusion
linktitle: Verdrehungsversatz in der linearen Extrusion
second_title: Aspose.3D .NET API
description: Entdecken Sie die Magie von Aspose.3D für .NET mit unserer Schritt-für-Schritt-Anleitung zum Twist Offset in der linearen Extrusion. Werten Sie Ihre 3D-Projekte mühelos auf.
type: docs
weight: 15
url: /de/net/linear-extrusion/twist-offset-in-linear-extrusion/
---
## Einführung

Willkommen in der Welt von Aspose.3D für .NET, einer vielseitigen Bibliothek, die Entwicklern die einfache Handhabung von 3D-Manipulationen ermöglicht. In diesem Tutorial befassen wir uns mit einer der faszinierenden Funktionen – dem „Twist Offset in Linear Extrusion“. Wenn Sie bereit sind, Ihre 3D-Programmierkenntnisse zu verbessern, können Sie gleich loslegen!

## Voraussetzungen

Bevor wir uns auf diese spannende Reise begeben, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

-  Aspose.3D für .NET-Bibliothek: Laden Sie die Bibliothek von herunter und installieren Sie sie[Release-Seite](https://releases.aspose.com/3d/net/).

- Ihre Entwicklungsumgebung: Stellen Sie sicher, dass Ihre Entwicklungsumgebung eingerichtet und einsatzbereit ist.

## Namespaces importieren

Beginnen Sie mit dem Importieren der erforderlichen Namespaces, um auf die von Aspose.3D für .NET bereitgestellten Funktionen zuzugreifen. In Ihrem Code könnte dies so aussehen:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Lassen Sie uns das Beispiel nun in überschaubare Schritte unterteilen, um den Verdrehungsversatz in der linearen Extrusion zu meistern:

## Schritt 1: Initialisieren Sie das Basisprofil

Beginnen Sie mit der Erstellung eines Basisprofils, hier am Beispiel einer Rechteckform mit einem bestimmten Rundungsradius.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Schritt 2: Erstellen Sie eine Szene

Generieren Sie eine 3D-Szene, um Ihre Knoten und Formen zu hosten.

```csharp
Scene scene = new Scene();
```

## Schritt 3: Knoten erstellen

Konstruieren Sie Knoten innerhalb der Szene, sowohl links als auch rechts.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## Schritt 4: Lineare Extrusion am linken Knoten

Führen Sie eine lineare Extrusion am linken Knoten mithilfe der Eigenschaft „Twist and Slices“ durch.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Schritt 5: Lineare Extrusion am rechten Knoten mit Verdrehungsversatz

Führen Sie auf dem rechten Knoten eine lineare Extrusion mit der Eigenschaft „Drehung“, „Drehungsversatz“ und „Slices“ durch.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## Schritt 6: 3D-Szene speichern

Speichern Sie die 3D-Szene im gewünschten Ausgabeverzeichnis und geben Sie als Dateiformat WavefrontOBJ an.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Glückwunsch! Sie haben den Verdrehungsversatz in der linearen Extrusion mit Aspose.3D für .NET erfolgreich implementiert.

## Abschluss

In diesem Tutorial haben wir die leistungsstarken Funktionen von Aspose.3D für .NET untersucht und uns dabei insbesondere auf den Verdrehungsversatz bei der linearen Extrusion konzentriert. Mit diesen neu erworbenen Fähigkeiten sind Sie bestens gerüstet, um Ihren 3D-Projekten Dynamik zu verleihen.

## FAQs

### F1: Kann ich Aspose.3D für .NET mit anderen Programmiersprachen verwenden?

A1: Aspose.3D unterstützt hauptsächlich .NET-Sprachen, Aspose bietet jedoch ähnliche Bibliotheken für Java und andere Plattformen.

### F2: Wie erhalte ich eine temporäre Lizenz für Aspose.3D für .NET?

 A2: Besuchen[dieser Link](https://purchase.aspose.com/temporary-license/) eine temporäre Lizenz zu Testzwecken zu erwerben.

### F3: Gibt es ein Community-Forum für Aspose.3D für .NET?

 A3: Auf jeden Fall! Treten Sie der Community bei[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) mit anderen Entwicklern in Kontakt zu treten und Unterstützung zu suchen.

### F4: Sind zusätzliche Beispiele und Dokumentation verfügbar?

 A4: Entdecken Sie die[Dokumentation](https://reference.aspose.com/3d/net/) für ausführliche Anleitungen und Beispiele.

### F5: Wo kann ich Aspose.3D für .NET kaufen?

 A5: Gehen Sie zu[dieser Link](https://purchase.aspose.com/buy) um einen Kauf zu tätigen und das volle Potenzial von Aspose.3D auszuschöpfen.