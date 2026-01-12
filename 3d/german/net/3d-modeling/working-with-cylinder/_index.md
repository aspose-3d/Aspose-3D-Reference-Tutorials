---
date: 2026-01-12
description: Erfahren Sie, wie Sie einen Shear‑Bottom‑Zylinder erstellen und ein 3D‑Modell
  im OBJ‑Format mit Aspose.3D für .NET exportieren. Folgen Sie dieser Schritt‑für‑Schritt‑Anleitung,
  um die 3D‑Modellierung zu meistern.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Wie man einen Schrägboden‑Zylinder mit Aspose.3D für .NET erstellt
url: /de/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Benutzerdefinierter Scherzboden‑Zylinder

## Einführung
Willkommen zu unserem umfassenden Leitfaden, in dem **Sie lernen, wie man Scherzboden‑Zylinder**‑Modelle mit Aspose.3D für .NET erstellt. Egal, ob Sie ein Spiel‑Asset, ein mechanisches Bauteil oder eine visuelle Demo bauen, dieses Tutorial zeigt Ihnen genau, wie Sie den Boden eines Zylinders formen, eine Scherung anwenden und schließlich **die 3D‑Modell‑OBJ**‑Datei für die Verwendung in jeder nachgelagerten Pipeline exportieren. Lassen Sie uns gemeinsam jeden Schritt durchgehen, damit Sie in wenigen Minuten benutzerdefinierte Geometrie erzeugen können.

