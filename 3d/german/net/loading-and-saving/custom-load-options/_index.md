---
title: Benutzerdefinierte Ladeoptionen
linktitle: Benutzerdefinierte Ladeoptionen
second_title: Aspose.3D .NET API
description: Entdecken Sie Aspose.3D für .NET, die ultimative Lösung für das nahtlose Laden und Speichern von 3D-Modellen.
type: docs
weight: 15
url: /de/net/loading-and-saving/custom-load-options/
---
## Einführung

Willkommen in der Welt von Aspose.3D für .NET – einer leistungsstarken Bibliothek, die Entwicklern die nahtlose Arbeit mit 3D-Dateien ermöglicht. In diesem Tutorial befassen wir uns mit den Feinheiten des Ladens und Speicherns von 3D-Modellen und konzentrieren uns dabei auf benutzerdefinierte Ladeoptionen. Egal, ob Sie ein erfahrener Entwickler oder ein Neuling sind, dieser Leitfaden führt Sie Schritt für Schritt durch den Prozess und stellt sicher, dass Sie das volle Potenzial von Aspose.3D für .NET nutzen.

## Voraussetzungen

Bevor wir uns auf diese Reise begeben, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

-  Aspose.3D für .NET: Stellen Sie sicher, dass Sie die Bibliothek installiert haben. Sie können es herunterladen[Hier](https://releases.aspose.com/3d/net/).

- Dokumentverzeichnis: Erstellen Sie ein Verzeichnis zum Speichern Ihrer 3D-Modelldateien.

Nachdem Sie nun das Wesentliche kennen, tauchen wir ein in die aufregende Welt der 3D-Modellmanipulation!

## Namespaces importieren

Als Erstes importieren wir die erforderlichen Namespaces. Dies wird die Bühne für unsere Reise in den Aspose.3D-Bereich bereiten.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Laden und Speichern – Benutzerdefinierte Ladeoptionen

### Schritt 1: Laden von Discreet3DS-Dateien

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Legen Sie benutzerdefinierte Optionen fest
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Laden Sie die Datei mit den Ladeoptionen
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### Schritt 2: Laden von OBJ-Dateien

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Legen Sie benutzerdefinierte Optionen fest
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Laden Sie die Datei mit den Ladeoptionen
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### Schritt 3: STL-Dateien laden

```csharp
private static void STLLoadOption()
{
    // Der Pfad zum Dokumentenverzeichnis.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Legen Sie benutzerdefinierte Optionen fest
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Laden Sie die Datei mit den Ladeoptionen
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### Schritt 4: U3D-Dateien laden

```csharp
private static void U3DLoadOption()
{
    // Der Pfad zum Dokumentenverzeichnis.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Legen Sie benutzerdefinierte Optionen fest
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Laden Sie die Datei mit den Ladeoptionen
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### Schritt 5: Laden von glTF-Dateien

```csharp
private static void glTFLoadOptions()
{
    // Der Pfad zum Dokumentenverzeichnis.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Legen Sie benutzerdefinierte Optionen fest
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### Schritt 6: PLY-Dateien laden

```csharp
private static void PlyLoadOptions()
{
    // Der Pfad zum Dokumentenverzeichnis.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Legen Sie benutzerdefinierte Optionen fest
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### Schritt 7: FBX-Dateien laden

```csharp
private static void FBXLoadOptions()
{
    // Der Pfad zum Dokumentenverzeichnis.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Legen Sie benutzerdefinierte Optionen fest
    scene.Open("test.FBX", opt);

    // Ausgabeeigenschaften, die in GlobalSettings in der FBX-Datei definiert sind
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Abschluss

Glückwunsch! Sie haben sich erfolgreich durch die komplizierte Welt des Ladens und Speicherns von 3D-Modellen mit Aspose.3D für .NET navigiert. In diesem Tutorial wurden verschiedene Dateiformate und ihre benutzerdefinierten Ladeoptionen behandelt, sodass Sie 3D-Assets problemlos bearbeiten können.

## FAQs

### F1: Ist Aspose.3D für .NET für Anfänger geeignet?

A1: Auf jeden Fall! Aspose.3D für .NET bietet eine benutzerfreundliche Oberfläche und macht es für Entwickler aller Erfahrungsstufen zugänglich.

### F2: Kann ich Aspose.3D für kommerzielle Projekte verwenden?

A2: Ja, Aspose.3D für .NET wird mit einer kommerziellen Lizenz geliefert, sodass Sie es in Ihren Projekten verwenden können.

### F3: Gibt es Einschränkungen hinsichtlich der unterstützten Dateiformate?

 A3: Aspose.3D für .NET unterstützt eine Vielzahl beliebter 3D-Dateiformate, darunter OBJ, STL, FBX und mehr. Siehe die[Dokumentation](https://reference.aspose.com/3d/net/) für eine umfassende Liste.

### F4: Gibt es eine Testversion?

A4: Ja, Sie können die Funktionen von Aspose.3D für .NET erkunden, indem Sie das herunterladen[Kostenlose Testphase](https://releases.aspose.com/).

### F5: Wo kann ich Unterstützung für Aspose.3D für .NET suchen?

 A5: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für die Unterstützung und Unterstützung der Gemeinschaft.