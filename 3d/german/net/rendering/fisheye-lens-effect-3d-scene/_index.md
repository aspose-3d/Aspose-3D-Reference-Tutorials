---
title: Anwenden des Fisheye-Linseneffekts mit Aspose.3D für .NET
linktitle: Anwenden des Fischaugen-Linseneffekts auf eine 3D-Szene
second_title: Aspose.3D .NET API
description: Verbessern Sie Ihre 3D-Szenen mit Aspose.3D für .NET! Erfahren Sie Schritt für Schritt, wie Sie einen faszinierenden Fischaugen-Linseneffekt anwenden. Jetzt downloaden!
weight: 12
url: /de/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Anwenden des Fisheye-Linseneffekts mit Aspose.3D für .NET

## Einführung
Möchten Sie die visuelle Attraktivität Ihrer 3D-Szenen verbessern? Tauchen Sie mit Aspose.3D für .NET in die faszinierende Welt der Fischaugen-Linseneffekte ein. Dieses Tutorial führt Sie Schritt für Schritt durch die Anwendung eines Fischaugen-Linseneffekts auf Ihre 3D-Szenen, um ihnen eine einzigartige und faszinierende Perspektive zu verleihen.
## Voraussetzungen
Bevor wir beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:
-  Aspose.3D für .NET: Stellen Sie sicher, dass Sie die Aspose.3D-Bibliothek für .NET installiert haben. Wenn nicht, können Sie es herunterladen[Hier](https://releases.aspose.com/3d/net/).
-  Beispiel einer 3D-Szene: Wir werden mit einer Beispieldatei einer 3D-Szene (VirtualCity.glb) arbeiten. Sie können Ihre eigene Szene verwenden oder das Beispiel von herunterladen[Aspose.3D-Dokumentation](https://reference.aspose.com/3d/net/).
## Namespaces importieren
Fügen Sie in Ihr .NET-Projekt die erforderlichen Namespaces ein, um auf die Aspose.3D-Funktionen zuzugreifen. Fügen Sie am Anfang Ihres Codes die folgenden Namespaces hinzu:
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
## Schritt 1: Laden Sie die 3D-Szene
Laden Sie die 3D-Szenendatei mit dem folgenden Code in Ihr Projekt:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Schritt 2: Kamera und Beleuchtung einrichten
Erstellen Sie eine Kamera und Lichter, um die visuellen Aspekte Ihrer Szene zu verbessern. Passen Sie Parameter wie NearPlane, FarPlane und RotationMode nach Bedarf an:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## Schritt 3: Erstellen Sie Renderer und Renderziele
Richten Sie den Renderer ein und erstellen Sie Renderziele für Cube Map und 2D-Textur:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## Schritt 4: Wenden Sie den Fischaugen-Linseneffekt an
Führen Sie die Nachbearbeitung des Fischaugenlinseneffekts auf der gerenderten Würfelkarte aus:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## Abschluss
Glückwunsch! Sie haben mit Aspose.3D für .NET erfolgreich einen Fischaugen-Linseneffekt auf Ihre 3D-Szene angewendet. Experimentieren Sie mit verschiedenen Szenen und Parametern, um Ihrer Kreativität freien Lauf zu lassen.
## Häufig gestellte Fragen
### Kann ich den Fischaugeneffekt auf jede 3D-Szene anwenden?
Ja, Sie können den Fischaugeneffekt auf jede 3D-Szene anwenden. Stellen Sie sicher, dass die Szene richtig geladen und beleuchtet ist, um optimale Ergebnisse zu erzielen.
### Welche Bedeutung hat es, das Sichtfeld (fov) auf 360 Grad anzupassen?
Ein Sichtfeld von 360 Grad sorgt für eine vollständig sphärische Projektion und erzeugt einen atemberaubenden Fischaugeneffekt.
### Wie kann ich die Beleuchtung in meiner 3D-Szene anpassen?
Sie können die Eigenschaften der Lichter wie Position, Typ und Farbe anpassen, um die gewünschten Lichteffekte zu erzielen.
### Gibt es eine Grenze für die Größe der 3D-Szene, die verarbeitet werden kann?
Die Größe der 3D-Szene wird hauptsächlich durch die Systemressourcen begrenzt. Stellen Sie sicher, dass Ihre Hardware die Größe Ihrer Szene bewältigen kann.
### Kann ich für das Ergebnis des Fischaugeneffekts ein anderes Ausgabeformat anstelle von PNG verwenden?
Ja, Sie können den Code ändern, um die Ausgabe entsprechend Ihren Anforderungen in verschiedenen Bildformaten zu speichern.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
