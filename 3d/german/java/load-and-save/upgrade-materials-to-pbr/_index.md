---
date: 2025-12-22
description: Erfahren Sie, wie Sie Szenen in Java mit Aspose.3D nach glTF exportieren
  und dabei 3D‑Materialien auf PBR aktualisieren, um die Realistik zu verbessern.
linktitle: Export Scene to glTF in Java with Aspose.3D
second_title: Upgrade 3D Materials to PBR
title: Szene in Java mit Aspose.3D nach glTF exportieren
url: /de/java/load-and-save/upgrade-materials-to-pbr/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Szene nach glTF in Java mit Aspose.3D – Materialien auf PBR aktualisieren

## Einführung

In diesem Tutorial lernen Sie, wie Sie **export scene to glTF** in Java mit Aspose.3D durchführen, während Sie Ihre 3D‑Materialien auf Physically‑Based Rendering (PBR) aktualisieren. Das Upgrade auf PBR verleiht Ihren Modellen ein deutlich realistischeres Aussehen, und das Exportieren in das weit verbreitete glTF 2.0‑Format ermöglicht das Teilen dieser hochwertigen Assets über Engines, Browser und AR/VR‑Plattformen. Wir gehen die Voraussetzungen durch, importieren die notwendigen Pakete und zerlegen jedes Beispiel Schritt für Schritt, damit Sie die Technik in Ihren eigenen Projekten anwenden können.

## Schnelle Antworten
- **Was bedeutet „export scene to glTF“?** Es konvertiert eine Aspose.3D‑Szene in das glTF 2.0‑Dateiformat und bewahrt Geometrie, Materialien und Hierarchie.  
- **Warum zuerst Materialien auf PBR aktualisieren?** PBR‑Materialien lassen sich direkt auf den Metallic‑Roughness‑Workflow von glTF abbilden und liefern realistische Beleuchtung ohne zusätzliche Konvertierungsschritte.  
- **Benötige ich eine Lizenz, um den Code auszuführen?** Eine kostenlose Testversion reicht für die Entwicklung; für den Produktionseinsatz ist eine kommerzielle Lizenz erforderlich.  
- **Welche Java‑IDEs werden unterstützt?** Jede IDE, die Java kompilieren kann (Eclipse, IntelliJ IDEA, VS Code usw.).  
- **Kann ich große Szenen exportieren?** Ja, Aspose.3D streamt Daten effizient; stellen Sie nur sicher, dass ausreichend Heap‑Speicher für sehr große Modelle vorhanden ist.

## Was ist „export scene to glTF“?
Das Exportieren einer Szene nach glTF bedeutet, die gesamte 3D‑Szene – einschließlich Meshes, Knoten, Kameras, Lichter und Materialien – in das GL Transmission Format (glTF) zu serialisieren. glTF ist ein offener Standard, der für Echtzeit‑Rendering optimiert ist und sich ideal für Web, Mobile und Spiel‑Engines eignet.

## Warum Materialien vor dem Export auf PBR aktualisieren?
PBR‑ (Physically‑Based Rendering) Materialien beschreiben, wie Licht mit Oberflächen interagiert, unter Verwendung von Parametern wie Albedo, Metallic und Roughness. glTF 2.0 unterstützt PBR nativ, sodass die Konvertierung von Phong‑ oder benutzerdefinierten Materialien zu PBR sicherstellt, dass Farben, Reflexionen und Schattierungen korrekt dargestellt werden, wenn das Modell in einem beliebigen glTF‑kompatiblen Viewer geladen wird.

## Voraussetzungen

