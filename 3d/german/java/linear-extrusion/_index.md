---
date: 2026-05-24
description: Erfahren Sie, wie Sie Formen mit Aspose.3D for Java extrudieren. Dieses
  Java 3D‑Modellierungs‑Tutorial behandelt linear extrusion, center control, direction,
  slices, twist und mehr!
keywords:
- how to extrude shape
- java 3d geometry
- create 3d model java
- create solid from 2d
linktitle: 3D-Modelle mit Linear Extrusion in Java erstellen
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  headline: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  type: TechArticle
- description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  name: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  steps:
  - name: Define the 2‑D profile
    text: Create a `Polygon` or `Polyline` that represents the shape you want to extrude.
      *A `Polygon` represents a closed shape defined by vertices, while a `Polyline`
      is an open series of line segments.* Ready to get started? [Perform Linear Extrusion
      Now](./performing-linear-extrusion/) For a detailed tuto
  - name: Configure extrusion options
    text: 'Set the center, direction, slices, twist, and twist offset on an `Extrusion`
      object. *The `Extrusion` class encapsulates all parameters needed to generate
      a 3‑D mesh from a 2‑D profile.* Get hands‑on with center control: [Control Center
      in Linear Extrusion](./controlling-center/) Read more about cen'
  - name: Add the extrusion to the scene
    text: 'Instantiate a `Scene`, attach the extrusion mesh, and export to your desired
      format. *`Scene` is the container that holds all 3‑D objects and handles exporting
      to various file formats.* Ready to set the direction? [Explore Now](./setting-direction/)
      Learn more about direction: [Setting Direction in '
  - name: Export or render
    text: 'Use `Scene.save()` to write the model to OBJ, STL, or any supported format.
      *`Scene.save()` writes the entire scene to the specified file format, applying
      any necessary post‑processing.* Start specifying slices: [Learn More](./specifying-slices/)
      Detailed guide: [Specifying Slices in Linear Extrusio'
  type: HowTo
- questions:
  - answer: Yes, a valid Aspose license is required for production use, but a free
      trial is available for evaluation.
    question: Can I use Aspose.3D for Java in a commercial project?
  - answer: The library works with Java 8 and newer runtimes, including Java 11, 17,
      and 21.
    question: Which Java versions are supported?
  - answer: Aspose.3D handles mesh generation efficiently, but you can call `scene.dispose()`
      when you’re done with large scenes to free native resources.
    question: Do I need to manage memory for large extrusions?
  - answer: Absolutely – you can create several extrusion objects, position them independently,
      and add them to the same scene.
    question: Can I combine multiple extrusion operations in one model?
  - answer: Yes, the “Applying Twist” and “Using Twist Offset” tutorials demonstrate
      how to set both properties on the same extrusion object.
    question: Is there sample code for applying twist and twist offset together?
  type: FAQPage
second_title: Aspose.3D Java API
title: Wie man Formen extrudiert – 3D-Modelle mit Linear Extrusion in Java erstellen
url: /de/java/linear-extrusion/
weight: 23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man Formen extrudiert – 3D-Modelle mit linearer Extrusion in Java erstellen

Wenn Sie sich jemals gefragt haben, **wie man Formen extrudiert** in einer Java-Anwendung, sind Sie hier genau richtig. In diesem Tutorial führen wir Sie durch die linearen Extrusionsfunktionen von Aspose.3D für Java und zeigen, wie Sie einfache 2‑D‑Profile in vollwertige 3‑D‑Modelle verwandeln. Egal, ob Sie einen CAD‑ähnlichen Viewer, eine Game‑Asset‑Pipeline bauen oder einfach mit Geometrie experimentieren, das Beherrschen der linearen Extrusion gibt Ihnen das Vertrauen, komplexe Formen mit nur wenigen Codezeilen zu erstellen.

## Schnelle Antworten
- **Was ist lineare Extrusion?** Ein 2‑D‑Skizze in einen 3‑D‑Körper verwandeln, indem sie entlang einer Richtung erweitert wird.  
- **Welche Bibliothek hilft Ihnen?** Aspose.3D für Java bietet eine fluente API für Extrusionsaufgaben.  
- **Benötige ich eine Lizenz?** Eine kostenlose Testversion reicht für das Lernen; für die Produktion ist eine kommerzielle Lizenz erforderlich.  
- **Welche Java-Version wird benötigt?** Java 8 oder höher.  
- **Kann ich Drehungen oder Versätze anwenden?** Ja – die API unterstützt Drehwinkel und Drehversatz von Haus aus.  

## Was bedeutet „wie man Formen extrudiert“ in Java?
Der `Extrusion`‑Vorgang ist das Kernfeature von Aspose.3D, das ein flaches Kontur in ein volumetrisches Mesh umwandelt. Einfach ausgedrückt, liefern Sie ein 2‑D‑Profil (z. B. ein Rechteck oder ein benutzerdefiniertes Polygon), geben dem Motor an, wie weit es gezogen werden soll, und die Bibliothek erstellt die 3‑D‑Geometrie für Sie.

## Warum Aspose.3D für Java verwenden?
Aspose.3D unterstützt **mehr als 50 Eingabe‑ und Ausgabeformate** – darunter OBJ, STL, FBX und GLTF – und kann Meshes mit bis zu **10 000 Vertices pro Extrusion** erzeugen, ohne die gesamte Szene in den Speicher zu laden. Seine plattformübergreifende Engine läuft auf Windows, Linux und macOS und liefert konsistente Ergebnisse, egal ob Sie an einem Desktop‑Workstation oder einem headless CI‑Server arbeiten.

## Voraussetzungen
- Java 8 oder neuer, installiert auf Ihrer Entwicklungsmaschine.  
- Maven oder Gradle für das Abhängigkeitsmanagement.  
- Eine Aspose.3D für Java Lizenzdatei (optional für die Testversion).  

## Wie funktioniert lineare Extrusion?
Lineare Extrusion erzeugt einen 3‑D‑Körper, indem ein 2‑D‑Profil entlang einer geraden Linie ausgesweept wird. Die Engine trianguliert zunächst das Profil, repliziert es dann in jedem Schnitt entlang der Extrusionsachse und fügt schließlich die Schnitte zusammen, um ein wasserdichtes Mesh zu bilden. Dieser Prozess berechnet automatisch Normalen und UV‑Koordinaten, sodass Sie das Ergebnis ohne zusätzliche Geometrie‑Verarbeitung rendern können.

## Was sind die wichtigsten Parameter für eine lineare Extrusion?
Lineare Extrusion kann mit mehreren Parametern angepasst werden. Der **center** definiert den Drehpunkt des Profils vor der Extrusion. Der **direction**‑Vektor legt die Extrusionsachse fest, standardmäßig die positive Z‑Achse. **Slices** steuern, wie viele Zwischen‑Querschnitte erzeugt werden, was die Glätte bei verdrehten oder konischen Formen beeinflusst. **Twist angle** dreht das Profil progressiv von Anfang bis Ende, während **twist offset** eine lineare Verschiebung entlang der Achse hinzufügt und spiralförmige Formen ermöglicht.

- **Center** – Der Drehpunkt, um den das Profil vor der Extrusion positioniert wird.  
- **Direction** – Ein Vektor, der die Extrusionsachse definiert; Standard ist die positive Z‑Achse.  
- **Slices** – Die Anzahl der Zwischen‑Querschnitte; mehr Schnitte ergeben glattere Übergänge bei verdrehten oder konischen Extrusionen.  
- **Twist Angle** – Die Gesamtdrehung, die auf das Profil von Anfang bis Ende angewendet wird, angegeben in Grad.  
- **Twist Offset** – Ein linearer Versatz, der das Profil entlang der Extrusionsachse verschiebt, während es gedreht wird, und spiralförmige Formen ermöglicht.  

## Durchführung linearer Extrusion in Aspose.3D für Java
Laden Sie Ihr Profil, konfigurieren Sie die Parameter und lassen Sie die API das Mesh erzeugen. Die folgenden Schritte skizzieren den typischen Arbeitsablauf.

### Schritt 1: Definieren Sie das 2‑D‑Profil
Erstellen Sie ein `Polygon` oder `Polyline`, das die Form darstellt, die Sie extrudieren möchten.  
*Ein `Polygon` stellt eine geschlossene Form dar, die durch Vertices definiert ist, während ein `Polyline` eine offene Reihe von Liniensegmenten ist.*  
Bereit, loszulegen? [Lineare Extrusion jetzt durchführen](./performing-linear-extrusion/)  
Für ein detailliertes Tutorial siehe [Lineare Extrusion in Aspose.3D für Java durchführen](./performing-linear-extrusion/).

### Schritt 2: Extrusionsoptionen konfigurieren
Setzen Sie den center, direction, slices, twist und twist offset auf einem `Extrusion`‑Objekt.  
*Die `Extrusion`‑Klasse fasst alle Parameter zusammen, die zum Erzeugen eines 3‑D‑Meshes aus einem 2‑D‑Profil benötigt werden.*  
Praktische Anleitung zur Zentrumskontrolle: [Zentrumskontrolle in linearer Extrusion](./controlling-center/)  
Mehr über die Zentrumskontrolle lesen: [Zentrumskontrolle in linearer Extrusion mit Aspose.3D für Java](./controlling-center/)

### Schritt 3: Fügen Sie die Extrusion zur Szene hinzu
Instanziieren Sie ein `Scene`, hängen Sie das Extrusions‑Mesh an und exportieren Sie in das gewünschte Format.  
*`Scene` ist der Container, der alle 3‑D‑Objekte hält und den Export in verschiedene Dateiformate übernimmt.*  
Bereit, die Richtung festzulegen? [Jetzt erkunden](./setting-direction/)  
Mehr über die Richtung erfahren: [Richtung in linearer Extrusion mit Aspose.3D für Java festlegen](./setting-direction/)

### Schritt 4: Exportieren oder rendern
Verwenden Sie `Scene.save()`, um das Modell in OBJ, STL oder ein beliebiges unterstütztes Format zu schreiben.  
*`Scene.save()` schreibt die gesamte Szene in das angegebene Dateiformat und wendet ggf. notwendige Nachbearbeitung an.*  
Beginnen Sie mit der Angabe von Schnitten: [Mehr erfahren](./specifying-slices/)  
Detaillierte Anleitung: [Schnitte in linearer Extrusion mit Aspose.3D für Java festlegen](./specifying-slices/)

## Wie wendet man eine Drehung auf eine Extrusion an?
Wenden Sie eine Drehung an, indem Sie die `twistAngle`‑Eigenschaft in den Extrusionsoptionen setzen. Die Engine rotiert jeden Schnitt proportional und erzeugt einen helikalen Effekt. Durch Anpassen des Winkels können Sie alles von subtiler Torsion bis zu vollen 360°‑Spiralen erzeugen, nützlich für dekorative Elemente oder funktionale Federn.  
Bereit, zu drehen? [Drehung jetzt anwenden](./applying-twist/)  
Vollständiges Beispiel: [Drehung in linearer Extrusion mit Aspose.3D für Java anwenden](./applying-twist/)

## Wie verwendet man Drehversatz für spiralförmige Formen?
Drehversatz verschiebt jeden Schnitt entlang der Extrusionsachse, während er rotiert, und bildet eine Spiraltreppe oder Schraubenform. Die Kombination von Drehwinkel mit einem positiven Versatz ergibt eine glatte helikale Rampe, während ein negativer Versatz absteigende Spiralen erzeugen kann. Diese Technik ist ideal zum Modellieren von Gewinden, Federn oder künstlerischen Bändern.  
Verbessern Sie Ihre Fähigkeiten: [Drehversatz lernen](./using-twist-offset/)  
Umfassender Leitfaden: [Drehversatz in linearer Extrusion mit Aspose.3D für Java verwenden](./using-twist-offset/)

## Häufige Anwendungsfälle für lineare Extrusion
- **Mechanical parts** – Schnell Bolzen, Wellen und Halterungen aus einfachen Skizzen erzeugen.  
- **Architectural elements** – Grundrisse in Wände oder Säulen für BIM‑Prototypen extrudieren.  
- **Game assets** – Low‑Poly‑Requisiten wie Zäune, Rohre oder dekorative Schienen direkt aus 2‑D‑Grafiken erstellen.  
- **Educational tools** – Mathematische Oberflächen visualisieren, indem parametrische Kurven extrudiert werden.  

## Fehlersuche bei häufigen Problemen
- **Missing faces** – Stellen Sie sicher, dass das Profil ein geschlossener Kreis ist; offene Konturen erzeugen Lücken.  
- **Excessive memory usage** – Reduzieren Sie die Anzahl der `slices` oder aktivieren Sie `scene.setMemoryOptimization(true)`.  
- **Incorrect twist direction** – Positive Winkel drehen im Uhrzeigersinn, wenn man entlang der Extrusionsrichtung blickt; verwenden Sie negative Werte, um die Richtung umzukehren.  

## Häufig gestellte Fragen

**Q: Kann ich Aspose.3D für Java in einem kommerziellen Projekt verwenden?**  
A: Ja, für den Produktionseinsatz ist eine gültige Aspose‑Lizenz erforderlich, aber eine kostenlose Testversion steht zur Evaluierung bereit.

**Q: Welche Java‑Versionen werden unterstützt?**  
A: Die Bibliothek funktioniert mit Java 8 und neueren Laufzeiten, einschließlich Java 11, 17 und 21.

**Q: Muss ich den Speicher für große Extrusionen verwalten?**  
A: Aspose.3D verarbeitet die Mesh‑Erzeugung effizient, Sie können jedoch `scene.dispose()` aufrufen, wenn Sie mit großen Szenen fertig sind, um native Ressourcen freizugeben.

**Q: Kann ich mehrere Extrusionsvorgänge in einem Modell kombinieren?**  
A: Absolut – Sie können mehrere Extrusionsobjekte erstellen, sie unabhängig positionieren und dem selben Szene hinzufügen.

**Q: Gibt es Beispielcode für die gleichzeitige Anwendung von Drehung und Drehversatz?**  
A: Ja, die Tutorials „Applying Twist“ und „Using Twist Offset“ zeigen, wie beide Eigenschaften am selben Extrusionsobjekt gesetzt werden können.

**Zuletzt aktualisiert:** 2026-05-24  
**Getestet mit:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Verwandte Tutorials

- [Java 3D Grafik Tutorial – Zentrum in linearer Extrusion](/3d/java/linear-extrusion/controlling-center/)
- [Wie man die Richtung in linearer Extrusion mit Aspose.3D für Java festlegt](/3d/java/linear-extrusion/setting-direction/)
- [3D-Extrusion mit Schnitten erstellen – Aspose.3D für Java](/3d/java/linear-extrusion/specifying-slices/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}