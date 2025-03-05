---
title: Optimieren Sie das Speichern von 3D-Dateien in Java mit Aspose.3D SaveOptions
linktitle: Optimieren Sie das Speichern von 3D-Dateien in Java mit Aspose.3D SaveOptions
second_title: Aspose.3D Java-API
description: Erfahren Sie, wie Sie das Speichern von 3D-Dateien in Java mit Aspose.3D SaveOptions optimieren. Verbessern Sie die Leistung und passen Sie die Ausgaben mühelos an.
type: docs
weight: 16
url: /de/java/load-and-save/optimize-3d-file-saving/
---
## Einführung

Aspose.3D ist eine funktionsreiche Java-Bibliothek, die Entwicklern die nahtlose Arbeit mit 3D-Modellen ermöglicht. Wenn es um das Speichern von 3D-Dateien geht, bietet die SaveOptions-Klasse eine Vielzahl von Einstellungen, um die Ausgabe entsprechend Ihren Anforderungen anzupassen. In diesem Tutorial untersuchen wir verschiedene Speicheroptionen und wie sie zur Optimierung des Prozesses genutzt werden können.

## Voraussetzungen

Bevor wir uns mit dem Tutorial befassen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

-  Aspose.3D für Java: Stellen Sie sicher, dass die Aspose.3D-Bibliothek in Ihr Java-Projekt integriert ist. Sie können es herunterladen[Hier](https://releases.aspose.com/3d/java/).

- Java-Entwicklungsumgebung: Richten Sie auf Ihrem Computer eine funktionsfähige Java-Entwicklungsumgebung ein.

- Dokumentverzeichnis: Erstellen Sie ein Verzeichnis, in dem Sie Ihre 3D-Dateien speichern möchten, und notieren Sie sich den Pfad zur späteren Verwendung.

## Pakete importieren

 Importieren Sie in Ihrem Java-Projekt die notwendigen Pakete für die Arbeit mit Aspose.3D. Dazu gehört die`Scene` Klasse und verschiedene SaveOptions-Klassen. Nachfolgend finden Sie ein einfaches Beispiel:

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

Lassen Sie uns nun jedes Beispiel in mehrere Schritte unterteilen, um die Verwendung verschiedener SaveOptions zu demonstrieren.

## Schritt 1: Pretty Print in GLTF SaveOption

 Der`prettyPrintInGltfSaveOption` Mit der Methode können Sie eine GLTF-Datei mit eingerücktem JSON-Inhalt für die menschliche Lesbarkeit generieren.

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // 3D-Szene initialisieren
    Scene scene = new Scene(new Sphere());
    
    // GLTFSaveOptions initialisieren
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // Aktivieren Sie Pretty Print für eine bessere Lesbarkeit
    opt.setPrettyPrint(true);
    
    // Speichern Sie die 3D-Szene
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## Schritt 2: HTML5 SaveOption

 Der`html5SaveOption` Die Methode zeigt, wie eine 3D-Szene als HTML5-Datei gespeichert wird, einschließlich Anpassungsoptionen.

```java
public static void html5SaveOption() throws IOException {
    // Initialisieren Sie eine Szene
    Scene scene = new Scene();
    
    // Erstellen Sie einen untergeordneten Knoten mit einem Zylinder
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //Legen Sie Eigenschaften für den untergeordneten Knoten fest
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // Fügen Sie der Szene ein Licht hinzu
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // Initialisieren Sie HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // Optionen anpassen (z. B. Raster und Benutzeroberfläche ausschalten)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // Speichern Sie die Szene als HTML5-Datei
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

 Fahren Sie mit ähnlichen Aufschlüsselungen für andere SaveOptions-Methoden fort, z`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` , Und`drcSaveOptions`.

## Abschluss

Durch die Befolgung dieses umfassenden Tutorials haben Sie gelernt, wie Sie das Speichern von 3D-Dateien in Java mit Aspose.3D SaveOptions optimieren. Egal, ob Sie GLTF-Dateien hübsch drucken oder HTML5-Ausgaben anpassen möchten, Aspose.3D stattet Sie mit den Tools aus, mit denen Sie Ihren 3D-Grafik-Workflow verbessern können.

## FAQs

### F1: Wie kann ich Assets in eine glTF-Datei einbetten?

 A1: Um Assets einzubetten, verwenden Sie die`setEmbedAssets(true)` Methode in der`GltfSaveOptions` Klasse.

###  F2: Was ist der Zweck des`setPositionBits` method in `DracoSaveOptions`?

 A2: Die`setPositionBits` Die Methode setzt die Quantisierungsbits für die Position im Draco-Komprimierungsalgorithmus.

### F3: Kann ich normale Daten in eine U3D-Datei exportieren?

 A3: Ja, Sie können normale Daten per Einstellung exportieren`setExportNormals(true)` im`U3dSaveOptions` Klasse.

### F4: Wie verwerfe ich das Speichern von Materialdateien in einem OBJ-Export?

A4: Nutzen Sie die`setFileSystem(new DummyFileSystem())` Methode in der`ObjSaveOptions` Klasse zum Verwerfen von Materialdateien.

### F5: Gibt es eine Möglichkeit, Abhängigkeiten in einem lokalen Verzeichnis in einer OBJ-Datei zu speichern?

 A5: Ja, verwenden Sie das`setFileSystem(new LocalFileSystem(MyDir))` Methode in der`ObjSaveOptions` Klasse, um Abhängigkeiten lokal zu speichern.