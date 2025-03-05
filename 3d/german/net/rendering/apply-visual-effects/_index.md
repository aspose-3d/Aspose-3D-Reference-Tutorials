---
title: Anwenden visueller Effekte in 3D-Ansichtsfenstern
linktitle: Anwenden visueller Effekte in 3D-Ansichtsfenstern
second_title: Aspose.3D .NET API
description: Entdecken Sie die Welt der 3D-Visualisierung mit Aspose.3D für .NET. Erfahren Sie anhand von Schritt-für-Schritt-Anleitungen, wie Sie fesselnde visuelle Effekte auf Ihre Szenen anwenden. Werten Sie Ihre Projekte mit Pixelierung, Graustufen, Kantenerkennung und Unschärfeeffekten auf.
type: docs
weight: 10
url: /de/net/rendering/apply-visual-effects/
---
## Einführung

Die Verbesserung der visuellen Attraktivität von 3D-Szenen ist ein entscheidender Aspekt bei der Schaffung immersiver Erlebnisse. Aspose.3D für .NET bietet leistungsstarke Tools zum Anwenden visueller Effekte auf 3D-Ansichtsfenster. In diesem Tutorial führen wir den Prozess der Anwendung verschiedener Effekte auf eine 3D-Szene durch, darunter Pixelierung, Graustufen, Kantenerkennung und Unschärfe.

## Voraussetzungen

Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass Sie über Folgendes verfügen:

- Grundkenntnisse in der C#- und .NET-Entwicklung.
-  Aspose.3D für .NET-Bibliothek installiert. Sie können es herunterladen unter[Hier](https://releases.aspose.com/3d/net/).
- Eine 3D-Szenendatei (z. B. „scene.obj“) zum Experimentieren.

## Namespaces importieren

Importieren Sie zunächst die erforderlichen Namespaces für Aspose.3D und andere Abhängigkeiten. Fügen Sie Ihrem Code die folgenden Zeilen hinzu:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## Schritt 1: Laden Sie eine vorhandene 3D-Szene

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 Laden Sie Ihre 3D-Szene mit`Scene` Klasse.

## Schritt 2: Erstellen Sie eine Kamera

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

Erstellen Sie eine Kamerainstanz und legen Sie deren Position und Ziel fest.

## Schritt 3: Fügen Sie der Szene Licht hinzu

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

Führen Sie Beleuchtung ein, um die visuellen Effekte zu verstärken.

## Schritt 4: Erstellen Sie einen Renderer und ein Renderziel

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // Konfigurieren Sie die Renderer-Einstellungen
    renderer.EnableShadows = false;

    // Erstellen Sie ein Renderziel
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // Ansichtsfenster konfigurieren
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // Rendern Sie die Szene in eine Textur
        renderer.Render(rt);

        // Speichern Sie die gerenderte Textur in einer Datei
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // Weiter mit Nachbearbeitungseffekten...
    }
}
```

Erstellen Sie einen Renderer und ein Renderziel, um die Szene aufzunehmen.

## Schritt 5: Nachbearbeitungseffekte anwenden

### Schritt 5.1 Pixelierungseffekt

```csharp
// Erstellen Sie einen Pixeleffekt
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

Wenden Sie den Pixelierungseffekt an und speichern Sie das Ergebnis.

### Schritt 5.2 Graustufeneffekt

```csharp
// Graustufeneffekt erstellen
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

Wenden Sie den Graustufeneffekt an und speichern Sie das Ergebnis.

### Schritt 5.3 Effekte kombinieren

```csharp
// Kombinieren Sie Graustufen- und Pixelierungseffekte
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

Kombinieren Sie mehrere Effekte für einzigartige Ergebnisse.

### Schritt 5.4 Kantenerkennungseffekt

```csharp
// Erstellen Sie einen Kantenerkennungseffekt
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

Wenden Sie den Kantenerkennungseffekt an und speichern Sie das Ergebnis.

### Schritt 5.5 Unschärfeeffekt

```csharp
// Erstellen Sie einen Unschärfeeffekt
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

Wenden Sie den Unschärfeeffekt an und speichern Sie das Ergebnis.

## Abschluss

Das Experimentieren mit visuellen Effekten in 3D-Ansichtsfenstern verleiht Ihren Szenen Tiefe und Kreativität. Aspose.3D für .NET vereinfacht diesen Prozess und bietet eine Reihe von Nachbearbeitungseffekten, um Ihre Projekte zu verbessern.

## FAQs

### F1: Kann ich mehrere Effekte gleichzeitig anwenden?

A1: Ja, Sie können verschiedene Nachbearbeitungseffekte kombinieren, um einzigartige und komplexe Ergebnisse zu erzielen.

### F2: Wie kann ich die Intensität visueller Effekte anpassen?

A2: Jeder Effekt verfügt möglicherweise über Parameter, die Sie anpassen können, um seine Intensität zu steuern. Spezifische Einzelheiten finden Sie in der Dokumentation.

### F3: Ist Aspose.3D für die Spieleentwicklung geeignet?

A3: Während Aspose.3D in erster Linie für die 3D-Modellierung und das Rendering konzipiert ist, kann es in bestimmten Aspekten der Spieleentwicklung verwendet werden.

### F4: Sind zusätzliche Nachbearbeitungseffekte verfügbar?

A4: Aspose.3D bietet eine Vielzahl integrierter Nachbearbeitungseffekte, und Sie können mithilfe der Bibliothek benutzerdefinierte Effekte erstellen.

### F5: Kann ich Aspose.3D für kommerzielle Projekte verwenden?

 A5: Ja, Sie können Aspose.3D für kommerzielle Zwecke nutzen. Siehe die[Kaufseite](https://purchase.aspose.com/buy) für Lizenzdetails.