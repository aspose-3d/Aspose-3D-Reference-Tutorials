---
date: 2026-02-22
description: Erfahren Sie, wie Sie mit Aspose.3D für Java 3D‑Extrusionen mit Scheiben
  erstellen. Diese Schritt‑für‑Schritt‑Anleitung behandelt lineare Extrusion, das
  Festlegen des Rundungsradius und das Exportieren von OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: 3D-Extrusion mit Scheiben erstellen – Aspose.3D für Java
url: /de/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Erstellen von 3D-Extrusionen mit Slices – Aspose.3D für Java

## Einführung

Wenn Sie **3D-Extrusion**‑Objekte erstellen müssen, die glatt und präzise aussehen, ist die Kontrolle der Anzahl der Slices der Schlüssel. In diesem Tutorial zeigen wir, wie man Slices beim Durchführen einer linearen Extrusion mit Aspose.3D für Java angibt. Sie werden sehen, warum die Slice‑Anzahl wichtig ist, wie man einen Rundungsradius festlegt und wie man das Ergebnis als OBJ‑Datei exportiert, die in jeder 3D‑Pipeline verwendet werden kann.

## Schnelle Antworten
- **Was steuert “slices”?** Die Anzahl der Zwischenschnitte, die verwendet werden, um die Extrusionsfläche zu approximieren.  
- **Welche Methode legt die Slice‑Anzahl fest?** `LinearExtrusion.setSlices(int)`  
- **Kann ich den Rundungsradius des Profils ändern?** Ja, über `RectangleShape.setRoundingRadius(double)`  
- **Welches Dateiformat wird in diesem Beispiel verwendet?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Benötige ich eine Lizenz, um den Code auszuführen?** Eine kostenlose Testversion reicht für die Evaluierung; für den Produktionseinsatz ist eine kommerzielle Lizenz erforderlich.

## Was ist eine lineare Extrusion mit Slices?

Eine lineare Extrusion nimmt ein 2‑D‑Profil (wie ein Rechteck) und streckt es entlang einer geraden Linie, um einen 3‑D‑Körper zu erzeugen. Durch Angabe von **Slices** teilen Sie Aspose.3D mit, wie viele Zwischenschritte erzeugt werden sollen, was die Glätte gekrümmter Kanten wie bei einem abgerundeten Rechteck direkt beeinflusst.

## Warum Aspose.3D für Java zur Erstellung von 3D-Extrusionen verwenden?

* **Vollständige Kontrolle** – Sie können die Slice‑Anzahl, den Rundungsradius und das Exportformat programmgesteuert anpassen.  
* **Plattformübergreifend** – Funktioniert in jeder Java‑fähigen Umgebung ohne native Abhängigkeiten.  
* **Exportflexibilität** – Direktes Speichern nach OBJ, FBX, STL und vielen anderen Formaten.

## Voraussetzungen

1. **Java Development Kit** – JDK 8 oder höher installiert.  
2. **Aspose.3D für Java** – Laden Sie die Bibliothek von der offiziellen Seite [hier](https://releases.aspose.com/3d/java/) herunter.  
3. Eine IDE oder ein Texteditor Ihrer Wahl.

## Pakete importieren

Fügen Sie Ihrem Projekt den Aspose.3D‑Namensraum hinzu, damit Sie auf die 3‑D‑Modellierungsklassen zugreifen können.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Schritt‑für‑Schritt‑Anleitung

### Schritt 1: Szene einrichten und Profil definieren

Zuerst erstellen wir ein `RectangleShape` und geben ihm einen **Rundungsradius**, damit die Ecken glatt sind. Anschließend initialisieren wir ein neues `Scene`, das alle Geometrie enthält.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Schritt 2: **Child‑Node**‑Objekte für jede Extrusion erstellen

Jedes Geometrie‑Element befindet sich unter einem `Node`. Hier erzeugen wir zwei Geschwister‑Nodes – einen für eine Low‑Slice‑Extrusion und einen für eine High‑Slice‑Extrusion – und verschieben den linken Node leicht zur Seite, damit die Ergebnisse leicht zu vergleichen sind.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Schritt 3: Lineare Extrusion durchführen und **Slices setzen**

Jetzt erstellen wir tatsächlich **3D‑Extrusions**‑Objekte. Der Konstruktor `LinearExtrusion` nimmt das Profil und die Extrusionstiefe entgegen. Mit einer **anonymen inneren Klasse** rufen wir `setSlices` auf, um die Glätte zu steuern. Der linke Node erhält nur 2 Slices (grob), während der rechte Node 10 Slices (glatt) bekommt.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Schritt 4: **OBJ exportieren** – Szene speichern

Abschließend schreiben wir die Szene in eine Wavefront‑OBJ‑Datei, ein Format, das von vielen 3‑D‑Editoren und Spiel‑Engines unterstützt wird. Dies demonstriert die **export obj java**‑Funktionalität von Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Häufige Probleme und Lösungen

| Problem | Warum es passiert | Lösung |
|-------|----------------|-----|
| **Extrusion appears flat** | Slice count set to 1 or 0 | Ensure `setSlices` is called with a value ≥ 2. |
| **Rounded corners look jagged** | Rounding radius too small relative to slice count | Increase either the radius or the slice count for smoother curves. |
| **File not found on save** | `MyDir` points to a non‑existent folder | Create the directory beforehand or use an absolute path. |

## Häufig gestellte Fragen

**Q: Wie kann ich Aspose.3D für Java herunterladen?**  
A: Sie können die Bibliothek [hier](https://releases.aspose.com/3d/java/) herunterladen.

**Q: Wo finde ich die Dokumentation für Aspose.3D?**  
A: Sie finden die Dokumentation [hier](https://reference.aspose.com/3d/java/).

**Q: Gibt es eine kostenlose Testversion?**  
A: Ja, Sie können eine kostenlose Testversion [hier](https://releases.aspose.com/) ausprobieren.

**Q: Wie erhalte ich Support für Aspose.3D?**  
A: Besuchen Sie das Support‑Forum [hier](https://forum.aspose.com/c/3d/18).

**Q: Kann ich eine temporäre Lizenz erwerben?**  
A: Ja, eine temporäre Lizenz kann [hier](https://purchase.aspose.com/temporary-license/) erworben werden.

---

**Zuletzt aktualisiert:** 2026-02-22  
**Getestet mit:** Aspose.3D für Java 24.11 (zum Zeitpunkt des Schreibens aktuell)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}