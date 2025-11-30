---
date: 2025-11-30
description: Erfahren Sie, wie Sie Aspose in Java verwenden, um den Radius einer 3D‑Kugel
  zu ändern. Diese Schritt‑für‑Schritt‑Anleitung behandelt die Aspose.3D‑Java‑Bibliothek,
  wie man den Radius festlegt, die Kugel zur Szene hinzufügt und eine OBJ‑Datei in
  Java schreibt.
language: de
linktitle: 'How to Use Aspose: Modify 3D Sphere Radius in Java with Aspose.3D'
second_title: Aspose.3D Java API
title: 'Wie man Aspose verwendet: 3D‑Kugelradius in Java mit Aspose.3D ändern'
url: /java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man Aspose verwendet: Radius einer 3D‑Kugel in Java mit Aspose.3D ändern

## Einführung

Wenn Sie nach **how to use Aspose** suchen, um mit 3D‑Modellen in Java zu arbeiten, sind Sie hier genau richtig. In diesem Tutorial führen wir Sie durch jeden Schritt, der erforderlich ist, um die Größe einer Kugel zu ändern, sie zu einer Szene hinzuzufügen und schließlich eine OBJ‑Datei mit der **Aspose.3D Java library** zu schreiben. Am Ende haben Sie einen wiederverwendbaren Code‑Snippet, den Sie in jede Java‑basierte 3D‑Anwendung einbinden können.

## Schnelle Antworten
- **What is the primary purpose of this guide?** Um zu zeigen, wie man den Radius einer Kugel mit Aspose.3D in Java ändert.  
- **Which library do we use?** Die Aspose.3D Java library (eine vollwertige **java 3d library**).  
- **How do I set the radius?** Rufen Sie `sphere.setRadius(double)` auf einem `Sphere`‑Objekt auf.  
- **Can I export to OBJ?** Ja – verwenden Sie `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.  
- **Do I need a license?** Eine kostenlose Testversion funktioniert für die Entwicklung; für die Produktion ist eine Lizenz erforderlich.

## Was ist Aspose.3D für Java?

Aspose.3D ist eine **java 3d library**, die Entwicklern ermöglicht, 3D‑Dateien zu erstellen, zu bearbeiten und zu konvertieren, ohne externe Abhängigkeiten. Sie unterstützt gängige Formate wie OBJ, FBX, STL und weitere, was sie ideal für Spiele, CAD‑Tools und wissenschaftliche Visualisierungen macht.

## Warum Aspose.3D verwenden, um die Kugelgröße zu ändern?

- **No native 3D engine required** – alle Vorgänge werden auf dem Objektmodell ausgeführt.  
- **Cross‑platform** – funktioniert auf jedem Betriebssystem, das Java ausführt.  
- **High‑precision geometry** – Sie können exakte Radiuswerte festlegen, nicht nur approximative Skalierung.  

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie Folgendes haben:

- Grundlegendes Verständnis der Java‑Programmierung.  
- Aspose.3othek installiert – Sie können sie von der [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) herunterladen.  
- Java Development Kit (JDK) auf Ihrem Rechner installiert.

## Pakete importieren

Um zu beginnen, importieren Sie die erforderlichen Klassen in Ihr Java‑Projekt:

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Schritt 1: Szene initialisieren

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

Hier erstellen wir eine neue **3D scene**, die all unsere Geometrie enthält.

## Schritt 2: Kugel initialisieren

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

Ein `Sphere`‑Objekt stellt ein perfektes Kugel‑Primitive dar. An diesem Punkt verwendet es den Standardradius von 1,0.

## Schritt 3: Wie man den Radius einer Kugel setzt

```java
// set radius
sphere.setRadius(10);
```

Diese Zeile demonstriert **how to set radius**. Sie können `10` durch jeden beliebigen `double`‑Wert ersetzen, um die gewünschte Größe zu erreichen.

## Schritt 4: Kugel zur Szene hinzufügen

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Der Aufruf **adds sphere to scene** (oder „add sphere to scene“) erstellt einen Kindknoten unter dem Wurzelknoten.

## Schritt 5: OBJ‑Datei in Java schreiben

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Abschließend schreiben wir im **write OBJ file Java**‑Stil mit `scene.save`. Die Ausgabedatei `sphere.obj` kann in jedem 3D‑Betrachter geöffnet werden, der das Wavefront‑OBJ‑Format unterstützt.

## Häufige Probleme und Lösungen

| Issue | Solution |
|-------|----------|
| **Sphere appears too small in the viewer** | Überprüfen Sie, ob der Radiuswert korrekt gesetzt ist; denken Sie daran, dass Einheiten willkürlich sind, sofern Sie keine Skalierungstransformation anwenden. |
| **Exported OBJ has no material** | Aspose.3D schreibt nur Geometrie; fügen Sie der Kugel ein Material hinzu, wenn Sie Texturen benötigen (`sphere.setMaterial(...)`). |
| **License exception at runtime** | Stellen Sie sicher, dass Sie vor dem Erstellen der `Scene` entweder eine temporäre oder permanente Lizenzdatei geladen haben. |

## Häufig gestellte Fragen

### Q: Wo finde ich die Dokumentation für Aspose.3D für Java?

Sie können die [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) für umfassende Informationen und Nutzungshinweise konsultieren.

### Q: Wie lade ich Aspose.3D für Java herunter?

Laden Sie die Bibliothek von der Release‑Seite herunter: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

### Q: Gibt es eine kostenlose Testversion für Aspose.3D für Java?

Ja, erkunden Sie die Funktionen mit einer kostenlosen Testversion, indem Sie [Aspose.3D Free Trial](https://releases.com/) besuchen.

### Q: Wo kann ich Unterstützung für Aspose.3D für Java erhalten?

Treten Sie der Aspose‑Community im [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) bei, um Hilfe und Diskussionen zu erhalten.

### Q: Wie kann ich eine temporäre Lizenz für Aspose.3D erhalten?

Erhalten Sie eine temporäre Lizenz, indem Sie [Temporary License](https://purchase.aspose.com/temporary-license/) besuchen.

### Q: Kann ich diesen Code mit anderen 3D‑Formaten wie STL verwenden?

Absolut – ändern Sie einfach das `FileFormat`‑Enum beim Aufruf von `scene.save`, z. B. `FileFormat.STL`.

## Fazit

Sie haben nun **how to use Aspose** gemeistert, um den Radius einer Kugel zu ändern, sie zu einer Szene hinzuzufügen und das Ergebnis in Java als OBJ‑Datei zu exportieren. Experimentieren Sie gern mit anderen Primitiven, wenden Sie Materialien an oder verketten Sie mehrere Transformationen, um komplexere 3D‑Modelle zu erstellen.

---

**Zuletzt aktualisiert:** 2025-11-30  
**Getestet mit:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}