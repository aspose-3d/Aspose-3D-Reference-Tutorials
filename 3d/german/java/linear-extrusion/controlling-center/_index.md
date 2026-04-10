---
date: 2026-02-20
description: Lernen Sie ein Java‑3D‑Grafik‑Tutorial zur Steuerung des Zentrums bei
  linearer Extrusion mit Aspose.3D, einschließlich wie man den Rundungsradius einstellt
  und die OBJ‑Datei in Java speichert.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Java‑3D‑Grafik‑Tutorial – Mittelpunkt bei linearer Extrusion
url: /de/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D Graphics Tutorial – Center in Linear Extrusion

## Einführung

Wenn Sie 3D‑Visualisierungen in Java erstellen, ist das Beherrschen von Extrusions‑Techniken unerlässlich. Dieses **java 3d graphics tutorial** führt Sie durch die Steuerung des Zentrums einer linearen Extrusion mit Aspose.3D für Java, sodass Sie präzise, symmetrische Modelle ohne zusätzlichen Rechenaufwand erzeugen können. Am Ende dieses Leitfadens verstehen Sie, warum die `center`‑Eigenschaft wichtig ist, wie Sie **Rundungsradius festlegen** und wie Sie **save OBJ file java**‑kompatiblen Output erzeugen.

## Schnellantworten
- **Was bewirkt die center‑Eigenschaft?** Sie bestimmt, ob die Extrusion symmetrisch um den Ursprung des Profils liegt.  
- **Benötige ich eine Lizenz, um den Code auszuführen?** Eine temporäre Lizenz reicht für Tests; für die Produktion ist eine Voll‑Lizenz erforderlich.  
- **Welches Dateiformat wird für das Ergebnis verwendet?** Die Szene wird als Wavefront‑OBJ‑Datei gespeichert.  
- **Kann ich die Anzahl der Scheiben ändern?** Ja, verwenden Sie `setSlices(int)` am `LinearExtrusion`‑Objekt.  
- **Ist Aspose.3D mit Java 8+ kompatibel?** Absolut – es unterstützt alle modernen Java‑Versionen.

## Was ist ein java 3d graphics tutorial?

Ein **java 3d graphics tutorial** erklärt Schritt für Schritt, wie man Java‑Bibliotheken nutzt, um dreidimensionale Objekte zu erstellen, zu manipulieren und zu rendern. In diesem Fall konzentrieren wir uns auf die Extrusions‑API von Aspose.3D, die 2‑D‑Profile in vollwertige 3‑D‑Meshes umwandelt.

## Warum Aspose.3D für Java verwenden?

- **High‑Level‑API** – Keine Notwendigkeit, low‑level Mesh‑Berechnungen zu schreiben.  
- **Cross‑Format‑Support** – Export nach OBJ, FBX, STL und mehr.  
- **Performance‑optimiert** – Handhabt große Szenen effizient.  
- **Umfangreiche Dokumentation** – Enthält Beispiele wie das untenstehende.

## Voraussetzungen

Bevor wir starten, stellen Sie sicher, dass Sie Folgendes haben:

