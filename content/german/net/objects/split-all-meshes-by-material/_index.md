---
title: Aufteilen aller Szenennetze nach Material
linktitle: Aufteilen aller Szenennetze nach Material
second_title: Aspose.3D .NET API
description: Erfahren Sie, wie Sie mit Aspose.3D für .NET 3D-Netze nach Material aufteilen. Befolgen Sie unsere Schritt-für-Schritt-Anleitung für die effiziente Organisation und Verwaltung von 3D-Modellen.
type: docs
weight: 21
url: /de/net/objects/split-all-meshes-by-material/
---
## Einführung
Willkommen bei dieser Schritt-für-Schritt-Anleitung zum Aufteilen aller Netze einer 3D-Szene nach Material mit Aspose.3D für .NET. Wenn Sie mit 3D-Modellen arbeiten und Ihre Netze basierend auf Materialien effizient organisieren möchten, ist dieses Tutorial genau das Richtige für Sie. Aspose.3D ist eine leistungsstarke .NET-Bibliothek, die eine Reihe von Funktionen für die Arbeit mit 3D-Dateien bietet und somit eine ausgezeichnete Wahl für Entwickler ist.
## Voraussetzungen
Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:
- Grundlegendes Verständnis der Programmiersprache C#.
- Visual Studio ist auf Ihrem Computer installiert.
-  Aspose.3D für .NET-Bibliothek. Sie können es herunterladen unter[Hier](https://releases.aspose.com/3d/net/).
- Eine 3D-Eingabedatei (z. B. „test.fbx“), die Sie teilen möchten.
## Namespaces importieren
Beginnen Sie mit dem Importieren der erforderlichen Namespaces in Ihr C#-Projekt:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Schritt 1: Laden Sie die 3D-Datei
```csharp
// Der Pfad zum Dokumentenverzeichnis.
string input = RunExamples.GetDataFilePath("test.fbx");
// Laden Sie eine 3D-Datei
Scene scene = new Scene(input);
```
 In diesem Schritt laden wir die 3D-Datei mit Aspose.3Ds`Scene` Klasse.
## Schritt 2: Alle Netze teilen
```csharp
// Teilen Sie alle Netze auf
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
 Hier verwenden wir die`SplitMesh` Methode aus der`PolygonModifier`Klasse, um alle Netze basierend auf dem Material aufzuteilen.
## Schritt 3: Speichern Sie die geteilte Szene
```csharp
// Datei speichern
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
Speichern Sie die geänderte Szene in einer neuen Datei, um die Änderungen beizubehalten.
## Schritt 4: Erfolgsmeldung anzeigen
```csharp
// Erfolgsmeldung anzeigen
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
Drucken Sie eine Erfolgsmeldung, die angibt, dass der Vorgang erfolgreich abgeschlossen wurde.
## Abschluss
Glückwunsch! Sie haben erfolgreich gelernt, wie Sie mit Aspose.3D für .NET alle Netze einer 3D-Szene nach Material aufteilen. Dies kann eine wertvolle Technik zum Organisieren und Verwalten komplexer 3D-Modelle sein.
## FAQs
### 1. Kann ich Aspose.3D für .NET mit anderen Programmiersprachen verwenden?
Aspose.3D ist in erster Linie für .NET konzipiert, bietet jedoch durch .NET-Sprachbindungen Interoperabilität mit anderen Sprachen.
### 2. Gibt es eine Testversion?
 Ja, Sie können auf die kostenlose Testversion zugreifen[Hier](https://releases.aspose.com/).
### 3. Wo finde ich weitere Beispiele und Dokumentation?
 Entdecken Sie die umfassende Dokumentation unter[Aspose.3D-Dokumentation](https://reference.aspose.com/3d/net/).
### 4. Wie erhalte ich Unterstützung für Aspose.3D?
 Besuche den[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für Community-Unterstützung und Diskussionen.
### 5. Kann ich eine temporäre Lizenz erhalten?
 Ja, Sie können eine temporäre Lizenz erhalten[Hier](https://purchase.aspose.com/temporary-license/).