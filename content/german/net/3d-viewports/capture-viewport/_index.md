---
title: Erfassen von Ansichtsfenstern in 3D-Szenen
linktitle: Erfassen von Ansichtsfenstern in 3D-Szenen
second_title: Aspose.3D .NET API
description: Erfahren Sie, wie Sie mit Aspose.3D für .NET atemberaubende 3D-Ansichtsfenster erfassen. Schritt-für-Schritt-Anleitung zum flexiblen Rendern von Szenen.
type: docs
weight: 11
url: /de/net/3d-viewports/capture-viewport/
---
## Einführung

Im Bereich der 3D-Grafik und -Visualisierung ist die Erfassung von Ansichtsfenstern eine wesentliche Fähigkeit, die die Tiefe und Detailgenauigkeit Ihrer Szenen verbessert. Aspose.3D für .NET bietet eine robuste Lösung zum Rendern und Bearbeiten von 3D-Szenen. Dieses Tutorial führt Sie durch den Prozess der Erfassung von Ansichtsfenstern in 3D-Szenen mit Aspose.3D, sodass Sie ganz einfach beeindruckende Visualisierungen erstellen können.

## Voraussetzungen

Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

-  Aspose.3D für .NET-Bibliothek: Stellen Sie sicher, dass Sie die Aspose.3D-Bibliothek installiert haben. Sie können es herunterladen unter[Hier](https://releases.aspose.com/3d/net/).

## Namespaces importieren

Importieren Sie zunächst die erforderlichen Namespaces in Ihr .NET-Projekt:

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

Laden Sie zunächst eine vorhandene 3D-Szene in Ihr Projekt. Der folgende Codeausschnitt demonstriert dies:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## Schritt 2: Erstellen Sie eine Kamera

Erstellen Sie als Nächstes eine Instanz der Kamera und legen Sie deren Position und Ziel fest:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## Schritt 3: Fügen Sie der Szene Beleuchtung hinzu

Verschönern Sie Ihre Szene, indem Sie eine Lichtquelle hinzufügen. Der folgende Codeausschnitt zeigt, wie man ein Punktlicht erstellt:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Schritt 4: Renderer und Renderziel konfigurieren

Richten Sie den Renderer ein und erstellen Sie ein Renderziel für die Aufnahme der Szene:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (Fortsetzung in den nächsten Schritten)
    }
}
```

## Schritt 5: Ansichtsfenster definieren und rendern

Definieren Sie Ansichtsfenster und rendern Sie die Szene, um Ausgabebilder zu generieren:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Schritt 6: Ansichtsfenster ändern und erneut rendern

Ändern Sie Ansichtsfenster und rendern Sie die Szene noch einmal, um die Flexibilität von Aspose.3D zu demonstrieren:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

Experimentieren Sie weiter mit verschiedenen Konfigurationen, um die gewünschten visuellen Effekte zu erzielen.

## Abschluss

In diesem Tutorial haben wir den Prozess der Erfassung von Ansichtsfenstern in 3D-Szenen mit Aspose.3D für .NET untersucht. Mithilfe seiner leistungsstarken Funktionen können Sie Ihre 3D-Grafikprojekte auf ein neues Niveau heben und fesselnde visuelle Erlebnisse bieten.

## FAQs

### F1: Ist Aspose.3D mit anderen 3D-Dateiformaten kompatibel?

A1: Ja, Aspose.3D unterstützt verschiedene 3D-Dateiformate und gewährleistet so die Kompatibilität mit einer Vielzahl von Designtools.

### F2: Kann ich Aspose.3D für die Spieleentwicklung verwenden?

A2: Während Aspose.3D in erster Linie für Grafiken und Visualisierung konzipiert ist, können seine Funktionalitäten bestimmte Aspekte der Spieleentwicklung ergänzen.

### F3: Wo finde ich zusätzliche Beispiele und Dokumentation?

 A3: Entdecken Sie das Umfassende[Aspose.3D-Dokumentation](https://reference.aspose.com/3d/net/) Weitere Beispiele und detaillierte Informationen finden Sie hier.

### F4: Gibt es eine kostenlose Testversion?

 A4: Ja, Sie können auf eine kostenlose Testversion zugreifen[Hier](https://releases.aspose.com/).

### F5: Wie kann ich Hilfe suchen oder mich an der Community beteiligen?

 A5: Treten Sie der Aspose.3D-Community bei[Hilfeforum](https://forum.aspose.com/c/3d/18) für Hilfe und Zusammenarbeit.