---
title: Transformieren Sie 3D-Knoten mit Transformationsmatrizen mit Aspose.3D
linktitle: Transformieren Sie 3D-Knoten mit Transformationsmatrizen in Java mit Aspose.3D
second_title: Aspose.3D Java-API
description: Entdecken Sie die Welt der 3D-Grafiken in Java mit Aspose.3D. Lernen Sie, Knoten mithilfe von Transformationsmatrizen mühelos zu transformieren.
weight: 21
url: /de/java/geometry/transform-3d-nodes-with-matrices/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformieren Sie 3D-Knoten mit Transformationsmatrizen mit Aspose.3D

## Einführung

Willkommen zu dieser Schritt-für-Schritt-Anleitung zur Transformation von 3D-Knoten mit Transformationsmatrizen in Java mithilfe von Aspose.3D. Wenn Sie ein Java-Entwickler sind und Ihre 3D-Grafik- und Modellierungskenntnisse verbessern möchten, sind Sie hier richtig. In diesem Tutorial befassen wir uns mit dem Prozess der Anwendung von Transformationen auf 3D-Knoten innerhalb des Aspose.3D-Frameworks.

## Voraussetzungen

Bevor wir beginnen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

- Grundkenntnisse der Java-Programmierung.
-  Aspose.3D-Bibliothek installiert. Sie können es herunterladen unter[Hier](https://releases.aspose.com/3d/java/).
- Eine funktionierende integrierte Entwicklungsumgebung (IDE) für die Java-Entwicklung.

## Pakete importieren

Importieren Sie in Ihrem Java-Projekt die erforderlichen Pakete aus Aspose.3D. Stellen Sie sicher, dass Ihr Projekt richtig konfiguriert ist, um die Aspose.3D-Bibliothek zu verwenden. Hier ist eine Beispiel-Importanweisung:

```java
import com.aspose.threed.*;

```

## 3D-Knoten transformieren

### Schritt 1: Szenenobjekt initialisieren

Beginnen Sie mit der Initialisierung eines Szenenobjekts, das als Container für 3D-Elemente dient.

```java
Scene scene = new Scene();
```

### Schritt 2: Knotenklassenobjekt initialisieren

Erstellen Sie ein Node-Klassenobjekt, z. B. einen Würfel, der einer Transformation unterzogen wird.

```java
Node cubeNode = new Node("cube");
```

### Schritt 3: Erstellen Sie ein Netz mit Polygon Builder

Verwenden Sie die Common-Klasse, um mithilfe der Polygon-Builder-Methode ein Netz zu erstellen. Dadurch wird die Netzinstanz für den Würfel festgelegt.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

### Schritt 4: Punktknoten zur Netzgeometrie

Weisen Sie das erstellte Netz dem Würfelknoten zu.

```java
cubeNode.setEntity(mesh);
```

### Schritt 5: Legen Sie eine benutzerdefinierte Übersetzungsmatrix fest

Wenden Sie eine benutzerdefinierte Übersetzungsmatrix auf den Cube-Knoten an. In diesem Beispiel wird eine Transformationsmatrix für die Übersetzung festgelegt.

```java
cubeNode.getTransform().setTransformMatrix(new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
));
```

### Schritt 6: Würfel zur Szene hinzufügen

Fügen Sie den Würfelknoten in den Stammknoten der Szene ein.

```java
scene.getRootNode().addChildNode(cubeNode);
```

### Schritt 7: 3D-Szene speichern

Geben Sie das Verzeichnis und den Dateinamen zum Speichern der 3D-Szene in unterstützten Dateiformaten an, z. B. FBX.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Abschluss

Glückwunsch! Sie haben erfolgreich gelernt, wie Sie 3D-Knoten mit Aspose.3D in Java transformieren. Experimentieren Sie mit verschiedenen Matrizen und erkunden Sie die endlosen Möglichkeiten der 3D-Grafik.

## FAQs

### F1: Kann ich mehrere Transformationen auf einen einzelnen 3D-Knoten anwenden?

A1: Ja, Sie können mehrere Transformationsmatrizen für komplexe Transformationen verketten.

### F2: Wie kann ich ein 3D-Objekt in Aspose.3D drehen?

A2: Verwenden Sie die entsprechende Rotationsmatrix in der Transformationsmatrix für die gewünschte Rotation.

### F3: Gibt es eine Grenze für die Größe der 3D-Szenen, die ich erstellen kann?

A3: Die Größe Ihrer 3D-Szenen kann durch die Systemressourcen begrenzt sein, aber Aspose.3D ist auf Effizienz ausgelegt.

### F4: Wo finde ich zusätzliche Beispiele und Dokumentation?

 A4: Besuchen Sie die[Aspose.3D-Dokumentation](https://reference.aspose.com/3d/java/) Weitere Beispiele und Details finden Sie hier.

### F5: Wie erhalte ich eine temporäre Lizenz für Aspose.3D?

 A5: Sie können eine temporäre Lizenz erhalten[Hier](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