1. **Java Development Environment** – JDK 8 oder neuer installiert.  
2. **Aspose.3D for Java** – Laden Sie die Bibliothek und Dokumentation [hier](https://reference.aspose.com/3d/java/) herunter.  
3. **Document Directory** – Erstellen Sie einen Ordner auf Ihrem Rechner, um erzeugte Dateien zu speichern; wir nennen ihn **„Your Document Directory.“**

## Pakete importieren

Importieren Sie in Ihrer Java‑IDE die Aspose.3D‑Klassen, die Sie benötigen. Dadurch erhält der Compiler Zugriff auf die Extrusions‑ und Szenen‑Erstellungs‑Funktionen.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Schritt‑für‑Schritt‑Anleitung

### Schritt 1: Basis‑Profil festlegen

Erzeugen Sie zunächst die 2‑D‑Form, die extrudiert werden soll. Hier verwenden wir ein Rechteck und **set rounding radius** auf 0.3, wodurch die Ecken abgerundet werden.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Schritt 2: 3D‑Szene erstellen

Ein `Scene`‑Objekt fungiert als Container für alle 3‑D‑Knoten, Lichter und Kameras.

```java
Scene scene = new Scene();
```

### Schritt 3: Linke und rechte Knoten hinzufügen

Wir platzieren zwei separate Knoten nebeneinander, damit Sie die Extrusion mit und ohne Zentrierung vergleichen können.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Schritt 4: Lineare Extrusion – Kein Zentrum (Linker Knoten)

Erzeugen Sie die Extrusion am linken Knoten, deaktivieren Sie die Zentrierung und begrenzen Sie das Mesh auf drei Scheiben für eine Low‑Poly‑Vorschau.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Schritt 5: Boden‑Ebene zum Referenzieren hinzufügen (Linker Knoten)

Eine dünne Box dient als visueller Boden und hilft Ihnen, die Orientierung der Extrusion zu erkennen.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Schritt 6: Lineare Extrusion – Zentriert (Rechter Knoten)

Wiederholen Sie nun die Extrusion, diesmal mit aktiviertem `center`. Die Geometrie ist dann symmetrisch zum Ursprung des Profils.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Schritt 7: Boden‑Ebene zum Referenzieren hinzufügen (Rechter Knoten)

Die gleiche Boden‑Ebene für die rechte Seite, um den Vergleich klar zu machen.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Schritt 8: 3D‑Szene speichern

Exportieren Sie schließlich die gesamte Szene in eine Wavefront‑OBJ‑Datei – ein Format, das in den meisten 3‑D‑Editoren problemlos verwendet werden kann.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Häufige Probleme und Lösungen

| Problem | Warum es passiert | Lösung |
|-------|----------------|-----|
| **Extrusion erscheint versetzt** | `setCenter(false)` lässt das Profil an seiner Ecke verankert. | Verwenden Sie `setCenter(true)` für symmetrische Ergebnisse. |
| **OBJ‑Datei ist leer** | Ausgabeverzeichnis‑Pfad ist falsch oder Schreibrechte fehlen. | Stellen Sie sicher, dass `MyDir` auf einen existierenden Ordner zeigt und die Anwendung Schreibzugriff hat. |
| **Abgerundete Ecken wirken scharf** | Der Rundungsradius ist im Verhältnis zur Rechteckgröße zu klein. | Erhöhen Sie den Radiuswert (z. B. `setRoundingRadius(0.5)`). |

## Häufig gestellte Fragen

### Q1: Kann ich Aspose.3D für Java in kommerziellen Projekten verwenden?

A1: Ja, Aspose.3D für Java ist für den kommerziellen Einsatz verfügbar. Lizenzdetails finden Sie [hier](https://purchase.aspose.com/buy).

### Q2: Gibt es eine kostenlose Testversion?

A2: Ja, Sie können eine kostenlose Testversion von Aspose.3D für Java [hier](https://releases.aspose.com/) ausprobieren.

### Q3: Wo finde ich Support für Aspose.3D für Java?

A3: Das Aspose.3D‑Community‑Forum ist ein guter Ort, um Unterstützung zu erhalten und Erfahrungen zu teilen. Besuchen Sie das Forum [hier](https://forum.aspose.com/c/3d/18).

### Q4: Benötige ich eine temporäre Lizenz für Tests?

A4: Ja, wenn Sie eine temporäre Lizenz für Testzwecke benötigen, können Sie diese [hier](https://purchase.aspose.com/temporary-license/) erhalten.

### Q5: Wo finde ich die Dokumentation?

A5: Die Dokumentation für Aspose.3D für Java ist verfügbar [hier](https://reference.aspose.com/3d/java/).

## Fazit

Durch das Abschließen dieses **java 3d graphics tutorial** wissen Sie jetzt, wie Sie das Zentrum einer linearen Extrusion steuern, den Rundungsradius anpassen und **save OBJ file java**‑Ausgabe mit Aspose.3D speichern. Diese Techniken geben Ihnen feine Kontrolle über die Mesh‑Symmetrie, was für Spiel‑Assets, CAD‑Prototypen und wissenschaftliche Visualisierungen entscheidend ist. Experimentieren Sie gern mit verschiedenen Profilen, Scheibenzahlen und Exportformaten, um Ihre 3‑D‑Werkzeugkiste zu erweitern.

---

**Zuletzt aktualisiert:** 2026-02-20  
**Getestet mit:** Aspose.3D für Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}