---
date: 2025-12-18
description: Erfahren Sie, wie Sie eine 3D‑Szene erstellen und eine OBJ‑Datei mit
  Aspose.3D für Java speichern. Folgen Sie unserer Schritt‑für‑Schritt‑Anleitung zur
  linearen Extrusionsrichtung.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: 3D‑Szene erstellen – Extrusionsrichtung festlegen Aspose.3D Java
url: /de/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D‑Szene erstellen – Extrusionsrichtung festlegen Aspose.3D Java

## Einleitung

In diesem Tutorial lernen Sie **wie man 3d scene**‑Objekte erstellt und die Extrusionsrichtung mit Aspose.3D für Java steuert. Egal, ob Sie architektonische Visualisierungen, Produktprototypen oder Spiel‑Assets erstellen, das Beherrschen linearer Extrusion gibt Ihnen die Flexibilität, komplexe Formen schnell zu modellieren. Wir gehen jeden Schritt durch, vom Hinzufügen von Nodes in Java bis zum **Export 3d model obj**‑Dateien, sodass Sie das Ergebnis sofort sehen können.

## Schnelle Antworten
- **Was bedeutet “create 3d scene”?** Es bedeutet, ein Aspose.3D `Scene`‑Objekt zu initialisieren, das alle Geometrien, Lichter und Kameras enthält.  
- **Wie setze ich die Extrusionsrichtung?** Verwenden Sie die Methode `setDirection(Vector3)` auf einer `LinearExtrusion`‑Instanz.  
- **Welches Format sollte ich zum Export verwenden?** Das OBJ‑Format (`FileFormat.WAVEFRONTOBJ`) wird breit unterstützt für 3‑D‑Workflows.  
- **Brauche ich eine Lizenz für Aspose.3D?** Eine kostenlose Testversion funktioniert für die Entwicklung; für die Produktion ist eine kommerzielle Lizenz erforderlich.  
- **Kann ich weitere Nodes in Java hinzufügen?** Ja – verwenden Sie `scene.getRootNode().createChildNode()`, um beliebig viele Objekte hinzuzufügen.

## Was ist ein “create 3d scene”‑Workflow?

Ein **create 3d scene**‑Workflow beginnt mit einem leeren `Scene`‑Objekt, fügt Geometrie (wie extrudierte Profile) hinzu, positioniert sie mit Transformations‑Operationen und speichert schließlich die Szene in einem Dateiformat wie OBJ. Dieses Muster ist das Rückgrat der meisten 3‑D‑Anwendungen, die mit Aspose.3D erstellt werden.

## Warum die Extrusionsrichtung festlegen?

Das Festlegen der Extrusionsrichtung ermöglicht es Ihnen, die Form während der Extrusion zu kippen, zu drehen oder zu verzerren, wodurch Sie die endgültige Geometrie ohne zusätzliche Nachbearbeitung kontrollieren können. Besonders nützlich ist das für:

- Erstellen von konischen Säulen oder kundenspezifisch geformten Rohren.  
- Ausrichten von Extrusionen an nicht‑standardmäßigen Achsen in mechanischen Bauteilen.  
- Erzeugen künstlerischer Formen für visuelle Effekte.

## Voraussetzungen

- Grundkenntnisse in Java.  
- Aspose.3D‑Bibliothek installiert – laden Sie sie von [hier](https://releases.aspose.com/3d/java/) herunter.  
- Eine IDE wie Eclipse oder IntelliJ IDEA.

## Pakete importieren

Zuerst importieren Sie die erforderlichen Aspose.3D‑Klassen:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Schritt 1: Basisprofil initialisieren

Erstellen Sie das 2‑D‑Profil, das extrudiert werden soll. In diesem Beispiel verwenden wir ein abgerundetes Rechteck:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Pro‑Tipp:** Passen Sie den Rundungsradius an, um zu steuern, wie scharf oder glatt die Ecken des Rechtecks vor der Extrusion erscheinen.

## Schritt 2: Szene erstellen

Jetzt **erstellen wir eine 3d scene**, die unsere Objekte hostet:

```java
Scene scene = new Scene();
```

## Schritt 3: Nodes in Java hinzufügen – Positionierung der Objekte

Wir fügen dem Root‑Node der Szene zwei Child‑Nodes (links und rechts) hinzu und verschieben den linken leicht zur Seite:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Schritt 4: Wie extrudieren – Linker Node (Standardrichtung)

Extrudieren Sie das Profil am linken Node unter Verwendung der Standard‑Z‑Achsen‑Richtung. Wir setzen außerdem eine vollständige 360°‑Drehung und erhöhen die Slice‑Anzahl für mehr Glätte:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Schritt 5: Wie die Richtung setzen – Rechter Node

Hier **setzen wir die Richtung**, indem wir einen benutzerdefinierten `Vector3` übergeben. Dies kippt die Extrusion in Richtung des Vektors (0.3, 0.2, 1):

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Schritt 6: OBJ‑Datei speichern – 3D‑Modell exportieren

Abschließend **speichern wir die obj file**, um das Ergebnis in jedem 3‑D‑Betrachter zu sehen:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Wenn Sie die erzeugte OBJ‑Datei öffnen, sehen Sie zwei extrudierte Rechtecke: eines mit der Standard‑Richtung und eines, das gemäß dem gesetzten Vektor gekippt ist.

## Häufige Probleme und Lösungen

| Problem | Grund | Lösung |
|---------|-------|--------|
| OBJ‑Datei erscheint leer | Szene nicht gespeichert oder Pfad inkorrekt | Überprüfen Sie, dass `MyDir` auf einen beschreibbaren Ordner zeigt und der Dateiname mit `.obj` endet. |
| Extrusion wirkt flach | `setSlices` zu niedrig | Erhöhen Sie `setSlices` (z. B. 200) für glattere Geometrie. |
| Richtung scheint unverändert | Vektor nicht normalisiert | Verwenden Sie einen normalisierten `Vector3` oder passen Sie die Werte an, um die gewünschte Neigung zu erreichen. |

## Häufig gestellte Fragen

### Q1: Kann ich Aspose.3D mit anderen Programmiersprachen verwenden?
A1: Aspose.3D unterstützt verschiedene Sprachen, darunter .NET und Java.

### Q2: Gibt es eine kostenlose Testversion für Aspose.3D?
A2: Ja, Sie können die Funktionen von Aspose.3D mit einer kostenlosen Testversion [hier](https://releases.aspose.com/) erkunden.

### Q3: Wo finde ich die detaillierte Dokumentation für Aspose.3D für Java?
A3: Die umfassende Dokumentation ist [hier](https://reference.aspose.com/3d/java/) verfügbar.

### Q4: Wie kann ich Support für Aspose.3D erhalten?
A4: Besuchen Sie das [Aspose.3D‑Forum](https://forum.aspose.com/c/3d/18) für Unterstützung oder Fragen.

### Q5: Gibt es temporäre Lizenzen für Aspose.3D?
A5: Ja, Sie können eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/) erhalten.

---

**Last Updated:** 2025-12-18  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}