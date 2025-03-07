---
title: Exportieren in das PLY-Format als Punktwolke
linktitle: Exportieren in das PLY-Format als Punktwolke
second_title: Aspose.3D .NET API
description: Entdecken Sie die Welt der 3D-Modellierung mit Aspose.3D für .NET. Erfahren Sie, wie Sie Modelle mühelos in das PLY-Format exportieren. Werten Sie Ihre Projekte mit atemberaubenden Bildern auf.
weight: 16
url: /de/net/loading-and-saving/ply/export-to-ply-point-cloud/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Exportieren in das PLY-Format als Punktwolke

## Einführung
In der dynamischen Welt der 3D-Modellierung und -Entwicklung sticht Aspose.3D für .NET als leistungsstarkes Toolkit hervor. Dieses Tutorial führt Sie durch den Prozess des Exportierens von 3D-Modellen in das PLY-Format als Punktwolke mit Aspose.3D für .NET. Wenn Sie bereit sind, Ihre Projekte mit atemberaubenden Bildern zu bereichern, folgen Sie uns und nutzen Sie das volle Potenzial dieser vielseitigen Bibliothek.
## Voraussetzungen
Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:
-  Aspose.3D für .NET: Laden Sie die Bibliothek herunter und installieren Sie sie[Download-Seite](https://releases.aspose.com/3d/net/).
- Entwicklungsumgebung: Richten Sie Ihre bevorzugte .NET-Entwicklungsumgebung ein, z. B. Visual Studio.
## Namespaces importieren
Um mit Aspose.3D für .NET zu beginnen, importieren Sie die erforderlichen Namespaces in Ihr Projekt:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Schritt 1: Erstellen Sie ein 3D-Modell
Beginnen Sie mit der Erstellung eines 3D-Modells, das Sie als Punktwolke exportieren möchten. Lassen Sie uns zum Beispiel eine Kugel erstellen:
```csharp
Sphere sphere = new Sphere();
```
## Schritt 2: Definieren Sie die Exporteinstellungen
Geben Sie die Exporteinstellungen an, einschließlich des Dateiformats (PLY), und aktivieren Sie den Punktwolkenexport:
```csharp
PlySaveOptions saveOptions = new PlySaveOptions() { PointCloud = true };
```
## Schritt 3: Legen Sie den Exportpfad fest
Bestimmen Sie das Verzeichnis, in dem Sie die exportierte PLY-Datei speichern möchten:
```csharp
string exportPath = "Your Document Directory" + "sphere.ply";
```
## Schritt 4: Kodieren und exportieren
 Nutzen Sie die`Encode` Methode zum Exportieren des 3D-Modells in das PLY-Format:
```csharp
FileFormat.PLY.Encode(sphere, exportPath, saveOptions);
```
## Abschluss
Glückwunsch! Sie haben mit Aspose.3D für .NET erfolgreich ein 3D-Modell als Punktwolke in das PLY-Format exportiert. Dies eröffnet endlose Möglichkeiten, immersive Visuals in Ihre Anwendungen zu integrieren.

## FAQs
### 1. Ist Aspose.3D mit allen .NET Frameworks kompatibel?
Aspose.3D unterstützt verschiedene .NET-Frameworks und gewährleistet so die Kompatibilität mit einer Vielzahl von Entwicklungsumgebungen.
### 2. Kann ich Aspose.3D für kommerzielle Projekte verwenden?
 Absolut! Aspose.3D bietet flexible Lizenzoptionen, einschließlich kommerzieller Nutzung. Besuche die[Kaufseite](https://purchase.aspose.com/buy) für Details.
### 3. Wie erhalte ich Unterstützung für Aspose.3D?
 Besuche den[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) um mit der Community in Kontakt zu treten und Unterstützung von Experten zu erhalten.
### 4. Gibt es eine kostenlose Testversion?
 Ja, erkunden Sie die Funktionen mit einem[Kostenlose Testphase](https://releases.aspose.com/) bevor Sie eine Verpflichtung eingehen.
### 5. Wie erhalte ich eine temporäre Lizenz?
 Informationen zu temporären Lizenzoptionen finden Sie unter[dieser Link](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
