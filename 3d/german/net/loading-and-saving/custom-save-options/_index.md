---
title: Benutzerdefinierte Speicheroptionen
linktitle: Benutzerdefinierte Speicheroptionen
second_title: Aspose.3D .NET API
description: Entdecken Sie die Leistungsfähigkeit von Aspose.3D für .NET. Erfahren Sie, wie Sie Ihre 3D-Szenenspeicherung mit Schritt-für-Schritt-Anleitungen zu den Formaten Collada, USD, 3DS, FBX, OBJ, STL, U3D, glTF, DRC und RVM anpassen.
type: docs
weight: 21
url: /de/net/loading-and-saving/custom-save-options/
---
## Einführung

Willkommen in der Welt von Aspose.3D für .NET! Wenn Sie Ihre 3D-Entwicklungsfähigkeiten erweitern möchten, sind Sie hier richtig. In diesem Tutorial befassen wir uns mit den Lade- und Speicherfunktionen und konzentrieren uns dabei insbesondere auf benutzerdefinierte Speicheroptionen. Aspose.3D für .NET ist eine leistungsstarke Bibliothek, die Entwicklern die effiziente Bearbeitung und Speicherung von 3D-Szenen ermöglicht.

## Voraussetzungen

Bevor wir mit der Erkundung der aufregenden Funktionen von Aspose.3D beginnen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

- Grundlegendes Verständnis der C#- und .NET-Entwicklung.
-  Aspose.3D für .NET-Bibliothek installiert. Sie können es hier herunterladen[Release-Seite](https://releases.aspose.com/3d/net/).
- Eine mit Visual Studio oder einer anderen bevorzugten C#-IDE eingerichtete Entwicklungsumgebung.

## Namespaces importieren

Importieren wir zunächst die erforderlichen Namespaces:

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

Nachdem wir nun die Voraussetzungen geschaffen haben, unterteilen wir das Tutorial in mehrere Schritte.

## Schritt 1: Collada-Speicheroption

Beginnen wir mit Collada, einem beliebten 3D-Dateiformat. Befolgen Sie diese Schritte, um die Collada-Speicheroptionen anzupassen:

### 1. Verzeichnis einrichten:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Collada-Speicheroptionen initialisieren:
   ```csharp
   ColladaSaveOptions saveColladaOpts = new ColladaSaveOptions();
   ```

### 3. Optionen konfigurieren:
   ```csharp
   saveColladaOpts.Indented = true;
   saveColladaOpts.TransformStyle = ColladaTransformStyle.Matrix;
   saveColladaOpts.LookupPaths = new List<string>(new string[] { dataDir });
   ```

## Schritt 2: Diskrete 3DS-Speicheroption

Lassen Sie uns nun Discreet 3DS und seine Anpassungsoptionen erkunden:

### 1. Verzeichnis einrichten:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. 3DS-Speicheroptionen initialisieren:
   ```csharp
   Discreet3dsSaveOptions saveOpts = new Discreet3dsSaveOptions();
   ```

### 3. Optionen konfigurieren:
   ```csharp
   saveOpts.DuplicatedNameCounterBase = 2;
   // Zusätzliche Konfigurationsmöglichkeiten...
   ```

Setzen Sie diesen Schritt-für-Schritt-Ansatz für die Speicheroptionen FBX, OBJ, STL, U3D, glTF und DRC fort und passen Sie sie jeweils an Ihre Anforderungen an.

## Schritt 3: glTF-Speicheroptionen

Konzentrieren wir uns nun auf glTF, ein Format, das in Web- und Mobilanwendungen weit verbreitet ist. Passen Sie Ihre glTF-Speicheroptionen mit diesen Schritten an:

### 1. Szenenobjekt initialisieren:
   ```csharp
   Scene scene = new Scene();
   scene.RootNode.CreateChildNode("sphere", new Sphere());
   ```

### 2. Legen Sie die glTF-Speicheroptionen fest:
   ```csharp
   GltfSaveOptions opt = new GltfSaveOptions(FileContentType.ASCII);
   opt.EmbedAssets = true;
   opt.UseCommonMaterials = true;
   opt.BufferFile = "mybuf.bin";
   ```

### 3. glTF-Datei speichern:
   ```csharp
   scene.Save("Your Output Directory" + "glTFSaveOptions_out.gltf", opt);
   ```

Folgen Sie einer ähnlichen Struktur für andere Speicheroptionen wie DRC und RVM.

## Abschluss

Glückwunsch! Sie haben die benutzerdefinierten Speicheroptionen in Aspose.3D für .NET erfolgreich untersucht. Diese leistungsstarke Bibliothek bietet eine Vielzahl von Optionen zur individuellen Gestaltung Ihres 3D-Szenenspeicherprozesses.

## FAQs

### F1: Kann ich Aspose.3D für .NET mit anderen .NET-Frameworks verwenden?

A1: Ja, Aspose.3D ist mit verschiedenen .NET-Frameworks kompatibel und sorgt so für Flexibilität in Ihrer Entwicklungsumgebung.

### F2: Gibt es Lizenzoptionen für Aspose.3D?

 A2: Ja, Sie können Lizenzierungsoptionen erkunden[Hier](https://purchase.aspose.com/buy).

### F3: Wo finde ich Unterstützung für Aspose.3D-bezogene Abfragen?

 A3: Sie können auf der Website Unterstützung suchen[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18).

### F4: Gibt es eine kostenlose Testversion?

 A4: Ja, Sie können auf eine kostenlose Testversion zugreifen[Hier](https://releases.aspose.com/).

### F5: Wie kann ich eine temporäre Lizenz für Aspose.3D erhalten?

 A5: Besorgen Sie sich eine temporäre Lizenz[Hier](https://purchase.aspose.com/temporary-license/).