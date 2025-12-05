---
date: 2025-12-05
description: Erfahren Sie, wie Sie Zylinder‑Modelle mit versetzten Oberseiten in Aspose.3D
  für Java erstellen, Kindknoten‑Java‑Schritte hinzufügen und 3D‑Modelle im OBJ‑Format
  einfach exportieren.
language: de
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Wie man einen Zylinder mit versetztem oberen Ende in Aspose.3D für Java erstellt
url: /java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man einen Zylinder mit versetztem oberen Ende in Aspose.3D für Java erstellt

## Einführung

Wenn Sie **wie man einen Zylinder** mit einem benutzerdefinierten versetzten oberen Ende in einer Java‑basierten 3D‑Szene erstellen möchten, macht Aspose.3D den Vorgang unkompliziert. In diesem Tutorial führen wir Sie Schritt für Schritt durch den gesamten Prozess – vom Einrichten der Szene bis zum Export des finalen Modells als OBJ‑Datei – sodass Sie Zylinder mit versetztem oberen Ende sicher in Ihre Anwendungen integrieren können.

## Schnellantworten
- **Welche Bibliothek wird verwendet?** Aspose.3D für Java  
- **Kann ich das obere Ende eines Zylinders versetzen?** Ja, mit `setOffsetTop`  
- **Wie füge ich in Java einen Kind‑Knoten hinzu?** Aufrufen von `createChildNode` am Wurzelknoten  
- **In welches Format kann ich exportieren?** Wavefront OBJ (`export 3d model obj`)  
- **Benötige ich eine Lizenz für Tests?** Eine temporäre Lizenz ist für Evaluierungen verfügbar  

## Was bedeutet „wie man einen Zylinder“ mit versetztem oberen Ende?

Einen Zylinder mit versetztem oberen Ende zu erstellen bedeutet, dass die obere kreisförmige Fläche relativ zur Basis verschoben wird, wodurch Sie konische oder asymmetrische Formen modellieren können, ohne die Scheitelpunkte manuell zu bearbeiten. Aspose.3D stellt dafür einen speziellen Konstruktor und eine `OffsetTop`‑Eigenschaft bereit, die dies in nur wenigen Codezeilen ermöglichen.

## Warum Aspose.3D für Java verwenden?

- **High‑Level‑API:** Keine Notwendigkeit, Low‑Level‑Mesh‑Daten zu verwalten.  
- ** Funktioniert in jeder JVM‑kompatiblen Umgebung.  
- **Integrierte Exporter:** Direktes Speichern nach OBJ, STL, FBX und mehr.  
- **Erweiterbar:** Kind‑Knoten leicht hinzufügen, Transformationen anwenden und mit anderen Java‑Bibliotheken integrieren.

## Voraussetzungen

Bevor wir beginnen, stellen Sie sicher, dass Sie Folgendes haben:

- **Java Development Kit (JDK)** – eine kompatible Version installiert.  
- **Aspose.3D für Java Bibliothek** – laden Sie das neueste JAR von der offiziellen Seite [hier](https://releases.aspose.com/3d/java/) herunter.  
- Eine IDE Ihrer Wahl (Eclipse, IntelliJ IDEA, NetBeans usw.).

## Pakete importieren

Zuerst importieren wir die Klassen, die wir benötigen. Platzieren Sie diese Anweisungen am Anfang Ihrer Java‑Datei:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Schritt‑für‑Schritt‑Anleitung

### Schritt 1: Eine Szene erstellen

Eine Szene fungiert als Container für alle 3D‑Objekte.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Schritt 2: Zylinder mit versetztem oberen Ende initialisieren

Hier beantworten wir **wie man einen Zylinder** mit einem benutzerdefinierten Versatz erstellt. Der Konstruktor definiert Radius, Höhe, Segmente, Stufen und ob der Zylinder geschlossen ist. Anschließend verschieben wir das obere Ende mit `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Schritt 3: Wie man **Kind‑Knoten in Java hinzufügt** – Ersten Zylinder anhängen

Wir erstellen einen Kind‑Knoten unter dem Wurzelknoten der Szene und verschieben den Zylinder an die gewünschte Position.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Schritt 4: Einen zweiten Zylinder initialisieren (ohne Versatz)

Zum Vergleich fügen wir einen regulären Zylinder ohne Versatz hinzu.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Schritt 5: Wie man **Kind‑Knoten in Java hinzufügt** – Zweiten Zylinder anhängen

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Schritt 6: Wie man **3D‑Modell als OBJ exportiert** – Szene speichern

Abschließend exportieren wir die gesamte Szene (beide Zylinder) als Wavefront‑OBJ‑Datei, die von den meisten 3D‑Tools unterstützt wird.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Wenn Sie das Programm ausführen, finden Sie `CustomizedOffsetTopCylinder.obj` im angegebenen Verzeichnis, bereit zum Öffnen in Blender, Maya oder jedem anderen OBJ‑kompatiblen Viewer.

## Häufige Probleme und Lösungen

| Problem | Grund | Lösung |
|---------|-------|--------|
| **OBJ‑Datei ist leer** | Szene wurde nicht korrekt gespeichert oder falscher Pfad. | Stellen Sie sicher, dass das Ausgabeverzeichnis existiert und Sie Schreibrechte haben. |
| **Versatz wurde nicht angewendet** | Verwendung einer älteren Aspose.3D‑Version. | Aktualisieren Sie auf die neueste Bibliothek, in der `setOffsetTop` unterstützt wird. |
| **Kind‑Knoten ist nicht sichtbar** | Transformation wurde nicht angewendet. | Stellen Sie sicher, dass Sie `getTransform().setTranslation` nach dem Erstellen des Kind‑Knotens aufrufen. |

## Häufig gestellte Fragen

**F: Ist Aspose.3D mit verschiedenen Java‑IDEs kompatibel?**  
A: Ja, es funktioniert nahtlos mit Eclipse, IntelliJ IDEA, NetBeans und anderen IDEs.

**F: Kann ich Texturen auf die erstellten 3D‑Objekte anwenden?**  
A: Absolut! Verwenden Sie die `Material`‑Klasse, um Texturen und Oberflächeneigenschaften zuzuweisen.

**F: Welche Lizenzierungsoptionen gibt es für Aspose.3D?**  
A: Es stehen verschiedene Lizenzmodelle zur Verfügung; Sie können sie [hier](https://purchase.aspose.com/buy) erkunden.

**F: Wie kann ich Hilfe erhalten oder Erfahrungen teilen?**  
A: Treten Sie dem Aspose.3D‑Community‑Forum [hier](https://forum.aspose.com/c/3d/18) bei für Support und Diskussionen.

**F: Ist eine temporäre Lizenz für Tests verfügbar?**  
A: Ja, eine temporäre Lizenz kann für Evaluierungen [hier](https://purchase.aspose.com/temporary-license/) erhalten werden.

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---
**Zuletzt aktualisiert:** 2025-12-05  
**Getestet mit:** Aspose.3D für Java 24.12 (neueste)  
**Autor:** Aspose