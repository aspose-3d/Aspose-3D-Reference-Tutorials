---
title: Extrahieren von Informationen zu Szenen-Assets
linktitle: Extrahieren von Informationen zu Szenen-Assets
second_title: Aspose.3D .NET API
description: Verbessern Sie Ihre 3D-Szenen mühelos mit Aspose.3D für .NET. Erfahren Sie Schritt für Schritt, wie Sie wertvolle Asset-Informationen hinzufügen. Laden Sie es jetzt herunter und genießen Sie ein dynamisches 3D-Erlebnis.
type: docs
weight: 10
url: /de/net/asset-information/information-to-scene/
---
## Einführung

Willkommen zu diesem umfassenden Tutorial zur Verwendung von Aspose.3D für .NET, um wertvolle Informationen zu extrahieren und Ihre 3D-Szenen zu verbessern. Aspose.3D ist eine leistungsstarke Bibliothek, die Entwicklern die nahtlose Bearbeitung von 3D-Szenen in .NET-Anwendungen ermöglicht. In diesem Tutorial konzentrieren wir uns auf die entscheidende Aufgabe, Asset-Informationen zu einer Szene hinzuzufügen.

## Voraussetzungen

Bevor wir uns mit dem Tutorial befassen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

-  Aspose.3D für .NET: Stellen Sie sicher, dass Sie die Bibliothek installiert haben. Sie können es hier herunterladen[Aspose.3D für .NET-Seite](https://releases.aspose.com/3d/net/).

## Namespaces importieren

Stellen Sie in Ihrem .NET-Projekt sicher, dass Sie die erforderlichen Namespaces für den Zugriff auf Aspose.3D-Funktionen einschließen:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Schritt 1: Initialisieren Sie eine 3D-Szene

```csharp
Scene scene = new Scene();
```

 Erstellen Sie eine neue 3D-Szene mit`Scene` Klasse.

## Schritt 2: Legen Sie Anwendungs- und Anbieterinformationen fest

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Definieren Sie die Anwendungs- und Anbieternamen, die Ihrer 3D-Szene zugeordnet sind.

## Schritt 3: Maßeinheiten definieren

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Geben Sie die in Ihrer Szene verwendeten Maßeinheiten an. In diesem Beispiel verwenden wir altägyptische Einheiten namens „Stange“, wobei eine Stange 60 cm entspricht.

## Schritt 4: Speichern Sie die Szene

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Speichern Sie die Szene mit den hinzugefügten Asset-Informationen in einem 3D-unterstützten Dateiformat. Passen Sie das Ausgabeverzeichnis nach Bedarf an.

## Schritt 5: Erfolgsmeldung anzeigen

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Informieren Sie den Benutzer darüber, dass die Asset-Informationen erfolgreich hinzugefügt wurden und die Datei gespeichert wird.

## Abschluss

Glückwunsch! Sie haben erfolgreich gelernt, wie Sie mit Aspose.3D für .NET wichtige Asset-Informationen extrahieren und zu Ihren 3D-Szenen hinzufügen. Dieses Wissen eröffnet endlose Möglichkeiten für die Erstellung informativerer und ansprechenderer 3D-Inhalte.

## FAQs

### F1: Kann ich Aspose.3D für .NET mit anderen Programmiersprachen verwenden?

A1: Aspose.3D unterstützt hauptsächlich .NET-Sprachen, Sie können jedoch Interoperabilitätsoptionen für andere Sprachen erkunden.

### F2: Gibt es eine kostenlose Testversion für Aspose.3D für .NET?

 A2: Ja, Sie können auf die kostenlose Testversion zugreifen[Hier](https://releases.aspose.com/).

### F3: Wie erhalte ich Unterstützung für Aspose.3D-bezogene Abfragen?

 A3: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für Gemeinschaft und Unterstützung.

### F4: Kann ich eine temporäre Lizenz für Aspose.3D für .NET erwerben?

 A4: Ja, Sie können eine temporäre Lizenz erwerben[Hier](https://purchase.aspose.com/temporary-license/).

### F5: Wo finde ich eine ausführliche Dokumentation für Aspose.3D für .NET?

 A5: Siehe[Dokumentation](https://reference.aspose.com/3d/net/) für ausführliche Informationen.