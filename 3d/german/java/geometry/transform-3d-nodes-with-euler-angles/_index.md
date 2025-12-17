---
date: 2025-12-13
description: Erfahren Sie, wie Sie Aspose 3D Java verwenden, um 3D‑Knoten zu transformieren.
  Dieses Handbuch zeigt, wie man Euler‑Winkel nutzt, 3D‑Rotation hinzufügt und die
  Translation in Java festlegt.
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – 3D‑Knoten mit Euler‑Winkeln transformieren
url: /de/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformieren von 3D‑Knoten mit Euler‑Winkeln in Java mittels Aspose.3D

## Einleitung

In diesem Tutorial erfahren Sie **wie man aspose 3d java** verwendet, um 3D‑Knoten durch Anwendung von Euler‑Winkeln zu transformieren. Am Ende des Leitfadens können Sie 3D‑Rotation hinzufügen, Java‑Translation setzen und dynamische Szenen erstellen, die auf Echtzeitdaten reagieren.

## Schnelle Antworten
- **Welche Bibliothek übernimmt 3D‑Transformationen in Java?** Aspose 3D for Java.  
- **Welche Methode setzt die Rotation mit Euler‑Winkeln?** `setEulerAngles()` am Transform des Knotens.  
- **Wie bewege ich einen Knoten im Raum?** Verwenden Sie `setTranslation()` mit einem `Vector3`.  
- **Benötige ich eine Lizenz für die Produktion?** Ja, eine kommerzielle Aspose 3D‑Lizenz ist erforderlich.  
- **Kann ich nach FBX exportieren?** Absolut – `scene.save(..., FileFormat.FBX7500ASCII)` funktioniert sofort.

## Voraussetzungen

Bevor wir ins Tutorial einsteigen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

- Grundlegende Kenntnisse in der Java‑Programmierung.  
- Java Development Kit (JDK) auf Ihrem Rechner installiert.  
- Aspose.3D‑Bibliothek, die Sie von [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/) erhalten können.

## Pakete importieren

Beginnen Sie damit, die erforderlichen Pakete in Ihr Java‑Projekt zu importieren. Stellen Sie sicher, dass die Aspose.3D‑Bibliothek korrekt zu Ihrem Klassenpfad hinzugefügt wurde. Falls Sie sie noch nicht heruntergeladen haben, finden Sie den Download‑Link [hier](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## aspose 3d java – Arbeiten mit Euler‑Winkeln

### Schritt 1. Szene und Knoten initialisieren

Zuerst erstellen Sie eine Szene und einen Knoten, der die Geometrie enthält, die Sie transformieren möchten.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Schritt 2. Mesh erstellen und Geometrie setzen

Als Nächstes erzeugen Sie ein einfaches Mesh (in diesem Fall einen Würfel) und hängen es an den Knoten an.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## 3D‑Rotation zu einem Knoten hinzufügen

### Schritt 3. Euler‑Winkel und Translation setzen

Jetzt wenden wir die Rotation mit Euler‑Winkeln an und verschieben den Knoten zudem in eine sichtbare Position.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Translation in Java setzen – Positionierung des Knotens

Der obige Translation‑Schritt demonstriert **set translation java** in der Praxis: Der Knoten wird um 20 Einheiten entlang der Z‑Achse verschoben, sodass er nach dem Rendern sichtbar ist.

## Schritt 4. Knoten zur Szene hinzufügen

Hängen Sie den transformierten Knoten an den Root‑Knoten der Szene.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Schritt 5. 3D‑Szene speichern

Exportieren Sie schließlich die Szene in eine FBX‑Datei (oder ein anderes unterstütztes Format).

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Stellen Sie sicher, dass Sie `"Your Document Directory"` durch den entsprechenden Pfad auf Ihrem Rechner ersetzen.

## Fazit

Herzlichen Glückwunsch! Sie haben erfolgreich 3D‑Knoten mit Euler‑Winkeln in Java mittels **aspose 3d java** transformiert. Experimentieren Sie mit verschiedenen Winkeln und Translationen, um dynamische und ansprechende 3D‑Szenen zu erstellen.

## Häufig gestellte Fragen

**Q: Was ist der Unterschied zwischen Euler‑Winkeln und Quaternion‑Rotation?**  
A: Euler‑Winkel sind intuitiv (Pitch, Yaw, Roll), können jedoch unter Gimbal‑Lock leiden, während Quaternionen dieses Problem vermeiden und besser für sanfte Interpolationen geeignet sind.

**Q: Kann ich mehrere Transformationen am selben Knoten verketten?**  
A: Ja. Rufen Sie `setEulerAngles`, `setTranslation` und `setScale` in beliebiger Reihenfolge auf; die Bibliothek kombiniert sie zu einer einzigen Transformationsmatrix.

**Q: Ist es möglich, in andere Formate wie OBJ oder STL zu exportieren?**  
A: Absolut. Ersetzen Sie `FileFormat.FBX7500ASCII` durch `FileFormat.OBJ` oder `FileFormat.STL` im Aufruf von `scene.save`.

**Q: Wie wende ich dieselbe Rotation auf mehrere Knoten gleichzeitig an?**  
A: Erstellen Sie einen Eltern‑Knoten, wenden Sie die Rotation auf den Eltern‑Knoten an und fügen Sie darunter Kind‑Knoten hinzu. Alle Kinder erben die Transformation.

**Q: Muss ich nach dem Speichern Aufräum‑Methoden aufrufen?**  
A: Der Java‑Garbage‑Collector kümmert sich um die meisten Ressourcen, aber Sie können explizit `scene.dispose()` aufrufen, wenn Sie mit großen Szenen in einer langfristig laufenden Anwendung arbeiten.

---

**Last Updated:** 2025-12-13  
**Tested With:** Aspose.3D 23.12 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}