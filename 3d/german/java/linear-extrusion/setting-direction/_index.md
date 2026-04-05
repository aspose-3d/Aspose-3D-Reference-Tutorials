---
date: 2026-02-22
description: Erfahren Sie, wie Sie die Richtung bei linearer Extrusion festlegen und
  ein 3D‑Modell im OBJ‑Format mit Aspose.3D für Java exportieren. Folgen Sie unserer
  Schritt‑für‑Schritt‑Anleitung.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Wie man die Richtung bei linearer Extrusion mit Aspose.3D für Java festlegt
url: /de/java/linear-extrusion/setting-direction/
weight: 12
---

.3D for Java (latest release)

**Author:** Aspose

All unchanged.

Now produce final content.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man die Richtung bei Linearer Extrusion mit Aspose.3D für Java festlegt

## Einführung

In diesem umfassenden Tutorial erfahren Sie **wie man die Richtung festlegt**, wenn Sie eine lineare Extrusion mit Aspose.3D für Java durchführen. Egal, ob Sie ein CAD‑ähnliches Werkzeug erstellen oder Geometrie für eine Spiel‑Engine generieren, die Kontrolle der Extrusionsrichtung ermöglicht es Ihnen, exakt die gewünschte Form zu erzeugen. Wir gehen jeden Schritt durch, von der Initialisierung eines Profils bis zum Speichern des Ergebnisses als OBJ‑Datei, sodass Sie auch **3D‑Modell‑OBJ**‑Dateien direkt aus Java **exportieren** können.

## Schnelle Antworten
- **Was ist die primäre Klasse für lineare Extrusion?** `LinearExtrusion`
- **Welche Methode definiert die Extrusionsrichtung?** `setDirection(Vector3 direction)`
- **Kann ich das Ergebnis als OBJ exportieren?** Ja, mit `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Benötige ich eine Lizenz für die Entwicklung?** Eine kostenlose Testversion ist verfügbar; für die Produktion ist eine Lizenz erforderlich.
- **Welche Java‑IDE funktioniert am besten?** IntelliJ IDEA oder Eclipse werden beide vollständig unterstützt.

## Was ist lineare Extrusion?

Lineare Extrusion nimmt ein 2‑D‑Profil (wie ein Rechteck oder einen Kreis) und erstreckt es entlang einer geraden Linie, um einen 3‑D‑Körper zu erzeugen. Standardmäßig folgt die Extrusion der positiven Z‑Achse, aber Aspose.3D ermöglicht es Ihnen, diesen Pfad mit der `setDirection`‑Eigenschaft zu ändern.

## Warum die Richtung bei linearer Extrusion festlegen?

- Ausrichten der Geometrie an vorhandenen Objekten in einer Szene.
- Erstellen von schrägen oder geneigten Teilen ohne zusätzliche Transformationsschritte.
- Exportieren von Modellen, die einem bestimmten Koordinatensystem entsprechen müssen (z. B. für 3‑D‑Druck oder Spiel‑Engines).

## Voraussetzungen

- Grundkenntnisse in Java.
- Aspose.3D‑Bibliothek installiert. Sie können sie von [hier](https://releases.aspose.com/3d/java/) herunterladen.
- Eine IDE wie Eclipse oder IntelliJ IDEA.

## Pakete importieren

Importieren Sie zunächst die Namespaces, die die Kern‑3‑D‑Klassen und Hilfstypen bereitstellen.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Schritt 1: Basisprofil initialisieren

Erstellen Sie die Form, die extrudiert werden soll. In diesem Beispiel verwenden wir ein `RectangleShape` mit einem kleinen Abrundungsradius, um den Kanten ein glattes Aussehen zu verleihen.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Schritt 2: Szene erstellen

Ein `Scene`‑Objekt dient als Container für alle 3‑D‑Knoten, Lichter, Kameras und Materialien.

```java
Scene scene = new Scene();
```

## Schritt 3: Knoten erstellen

Fügen Sie dem Szenen‑Root zwei Kindknoten hinzu – einen für die linke Extrusion und einen für die rechte Extrusion. Der rechte Knoten wird verschoben, damit die beiden Objekte nicht überlappen.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Schritt 4: Lineare Extrusion am linken Knoten durchführen

Extrudieren Sie das Profil am linken Knoten mit der Standard‑Z‑Achsen‑Richtung. Wir fügen außerdem eine vollständige 360°‑Drehung hinzu und erhöhen die Scheibenanzahl für ein glatteres Mesh.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Schritt 5: Lineare Extrusion am rechten Knoten mit Richtung durchführen

Hier setzen wir die **Richtung**. Durch Übergabe eines benutzerdefinierten `Vector3` an `setDirection` folgt die Extrusion dem Vektor (0.3, 0.2, 1) und erzeugt eine schräge Form.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Schritt 6: 3D‑Szene speichern

Zum Schluss exportieren Sie die Szene in das Wavefront‑OBJ‑Format. Dieser Schritt zeigt, wie man **obj‑Dateien in Java**‑Projekten **speichert** und erleichtert das Betrachten des Ergebnisses in jedem 3‑D‑Viewer.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Häufige Probleme und Lösungen

| Problem | Warum es passiert | Lösung |
|---------|-------------------|--------|
| OBJ-Datei erscheint leer | Das Profil wurde nicht zu einem Knoten hinzugefügt | Stellen Sie sicher, dass `createChildNode` an einem gültigen Knoten aufgerufen wird |
| Richtung scheint unverändert | `setDirection` wurde nach der Konstruktion der Extrusion aufgerufen | Setzen Sie die Richtung innerhalb des `LinearExtrusion`‑Initialisierers, wie gezeigt |
| Mesh mit niedriger Auflösung | `setSlices`‑Wert ist zu niedrig | Erhöhen Sie die Scheibenanzahl (z. B. 100 oder mehr) |

## Fazit

Sie wissen jetzt **wie man die Richtung** bei einer linearen Extrusion festlegt, wie man Drehung und Scheiben‑Einstellungen anpasst und wie man **3D‑Modell‑OBJ**‑Dateien mit Aspose.3D für Java **exportiert**. Diese Techniken geben Ihnen eine feinkörnige Kontrolle über die Erstellung von Geometrie und erleichtern die Integration von 3‑D‑Assets in größere Pipelines.

## FAQ

### Q1: Kann ich Aspose.3D mit anderen Programmiersprachen verwenden?

A1: Aspose.3D unterstützt verschiedene Programmiersprachen, darunter .NET und Java.

### Q2: Gibt es eine kostenlose Testversion für Aspose.3D?

A2: Ja, Sie können die Funktionen von Aspose.3D mit einer kostenlosen Testversion [hier](https://releases.aspose.com/) erkunden.

### Q3: Wo finde ich die ausführliche Dokumentation für Aspose.3D für Java?

A3: Die umfassende Dokumentation ist [hier](https://reference.aspose.com/3d/java/) verfügbar.

### Q4: Wie kann ich Support für Aspose.3D erhalten?

A4: Besuchen Sie das [Aspose.3D‑Forum](https://forum.aspose.com/c/3d/18) für Unterstützung oder Fragen.

### Q5: Gibt es temporäre Lizenzen für Aspose.3D?

A5: Ja, Sie können eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/) erhalten.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-02-22  
**Tested With:** Aspose.3D for Java (latest release)  
**Author:** Aspose