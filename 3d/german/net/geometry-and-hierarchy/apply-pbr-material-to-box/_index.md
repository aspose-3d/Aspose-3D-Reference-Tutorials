---
date: 2026-01-17
description: Lernen Sie, wie Sie ein PBR‑Material auf eine Box mit Aspose.3D für .NET
  anwenden, ein PBR‑Material erstellen und STL‑ASCII‑Dateien mit physikalisch basierter
  Darstellung exportieren.
linktitle: Applying PBR Material to Box
second_title: Aspose.3D .NET API
title: Wie man PBR‑Material auf eine Box anwendet
url: /de/net/geometry-and-hierarchy/apply-pbr-material-to-box/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man PBR‑Material auf einen Würfel anwendet

## Einleitung

Willkommen in der faszinierenden Welt der 3D‑Grafik! In diesem Schritt‑für‑Schritt‑Leitfaden lernen Sie **wie man pbr**‑Material auf einen Würfel mit Aspose.3D für .NET anwendet. Wir führen Sie durch das Erstellen eines PBR‑Materials, das Hinzufügen zu einem Mesh und schließlich das **Exportieren von STL ASCII**, damit Sie das Modell in jedem nachgelagerten Workflow verwenden können. Egal, ob Sie einen Spiel‑Prototypen oder eine Produktvisualisierung erstellen, das Beherrschen dieses Workflows öffnet die Tür zu realistischem, physikalisch basierendem Rendering (PBR) in Ihren .NET‑Anwendungen.

## Schnelle Antworten
- **Was ist das Hauptziel?** Ein PBR‑Material auf einen Würfel anwenden und es als STL ASCII exportieren.  
- **Welche Bibliothek wird verwendet?** Aspose.3D für .NET (wie man Aspose verwendet).  
- **Benötige ich eine Lizenz?** Ja, für die Produktion ist eine temporäre oder vollständige Lizenz erforderlich.  
- **Unterstütztes Ausgabeformat?** STL ASCII (export stl ascii) und viele andere 3D‑Formate.  
- **Wie lange dauert es?** Etwa 10‑15 Minuten für eine Grundimplementierung.

## Was ist ein PBR‑Material?
Physically Based Rendering (PBR) ist ein Shading‑Modell, das simuliert, wie Licht mit realen Oberflächen interagiert. Durch Anpassen von Eigenschaften wie Metall‑ und Rauheitsfaktoren können Sie hochrealistische Ergebnisse erzielen, ohne komplexe Shader manuell abzustimmen.

## Warum Physically Based Rendering (PBR) verwenden?
- **Realismus:** Materialien reagieren auf Licht auf eine Weise, die der realen Physik entspricht.  
- **Konsistenz:** Das gleiche Material sieht in jeder Beleuchtungsumgebung korrekt aus.  
- **Effizienz:** Moderne GPUs sind für PBR‑Berechnungen optimiert, was Ihnen Leistung kostenlos liefert.

## Voraussetzungen

Bevor wir in den Code eintauchen, stellen Sie sicher, dass Sie Folgendes haben:

### Download und Installation von Aspose.3D für .NET
Besuchen Sie die [Aspose.3D für .NET Dokumentation](https://reference.aspose.com/3d/net/) für detaillierte Anweisungen zum Herunterladen und Installieren der Bibliothek.

### Lizenz erwerben
Um das volle Potenzial von Aspose.3D freizuschalten, erhalten Sie eine gültige Lizenz. Sie können eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/) erhalten oder eine Voll‑Lizenz [hier](https://purchase.aspose.com/buy) erwerben.

## Namespaces importieren
Stellen Sie zunächst sicher, dass Sie die erforderlichen Namespaces importieren, um die Möglichkeiten von Aspose.3D für .NET zu nutzen:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Schritt 1: Szene initialisieren
Beginnen Sie mit der Initialisierung einer 3D‑Szene mit dem folgenden Code‑Snippet:

```csharp
Scene scene = new Scene();
```

## Schritt 2: PBR‑Material erstellen
Jetzt **erstellen wir ein pbr‑Material**, das unserem Würfel ein realistisches Aussehen verleiht:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Schritt 3: Materialeigenschaften festlegen
Feinabstimmung der Materialeigenschaften, sodass es fast metallisch und sehr rau ist – perfekt für einen gebürsteten Metall‑Würfel:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Schritt 4: Einen Würfel erstellen
Erzeugen Sie einen Würfel, auf den das PBR‑Material angewendet wird:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Schritt 5: PBR‑Material zum Würfel hinzufügen
Weisen Sie den zuvor konfigurierten **add pbr material** dem erstellten Würfel‑Node zu:

```csharp
boxNode.Material = mat;
```

## Schritt 6: 3D‑Szene als STL ASCII speichern
Abschließend **export stl ascii**, damit das Modell in jedem gängigen 3D‑Viewer oder Slicer geöffnet werden kann:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Herzlichen Glückwunsch! Sie haben erfolgreich ein PBR‑Material auf einen Würfel in einer 3D‑Szene mit Aspose.3D für .NET angewendet.

## Häufige Fallstricke & Tipps
- **Lizenz nicht gefunden:** Stellen Sie sicher, dass die Lizenzdatei vor allen Aspose‑Aufrufen geladen wird; andernfalls läuft die Bibliothek im Evaluationsmodus.  
- **Falscher Dateipfad:** Verwenden Sie `Path.Combine`, um fehlende Pfadtrennzeichen auf verschiedenen Betriebssystemen zu vermeiden.  
- **Rauheit vs. Metall:** Das Einstellen beider Faktoren zu hoch kann die Oberfläche flach erscheinen lassen; experimentieren Sie mit Werten zwischen 0,5‑0,9 für ein ausgewogenes Aussehen.

## Fazit
Der Einstieg in die 3D‑Grafik mit Aspose.3D für .NET eröffnet endlose kreative Möglichkeiten. Mit seiner intuitiven API und robusten Funktionen wird das Erstellen visuell beeindruckender Szenen zu einem angenehmen Erlebnis für Entwickler. Als Nächstes können Sie den Würfel durch ein komplexeres Mesh ersetzen oder mit verschiedenen PBR‑Texturen experimentieren, um zu sehen, wie das Licht reagiert.

## Häufig gestellte Fragen

**Q1: Ist Aspose.3D mit anderen 3D‑Dateiformaten kompatibel?**  
A1: Ja, Aspose.3D unterstützt verschiedene 3D‑Dateiformate und bietet damit Flexibilität in Ihren Projekten.

**Q2: Kann ich Aspose.3D für kommerzielle Anwendungen nutzen?**  
A2: Absolut! Aspose.3D bietet kommerzielle Lizenzen für die nahtlose Integration in Ihre Anwendungen.

**Q3: Gibt es eine Testversion?**  
A3: Ja, Sie können die Fähigkeiten von Aspose.3D erkunden, indem Sie die kostenlose Testversion [hier](https://releases.aspose.com/) herunterladen.

**Q4: Wo finde ich Community‑Support und Diskussionen?**  
A4: Treten Sie der Aspose.3D‑Community in den [Aspose.3D‑Foren](https://forum.aspose.com/c/3d/18) bei, um Support und Diskussionen zu erhalten.

**Q5: Wie erhalte ich eine temporäre Lizenz für Aspose.3D?**  
A5: Sie können eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/) für Evaluierungszwecke erhalten.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-01-17  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

---