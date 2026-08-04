---
date: 2026-04-08
description: Erfahren Sie, wie Sie in Aspose.3D für Java einen Zylinder mit versetztem
  oberen Ende erstellen, einen Kindknoten in Java hinzufügen, das obere Ende versetzen,
  ein 3D‑Modell generieren und das OBJ mit einer temporären Aspose‑Lizenz exportieren.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Aspose Temporäre Lizenz – Zylinder mit versetztem oberen Ende erstellen
  (Java)
second_title: Aspose.3D Java API
title: Aspose Temporäre Lizenz – Zylinder mit versetztem oberen Ende erstellen (Java)
url: /de/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose Temporäre Lizenz – Zylinder mit versetztem oberen Ende erstellen (Java)

## Einführung

Wenn Sie **Zylinder**-Objekte mit einem benutzerdefinierten versetzten oberen Ende in einer Java‑basierten 3D‑Szene erstellen möchten, macht Aspose.3D den Prozess unkompliziert. In diesem Tutorial führen wir Sie durch jeden Schritt – vom Einrichten der Szene bis zum Export des finalen Modells als OBJ‑Datei – damit Sie Zylinder mit versetztem oberen Ende sicher in Ihre Anwendungen integrieren können. Am Ende des Leitfadens verstehen Sie außerdem, wie eine **aspose temporary license** Ihnen ermöglicht, diese Funktionen ohne vollständigen Kauf zu evaluieren.

## Schnelle Antworten
- **Welche Bibliothek wird verwendet?** Aspose.3D for Java  
- **Kann ich das obere Ende eines Zylinders versetzen?** Ja, mittels `setOffsetTop`  
- **Wie füge ich in Java einen Kindknoten hinzu?** Rufen Sie `createChildNode` am Wurzelknoten auf  
- **In welches Format kann ich exportieren?** Wavefront OBJ (`java export obj`)  
- **Benötige ich eine Lizenz für Tests?** Eine **aspose temporary license** ist für die Evaluierung verfügbar  

## Was ist die Aspose Temporäre Lizenz?

Eine **aspose temporary license** ist ein kurzzeitiger, kostenloser Evaluierungsschlüssel, der das komplette Funktionsspektrum von Aspose.3D for Java während Entwicklung und Tests freischaltet. Sie entfernt Evaluierungs‑Wasserzeichen und ermöglicht das Erzeugen von 3D‑Modelldateien wie OBJ, STL oder FBX, genau wie eine kostenpflichtige Lizenz.

## Warum Aspose.3D für Java verwenden?

- **High‑Level‑API:** Keine Notwendigkeit, Low‑Level‑Mesh‑Daten zu verwalten.  
- **Cross‑Platform:** Funktioniert in jeder JVM‑kompatiblen Umgebung.  
- **Integrierte Exporter:** Direktes Speichern nach OBJ, STL, FBX und mehr.  
- **Erweiterbar:** Einfach Kindknoten hinzufügen, Transformationen anwenden und mit anderen Java‑Bibliotheken integrieren.  

## Voraussetzungen

Bevor wir beginnen, stellen Sie sicher, dass Sie Folgendes haben:

