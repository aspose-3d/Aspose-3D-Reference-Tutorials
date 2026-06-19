---
date: 2026-04-29
description: Erfahren Sie, wie Sie die Größe von 3D‑Modellen reduzieren, indem Sie
  in Java ein Kugel‑Mesh erstellen und es mit Google Draco mithilfe von Aspose.3D
  komprimieren – unverzichtbar für den Export mit Aspose 3D.
keywords:
- reduce 3d model size
- aspose 3d export
- compress 3d mesh java
linktitle: Wie man ein Kugel‑Mesh in Java erstellt – 3D‑Meshes mit Google Draco komprimieren
second_title: Aspose.3D Java API
title: '3D‑Modellgröße reduzieren: Kugel‑Mesh in Java mit Draco erstellen'
url: /de/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Reduzieren der 3D‑Modellgröße: Erstellen eines Kugel‑Mesh in Java mit Draco

## Einführung

Wenn Sie nach einer schnellen Methode suchen, **die 3D‑Modellgröße zu reduzieren** und dabei hochwertige Geometrie zu liefern, sind Sie hier genau richtig. In diesem Tutorial zeigen wir, wie man ein Kugel‑Mesh mit **Aspose.3D for Java** erzeugt und anschließend dieses Mesh mit **Google Draco** komprimiert. Am Ende haben Sie eine einsatzbereite `.drc`‑Datei, die deutlich kleiner ist als das Original, ideal für webbasierte Viewer, mobile Spiele oder jede bandbreitenbeschränkte Java‑Anwendung.

## Schnelle Antworten
- **Worum geht es in diesem Tutorial?** Erstellen eines Kugel‑Mesh in Java und Komprimieren mit Google Draco über Aspose.3D.  
- **Primäre Bibliothek?** Aspose.3D for Java (wird sowohl für die Mesh‑Erstellung als auch für den Draco‑Export verwendet).  
- **Typische Implementierungszeit?** Etwa 10‑15 Minuten für eine einfache Kugel.  
- **Wichtige Voraussetzung?** Eine Java‑Entwicklungsumgebung mit den Aspose.3D‑JARs im Klassenpfad.  
- **Ergebnis?** Eine `.drc`‑Datei, die **die 3D‑Modellgröße** um bis zu **90 %** im Vergleich zu einem unkomprimierten Mesh **reduziert**.

## Was bedeutet „3D‑Modellgröße reduzieren“ im Kontext der 3D‑Entwicklung?

Das Reduzieren der 3D‑Modellgröße bedeutet, die Menge an Geometriedaten, die übertragen oder gespeichert werden müssen, zu verkleinern, ohne die visuelle Qualität merklich zu beeinträchtigen. Draco erreicht dies, indem Vertex‑Positionen, Normalen und andere Attribute in einem stark kompakten Binärformat kodiert werden. In Kombination mit Aspose.3D bleibt der gesamte Workflow in Java, sodass Sie keine nativen Bibliotheken jonglieren müssen.

## Warum Google‑Draco‑Mesh‑Kompression mit Aspose.3D verwenden?

- **Massive Größenreduktion:** Draco kann Mesh‑Daten um bis zu 90 % im Vergleich zu Formaten wie OBJ oder STL reduzieren.  
- **Schnelles Laufzeit‑Decoding:** Engines wie Unity, Unreal und three.js dekodieren Draco nativ, was zu schnelleren Ladezeiten führt.  
- **Nahtlose Java‑Integration:** Aspose.3D abstrahiert die native Draco‑Bibliothek, sodass Sie im Java‑Ökosystem bleiben können.  
- **Ein‑Stop‑Aspose‑3D‑Export:** Die gleiche API, die Sie zur Erstellung der Geometrie verwenden, übernimmt auch den Export und vereinfacht die Pipeline.

## Voraussetzungen

