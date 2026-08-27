---
date: 2026-08-02
description: Erfahren Sie, wie Sie die Extrusionsrichtung bei linearer Extrusion ändern
  und OBJ‑Dateien mit Aspose.3D für Java exportieren. Folgen Sie unserer Schritt‑für‑Schritt‑Anleitung.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Ändern der Extrusionsrichtung – Aspose.3D Java
og_description: Ändern Sie die Extrusionsrichtung bei linearer Extrusion mit Aspose.3D
  für Java und exportieren Sie OBJ‑Dateien. Dieser Leitfaden zeigt Schritt‑für‑Schritt‑Code
  und Tipps für Entwickler.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Ändern der Extrusionsrichtung – Aspose.3D Java Tutorial
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Ändern der Extrusionsrichtung in 3D-Modellen – Aspose.3D Java
url: /de/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Extrusionsrichtung in 3D‑Modellen ändern – Aspose.3D Java

## Einführung

In diesem umfassenden Tutorial erfahren Sie **wie man die Extrusionsrichtung** ändert, wenn Sie eine lineare Extrusion mit Aspose.3D für Java durchführen. Egal, ob Sie ein CAD‑ähnliches Werkzeug bauen, Assets für eine Spiel‑Engine vorbereiten oder Teile für den 3‑D‑Druck erzeugen, die Kontrolle der Extrusionsrichtung ermöglicht es Ihnen, exakt die gewünschte Form zu erstellen. Wir führen Sie durch jeden Schritt, von der Initialisierung eines Profils bis zum Speichern des Ergebnisses als OBJ‑Datei, sodass Sie auch **3D‑Modell‑OBJ**‑Dateien direkt aus Java **exportieren** können.

