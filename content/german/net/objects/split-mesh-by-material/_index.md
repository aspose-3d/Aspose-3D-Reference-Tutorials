---
title: Aufteilen des Netzes nach Material
linktitle: Aufteilen des Netzes nach Material
second_title: Aspose.3D .NET API
description: Erfahren Sie, wie Sie mit Aspose.3D für .NET 3D-Netze nach Material aufteilen. Verbessern Sie die Organisation und Effizienz der Szene. Schritt-für-Schritt-Anleitung für Entwickler.
type: docs
weight: 22
url: /de/net/objects/split-mesh-by-material/
---
## Einführung
Willkommen zu diesem umfassenden Tutorial zum Aufteilen eines Netzes nach Material mit Aspose.3D für .NET! Wenn Sie als Entwickler mit 3D-Grafiken arbeiten und Netze effizient verwalten und manipulieren möchten, sind Sie hier richtig. In diesem Leitfaden untersuchen wir den Prozess der Aufteilung eines Netzes nach Material, eine entscheidende Aufgabe bei der Erstellung vielfältiger und optisch ansprechender 3D-Szenen.
## Voraussetzungen
Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:
-  Aspose.3D für .NET: Stellen Sie sicher, dass die Aspose.3D-Bibliothek in Ihrem .NET-Projekt installiert ist. Wenn nicht, können Sie es hier herunterladen[Veröffentlichungen](https://releases.aspose.com/3d/net/) Seite.
- Grundkenntnisse der 3D-Grafik: Machen Sie sich mit den grundlegenden Konzepten der 3D-Grafik vertraut, um die Nuancen der Netzmanipulation zu verstehen.
- Entwicklungsumgebung: Richten Sie eine geeignete .NET-Entwicklungsumgebung ein, beispielsweise Visual Studio.
## Namespaces importieren
Beginnen Sie mit dem Importieren der erforderlichen Namespaces, um auf die Aspose.3D-Funktionalität zuzugreifen. Fügen Sie am Anfang Ihres Codes Folgendes ein:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
Lassen Sie uns das Beispiel nun in mehrere Schritte unterteilen:
## Schritt 1: Erstellen eines Kastennetzes
```csharp
// Erstellen Sie ein Netz aus einem Kasten (bestehend aus 6 Ebenen)
Mesh box = (new Box()).ToMesh();
```
Hier initialisieren wir mit Aspose.3D ein Netz, das einen Kasten mit sechs Ebenen darstellt.
## Schritt 2: Material zum Netz hinzufügen
```csharp
// Erstellen Sie auf diesem Netz ein Materialelement
VertexElementMaterial mat = (VertexElementMaterial)box.CreateElement(VertexElementType.Material, MappingMode.Polygon, ReferenceMode.Index);
// Geben Sie für jede Ebene einen anderen Materialindex an
mat.Indices.AddRange(new int[] { 0, 1, 2, 3, 4, 5 });
```
Dieser Schritt umfasst das Hinzufügen eines Materialelements zum Netz und die Zuweisung unterschiedlicher Materialindizes zu jeder Ebene.
## Schritt 3: Aufteilen des Netzes nach Material (CloneData-Richtlinie)
```csharp
// Teilen Sie es in 6 Unternetze auf, jede Ebene wird zu einem Unternetz
Mesh[] planes = PolygonModifier.SplitMesh(box, SplitMeshPolicy.CloneData);
```
Hier teilen wir das Netz basierend auf den angegebenen Materialien mithilfe der CloneData-Richtlinie in sechs Unternetze auf.
## Schritt 4: Materialindizes für Kompaktdaten aktualisieren
```csharp
mat.Indices.Clear();
mat.Indices.AddRange(new int[] { 0, 0, 0, 1, 1, 1 });
```
Aktualisieren Sie Materialindizes, um sich mit der CompactData-Richtlinie auf den nächsten Teilungsvorgang vorzubereiten.
## Schritt 5: Aufteilen des Netzes nach Material (CompactData-Richtlinie)
```csharp
// Teilen Sie es in zwei Unternetze auf, die jeweils bestimmte Ebenen enthalten
planes = PolygonModifier.SplitMesh(box, SplitMeshPolicy.CompactData);
```
Jetzt teilen wir das Netz in zwei Unternetze auf, gruppieren Ebenen nach Materialien und verwenden die CompactData-Richtlinie.
## Abschluss
Glückwunsch! Sie haben erfolgreich gelernt, wie Sie mit Aspose.3D für .NET ein Netz nach Material aufteilen. Diese Technik ist für die effiziente Verwaltung komplexer 3D-Szenen unerlässlich.
## Häufig gestellte Fragen
### F: Kann ich diese Technik auf benutzerdefinierte Netze anwenden?
Absolut! Solange Ihr Netz über definierte Materialien verfügt, können Sie diesen Ansatz verwenden.
### F: Wie unterscheidet sich die CloneData-Richtlinie von der CompactData-Richtlinie?
Die CloneData-Richtlinie stellt sicher, dass jedes Unternetz dieselben Kontrollpunktinformationen teilt, während die CompactData-Richtlinie jedes Unternetz mit seinen eigenen Kontrollpunktinformationen versorgt.
### F: Gibt es Leistungsaspekte bei der Verwendung dieser Methode?
Im Allgemeinen weist die CloneData-Richtlinie aufgrund gemeinsamer Kontrollpunktinformationen möglicherweise eine etwas bessere Leistung auf.
### F: Kann ich die Ergebnisse der Netzaufteilung visualisieren?
Ja, Sie können die resultierenden Teilnetze mit den Rendering-Funktionen von Aspose.3D rendern und visualisieren.
### F: Ist Aspose.3D für die Spieleentwicklung geeignet?
Während Aspose.3D hauptsächlich zum Modellieren und Rendern verwendet wird, kann es für bestimmte Aufgaben in Spieleentwicklungspipelines integriert werden.