- **Java Development Kit (JDK)** – Version 8 oder neuer.  
- **Aspose.3D for Java** – Laden Sie die neuesten JARs von der offiziellen Seite [hier](https://releases.aspose.com/3d/java/) herunter.  
- **Grundlegende Kenntnisse zu Google Draco** – Sie verwenden den Wrapper von Aspose.3D, sodass keine native Draco‑Installation erforderlich ist.

## Import Packages

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Schritt‑für‑Schritt‑Anleitung

### Schritt 1: Projekt einrichten

Erstellen Sie ein neues Java‑Projekt (jede IDE ist geeignet) und fügen Sie alle Aspose.3D‑JARs dem Klassenpfad hinzu. Legen Sie Ihre Quelldateien aus Gründen der Übersichtlichkeit in ein Paket wie `com.example.draco` ab.

### Schritt 2: Kugel‑Mesh in Java erstellen

```java
// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();
```

> **Pro‑Tipp:** Die Klasse `Sphere` erzeugt ein trianguliertes Mesh mit einem Standardradius von 1.0. Sie können einen benutzerdefinierten Radius, eine andere Tessellation oder Materialparameter übergeben, wenn Sie vor der Kompression ein anderes Detailniveau benötigen.

### Schritt 3: Mesh mit Google Draco komprimieren

```java
// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
```

Durch Setzen des Komprimierungsgrades auf `OPTIMAL` erhalten Sie die größte Größenreduktion bei gleichzeitigem Erhalt der visuellen Treue, was Ihnen hilft, **die 3D‑Modellgröße zu reduzieren**.

### Schritt 4: Komprimiertes Mesh speichern

```java
// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

Die resultierende Datei `SphereMeshtoDRC_Out.drc` kann an Clients gestreamt, in einem CDN gespeichert oder direkt von jeder Draco‑kompatiblen Engine geladen werden.

## Häufige Anwendungsfälle

| Szenario | Warum Modellgröße reduzieren? | Wie dieses Tutorial hilft |
|----------|-------------------------------|---------------------------|
| Web‑basierte Produktkonfiguratoren | Schnellere Seitenladezeiten bei langsamen Verbindungen | Draco‑komprimierte `.drc`‑Dateien laden in Sekunden |
| Mobile AR/VR‑Apps | Geringerer Speicherverbrauch auf Geräten | Kleinere Meshes halten die App reaktionsschnell |
| Cloud‑gerenderte Szenen | Bandbreitenkosten senken | Ein‑Klick‑Export von Aspose.3D zu Draco |

## Häufige Probleme und Lösungen

| Problem | Grund | Lösung |
|---------|-------|--------|
| **`NoClassDefFoundError` für Draco‑Klassen** | Aspose.3D‑JARs nicht im Klassenpfad | Stellen Sie sicher, dass *alle* Aspose.3D‑JAR‑Dateien enthalten sind und die Version mit der Dokumentation übereinstimmt. |
| **Ausgabedatei ist leer** | `MyDir` verweist auf einen nicht existierenden Ordner | Erstellen Sie das Verzeichnis programmgesteuert (`Files.createDirectories(Paths.get(MyDir))`) bevor Sie die Datei schreiben. |
| **Komprimiertes Mesh wirkt verzerrt** | Verwendung eines niedrigen Komprimierungsgrades oder unzureichender Tessellation | Wechseln Sie zu `DracoCompressionLevel.OPTIMAL` und erhöhen Sie die Tessellation der Kugel (z. B. `new Sphere(1.0, 64, 64)`). |

## Häufig gestellte Fragen

**F: Ist Aspose.3D mit verschiedenen 3D‑Dateiformaten kompatibel?**  
A: Ja, Aspose.3D unterstützt OBJ, FBX, STL, GLTF und viele weitere Formate, wodurch es eine vielseitige Wahl für **Aspose 3D‑Export**‑Pipelines ist.

**F: Kann ich Google Draco auch in anderen Programmiersprachen zur Kompression nutzen?**  
A: Absolut. Draco bietet native Bibliotheken für C++, Python und JavaScript. Dieses Tutorial konzentriert sich auf Java, aber die Konzepte gelten sprachübergreifend.

**F: Wo finde ich weitere Aspose.3D‑Dokumentation?**  
A: Besuchen Sie die [Aspose.3D Java‑Dokumentation](https://reference.aspose.com/3d/java/) für vollständige API‑Referenzen und weitere Beispiele.

**F: Wie erhalte ich eine temporäre Lizenz für Aspose.3D?**  
A: Erkunden Sie temporäre Lizenzoptionen [hier](https://purchase.aspose.com/temporary-license/).

**F: Gibt es ein Community‑Forum für Aspose.3D‑Support?**  
A: Ja, treten Sie der Diskussion im [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) bei.

## Fazit

In diesem Leitfaden haben wir gezeigt, wie man **die 3D‑Modellgröße** reduziert, indem man ein Kugel‑Mesh in Java erstellt und anschließend mit Google Draco über Aspose.3D komprimiert. Durch Befolgen dieser knappen Schritte können Sie Mesh‑Dateien dramatisch verkleinern, Ladezeiten verbessern und Ihre Java‑basierten 3D‑Anwendungen reaktionsschnell und bandbreitenfreundlich halten.

---

**Zuletzt aktualisiert:** 2026-04-29  
**Getestet mit:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}