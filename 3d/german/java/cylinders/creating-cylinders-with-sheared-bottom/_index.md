---
date: 2025-12-09
description: Erfahren Sie, wie Sie Aspose verwenden, um benutzerdefinierte Zylinder
  mit abgeschrägten Böden in Java zu erstellen, ideal für 3D‑Modellierung in Java
  und zum Speichern von Szenen als OBJ.
language: de
linktitle: 'How to Use Aspose: Create Cylinders with Sheared Bottom in Java'
second_title: Aspose.3D Java API
title: 'Wie man Aspose verwendet: Zylinder mit abgeschrägtem Boden in Java erstellen'
url: /java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man Aspose verwendet: Zylinder mit schrägem Boden in Java erstellen

## Einleitung

In diesem praxisorientierten Tutorial entdecken Sie **wie man Aspose** verwendet, um einen Zylinder zu erstellen, dessen Boden schräg ist – eine Technik, die häufig in *java 3d modeling* Projekten benötigt wird. Wir gehen jeden Schritt durch, vom Einrichten der Szene bis zum Speichern des finalen Modells als OBJ‑Datei. Am Ende haben Sie ein wiederverwendbares Code‑Snippet, das Sie in jede Java‑basierte 3D‑Anwendung einbinden können.

## Schnelle Antworten
- **Was bedeutet „shear bottom“?** Es kippt die Basis des Zylinders um einen angegebenen Winkel in der XY‑Ebene.  
- **Welche Bibliothek übernimmt die 3D‑Mathematik?** Aspose.3D for Java stellt die Klassen `Cylinder` und `Vector2` bereit.  
- **Benötige ich eine Lizenz, um das Beispiel auszuführen?** Eine temporäre Lizenz funktioniert für die Evaluierung; für die Produktion ist eine Voll‑Lizenz erforderlich.  
- **Kann ich das Modell in andere Formate exportieren?** Ja – verwenden Sie `scene.save(..., FileFormat.WAVEFRONTOBJ)`, um eine OBJ‑Datei zu erhalten.  
- **Welche Java‑Version wird benötigt?** JDK 8 oder höher reicht aus.

## Was bedeutet „how to use aspose“ im Kontext von 3D‑Modellierung?

Aspose.3D for Java ist eine High‑Level‑API, die die Komplexität von 3D‑Geometrie, Dateiformaten und Transformationen abstrahiert. Anstatt sich mit Low‑Level‑Vertex‑Buffers zu befassen, rufen Sie intuitive Methoden wie `new Cylinder(...)` auf und lassen Aspose die schwere Arbeit erledigen.

## Warum Aspose für Java‑3D‑Modellierung verwenden?

- **Schnelle Entwicklung:** Erstellen Sie komplexe Formen mit wenigen Code‑Zeilen.  
- **Breite Formatunterstützung:** Exportieren Sie zu OBJ, STL, FBX und mehr.  
- **Plattformübergreifend:** Funktioniert auf jedem Betriebssystem, das Java unterstützt.  
- **Konsistente API:** Der gleiche Code funktioniert für Desktop-, Server‑ oder Android‑Umgebungen.

## Voraussetzungen

Stellen Sie vor Beginn sicher, dass Sie Folgendes haben:

- **Java Development Kit (JDK) 8+** installiert und in Ihrer IDE konfiguriert.  
- **Aspose.3D for Java** Bibliothek zum Klassenpfad Ihres Projekts hinzugefügt. Sie können sie von der offiziellen Seite [hier](https://releases.aspose.com/3d/java/) herunterladen.  
- **Eine temporäre oder Voll‑Lizenz** (optional für Testläufe).

## Pakete importieren

Um zu beginnen, importieren Sie die wesentlichen Aspose.3D‑Klassen und Java‑Hilfsmittel:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Schritt 1: Eine Szene erstellen

Eine *Szene* ist der Container, der alle 3D‑Objekte, Lichter und Kameras enthält. Denken Sie daran als Bühne, auf der Sie Ihre Zylinder platzieren.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Schritt 2: Zylinder 1 erstellen (Schräger Boden)

Jetzt erstellen wir den ersten Zylinder und wenden eine Schertransformation auf dessen Boden an. Die Methode `setShearBottom` nimmt ein `Vector2` entgegen, wobei die X‑Komponente den Scherfaktor entlang der X‑Achse und die Y‑Komponente entlang der Y‑Achse darstellt.

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

> **Pro Tipp:** Der Scherfaktor `0.83` entspricht etwa 47,5°; passen Sie diesen Wert an, um den genauen gewünschten Winkel zu erreichen.

## Schritt 3: Zylinder 2 erstellen (Standard)

Zum Vergleich fügen wir einen zweiten Zylinder ohne Scherung hinzu. Das hilft Ihnen, den visuellen Unterschied direkt in der exportierten OBJ‑Datei zu sehen.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Schritt 4: Szene speichern (Wie man Szene als OBJ speichert)

Abschließend speichern wir die Szene auf die Festplatte. Die Konstante `FileFormat.WAVEFRONTOBJ` weist Aspose an, eine OBJ‑Datei zu schreiben, die von vielen 3D‑Editoren wie Blender und Maya unterstützt wird.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Hinweis:** Ersetzen Sie `"Your Document Directory"` durch einen absoluten oder relativen Pfad, der für Ihre Umgebung geeignet ist.

## Häufige Probleme und Lösungen

| Problem | Ursache | Lösung |
|-------|-------|----------|
| **Zylinder erscheint flach** | Falscher Scherfaktor (außerhalb des Bereichs 0‑1) | Verwenden Sie einen Wert zwischen 0 und 1; passen Sie ihn schrittweise beim Vorschau‑Rendern an. |
| **OBJ‑Datei wird im Viewer nicht geladen** | Fehlende Materialdefinitionen | Fügen Sie jedem Knoten ein einfaches Material hinzu oder exportieren Sie als STL für reines Geometrietest. |
| **LicenseException zur Laufzeit** | Keine gültige Lizenzdatei | Platzieren Sie `Aspose.3D.lic` im Projektstammverzeichnis oder verwenden Sie die Klasse `License`, um sie programmgesteuert zu laden. |

## Häufig gestellte Fragen

### Q1: Kann ich Aspose.3D for Java mit anderen Java‑3D‑Bibliotheken verwenden?
**A:** Aspose.3D for Java ist so konzipiert, dass es eigenständig funktioniert. Während Sie es mit anderen Bibliotheken integrieren können, bietet es von selbst einen vollständigen Funktionsumfang für die meisten 3D‑Modellierungsaufgaben.

### Q2: Ist Aspose.3D für Einsteiger in die 3D‑Modellierung geeignet?
**A:** Ja, Aspose.3D bietet eine benutzerfreundliche API, die Low‑Level‑Details abstrahiert und sie sowohl für Einsteiger als auch für erfahrene Entwickler zugänglich macht.

### Q3: Wo finde ich zusätzlichen Support für Aspose.3D for Java?
**A:** Besuchen Sie das [Aspose.3D‑Forum](https://forum.aspose.com/c/3d/18) für Community‑Support, Tutorials und Diskussionen.

### Q4: Wie kann ich eine temporäre Lizenz für Aspose.3D erhalten?
**A:** Sie können eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/) erhalten.

### Q5: Kann ich Aspose.3D for Java kaufen?
**A:** Ja, Sie können Aspose.3D for Java [hier](https://purchase.aspose.com/buy) erwerben.

## Fazit

Wir haben **wie man Aspose** verwendet, um zwei Zylinder zu erstellen – einen mit schrägem Boden und einen Standard‑Zylinder – und das Ergebnis als OBJ‑Datei gespeichert. Diese Technik ist ein Baustein für komplexere 3D‑Modelle, wie benutzerdefinierte Teile, architektonische Elemente oder Spiel‑Assets. Experimentieren Sie gern mit verschiedenen Scherwerten, Radien und Höhen, um Ihren Projektanforderungen gerecht zu werden.

---

**Zuletzt aktualisiert:** 2025-12-09  
**Getestet mit:** Aspose.3D for Java 24.11 (aktuell zum Zeitpunkt des Schreibens)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}