- **Java Development Kit (JDK)** – eine kompatible Version installiert.  
- **Aspose.3D for Java library** – laden Sie das neueste JAR von der offiziellen Seite [here](https://releases.aspose.com/3d/java/) herunter.  
- Eine IDE Ihrer Wahl (Eclipse, IntelliJ IDEA, NetBeans usw.).

## Pakete importieren

Zuerst importieren Sie die Klassen, die wir benötigen. Platzieren Sie diese Anweisungen am Anfang Ihrer Java‑Datei:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Schritt‑für‑Schritt‑Anleitung

### Schritt 1: Erstellen einer Java‑3D‑Szene

Eine **java 3d scene** fungiert als Container für alle 3D‑Objekte.

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

### Schritt 3: Kindknoten in Java hinzufügen – Ersten Zylinder anhängen

Wir erstellen einen Kindknoten unter dem Wurzelknoten der Szene und verschieben den Zylinder an die gewünschte Position.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Schritt 4: Zweiten Zylinder initialisieren (ohne Versatz)

Zum Vergleich fügen wir einen regulären Zylinder ohne Versatz hinzu.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Schritt 5: Kindknoten in Java hinzufügen – Zweiten Zylinder anhängen

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Schritt 6: Java Export OBJ – Szene als OBJ speichern

Abschließend **java export obj** wir die gesamte Szene (beide Zylinder) als Wavefront‑OBJ‑Datei, die von vielen 3D‑Werkzeugen unterstützt wird.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Wenn Sie das Programm ausführen, finden Sie `CustomizedOffsetTopCylinder.obj` im angegebenen Verzeichnis, bereit zum Öffnen in Blender, Maya oder jedem anderen OBJ‑kompatiblen Viewer.

## Wie man ein 3D‑Modell erzeugt und OBJ in Java exportiert

Die Kombination aus `Scene.save(..., FileFormat.WAVEFRONTOBJ)` und der **aspose temporary license** ermöglicht es Ihnen, **3d‑Modelle** schnell zu **generieren**, ohne externe Konverter zu benötigen. Das ist besonders praktisch beim Prototyping oder beim Teilen von Assets mit Designern.

## Praxisbeispiele

- **Architektonische Visualisierung:** Zylinder mit versetztem oberen Ende modellieren Säulen, die zur Decke hin zulaufen.  
- **Mechanische Bauteile:** Erstellen Sie Kolben oder Getriebegehäuse, bei denen die Oberseite bewusst verschoben ist.  
- **Spiele‑Assets:** Erzeugen Sie variierende Pfeilerformen on‑the‑fly, wodurch der Bedarf an handgefertigten Meshes reduziert wird.  

## Häufige Probleme und Lösungen

| Problem | Ursache | Lösung |
|-------|--------|-----|
| **OBJ-Datei ist leer** | Szene wurde nicht korrekt gespeichert oder falscher Pfad. | Stellen Sie sicher, dass das Ausgabeverzeichnis existiert und Sie Schreibrechte haben. |
| **Versatz nicht angewendet** | Verwendung einer älteren Aspose.3D‑Version. | Aktualisieren Sie auf die neueste Bibliothek, in der `setOffsetTop` unterstützt wird. |
| **Kindknoten nicht sichtbar** | Transformation wurde nicht angewendet. | Stellen Sie sicher, dass Sie `getTransform().setTranslation` nach dem Erstellen des Kindknotens aufrufen. |

## Häufig gestellte Fragen

**Q: Ist Aspose.3D mit verschiedenen Java‑IDEs kompatibel?**  
A: Ja, es funktioniert nahtlos mit Eclipse, IntelliJ IDEA, NetBeans und anderen IDEs.

**Q: Kann ich Texturen auf die erstellten 3D‑Objekte anwenden?**  
A: Absolut! Verwenden Sie die `Material`‑Klasse, um Texturen und Oberflächeneigenschaften zuzuweisen.

**Q: Gibt es Lizenzierungsoptionen für Aspose.3D?**  
A: Verschiedene Lizenzmodelle stehen zur Verfügung; Sie können sie [here](https://purchase.aspose.com/buy) erkunden.

**Q: Wie kann ich Hilfe erhalten oder Erfahrungen teilen?**  
A: Treten Sie dem Aspose.3D‑Community‑Forum [here](https://forum.aspose.com/c/3d/18) für Unterstützung und Diskussion bei.

**Q: Ist eine temporäre Lizenz für Tests verfügbar?**  
A: Ja, eine **aspose temporary license** kann für die Evaluierung [here](https://purchase.aspose.com/temporary-license/) erhalten werden.

---

**Last Updated:** 2026-04-08  
**Tested With:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}