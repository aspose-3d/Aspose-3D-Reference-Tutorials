---
date: 2026-01-27
description: Lernen Sie Java‑3D‑Modellierung, indem Sie Zylinder mit einer schrägen
  Unterseite mit Aspose.3D für Java erstellen. Dieses Anfänger‑3D‑Tutorial zeigt,
  wie man Aspose 3D installiert, eine Schertransformation anwendet und eine OBJ‑Datei
  in Java exportiert.
linktitle: Java 3D Modeling – Sheared Bottom Cylinders with Aspose.3D
second_title: Aspose.3D Java API
title: Java 3D‑Modellierung – Schräg gestellte Zylinder am Boden mit Aspose.3D
url: /de/java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D Modeling – Schräg gestellte Zylinderböden mit Aspose.3D

## Einleitung

Willkommen zu diesem **java 3d modeling** Tutorial! In dieser Schritt‑für‑Schritt‑Anleitung zeigen wir, wie man einen Zylinder erstellt, dessen Boden schräg gestellt ist, mithilfe der Aspose.3D Bibliothek für Java. Egal, ob Sie einem **beginner 3d tutorial** folgen oder einer bestehenden Modell eine benutzerdefinierte Schertransformation hinzufügen möchten, Sie sehen genau, wie Sie die Szene einrichten, die Scherung anwenden und schließlich **export OBJ file java** für die Verwendung in anderen Tools exportieren.

## Schnelle Antworten
- **Welche Bibliothek wird verwendet?** Aspose.3D für Java  
- **Kann ich Aspose 3D über Maven installieren?** Ja – fügen Sie die Aspose.3D‑Abhängigkeit zu Ihrer `pom.xml` hinzu  
- **Ist für die Entwicklung eine Lizenz erforderlich?** Eine temporäre Lizenz reicht für Tests aus; für die Produktion wird eine Voll‑Lizenz benötigt  
- **Welches Dateiformat wird demonstriert?** Wavefront OBJ (`.obj`)  
- **Wie lange dauert die Ausführung des Beispiels?** Unter einer Sekunde auf einem typischen Arbeitsplatzrechner  

## Voraussetzungen

Bevor wir beginnen, stellen Sie sicher, dass Sie Folgendes haben:

- Java Development Kit (JDK) auf Ihrem System installiert.  
- **Install Aspose 3D** – laden Sie die Bibliothek von der offiziellen Seite [here](https://releases.aspose.com/3d/java/) herunter.  
- Eine IDE oder ein Build‑Tool (Maven/Gradle), um die Aspose.3D‑Abhängigkeit zu verwalten.  

## Pakete importieren

Zuerst importieren wir die Klassen, die wir für die Szene, Geometrie und Dateiverarbeitung benötigen.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Schritt 1: Szene erstellen

Eine Szene ist der Container für alle 3‑D‑Objekte. Wir beginnen mit der Erstellung einer leeren Szene.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Schritt 2: Zylinder 1 erstellen – Wie man einen Zylinder schert

Jetzt erstellen wir den ersten Zylinder und **wenden eine Schertransformation** auf dessen Boden an. Dies demonstriert, **wie man Zylinder schert** Geometrie direkt über die API.

```java
// ExStart:4
// Create cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Customized shear bottom for cylinder 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Shear 47.5deg in the xy plane (z-axis)
// Add cylinder 1 to the scene
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Schritt 3: Zylinder 2 erstellen – Standardzylinder (kein Scherung)

Zum Vergleich fügen wir einen zweiten Zylinder hinzu, der **keinen** schräg gestellten Boden hat.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Schritt 4: Szene speichern – Export OBJ File Java

Abschließend exportieren wir die Szene in eine Wavefront OBJ‑Datei, um die Verwendung von **export obj file java** zu veranschaulichen.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Warum das für Java 3D‑Modellierung wichtig ist

Das Hinzufügen einer Scherung zu einem Primitive ermöglicht es, organischere Formen zu erzeugen, ohne auf externe Modellierungswerkzeuge zurückzugreifen. Diese Technik ist praktisch für:

- Architektonische Visualisierungen, bei denen geneigte Basen erforderlich sind.  
- Spiele‑Assets, die benutzerdefinierte Grundflächen benötigen, dabei aber die Geometrie leicht halten.  
- Schnelles Prototyping, bei dem Sie Abmessungen programmgesteuert anpassen möchten.

## Häufige Probleme & Lösungen

| Problem | Lösung |
|-------|----------|
| **Scherung erscheint zu extrem** | Passen Sie die `Vector2`‑Werte an; sie repräsentieren den Scherfaktor (Bereich 0‑1). |
| **OBJ‑Datei lässt sich im Viewer nicht öffnen** | Stellen Sie sicher, dass das Zielverzeichnis existiert und Sie Schreibrechte haben. |
| **Lizenzausnahme zur Laufzeit** | Wenden Sie vor dem Erstellen der Szene eine temporäre oder permanente Lizenz an (`License license = new License(); license.setLicense("Aspose.3D.lic");`). |

## Häufig gestellte Fragen

**Q: Kann ich Aspose.3D für Java mit anderen Java‑3D‑Bibliotheken verwenden?**  
A: Aspose.3D ist so konzipiert, dass es eigenständig funktioniert. Während Sie es mit anderen Bibliotheken integrieren können, bietet es bereits eine vollwertige API für die meisten 3‑D‑Aufgaben.

**Q: Ist Aspose.3D für Anfänger im 3D‑Modellieren geeignet?**  
A: Absolut. Die API ist unkompliziert, und dieses **beginner 3d tutorial** demonstriert die Kernkonzepte mit minimalem Code.

**Q: Wo finde ich zusätzlichen Support für Aspose.3D für Java?**  
A: Besuchen Sie das [Aspose.3D forum](https://forum.aspose.com/c/3d/18) für Community‑Hilfe und offizielle Antworten.

**Q: Wie kann ich eine temporäre Lizenz für Aspose.3D erhalten?**  
A: Sie können eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/) erhalten.

**Q: Wo kann ich eine vollständige Aspose.3D‑Lizenz für Java erwerben?**  
A: Kaufoptionen sind [hier](https://purchase.aspose.com/buy) verfügbar.

---

**Last Updated:** 2026-01-27  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-01-27  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose