---
title: Erstellen einer Szene mit eingebetteter Textur
linktitle: Erstellen einer Szene mit eingebetteter Textur
second_title: Aspose.3D .NET API
description: Erstellen Sie mit Aspose.3D für .NET faszinierende 3D-Szenen mit eingebetteten Texturen. Befolgen Sie unsere Schritt-für-Schritt-Anleitung für atemberaubende Ergebnisse.
type: docs
weight: 10
url: /de/net/materials/create-scene-embedded-texture/
---
## Einführung
Willkommen in der aufregenden Welt der 3D-Grafik mit Aspose.3D für .NET! In diesem umfassenden Tutorial führen wir Sie durch den Prozess der Erstellung beeindruckender 3D-Szenen mit eingebetteten Texturen mithilfe von Aspose.3D, einer leistungsstarken und vielseitigen Bibliothek für .NET-Entwickler.
## Voraussetzungen
Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:
- Ein grundlegendes Verständnis der C#- und .NET-Programmierung.
- Visual Studio ist auf Ihrem Computer installiert.
-  Aspose.3D für .NET-Bibliothek, die Sie herunterladen können[Hier](https://releases.aspose.com/3d/net/).
- Vertrautheit mit den Konzepten der 3D-Grafik und Szenenerstellung.
## Namespaces importieren
Beginnen Sie mit dem Importieren der erforderlichen Namespaces in Ihr Projekt. Diese Namespaces stellen Ihnen die Tools und Funktionalitäten zur Verfügung, die für die Bearbeitung von 3D-Grafiken erforderlich sind.
```csharp
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
```
## Schritt 1: Erstellen einer Szene
Beginnen Sie mit der Erstellung einer neuen 3D-Szene mit Aspose.3D für .NET. Dies dient als Leinwand für Ihr 3D-Meisterwerk.
```csharp
// Erstellen Sie eine FBX-Datei mit eingebetteten Texturen
Scene scene = new Scene();
```
## Schritt 2: Erstellen einer eingebetteten Textur
Jetzt verleihen wir Ihrer Szene etwas visuelles Flair, indem wir eine Textur einbetten. Wir erstellen eine Textur mit benutzerdefiniertem Inhalt und weisen ihr einen Dateinamen zu.
```csharp
// Erstellen Sie eine eingebettete Textur
Texture tex = new Texture()
{
    Content = CreateTextureContent(),
    // Der Dateiname ist erforderlich, wenn die eingebettete Textur verwendet wird.
    FileName = "test.png"
};
tex.SetProperty("TexProp", "value");
```
## Schritt 3: Erstellen eines Materials
Erstellen Sie als Nächstes ein Material für Ihre 3D-Objekte und integrieren Sie dabei die zuvor erstellte Textur und benutzerdefinierte Eigenschaften.
```csharp
// Erstellen Sie ein Material mit benutzerdefinierten Eigenschaften
LambertMaterial mat = new LambertMaterial("my-mat");
mat.SetTexture(Material.MapDiffuse, tex);
mat.SetProperty("MyProp", 1.0);
```
## Schritt 4: Erstellen eines 3D-Objekts
Jetzt erwecken wir Ihre Szene zum Leben, indem wir ein 3D-Objekt hinzufügen. In diesem Beispiel verwenden wir einen Torus und wenden das gerade erstellte Material an.
```csharp
// Erstellen Sie einen Torus, indem Sie das zuvor erstellte Material anwenden
scene.RootNode.CreateChildNode(new Torus()).Material = mat;
```
## Schritt 5: Speichern der Szene
Speichern Sie abschließend Ihr Meisterwerk in einer Datei. In diesem Beispiel speichern wir es im FBX-Format.
```csharp
// Speichern Sie die Szene in einer Datei
scene.Save(RunExamples.GetOutputFilePath(@"test.fbx"), FileFormat.FBX7500ASCII);
```
Glückwunsch! Sie haben mit Aspose.3D für .NET erfolgreich eine 3D-Szene mit eingebetteten Texturen erstellt.
## CreateTextureContent-Quellcode
```csharp
        private static byte[] CreateTextureContent()
        {
            using (var bitmap = new Bitmap(256, 256))
            {
                using (var g = Graphics.FromImage(bitmap))
                {
                    g.Clear(Color.White);
                    LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, 128, 128), Color.Moccasin,
                        Color.ForestGreen, 45);
                    using (var font = new Font(FontFamily.GenericSerif, 40))
                    {
                        g.DrawString("Aspose.3D", font, brush, Point.Empty);
                    }
                }
                using (var ms = new MemoryStream())
                {
                    bitmap.Save(ms, ImageFormat.Png);
                    return ms.ToArray();
                }
            }
        }
```
## Abschluss
In diesem Tutorial haben wir die Grundlagen der Erstellung visuell beeindruckender 3D-Szenen mit eingebetteten Texturen mit Aspose.3D für .NET erkundet. Mit diesem Wissen können Sie Ihrer Kreativität freien Lauf lassen und faszinierende 3D-Anwendungen erstellen.

## Häufig gestellte Fragen

### F: Kann ich Aspose.3D für .NET mit anderen Programmiersprachen verwenden?
A: Aspose.3D ist in erster Linie für .NET konzipiert, es stehen jedoch ähnliche Bibliotheken für andere Sprachen zur Verfügung.
### F: Wie kann ich Animationen auf meine 3D-Szenen anwenden?
A: Aspose.3D bietet Animationsfunktionen; Ausführliche Anweisungen finden Sie in der Dokumentation.
### F: Gibt es eine Testversion für Aspose.3D für .NET?
 A: Ja, Sie können die Testversion herunterladen[Hier](https://releases.aspose.com/).
### F: Wo finde ich zusätzliche Unterstützung und Ressourcen?
 A: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für Community-Unterstützung und Diskussionen.
### F: Kann ich Aspose.3D für kommerzielle Projekte verwenden?
 A: Ja, Sie können eine Lizenz erwerben[Hier](https://purchase.aspose.com/buy).