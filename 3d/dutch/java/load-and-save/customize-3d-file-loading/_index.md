---
date: 2026-02-25
description: Leer hoe u het coördinatensysteem kunt omkeren en de 3D-import kunt aanpassen
  met Aspose.3D LoadOptions in Java. Stapsgewijze gids voor 3DS, OBJ, STL, U3D, glTF,
  PLY, X en optioneel FBX.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Coördinatensysteem omkeren – Pas het laden van 3D‑bestanden in Java aan met
  Aspose.3D
url: /nl/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Coördinatensysteem omkeren – 3D-bestandsladen aanpassen in Java met Aspose.3D

In het voortdurend evoluerende landschap van 3D-ontwerp en -ontwikkeling is **het omkeren van het coördinatensysteem** bij het importeren van modellen een veelvoorkomende eis. Of je nu assets converteert van een rechtshandig naar een linkshandig systeem of modellen moet afstemmen op de asconventies van je engine, Aspose.3D voor Java geeft je fijnmazige controle. Deze tutorial leidt je stap voor stap door het **aanpassen van 3D-import** met behulp van Aspose.3D’s `LoadOptions`, en behandelt de populairste formaten zoals 3DS, OBJ, STL, U3D, glTF, PLY, X en optioneel FBX.

## Quick Answers
- **Wat doet “flip coordinate system”?** Het verwisselt de X/Y/Z-assen om overeen te komen met de doelcoördinatenconventie.  
- **Welke formaten ondersteunen omkeren?** Alle belangrijke formaten (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) bieden een `setFlipCoordinateSystem`‑optie.  
- **Heb ik extra bibliotheken nodig?** Alleen de Aspose.3D voor Java JAR; er zijn geen externe converters vereist.  
- **Kan ik materialen tegelijk laden?** Ja—gebruik `setEnableMaterials(true)` voor OBJ‑bestanden.  
- **Is een licentie vereist voor productie?** Een geldige Aspose.3D‑licentie is nodig voor niet‑trial‑implementaties.

## What is “flip coordinate system”?
Het omkeren van het coördinatensysteem wijzigt de oriëntatie van de assen die door het geïmporteerde model worden gebruikt. Dit is essentieel wanneer het bronbestand een andere handigheid (rechtshandig vs. linkshandig) heeft dan je renderengine, waardoor modellen niet gespiegeld of omgekeerd verschijnen.

## Why customize 3D import?
- Behoud animatietransformaties (`setApplyAnimationTransform`).  
- Corrigeer kleurafhandeling (`setGammaCorrectedColor`).  
- Los externe resource‑paden op via `getLookupPaths()`.  
- Optimaliseer geheugenverbruik door alleen te laden wat je nodig hebt.

## Prerequisites

- Basiskennis van Java‑programmeren.  
- Geïnstalleerde Java Development Kit (JDK).  
- Aspose.3D voor Java‑bibliotheek gedownload. Je kunt het verkrijgen [hier](https://releases.aspose.com/3d/java/).  
- Bekendheid met 3D‑bestandsformaten zoals 3DS, OBJ, STL, U3D, glTF, PLY, X en FBX.

## Import Packages

Zorg ervoor dat je in je Java‑project de benodigde Aspose.3D‑pakketten importeert:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## How to customize 3D import with LoadOptions

Hieronder vind je stap‑voor‑stap code‑fragmenten die laten zien hoe je de **flip coordinate system**‑optie inschakelt voor elk ondersteund formaat. De fragmenten zijn klaar om in je project te plakken; vervang gewoon `"Your Document Directory"` door het daadwerkelijke pad naar je assets.

### Stap 1: 3DS‑bestand laden aanpassen

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### Stap 2: OBJ‑bestand laden aanpassen

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Stap 3: STL‑bestand laden aanpassen

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Stap 4: U3D‑bestand laden aanpassen

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Stap 5: glTF‑bestand laden aanpassen

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Stap 6: PLY‑bestand laden aanpassen

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Stap 7: X‑bestand laden aanpassen

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Stap 8: FBX‑bestand laden aanpassen (optioneel)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## Common Issues and Solutions
- **Model verschijnt gespiegeld na het laden** – Controleer of `setFlipCoordinateSystem(true)` is ingesteld voor het juiste formaat.  
- **Materialen ontbreken** – Zorg ervoor dat voor OBJ‑bestanden `setEnableMaterials(true)` is ingeschakeld en dat de materiaalbestanden (.mtl) zich in een van de lookup‑paden bevinden.  
- **Texture‑coördinaten staan ondersteboven** – Voor glTF moet je mogelijk `setFlipTexCoordV(true)` gebruiken naast het omkeren van de assen.  
- **Bestand niet gevonden‑fouten** – Voeg de map met externe resources (textures, aanvullende bestanden) toe aan `loadOpts.getLookupPaths()`.

## Conclusion

Door gebruik te maken van Aspose.3D’s `LoadOptions`, kun je **het coördinatensysteem omkeren** en **3D‑import aanpassen** voor praktisch elk belangrijk formaat. Dit niveau van controle elimineert de noodzaak voor post‑processing‑scripts en zorgt ervoor dat je assets de eerste keer correct worden gerenderd.

## Frequently Asked Questions

### Q1: Waar kan ik de Aspose.3D voor Java‑documentatie vinden?
A1: De documentatie is beschikbaar [hier](https://reference.aspose.com/3d/java/).

### Q2: Hoe kan ik Aspose.3D voor Java downloaden?
A2: Je kunt het downloaden [hier](https://releases.aspose.com/3d/java/).

### Q3: Is er een gratis proefversie beschikbaar?
A3: Ja, je kunt de gratis proefversie benaderen [hier](https://releases.aspose.com/).

### Q4: Waar kan ik ondersteuning krijgen voor Aspose.3D voor Java?
A4: Bezoek het ondersteuningsforum [hier](https://forum.aspose.com/c/3d/18).

### Q5: Heb ik een tijdelijke licentie nodig voor testen?
A5: Ja, verkrijg een tijdelijke licentie [hier](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Laatst bijgewerkt:** 2026-02-25  
**Getest met:** Aspose.3D for Java 24.11 (latest)  
**Auteur:** Aspose