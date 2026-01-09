---
date: 2026-01-09
description: Erfahren Sie, wie Sie mit Aspose.3D für .NET eine 3D‑Szene erstellen,
  einschließlich des Exports von Wavefront‑OBJ und wie man den Versatz bei linearer
  Extrusion verdreht.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Wie man eine 3D‑Szene mit Drehversatz bei linearer Extrusion erstellt
url: /de/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D‑Szene erstellen: Twist‑Versatz bei linearer Extrusion

## Einführung

Wenn Sie **3D‑Szene erstellen** Objekte schnell erzeugen und dynamische Geometrie hinzufügen möchten, bietet Aspose.3D für .NET genau die Werkzeuge, die Sie benötigen. In diesem **Aspose 3D Tutorial** gehen wir die *wie man Twist‑Versatz anwendet* Technik durch, während wir eine **linear extrusion twist** durchführen und schließlich **Wavefront OBJ** Dateien exportieren. Am Ende haben Sie ein voll ausgestattetes 3‑D‑Modell, das bereit für das Rendern oder die Weiterverarbeitung ist.

## Schnellantworten
- **Was bewirkt “twist offset”?** Es verschiebt den Startpunkt der Drehung entlang der Extrusionsachse.  
- **Welche Methode exportiert Wavefront OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Benötige ich eine Lizenz, um das Beispiel auszuführen?** Eine temporäre Lizenz funktioniert für Tests; für die Produktion ist eine Voll‑Lizenz erforderlich.  
- **Welche .NET‑Versionen werden unterstützt?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Wie viele Slices werden für glatte Drehungen empfohlen?** Etwa 100 Slices bieten ein gutes Gleichgewicht zwischen Qualität und Leistung.

## Was bedeutet **3D‑Szene erstellen**?

Eine 3‑D‑Szene zu erstellen bedeutet, eine hierarchische Struktur aufzubauen, die Geometrie, Lichter, Kameras und Transformationen enthält. Aspose.3D stellt die Klasse `Scene` bereit, die als Wurzel‑Container für alle hinzugefügten Knoten dient.

## Warum **linear extrusion twist** verwenden?

Eine lineare Extrusion mit Drehung ermöglicht es, ein 2‑D‑Profil in ein spiralförmiges 3‑D‑Objekt zu verwandeln – ideal für Schrauben, Federn oder dekorative Säulen. Durch Hinzufügen eines Twist‑Versatzes erhalten Sie noch mehr Kontrolle über den Start der Rotation, was asymmetrische Designs ermöglicht.

## Voraussetzungen

Bevor wir beginnen, stellen Sie sicher, dass Sie Folgendes haben:

- Aspose.3D für .NET Bibliothek: Laden Sie die Bibliothek von der [release page](https://releases.aspose.com/3d/net/) herunter und installieren Sie sie.  
- Ihre Entwicklungsumgebung: Visual Studio 2022 (oder jede C#‑IDE), bereit für .NET‑Entwicklung.

## Namespaces importieren

Importieren Sie zunächst die erforderlichen Namespaces, um auf die Aspose.3D‑Funktionalität zuzugreifen.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Schritt‑für‑Schritt‑Anleitung

### Schritt 1: Basisprofil initialisieren  

Wir verwenden ein Rechteck mit einem kleinen Abrundungsradius als Profil, das extrudiert wird.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Schritt 2: Szene erstellen  

Dies ist der Container, in dem wir **3D‑Szene**‑Knoten erstellen.

```csharp
Scene scene = new Scene();
```

### Schritt 3: Knoten erstellen  

Zwei Geschwisterknoten werden zur Wurzel hinzugefügt – einer für die reguläre Extrusion und einer für die Versatz‑Version.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### Schritt 4: Lineare Extrusion am linken Knoten (einfache Drehung)  

Hier demonstrieren wir eine klassische **linear extrusion twist** ohne jeglichen Versatz.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Schritt 5: Lineare Extrusion am rechten Knoten mit **Twist Offset**  

Jetzt wenden wir die *wie man Twist‑Versatz anwendet* Technik an, indem wir einen `TwistOffset`‑Vektor bereitstellen.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### Schritt 6: **Export Wavefront OBJ**  

Speichern Sie schließlich die zusammengestellte Szene in einer OBJ‑Datei, sodass Sie sie in jedem gängigen 3‑D‑Viewer ansehen können.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Häufige Probleme & Tipps

- **Drehung wirkt flach?** Erhöhen Sie den `Slices`‑Wert für glattere Geometrie.  
- **Versatz nicht sichtbar?** Stellen Sie sicher, dass der `TwistOffset`‑Vektor von Null verschieden ist und mit der Extrusionsrichtung übereinstimmt.  
- **OBJ‑Datei fehlt Texturen?** OBJ speichert nur Geometrie; verwenden Sie MTL‑Dateien für Materialdefinitionen, falls nötig.

## Häufig gestellte Fragen

**Q: Kann ich Aspose.3D für .NET mit anderen Programmiersprachen verwenden?**  
A: Aspose.3D richtet sich hauptsächlich an .NET‑Sprachen, aber gleichwertige Bibliotheken existieren für Java und andere Plattformen.

**Q: Wie erhalte ich eine temporäre Lizenz für Aspose.3D für .NET?**  
A: Besuchen Sie [this link](https://purchase.aspose.com/temporary-license/), um eine temporäre Lizenz für Testzwecke zu erhalten.

**Q: Gibt es ein Community‑Forum für Aspose.3D für .NET?**  
A: Absolut! Treten Sie der Community unter [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) bei, um sich mit anderen Entwicklern auszutauschen und Unterstützung zu erhalten.

**Q: Gibt es zusätzliche Beispiele und Dokumentation?**  
A: Erkunden Sie die [documentation](https://reference.aspose.com/3d/net/) für umfangreiche Anleitungen und Beispiele.

**Q: Wo kann ich Aspose.3D für .NET kaufen?**  
A: Gehen Sie zu [this link](https://purchase.aspose.com/buy), um einen Kauf zu tätigen und das volle Potenzial von Aspose.3D freizuschalten.

## Fazit

In diesem **aspose 3d tutorial** haben Sie gelernt, wie man **3D‑Szene erstellt**, eine **linear extrusion twist** anwendet, den **twist offset** steuert und **Wavefront OBJ** Dateien exportiert. Diese Techniken ermöglichen es Ihnen, anspruchsvolle, verdrehte Geometrie zu jedem 3‑D‑Projekt mit nur wenigen Codezeilen hinzuzufügen.

---

**Last Updated:** 2026-01-09  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}