---
title: Transformieren Sie 3D-Knoten mit Quaternionen in Java mit Aspose.3D
linktitle: Transformieren Sie 3D-Knoten mit Quaternionen in Java mit Aspose.3D
second_title: Aspose.3D Java-API
description: Erweitern Sie Ihre Java-Anwendungen mit Aspose.3D für leistungsstarke 3D-Transformationen. Erfahren Sie in dieser Schritt-für-Schritt-Anleitung, wie Sie Knoten mithilfe von Quaternionen transformieren.
weight: 20
url: /de/java/geometry/transform-3d-nodes-with-quaternions/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformieren Sie 3D-Knoten mit Quaternionen in Java mit Aspose.3D

## Einführung

Willkommen zu dieser Schritt-für-Schritt-Anleitung zur Transformation von 3D-Knoten mit Quaternionen in Java mithilfe von Aspose.3D. Wenn Sie Ihre Java-Anwendung mit leistungsstarken 3D-Transformationen erweitern möchten, ist dieses Tutorial genau das Richtige für Sie. Aspose.3D für Java bietet eine Reihe robuster Funktionen für die Arbeit mit 3D-Grafiken. In diesem Tutorial konzentrieren wir uns auf die Transformation von 3D-Knoten mithilfe von Quaternionen.

## Voraussetzungen

Bevor wir uns mit dem Tutorial befassen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

- Grundkenntnisse der Java-Programmierung.
- Aspose.3D für Java installiert. Sie können es herunterladen[Hier](https://releases.aspose.com/3d/java/).
- Ein zum Speichern Ihrer 3D-Szenen eingerichtetes Dokumentenverzeichnis.

## Pakete importieren

In diesem Abschnitt importieren wir die notwendigen Pakete, um mit 3D-Transformationen mit Aspose.3D zu beginnen.

```java
import com.aspose.threed.*;
```

## Schritt 1: Szenenobjekt initialisieren

Erstellen Sie zunächst ein Szenenobjekt, das als Container für Ihre 3D-Elemente dient.

```java
Scene scene = new Scene();
```

## Schritt 2: Knotenklassenobjekt initialisieren

Erstellen Sie nun ein Knotenklassenobjekt, das in diesem Fall einen Würfel darstellt.

```java
Node cubeNode = new Node("cube");
```

## Schritt 3: Erstellen Sie ein Netz mit Polygon Builder

Verwenden Sie die allgemeine Klasse, um mithilfe der Polygon-Builder-Methode ein Netz zu erstellen.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Schritt 4: Netzgeometrie festlegen

Weisen Sie das erstellte Netz dem Würfelknoten zu.

```java
cubeNode.setEntity(mesh);
```

## Schritt 5: Rotation mit Quaternion festlegen

Wenden Sie mithilfe von Quaternionen eine Drehung auf den Würfelknoten an.

```java
cubeNode.getTransform().setRotation(Quaternion.fromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1)));
```

## Schritt 6: Übersetzung festlegen

Geben Sie die Übersetzung für den Cube-Knoten an.

```java
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Schritt 7: Würfel zur Szene hinzufügen

Fügen Sie den Cube-Knoten in die Szene ein.

```java
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Schritt 8: 3D-Szene speichern

Speichern Sie die 3D-Szene in einem unterstützten Dateiformat, zum Beispiel FBX7500ASCII.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Abschluss

Glückwunsch! Sie haben erfolgreich gelernt, wie Sie mit Aspose.3D 3D-Knoten mithilfe von Quaternionen in Java transformieren. Experimentieren Sie mit verschiedenen Transformationen, um Ihren 3D-Anwendungen Leben einzuhauchen.

## FAQs

### F1: Kann ich Aspose.3D für Java kostenlos nutzen?

A1: Aspose.3D für Java bietet eine kostenlose Testversion. Du kannst es finden[Hier](https://releases.aspose.com/).

### F2: Wo finde ich die Dokumentation für Aspose.3D für Java?

 A2: Die Dokumentation ist verfügbar[Hier](https://reference.aspose.com/3d/java/).

### F3: Wie erhalte ich Unterstützung für Aspose.3D für Java?

 A3: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) zur Unterstützung.

### F4: Sind temporäre Lizenzen verfügbar?

 A4: Ja, Sie können eine temporäre Lizenz erhalten[Hier](https://purchase.aspose.com/temporary-license/).

### F5: Wo kann ich Aspose.3D für Java kaufen?

 A5: Sie können es kaufen[Hier](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