## Schnelle Antworten
- **Welche Klasse führt die lineare Extrusion aus?** `LinearExtrusion`
- **Welche Methode setzt den Extrusionsvektor?** `setDirection(Vector3 direction)`
- **Kann das Ergebnis als OBJ gespeichert werden?** Ja—verwenden Sie `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Ist für den Produktionseinsatz eine Lizenz erforderlich?** Eine kostenlose Testversion ist verfügbar; für die kommerzielle Nutzung ist eine Lizenz zwingend erforderlich.
- **Welche IDE funktioniert am besten mit Aspose.3D?** IntelliJ IDEA und Eclipse werden vollständig unterstützt.

## Was ist lineare Extrusion?

Lineare Extrusion ist der Vorgang, bei dem eine 2‑D‑Skizze (wie ein Rechteck oder ein Kreis) entlang einer Geraden erweitert wird, um einen 3‑D‑Körper zu erzeugen. Standardmäßig folgt die Extrusion der positiven Z‑Achse, aber Aspose.3D ermöglicht es Ihnen, diesen Pfad mit der Eigenschaft `setDirection` zu ändern, wodurch Sie die volle Kontrolle über die endgültige Geometrie erhalten.

## Warum die Extrusionsrichtung bei linearer Extrusion ändern?

Das Ändern der Extrusionsrichtung ermöglicht es Ihnen, neue Geometrie mit bestehenden Objekten auszurichten, schräg verlaufende Komponenten ohne zusätzliche Transformationen zu erstellen und Modelle zu erzeugen, die dem von nachgelagerten Pipelines (z. B. 3‑D‑Druckern oder Spiel‑Engines) benötigten Koordinatensystem entsprechen. Dies eliminiert den Bedarf an Nachbearbeitungsschritten und reduziert den Dateigrößen‑Overhead um bis zu 15 %, wenn Richtungsvektoren verwendet werden, die unnötige Rotationen vermeiden.

## Voraussetzungen

- Grundkenntnisse in Java.
- Aspose.3D‑Bibliothek installiert. Sie können sie von [hier](https://releases.aspose.com/3d/java/) herunterladen. Alle Aspose‑Veröffentlichungen können Sie auch auf der Hauptseite [hier](https://releases.aspose.com/) durchsuchen.
- Eine IDE wie Eclipse oder IntelliJ IDEA.

## Pakete importieren

Der Namensraum `com.aspose.threed` stellt die Kern‑3‑D‑Klassen und Hilfstypen bereit.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Schritt 1: Basisprofil initialisieren

Die Klasse `RectangleShape` erzeugt das 2‑D‑Profil, das extrudiert wird. Ein kleiner Abrundungsradius verleiht den Kanten ein glattes Aussehen.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Schritt 2: Szene erstellen

Die Klasse `Scene` ist Aspose.3D's oberster Container, der alle 3‑D‑Knoten, Lichter, Kameras und Materialien enthält.

```java
Scene scene = new Scene();
```

## Schritt 3: Knoten erstellen

Ein `Node` repräsentiert ein Objekt im Szenengraphen und ermöglicht das Anfügen von Geometrie, Transformationen und anderen Eigenschaften.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Schritt 4: Lineare Extrusion am linken Knoten ausführen

`LinearExtrusion` führt die Extrusionsoperation aus und wandelt ein 2‑D‑Profil in ein 3‑D‑Mesh um.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Schritt 5: Lineare Extrusion am rechten Knoten mit Richtung ausführen

Hier **ändern wir die Extrusionsrichtung**. Durch Übergabe eines benutzerdefinierten `Vector3` an `setDirection` folgt die Extrusion dem Vektor (0.3, 0.2, 1) und erzeugt eine schräg verlaufende Form, die mit dem Koordinatensystem der Szene übereinstimmt.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Schritt 6: 3D‑Szene speichern

Die Methode `save` schreibt die Szene in eine Datei im angegebenen Format.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Häufige Probleme und Lösungen

| Problem | Warum es passiert | Lösung |
|---------|-------------------|--------|
| OBJ‑Datei erscheint leer | Das Profil wurde keinem Knoten hinzugefügt | Stellen Sie sicher, dass `createChildNode` an einem gültigen Knoten aufgerufen wird |
| Richtung scheint unverändert | `setDirection` wurde aufgerufen, nachdem die Extrusion bereits erstellt wurde | Setzen Sie die Richtung innerhalb des `LinearExtrusion`‑Initialisierers, wie gezeigt |
| Niedrigauflösendes Mesh | `setSlices`‑Wert ist zu niedrig | Erhöhen Sie die Slice‑Anzahl (z. B. 100 oder mehr) |

## Fazit

Sie wissen jetzt **wie man die Extrusionsrichtung** bei einer linearen Extrusion ändert, wie man Twist‑ und Slice‑Einstellungen anpasst und wie man **3D‑Modell‑OBJ**‑Dateien mit Aspose.3D für Java **exportiert**. Diese Techniken geben Ihnen eine feinkörnige Kontrolle über die Erstellung von Geometrie und erleichtern die Integration von 3‑D‑Assets in größere Pipelines.

## Häufig gestellte Fragen

**Q:** Kann ich Aspose.3D mit anderen Programmiersprachen verwenden?  
**A:** Ja—Aspose.3D stellt APIs für .NET und Java bereit, die plattformübergreifende Entwicklung ermöglichen.

**Q:** Gibt es eine kostenlose Testversion für Aspose.3D?  
**A:** Auf jeden Fall. Sie können das vollständige Funktionsset mit einer kostenlosen Testversion [hier](https://releases.aspose.com/) erkunden.

**Q:** Wo finde ich die ausführliche Dokumentation für Aspose.3D für Java?  
**A:** Die umfassende Referenz ist [hier](https://reference.aspose.com/3d/java/) verfügbar.

**Q:** Wie erhalte ich Support für Aspose.3D?  
**A:** Besuchen Sie das offizielle [Aspose.3D‑Forum](https://forum.aspose.com/c/3d/18) für Unterstützung durch die Community und das Produktteam.

**Q:** Gibt es temporäre Lizenzen für Tests?  
**A:** Ja—temporäre Lizenzen können [hier](https://purchase.aspose.com/temporary-license/) erhalten werden.

---

**Zuletzt aktualisiert:** 2026-08-02  
**Getestet mit:** Aspose.3D für Java (neueste Version)  
**Autor:** Aspose

{{< blocks/products/products-backtop-button >}}

## Verwandte Tutorials

- [Wie man Formen extrudiert – 3D‑Modelle mit linearer Extrusion in Java erstellen](/3d/java/linear-extrusion/)
- [3D‑Extrusion in Java mit Aspose.3D erstellen](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Java 3D‑Grafik‑Tutorial – Mittelpunkt bei linearer Extrusion](/3d/java/linear-extrusion/controlling-center/)

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}