---
date: 2025-12-17
description: Erfahren Sie, wie Sie ein verdrehtes 3D‑Modell mit Aspose.3D für Java
  mittels linearer Extrusion mit Drehung erstellen und die OBJ‑Datei in Java exportieren.
  Folgen Sie unserer Schritt‑für‑Schritt‑Anleitung.
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Erstellen eines verdrehten 3D‑Modells – Anwendung einer Verdrehung bei linearer
  Extrusion mit Aspose.3D für Java
url: /de/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Anwenden von Twist bei linearer Extrusion mit Aspose.3D für Java

## Einleitung

Willkommen zu diesem Schritt‑für‑Schritt‑Tutorial, wie man ein verdrehtes 3D‑Modell erstellt, indem man während der linearen Extrusion einen Twist anwendet, mit Aspose.3D für Java. Egal, ob Sie architektonische Visualisierungen, Spiel‑Assets oder technische Prototypen erstellen, das Hinzufügen eines Twists kann Ihrer Geometrie mit nur wenigen Codezeilen ein dynamisches, spiralförmiges Aussehen verleihen.

## Schnelle Antworten
- **Was bedeutet „twist“ bei der Extrusion?** Sie dreht das Profil um die Extrusionsachse, während die Form verlängert wird.  
- **Welche API‑Klasse verarbeitet den Twist?** `LinearExtrusion` stellt die Methode `setTwist` bereit.  
- **Benötige ich eine Lizenz, um das Beispiel auszuführen?** Eine kostenlose Testversion funktioniert für die Evaluierung; für die Produktion ist eine kommerzielle Lizenz erforderlich.  
- **Kann ich das Ergebnis als OBJ exportieren?** Ja, verwenden Sie `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Welche Java‑Version wird benötigt?** Java 8 oder höher wird vollständig unterstützt.

## Voraussetzungen

Bevor Sie in das Tutorial eintauchen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllt haben:

- Java-Entwicklungsumgebung: Stellen Sie sicher, dass Java auf Ihrem System installiert ist.  
- Aspose.3D-Bibliothek: Laden Sie die Aspose.3D-Bibliothek für Java von dem [download link](https://releases.aspose.com/3d/java/) herunter und installieren Sie sie.  
- Dokumentation: Konsultieren Sie die [Aspose.3D documentation](https://reference.aspose.com/3d/java/) für umfassende Anleitungen.

## Pakete importieren

Bevor Sie mit dem Codieren beginnen, importieren Sie die notwendigen Pakete in Ihr Java‑Projekt. Hier ein Beispiel, wie das geht:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Dokumentverzeichnis festlegen

Zuerst definieren Sie, wo die erzeugte 3D‑Datei gespeichert werden soll.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Basisprofil initialisieren

Als Nächstes erstellen Sie die Form, die extrudiert werden soll. In diesem Beispiel verwenden wir ein Rechteck mit einem kleinen Abrundungsradius.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Eine Szene erstellen

Ein `Scene`‑Objekt fungiert als Container für alle 3D‑Knoten.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Knoten erstellen

Fügen Sie der Szene zwei Kindknoten hinzu – einer bleibt gerade, der andere erhält den Twist.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Linear Extrusion Twist

Jetzt führen wir **linear extrusion twist** für beide Knoten aus. Der linke Knoten bekommt einen 0°‑Twist (gerade), während der rechte Knoten einen 90°‑Twist erhält, wodurch eine spiralförmige Form entsteht. Wir setzen außerdem die Anzahl der Slices, um eine glatte Geometrie zu gewährleisten.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## OBJ-Datei exportieren Java

Speichern Sie schließlich die Szene im weit verbreiteten OBJ‑Format. Dies demonstriert die **export OBJ file Java**‑Fähigkeit von Aspose.3D.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Warum das wichtig ist

Das Erstellen eines verdrehten 3D‑Modells liefert Ihnen einen kraftvollen visuellen Effekt, ohne externe Modellierungswerkzeuge zu benötigen. Besonders nützlich ist es für:

- **Mechanische Teile**, die spiralförmige Merkmale benötigen (z. B. Federn, Schrauben).  
- **Künstlerische Designs**, bei denen eine subtile Spirale visuelles Interesse erzeugt.  
- **Spiel‑Assets**, die von Low‑Poly, prozedural generierter Geometrie profitieren.

## Häufige Probleme & Tipps

| Problem | Lösung |
|---------|--------|
| Twist erscheint flach oder fehlt | Stellen Sie sicher, dass `setSlices` hoch genug ist (z. B. 100) für eine glatte Rotation. |
| OBJ-Datei öffnet sich nicht im Viewer | Überprüfen Sie, ob der Ausgabepfad (`MyDir`) korrekt ist und die Datei Schreibrechte hat. |
| Unerwartete Skalierung | Prüfen Sie das Einheitensystem Ihres Quellprofils; Aspose.3D arbeitet standardmäßig in Metern. |

## Häufig gestellte Fragen

**Q: Kann ich Aspose.3D für Java verwenden, um mit anderen 3D‑Dateiformaten zu arbeiten?**  
A: Ja, Aspose.3D unterstützt eine breite Palette von Formaten wie FBX, STL, 3MF und mehr.

**Q: Wo finde ich Support für Aspose.3D für Java?**  
A: Besuchen Sie das [Aspose.3D forum](https://forum.aspose.com/c/3d/18) für Community‑Hilfe und offizielle Unterstützung.

**Q: Gibt es eine kostenlose Testversion?**  
A: Ja, Sie können eine Testversion von [hier](https://releases.aspose.com/) herunterladen.

**Q: Wie erhalte ich eine temporäre Lizenz für Tests?**  
A: Holen Sie sich eine temporäre Lizenz von der [temporary license page](https://purchase.aspose.com/temporary-license/).

**Q: Wo kann ich eine Voll‑Lizenz erwerben?**  
A: Kaufen Sie Aspose.3D für Java über die [buying page](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Zuletzt aktualisiert:** 2025-12-17  
**Getestet mit:** Aspose.3D 24.11 für Java  
**Autor:** Aspose  

---