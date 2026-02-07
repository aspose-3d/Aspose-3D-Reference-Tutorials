---
date: 2026-02-07
description: Erfahren Sie, wie Sie Zylinder‑Modelle mit versetzten Oberseiten in Aspose.3D
  für Java erstellen, Kindknoten‑Java‑Schritte hinzufügen und 3D‑Modelle im OBJ‑Format
  einfach exportieren.
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Wie man einen Zylinder mit versetztem oberen Ende in Aspose.3D für Java erstellt
url: /de/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man einen Zylinder mit versetztem oberen Ende in Aspose.3D für Java erstellt

## Einführung

Wenn Sie **wie man einen Zylinder erstellt** Objekte mit einem benutzerdefinierten versetzten oberen Ende in einer Java‑basierten 3D‑Szene suchen, macht Aspose.3D den Prozess unkompliziert. In diesem Tutorial führen wir Sie durch jeden Schritt – vom Einrichten der Szene bis zum Export des finalen Modells als OBJ‑Datei – sodass Sie Zylinder mit versetztem oberen Ende sicher in Ihre Anwendungen integrieren können. Am Ende des Leitfadens beherrschen Sie das Erstellen von Zylinderformen mit benutzerdefinierten Versätzen in nur wenigen Codezeilen.

## Schnelle Antworten
- **Welche Bibliothek wird verwendet?** Aspose.3D for Java  
- **Kann ich die Oberseite eines Zylinders versetzen?** Ja, mit `setOffsetTop`  
- **Wie füge ich in Java einen Kindknoten hinzu?** Rufen Sie `createChildNode` am Wurzelknoten auf  
- **In welches Format kann ich exportieren?** Wavefront OBJ (`export 3d model obj`)  
- **Benötige ich eine Lizenz für Tests?** Eine temporäre Lizenz ist für die Evaluierung verfügbar  

## Was ist „wie man einen Zylinder erstellt“ mit einem versetzten oberen Ende?

Das Erstellen eines Zylinders mit versetztem oberen Ende bedeutet, dass die obere kreisförmige Fläche relativ zur Basis verschoben wird, wodurch Sie konische oder asymmetrische Formen modellieren können, ohne die Vertex‑Daten manuell zu bearbeiten. Aspose.3D bietet einen speziellen Konstruktor und eine `OffsetTop`‑Eigenschaft, um dies in nur wenigen Codezeilen zu erreichen.

## Warum Aspose.3D für Java verwenden?

- **High‑level API:** Keine Notwendigkeit, Low‑level Mesh‑Daten zu verwalten.  
- **Cross‑platform:** Funktioniert in jeder JVM‑kompatiblen Umgebung.  
- **Built‑in Exporter:** Direktes Speichern nach OBJ, STL, FBX und mehr.  
- **Erweiterbar:** Einfach Kindknoten hinzufügen, Transformationen anwenden und mit anderen Java‑Bibliotheken integrieren.

## Voraussetzungen

