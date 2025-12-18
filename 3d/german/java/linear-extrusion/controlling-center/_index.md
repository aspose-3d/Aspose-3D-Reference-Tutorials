---
date: 2025-12-18
description: Erfahren Sie, wie Sie eine Grundfläche hinzufügen und die Center‑Eigenschaft
  bei linearer Extrusion mit Aspose.3D für Java festlegen, mit schrittweisen Code‑Beispielen.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Wie man eine Grundebene und ein Steuerzentrum bei linearer Extrusion mit Aspose.3D
  für Java hinzufügt
url: /de/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Controlling Center in Linear Extrusion with Aspose.3D for Java

## Einführung

Wenn Sie 3D‑Szenen in Java erstellen, kann die Möglichkeit, **add ground plane** während Sie die **set center property** einer linearen Extrusion präzise festlegen, den Unterschied zwischen einem flachen Prototyp und einer ausgereiften Visualisierung ausmachen. In diesem Tutorial führen wir Sie durch den gesamten Prozess, das Zentrum der Extrusion zu steuern und eine Grundfläche hinzuzufügen, wobei Aspose.3D für Java verwendet wird. Sie sehen, warum das wichtig ist, wie Sie es einrichten, und erhalten ein sofort ausführbares Code‑Beispiel, das Sie an Ihre eigenen Projekte anpassen können.

## Schnelle Antworten
- **What does “add ground plane” do?** Es erstellt eine dünne Referenzgeometrie, die Ihnen hilft, die Position der Extrusion relativ zu den Weltachsen zu sehen.  
- **How do I set the center of a linear extrusion?** Verwenden Sie die Methode `setCenter(boolean)` des `LinearExtrusion`‑Objekts.  
- **Do I need a license to run the sample?** Eine temporäre Lizenz funktioniert für Tests; für die Produktion ist eine Voll‑Lizenz erforderlich.  
- **Which file format is used for saving?** Das Beispiel speichert im Wavefront‑OBJ‑Format (`.obj`).  
- **What Java version is required?** Java 8 oder höher ist ausreichend.

## Was ist “add ground plane” in einer 3D‑Szene?

Das Hinzufügen einer Grundfläche bedeutet, eine dünne rechteckige Geometrie (oft ein Kasten mit minimaler Dicke) einzufügen, die in der X‑Z‑Ebene liegt. Sie dient als visuelle Bodenfläche und erleichtert das Einschätzen von Höhe und Ausrichtung anderer Objekte, insbesondere wenn Sie mit Extrusionszentren experimentieren.

## Warum die center‑Property bei einer linearen Extrusion setzen?

Standardmäßig beginnt eine lineare Extrusion am Ursprung des Profils. Das Setzen der center‑Property (`setCenter(true)`) verschiebt das Profil, sodass die Extrusion um den Ursprung zentriert ist, was für symmetrische Designs oder bei Bedarf einer konsistenten Ausrichtung über mehrere Objekte hinweg nützlich ist.

## Prerequisites

Bevor wir diese Tutorial‑Reise beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