1. **Aspose.3D for Java** – herunterladen von der [release page](https://releases.aspose.com/3d/java/).  
2. **Java Development Environment** – JDK 8 oder höher und eine IDE Ihrer Wahl.  
3. **Document Directory** – ein Ordner auf Ihrem Rechner, in dem Sie 3D‑Dateien lesen/ schreiben.

## Pakete importieren

Fügen Sie den Kern‑Namespace von Aspose.3D zu Ihrem Projekt hinzu:

```java
import com.aspose.threed.*;
```

Dieser einzelne Import gibt Ihnen Zugriff auf `Scene`, `Box`, `PhongMaterial`, `PbrMaterial`, `GltfSaveOptions` und die Material‑Konvertierungs‑API.

## Schritt 1: Eine neue 3D‑Szene initialisieren

Erstellen Sie eine neue Szene, die Ihre Geometrie und Materialien enthält:

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene s = new Scene();
// ExEnd:InitializeScene
```

> **Pro‑Tipp:** Behalten Sie `MyDir` während der Entwicklung als absoluten Pfad, um Datei‑nicht‑gefunden‑Fehler zu vermeiden.

## Schritt 2: Eine Box mit einem PhongMaterial erstellen

Wir beginnen mit einer einfachen Box, die ein klassisches Phong‑Material verwendet. Dieses wird später beim Export in ein PBR‑Material konvertiert:

```java
// ExStart:CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd:CreateBoxWithMaterial
```

> **Warum Phong?** PhongMaterial ist einfach einzurichten und demonstriert, wie die Konvertierungslogik funktioniert.

## Schritt 3: Im GLTF 2.0‑Format speichern (Export Scene to glTF)

Konfigurieren Sie die GLTF‑Speicheroptionen, um automatisch jedes `PhongMaterial` in ein `PbrMaterial` zu konvertieren. Dies ist das Kernstück von **export scene to glTF**:

```java
// ExStart:SaveInGLTF
GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
opt.setMaterialConverter(new MaterialConverter() {
    @Override
    public Material call(Material material) {
        PhongMaterial m = (PhongMaterial) material;
        PbrMaterial ret = new PbrMaterial();
        ret.setAlbedo(m.getDiffuseColor());
        return ret;
    }
});
s.save(MyDir + "Non_PBRtoPBRMaterial_Out.gltf", opt);
// ExEnd:SaveInGLTF
```

Wenn dieser Code ausgeführt wird, wird die Szene in `Non_PBRtoPBRMaterial_Out.gltf` geschrieben. Der benutzerdefinierte `MaterialConverter` sorgt dafür, dass das Phong‑Material in ein PBR‑Material umgewandelt wird, sodass die resultierende glTF‑Datei in jedem glTF‑Viewer mit realistischem Shading angezeigt wird.

## Häufige Probleme & Lösungen

| Problem | Lösung |
|-------|----------|
| **FileNotFoundException** beim Speichern | Stellen Sie sicher, dass `MyDir` auf einen vorhandenen Ordner zeigt und die Anwendung Schreibrechte hat. |
| **ClassCastException** im Konverter | Vergewissern Sie sich, dass das an den Konverter übergebene Material tatsächlich ein `PhongMaterial` ist. Fügen Sie bei gemischten Materialtypen eine `instanceof`‑Prüfung hinzu. |
| **Missing textures** nach dem Export | glTF erwartet Texturen separat bereitgestellt; fügen Sie bei Bedarf eine Textur‑Verarbeitung im Konverter hinzu. |

## Häufig gestellte Fragen

**Q: Ist Aspose.3D mit anderen Java‑Entwicklungsumgebungen als Eclipse kompatibel?**  
A: Ja, Aspose.3D funktioniert mit jeder Java‑IDE, einschließlich IntelliJ IDEA, NetBeans und VS Code.

**Q: Kann ich Aspose.3D für kommerzielle Projekte nutzen?**  
A: Ja, Sie können Aspose.3D sowohl für private als auch für kommerzielle Projekte verwenden. Besuchen Sie die [purchase page](https://purchase.aspose.com/buy) für Lizenzdetails.

**Q: Gibt es eine kostenlose Testversion?**  
A: Ja, Sie können eine kostenlose Testversion [hier](https://releases.aspose.com/) erhalten.

**Q: Wo finde ich Support für Aspose.3D?**  
A: Durchsuchen Sie das [Aspose.3D forum](https://forum.aspose.com/c/3d/18) für Community‑Support.

**Q: Wie erhalte ich eine temporäre Lizenz für Aspose.3D?**  
A: Besuchen Sie [diesen Link](https://purchase.aspose.com/temporary-license/) für Informationen zur temporären Lizenz.

## Fazit

Durch die oben beschriebenen Schritte wissen Sie jetzt, wie Sie **export scene to glTF** in Java mit Aspose.3D durchführen und dabei Phong‑Materialien automatisch auf PBR aktualisieren. Dieser Workflow ermöglicht es Ihnen, hochwertige, physikalisch basierte Assets zu erstellen, die für moderne Rendering‑Pipelines, Web‑Viewer und AR/VR‑Erlebnisse bereit sind. Experimentieren Sie mit komplexeren Geometrien, Texturen und Beleuchtung, um das volle Potenzial von PBR und glTF auszuschöpfen.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Zuletzt aktualisiert:** 2025-12-22  
**Getestet mit:** Aspose.3D 24.12 für Java  
**Autor:** Aspose  

---