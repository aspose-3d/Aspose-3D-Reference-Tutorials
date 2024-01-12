---
title: Rendern der Szene in Cubemap mit sechs Gesichtern
linktitle: Rendern der Szene in Cubemap mit sechs Gesichtern
second_title: Aspose.3D .NET API
description: Erstellen Sie atemberaubende Cubemaps mit Aspose.3D für .NET. Folgen Sie unserer Schritt-für-Schritt-Anleitung zum Rendern von 3D-Szenen in faszinierende Würfelkarten mit sechs Gesichtern.
type: docs
weight: 14
url: /de/net/rendering/render-scene-cubemap/
---
## Einführung
Willkommen bei dieser Schritt-für-Schritt-Anleitung zum Rendern einer Szene in eine Cubemap mit sechs Flächen mit Aspose.3D für .NET. In diesem Tutorial führen wir Sie durch den Prozess der Erstellung einer beeindruckenden Cubemap durch Rendern einer 3D-Szene. Aspose.3D ist eine leistungsstarke .NET-API, die die Bearbeitung von 3D-Grafiken vereinfacht. Mit diesem Leitfaden nutzen Sie ihre Funktionen, um faszinierende Cubemaps zu erstellen.
## Voraussetzungen
Bevor wir uns mit dem Tutorial befassen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:
- Grundkenntnisse in der C#- und .NET-Entwicklung.
- Aspose.3D für .NET installiert. Sie können es herunterladen[Hier](https://releases.aspose.com/3d/net/).
- Eine 3D-Szenendatei im GLB-Format (z. B. „VirtualCity.glb“) zum Rendern.
## Namespaces importieren
Importieren Sie zunächst die erforderlichen Namespaces für Aspose.3D in Ihren C#-Code:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## Schritt 1: Laden Sie die Szene
Laden Sie die 3D-Szenendatei mit dem folgenden Code:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Schritt 2: Kamera und Lichter erstellen
Erstellen Sie eine Kamera und zwei Lichter, um die Szene zu beleuchten:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## Schritt 3: Renderer und Renderziel erstellen
Erstellen Sie einen Renderer und ein Cube-Map-Renderziel mit Tiefentextur:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Schritt 4: Cubemap-Gesichter speichern
Speichern Sie jede Fläche der Cubemap mit den angegebenen Dateinamen auf der Festplatte:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## Abschluss
Glückwunsch! Sie haben mit Aspose.3D für .NET erfolgreich eine 3D-Szene in eine Cubemap gerendert. Entdecken Sie weitere Anpassungsoptionen und verbessern Sie Ihre 3D-Grafikprojekte mit dieser leistungsstarken API.
## Häufig gestellte Fragen
### F: Kann ich Aspose.3D für .NET mit anderen 3D-Dateiformaten verwenden?
Ja, Aspose.3D unterstützt verschiedene 3D-Dateiformate und bietet so Flexibilität bei Ihren Projekten.
### F: Wie kann ich Unterstützung für Aspose.3D erhalten?
 Besuche den[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für Community-Unterstützung und Diskussionen.
### F: Gibt es eine kostenlose Testversion?
 Ja, Sie können auf die kostenlose Testversion zugreifen[Hier](https://releases.aspose.com/).
### F: Kann ich mit Aspose.3D Szenen mit Animationen rendern?
Absolut! Aspose.3D unterstützt das Rendern animierter 3D-Szenen.
### F: Wo finde ich eine ausführliche Dokumentation?
 Siehe die[Aspose.3D-Dokumentation](https://reference.aspose.com/3d/net/) für ausführliche Informationen.