1. **Java Development Environment** – Stellen Sie sicher, dass Sie eine Java‑Entwicklungsumgebung auf Ihrem Rechner eingerichtet haben.  
2. **Aspose.3D for Java** – Laden Sie die Aspose.3D‑Bibliothek herunter und installieren Sie sie. Die Bibliothek und ihre Dokumentation finden Sie [here](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Erstellen Sie ein Verzeichnis, um Ihre Java‑Dokumente zu speichern. Wir nennen es “Your Document Directory.”

## Pakete importieren

Importieren Sie in Ihrer Java‑Entwicklungsumgebung die erforderlichen Pakete für Aspose.3D. Dadurch hat Ihr Code Zugriff auf die von der Bibliothek bereitgestellten Funktionen.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Schritt 1: Basisprofil einrichten

Initialisieren Sie das Basisprofil, das extrudiert werden soll. In diesem Beispiel verwenden wir eine Rechteckform mit einem Abrundungsradius von 0,3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Schritt 2: 3D‑Szene erstellen

Erstellen Sie die Grundlage Ihrer 3D‑Welt, indem Sie eine Szene erzeugen.

```java
Scene scene = new Scene();
```

## Schritt 3: Linke und rechte Knoten erstellen

Erstellen Sie linke und rechte Knoten innerhalb Ihrer Szene. Diese Knoten dienen als Leinwand für Ihre 3D‑Objekte.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Schritt 4: Lineare Extrusion mit center‑Property (linker Knoten)

Führen Sie eine lineare Extrusion am linken Knoten **ohne Zentrierung** durch und setzen Sie die Anzahl der Scheiben auf 3. Beachten Sie den Aufruf `setCenter(false)` – hier **set center property** auf *false*.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Schritt 5: Grundfläche zur Referenz hinzufügen (linker Knoten)

Verbessern Sie die visuelle Darstellung, indem Sie **add ground plane** zum linken Knoten hinzufügen. Der dünne Kasten fungiert als Boden, sodass Sie die Höhe der Extrusion deutlich sehen können.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Schritt 6: Lineare Extrusion mit center‑Property (rechter Knoten)

Führen Sie nun eine lineare Extrusion am rechten Knoten durch, diesmal **mit Zentrierung der Extrusion**. Der Aufruf `setCenter(true)` zeigt, wie **set center property** auf *true* gesetzt wird.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Schritt 7: Grundfläche zur Referenz hinzufügen (rechter Knoten)

Wie auf der linken Seite fügen Sie auch dem rechten Knoten eine Grundfläche hinzu, um eine konsistente visuelle Basis zu erhalten.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Schritt 8: 3D‑Szene speichern

Speichern Sie Ihre 3D‑Szene im Wavefront‑OBJ‑Format, damit Sie sie in jedem gängigen 3D‑Betrachter ansehen können.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Häufige Probleme und Lösungen

| Problem | Warum es passiert | Lösung |
|---------|-------------------|--------|
| Grundfläche nicht sichtbar | Die Dicke des Kastens ist für die Skalierung des Betrachters zu klein. | Erhöhen Sie die Dicke (erster Parameter von `Box`) oder zoomen Sie im Betrachter heraus. |
| Extrusion erscheint versetzt | `setCenter`‑Wert ist nicht wie beabsichtigt gesetzt. | Überprüfen Sie den an `setCenter` übergebenen Booleschen Wert. |
| Datei wird nicht gespeichert | Falscher Verzeichnispfad oder fehlende Schreibrechte. | Stellen Sie sicher, dass `MyDir` auf einen existierenden Ordner mit Schreibzugriff zeigt. |

## Häufig gestellte Fragen

**Q1: Kann ich Aspose.3D für Java in kommerziellen Projekten verwenden?**  
A1: Ja, Aspose.3D für Java ist für die kommerzielle Nutzung verfügbar. Für Lizenzdetails besuchen Sie [here](https://purchase.aspose.com/buy).

**Q2: eine kostenlose Testversion?**  
A2: Ja, Sie können eine kostenlose Testversion von Aspose.3D für Java [here](https://releases.aspose.com/) ausprobieren.

**Q3: Wo finde ich Support für Aspose.3D für Java?**  
A3: Das Aspose.3D‑Community‑Forum ist ein guter Ort, um Unterstützung zu erhalten und Erfahrungen zu teilen. Besuchen Sie das Forum [here](https://forum.aspose.com/c/3d/18).

**Q4: Benötige ich eine temporäre Lizenz für Tests?**  
A4: Ja, wenn Sie eine temporäre Lizenz für Testzwecke benötigen, können Sie diese [here](https://purchase.aspose.com/temporary-license/) erhalten.

**Q5: Wo finde ich die Dokumentation?**  
A5: Die Dokumentation für Aspose.3D für Java ist [here](https://reference.aspose.com/3d/java/) verfügbar.

## Fazit

Die Steuerung des Zentrums bei linearer Extrusion **und** das Erlernen, wie man **add ground plane** mit Aspose.3D für Java hinzufügt, eröffnet spannende Möglichkeiten in der 3D‑Grafikentwicklung. Durch das Befolgen der obigen Schritte haben Sie nun ein wiederverwendbares Muster zum Erstellen zentrierter Extrusionen, visueller Referenzflächen und zum Exportieren des Ergebnisses nach OBJ. Experimentieren Sie gern mit verschiedenen Profilen, Scheibenzahlen und Transformationen, um Ihre Projektanforderungen zu erfüllen.

---

**Zuletzt aktualisiert:** 2025-12-18  
**Getestet mit:** Aspose.3D 24.11 for Java (latest at time of writing)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}