---
title: Knotenhierarchie verstehen
linktitle: Knotenhierarchie verstehen
second_title: Aspose.3D .NET API
description: Nutzen Sie die Leistungsfähigkeit von Aspose.3D für .NET! Tauchen Sie mit dieser Schritt-für-Schritt-Anleitung in die Manipulation der Knotenhierarchie ein. Erstellen Sie mühelos atemberaubende 3D-Szenen.
weight: 16
url: /de/net/geometry-and-hierarchy/node-hierarchy/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Knotenhierarchie verstehen

## Einführung

Willkommen in der Welt von Aspose.3D für .NET, einer leistungsstarken Bibliothek, die Entwicklern die nahtlose Arbeit mit 3D-Szenen und -Modellen in ihren .NET-Anwendungen ermöglicht. In diesem Tutorial werden wir uns mit den Feinheiten des Verständnisses der Knotenhierarchie in 3D-Szenen mithilfe von Aspose.3D befassen. Am Ende dieses Leitfadens verfügen Sie über ein solides Verständnis dafür, wie Sie die Struktur von 3D-Szenen über Knoten manipulieren und so atemberaubende visuelle Erlebnisse schaffen können.

## Voraussetzungen

Bevor wir uns auf diese 3D-Reise begeben, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

-  Aspose.3D für .NET-Bibliothek: Stellen Sie sicher, dass die Aspose.3D-Bibliothek in Ihr .NET-Projekt integriert ist. Wenn Sie dies noch nicht getan haben, gehen Sie zu[Dokumentation](https://reference.aspose.com/3d/net/) zur Führung.

-  Laden Sie die Bibliothek herunter: Wenn Sie die Aspose.3D-Bibliothek nicht heruntergeladen haben, holen Sie sich die neueste Version von[Download-Link](https://releases.aspose.com/3d/net/) und befolgen Sie die Installationsanweisungen in der Dokumentation.

-  Holen Sie sich eine Lizenz: Um das volle Potenzial von Aspose.3D auszuschöpfen, benötigen Sie eine gültige Lizenz. Wenn Sie keins haben, können Sie es erhalten[Hier](https://purchase.aspose.com/buy) oder entscheiden Sie sich für a[Kostenlose Testphase](https://releases.aspose.com/) um seine Fähigkeiten zu erkunden.

-  Support und Community: Treten Sie der Aspose.3D-Community auf der bei[Hilfeforum](https://forum.aspose.com/c/3d/18)um mit anderen Entwicklern in Kontakt zu treten, Hilfe zu suchen und über die neuesten Entwicklungen auf dem Laufenden zu bleiben.

-  Temporäre Lizenz (optional): Wenn Sie Aspose.3D erkunden, bevor Sie einen Kauf tätigen, sollten Sie den Erwerb einer vorläufigen Lizenz in Betracht ziehen[temporäre Lizenz](https://purchase.aspose.com/temporary-license/) für erweiterten Zugriff.

Nachdem wir nun unsere Tools bereit haben, tauchen wir ein in die aufregende Welt der Manipulation der 3D-Knotenhierarchie mit Aspose.3D.

## Namespaces importieren

Stellen Sie in Ihrem .NET-Projekt sicher, dass Sie die erforderlichen Namespaces importieren, um die von Aspose.3D bereitgestellten Funktionen nutzen zu können. Fügen Sie Ihrem Code die folgenden Zeilen hinzu:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Diese Namespaces ermöglichen Ihnen den Zugriff auf wichtige Klassen und Methoden für die Arbeit mit 3D-Szenen.

## Schritt 1: Szenenobjekt initialisieren

```csharp
Scene scene = new Scene();
```

 Beginnen Sie mit der Erstellung einer neuen 3D-Szene mit`Scene` Klasse.

## Schritt 2: Untergeordnete Knoten erstellen

```csharp
Node top = scene.RootNode.CreateChildNode();
Node cube1 = top.CreateChildNode("cube1");
Node cube2 = top.CreateChildNode("cube2");
```

 Richten Sie eine hierarchische Struktur ein, indem Sie Eltern-Kind-Beziehungen zwischen Knoten erstellen. In diesem Beispiel,`cube1` Und`cube2` sind untergeordnete Knoten der`top` Knoten.

## Schritt 3: Netz erstellen und zuweisen

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
cube1.Entity = mesh;
cube2.Entity = mesh;
```

 Erzeugen Sie ein Netz mit einer geeigneten Methode (hier:`CreateMeshUsingPolygonBuilder`) und weisen Sie es den untergeordneten Knoten zu.

## Schritt 4: Übersetzungen festlegen

```csharp
cube1.Transform.Translation = new Vector3(-10, 0, 0);
cube2.Transform.Translation = new Vector3(10, 0, 0);
```

Definieren Sie Übersetzungen für jeden Würfelknoten und positionieren Sie sie im 3D-Raum.

## Schritt 5: Wenden Sie die Drehung auf den übergeordneten Knoten an

```csharp
top.Transform.Rotation = Quaternion.FromEulerAngle(Math.PI, 4, 0);
```

Drehen Sie den übergeordneten Knoten (`top`) und beobachten Sie, wie sich diese Transformation auf alle untergeordneten Knoten auswirkt.

## Schritt 6: Speichern Sie die 3D-Szene

```csharp
string output = "Your Output Directory" + "NodeHierarchy.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Geben Sie das Ausgabeverzeichnis an und speichern Sie die 3D-Szene im gewünschten Dateiformat (hier FBX7500ASCII).

## Schritt 7: Erfolgsmeldung anzeigen

```csharp
Console.WriteLine("\nNode hierarchy added successfully to document.\nFile saved at " + output);
```

Informieren Sie den Benutzer über das erfolgreiche Hinzufügen der Knotenhierarchie und den Speicherort der gespeicherten Datei.

## Abschluss

Glückwunsch! Sie haben sich erfolgreich in der komplizierten Welt der 3D-Knotenhierarchie in Aspose.3D für .NET zurechtgefunden. Dieses Tutorial vermittelt Ihnen die Kenntnisse zum einfachen Erstellen, Bearbeiten und Speichern von 3D-Szenen. Entdecken Sie im weiteren Verlauf weitere Funktionen und entfesseln Sie das volle Potenzial von Aspose.3D in Ihren .NET-Projekten.

## FAQs

### F1: Kann ich Aspose.3D für .NET ohne Lizenz verwenden?

A1: Während eine Lizenz alle Funktionen freischaltet, können Sie Aspose.3D mit eingeschränkten Funktionen mithilfe der kostenlosen Testversion erkunden.

### F2: Gibt es andere unterstützte Dateiformate zum Speichern von 3D-Szenen?

A2: Ja, Aspose.3D unterstützt verschiedene Formate; Eine umfassende Liste finden Sie in der Dokumentation.

### F3: Wie kann ich zur Aspose.3D-Community beitragen?

A3: Treten Sie dem Support-Forum bei, teilen Sie Ihre Erfahrungen und tragen Sie bei, indem Sie anderen bei ihren Fragen helfen.

### F4: Ist Aspose.3D für die Spieleentwicklung geeignet?

A4: Auf jeden Fall! Aspose.3D ist vielseitig und kann in Spieleentwicklungsprojekte integriert werden.

### F5: Was ist der Unterschied zwischen einer temporären Lizenz und einer Volllizenz?

A5: Eine temporäre Lizenz bietet kurzfristigen Zugriff zu Testzwecken, während eine Volllizenz eine uneingeschränkte Nutzung ermöglicht.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