- **Java Development Kit (JDK)** – eine kompatible Version installiert.  
- **Aspose.3D for Java library** – Laden Sie die neueste JAR von der offiziellen Seite [hier](https://releases.aspose.com/3d/java/) herunter.  
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

### Schritt 1: Szene erstellen

Eine Szene fungiert als Container für alle 3D‑Objekte.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Schritt 2: Zylinder mit versetztem oberen Ende initialisieren

Hier beantworten wir **wie man einen Zylinder erstellt** mit einem benutzerdefinierten Versatz. Der Konstruktor definiert Radius, Höhe, Segmente, Stufen und ob der Zylinder geschlossen ist. Anschließend verschieben wir die Oberseite mit `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Schritt 3: Wie man **add child node Java** – Erster Zylinder anhängen

Wir erstellen einen Kindknoten unter dem Wurzelknoten der Szene und verschieben den Zylinder an die gewünschte Position.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Schritt 4: Zweiten Zylinder initialisieren (ohne Versatz)

Zum Vergleich fügen wir einen regulären Zylinder ohne Versatz hinzu.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Schritt 5: Wie man **add child node Java** – Zweiten Zylinder anhängen

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Schritt 6: Wie man **export OBJ** – Szene als OBJ speichern

Schließlich exportieren wir die gesamte Szene (beide Zylinder) als Wavefront‑OBJ‑Datei, die von den meisten 3D‑Tools unterstützt wird.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Wenn Sie das Programm ausführen, finden Sie `CustomizedOffsetTopCylinder.obj` im angegebenen Verzeichnis, bereit zum Öffnen in Blender, Maya oder jedem anderen OBJ‑kompatiblen Viewer.

## Warum das wichtig ist – Anwendungsfälle aus der Praxis

- **Architektonische Visualisierung:** Zylinder mit versetztem oberen Ende sind ideal, um Säulen zu modellieren, die zur Decke hin zulaufen.  
- **Mechanische Bauteile:** Erstellen Sie Kolben oder Getriebegehäuse, bei denen die Oberseite bewusst verschoben ist.  
- **Spiele-Assets:** Schnell verschiedene Pfeilerformen erzeugen, ohne Meshes von Hand zu erstellen.

## Wie man OBJ exportiert – Szene als OBJ speichern

Die Aspose 3D‑Export‑OBJ‑Funktion ermöglicht es Ihnen, Ihre Modelle fast in jede 3D‑Pipeline zu integrieren. Durch die Verwendung der Methode `scene.save(..., FileFormat.WAVEFRONTOBJ)` exportieren Sie **how to export obj** Dateien direkt aus Java und vermeiden den Einsatz von Drittanbieter‑Konvertern.

## Wie man **add child node Java** – Geometrie anhängen

Das Hinzufügen von Kindknoten ist der Standardweg, um einen Szenengraph zu organisieren. Jeder Aufruf von `createChildNode` liefert einen Knoten, der unabhängig transformiert werden kann, weshalb das Muster **add child node java** in diesem Tutorial zweimal vorkommt.

## Export 3D Model OBJ – Verwendung von Aspose 3D Export OBJ

Wenn Sie Ihre Modelle an Designer verteilen müssen, bietet die **export 3d model obj**‑Funktion eine leichte, textbasierte Darstellung, die in allen gängigen 3D‑Anwendungen funktioniert. Der gleiche API‑Aufruf aus Schritt 6 demonstriert den **aspose 3d export obj**‑Workflow.

## Häufige Probleme und Lösungen

| Problem | Grund | Lösung |
|---------|-------|--------|
| **OBJ-Datei ist leer** | Szene wurde nicht korrekt gespeichert oder falscher Pfad. | Stellen Sie sicher, dass das Ausgabeverzeichnis existiert und Sie Schreibrechte haben. |
| **Versatz nicht angewendet** | Verwendung einer älteren Aspose.3D-Version. | Aktualisieren Sie auf die neueste Bibliothek, in der `setOffsetTop` unterstützt wird. |
| **Kindknoten nicht sichtbar** | Transformation nicht angewendet. | Stellen Sie sicher, dass Sie `getTransform().setTranslation` nach dem Erstellen des Kindknotens aufrufen. |

## Häufig gestellte Fragen

**Q: Ist Aspose.3D mit verschiedenen Java‑IDEs kompatibel?**  
A: Ja, es funktioniert nahtlos mit Eclipse, IntelliJ IDEA, NetBeans und anderen IDEs.

**Q: Kann ich Texturen auf die erstellten 3D‑Objekte anwenden?**  
A: Absolut! Verwenden Sie die `Material`‑Klasse, um Texturen und Oberflächeneigenschaften zuzuweisen.

**Q: Gibt es Lizenzierungsoptionen für Aspose.3D?**  
A: Verschiedene Lizenzmodelle stehen zur Verfügung; Sie können sie [hier](https://purchase.aspose.com/buy) erkunden.

**Q: Wie kann ich Hilfe erhalten oder Erfahrungen teilen?**  
A: Treten Sie dem Aspose.3D‑Community‑Forum [hier](https://forum.aspose.com/c/3d/18) bei für Support und Diskussionen.

**Q: Ist eine temporäre Lizenz für Tests verfügbar?**  
A: Ja, eine temporäre Lizenz kann für die Evaluierung [hier](https://purchase.aspose.com/temporary-license/) erhalten werden.

**Zuletzt aktualisiert:** 2026-02-07  
**Getestet mit:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}