## Schnellantworten
- **Was ist ein Scherzboden‑Zylinder?** Ein Zylinder, dessen Bodenfläche schräg (gescheret) statt flach ist.  
- **Welche Bibliothek wird verwendet?** Aspose.3D für .NET.  
- **Wie exportiere ich das Modell?** Verwenden Sie `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Benötige ich eine Lizenz?** Eine Testversion ist verfügbar; für die Produktion ist eine kommerzielle Lizenz erforderlich.  
- **Welche Voraussetzungen gibt es?** .NET‑Entwicklungsumgebung und das Aspose.3D‑NuGet‑Paket.

## Was ist ein Scherzboden‑Zylinder?
Ein Scherzboden‑Zylinder ist ein standardmäßiges zylindrisches Mesh, dessen Bodenfläche durch eine Scheroperation transformiert wurde. Damit können Sie geneigte Basen, Rampen oder benutzerdefinierte Anschlüsse erstellen, ohne die Vertices manuell zu bearbeiten.

## Warum Aspose.3D für diese Aufgabe verwenden?
- **Vollständige Kontrolle** über Geometrie‑Parameter (Radius, Höhe, Segmente).  
- **Integrierte Scher‑Unterstützung** über die `ShearBottom`‑Eigenschaft, sodass Sie auf Low‑Level‑Mesh‑Manipulationen verzichten können.  
- **Ein‑Klick‑Export** in gängige Formate wie OBJ, FBX und STL, wodurch die Integration in andere Werkzeuge nahtlos funktioniert.

## Voraussetzungen
Bevor wir starten, stellen Sie sicher, dass Sie folgendes haben:

- Grundkenntnisse in C# und .NET.  
- Aspose.3D für .NET installiert. Sie können es **[hier](https://releases.aspose.com/3d/net/)** herunterladen.  
- Eine .NET‑kompatible IDE (Visual Studio, Rider oder VS Code).

## Namespaces importieren
Importieren Sie in Ihrer C#‑Datei die notwendigen Namespaces:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Schritt 1: Szene erstellen
Instanziieren Sie zunächst eine neue 3‑D‑Szene, die alle unsere Objekte aufnehmen wird.

```csharp
Scene scene = new Scene();
```

## Schritt 2: Zylinder 1 erstellen
Erzeugen Sie den primären Zylinder, den wir mit einem geschereten Boden anpassen werden.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Schritt 3: Scherzboden für Zylinder 1 anpassen
Wenden Sie die Scherung an, aktivieren Sie die Fan‑Generierung und passen Sie weitere Eigenschaften an, um die gewünschte Form zu erreichen.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Schritt 4: Zylinder 1 zur Szene hinzufügen
Platzieren Sie den angepassten Zylinder in der Szene und verschieben Sie ihn leicht nach rechts, damit wir beide Objekte nebeneinander sehen können.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Schritt 5: Zylinder 2 erstellen
Erzeugen Sie einen zweiten, einfachen Zylinder zum Vergleich.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Schritt 6: Zylinder 2 zur Szene hinzufügen
Fügen Sie den zweiten Zylinder ohne benutzerdefinierte Scherung hinzu – das veranschaulicht den Effekt der vorherigen Schritte.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Schritt 7: Szene speichern
Exportieren Sie schließlich die gesamte Szene als OBJ‑Datei, damit Sie sie in Blender, Maya oder einem anderen 3‑D‑Viewer öffnen können.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Häufige Probleme & Tipps
- **Scherwerte**: Der `Vector2` nimmt X‑ und Y‑Scherfaktoren entgegen. Ein Wert von `0.83` entspricht etwa 47,5°, Sie können ihn jedoch für andere Winkel anpassen.  
- **Exportpfad**: Stellen Sie sicher, dass der angegebene Ordner existiert und Sie Schreibrechte besitzen; andernfalls wirft `scene.Save` eine Ausnahme.  
- **Performance**: Bei sehr hochsegmentierten Zylindern sollten Sie die Segmentzahl (`20` im Beispiel) reduzieren, um die OBJ‑Dateigröße handhabbar zu halten.

## Häufig gestellte Fragen

### Ist Aspose.3D für .NET für Anfänger geeignet?
Absolut! Aspose.3D für .NET bietet eine benutzerfreundliche API und ist sowohl für Einsteiger als auch für erfahrene Entwickler leicht zugänglich.

### Kann ich unterschiedliche Scherwinkel für Zylinder anwenden?
Ja, Sie können das `ShearBottom` für jeden Zylinder individuell anpassen und so einzigartige Effekte erzielen.

### Gibt es eine Testversion?
Ja, die kostenlose Testversion finden Sie **[hier](https://releases.aspose.com/)**.

### Wo finde ich zusätzlichen Support?
Besuchen Sie das **[Aspose.3D‑Forum](https://forum.aspose.com/c/3d/18)** für Community‑Support und Diskussionen.

### Wie kann ich eine temporäre Lizenz erhalten?
Holen Sie sich Ihre temporäre Lizenz **[hier](https://purchase.aspose.com/temporary-license/)**.

**Zusätzliche Fragen & Antworten**

**F: Wie ändere ich das Exportformat zu FBX?**  
A: Ersetzen Sie `FileFormat.WavefrontOBJ` durch `FileFormat.FBX` im Aufruf von `scene.Save`.

**F: Kann ich den Zylinder nach dem Export animieren?**  
A: OBJ unterstützt keine Animation; verwenden Sie FBX oder GLTF, wenn Sie animierte Daten benötigen.

**F: Was, wenn ich einen größeren Zylinderradius brauche?**  
A: Passen Sie die ersten beiden Parameter des `Cylinder`‑Konstruktors an (z. B. `new Cylinder(4, 4, …)`).

## Fazit
Sie haben nun gelernt, **wie man Scherzboden‑Zylinder**‑Modelle erstellt und sie als OBJ‑Dateien mit Aspose.3D für .NET exportiert. Experimentieren Sie mit verschiedenen Scherwerten, Segmentzahlen und Exportformaten, um die Anforderungen Ihres Projekts zu erfüllen. Viel Spaß beim Modellieren!

---

**Zuletzt aktualisiert:** 2026-01-12  
**Getestet mit:** Aspose.3D für .NET 24.11 (zum Zeitpunkt der Erstellung)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}