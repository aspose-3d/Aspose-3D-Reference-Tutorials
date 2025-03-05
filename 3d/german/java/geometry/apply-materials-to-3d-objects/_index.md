---
title: Wenden Sie mit Aspose.3D Materialien auf 3D-Objekte in Java an
linktitle: Wenden Sie mit Aspose.3D Materialien auf 3D-Objekte in Java an
second_title: Aspose.3D Java-API
description: Entdecken Sie die Welt der 3D-Grafik mit Aspose.3D für Java. Erfahren Sie, wie Sie Materialien nahtlos auf 3D-Objekte anwenden. Werten Sie Ihre Projekte mit realistischen Bildern auf.
type: docs
weight: 14
url: /de/java/geometry/apply-materials-to-3d-objects/
---
## Einführung

In der dynamischen Welt der 3D-Grafik sticht Aspose.3D für Java als leistungsstarkes Werkzeug hervor, das Ihren Projekten Leben einhaucht. Das Hinzufügen von Materialien zu 3D-Objekten erhöht die visuelle Attraktivität und macht sie realistischer. In diesem Tutorial führen wir Sie durch den Prozess der Anwendung von Materialien auf einen 3D-Würfel mit Aspose.3D für Java.

## Voraussetzungen

Bevor Sie mit dem Tutorial beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

- Java Development Kit (JDK) auf Ihrem System installiert.
- Aspose.3D für Java-Bibliothek heruntergeladen und Ihrem Projekt hinzugefügt.
- Vertrautheit mit grundlegenden Java-Programmierkonzepten.

## Pakete importieren

Importieren Sie zunächst die erforderlichen Pakete in Ihr Java-Projekt. Fügen Sie am Anfang Ihres Codes die folgenden Zeilen hinzu:

```java
import com.aspose.threed.*;


import java.nio.file.Files;
import java.nio.file.Paths;
```

## Schritt 1: Szenenobjekt initialisieren

```java
// Szenenobjekt initialisieren
Scene scene = new Scene();
```

## Schritt 2: Cube-Knotenobjekt initialisieren

```java
// Cube-Knotenobjekt initialisieren
Node cubeNode = new Node("cube");
```

## Schritt 3: Erstellen Sie ein Netz mit Polygon Builder

```java
// Rufen Sie die allgemeine Klasse „Erstellen Sie ein Netz mithilfe der Polygon-Builder-Methode“ auf, um eine Netzinstanz festzulegen
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Schritt 4: Zeigen Sie den Knoten auf das Netz

```java
// Zeigen Sie den Knoten auf das Netz
cubeNode.setEntity(mesh);
```

## Schritt 5: Würfel zur Szene hinzufügen

```java
// Fügen Sie der Szene einen Würfel hinzu
scene.getRootNode().addChildNode(cubeNode);
```

## Schritt 6: PhongMaterial-Objekt initialisieren

```java
// Initialisieren Sie das PhongMaterial-Objekt
PhongMaterial mat = new PhongMaterial();
```

## Schritt 7: Texturobjekt initialisieren

```java
// Texturobjekt initialisieren
Texture diffuse = new Texture();
```

## Schritt 8: Legen Sie den lokalen Dateipfad für die Textur fest

```java
// Der Pfad zum Dokumentenverzeichnis.
String MyDir = "Your Document Directory";
```

## Schritt 9: Legen Sie den lokalen Dateipfad für die eingebettete Textur fest

```java
// Legen Sie den lokalen Dateipfad für die eingebettete Textur fest
diffuse.setFileName(MyDir + "surface.dds");
```

## Schritt 10: Legen Sie die Textur des Materials fest

```java
// Legen Sie die Textur des Materials fest
mat.setTexture(Material.MAP_DIFFUSE, diffuse);
```

## Schritt 11: Einbetten von Rohinhaltsdaten in FBX (optional)

```java
// Legen Sie den Dateinamen für die eingebettete Textur fest
diffuse.setFileName("embedded-texture.png");
// Binärinhalt festlegen
diffuse.setContent(Files.readAllBytes(Paths.get(MyDir, "aspose-logo.jpg")));
```

## Schritt 12: Glanzfarbe einstellen

```java
// Spiegelfarbe einstellen
mat.setSpecularColor(new Vector3(1, 0, 0));
```

## Schritt 13: Helligkeit einstellen

```java
// Helligkeit einstellen
mat.setShininess(100);
```

## Schritt 14: Legen Sie die Materialeigenschaft des Würfelobjekts fest

```java
// Legen Sie die Materialeigenschaft des Würfelobjekts fest
cubeNode.setMaterial(mat);
```

## Schritt 15: 3D-Szene speichern

```java
// Legen Sie den Dateinamen fest
MyDir = MyDir + "MaterialToCube.fbx";
// Speichern Sie die 3D-Szene in den unterstützten Dateiformaten
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Abschluss

Glückwunsch! Sie haben mit Aspose.3D für Java erfolgreich Materialien auf einen 3D-Würfel angewendet. Diese einfache, aber leistungsstarke Technik kann Ihre 3D-Projekte auf ein neues Niveau heben und ein realistisches und visuell beeindruckendes Erlebnis bieten.

## FAQs

### F1: Kann ich mehrere Materialien auf ein einzelnes 3D-Objekt anwenden?

A1: Ja, mit Aspose.3D können Sie für eine verbesserte Anpassung mehrere Materialien auf verschiedene Teile eines 3D-Objekts anwenden.

### F2: Welche Dateiformate unterstützt Aspose.3D zum Speichern von Szenen?

 A2: Aspose.3D unterstützt verschiedene Dateiformate, einschließlich FBX, STL und 3DS. Siehe die[Dokumentation](https://reference.aspose.com/3d/java/) für die vollständige Liste.

### F3: Ist eine temporäre Lizenz für Aspose.3D für Java verfügbar?

 A3: Ja, Sie können eine erhalten[temporäre Lizenz](https://purchase.aspose.com/temporary-license/) zu Auswertungszwecken.

### F4: Wo finde ich Unterstützung für Aspose.3D?

 A4: Besuchen Sie die[Aspose.3D-Forum](https://forum.aspose.com/c/3d/18) für Community-Unterstützung und Diskussionen.

### F5: Kann ich die Aspose.3D-Bibliothek über einen bestimmten Link herunterladen?

 A5: Ja, verwenden Sie das[Download-Link](https://releases.aspose.com/3d/java/) um auf die neueste Version von Aspose.3D für Java zuzugreifen.