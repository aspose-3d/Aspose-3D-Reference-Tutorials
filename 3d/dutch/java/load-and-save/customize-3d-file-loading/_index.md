---
title: Pas het laden van 3D-bestanden in Java aan met Aspose.3D LoadOptions
linktitle: Pas het laden van 3D-bestanden in Java aan met Aspose.3D LoadOptions
second_title: Aspose.3D Java-API
description: Verbeter het laden van 3D-bestanden in Java met aanpasbare Aspose.3D LoadOptions. Leer stapsgewijze aanpassingen voor 3DS, OBJ, STL, U3D, glTF, PLY, X en optionele FBX.
type: docs
weight: 12
url: /nl/java/load-and-save/customize-3d-file-loading/
---
## Invoering

In het voortdurend evoluerende landschap van 3D-ontwerp en -ontwikkeling is een efficiënte omgang met 3D-bestandsformaten cruciaal. Aspose.3D voor Java biedt een krachtige oplossing om het laden van verschillende 3D-bestandsformaten aan te passen. Deze tutorial leidt u door het proces van het aanpassen van het laden van 3D-bestanden in Java met behulp van Aspose.3D's LoadOptions.

## Vereisten

Voordat u in het aanpassingsproces duikt, moet u ervoor zorgen dat u over het volgende beschikt:

- Basiskennis van Java-programmeren.
- Java Development Kit (JDK) geïnstalleerd.
-  Aspose.3D voor Java-bibliotheek gedownload. Je kunt het verkrijgen[hier](https://releases.aspose.com/3d/java/).
- Bekendheid met 3D-bestandsformaten zoals 3DS, OBJ, STL, U3D, glTF, PLY, X en FBX.

## Pakketten importeren

Zorg ervoor dat u in uw Java-project de benodigde Aspose.3D-pakketten importeert:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Pas het laden van 3D-bestanden aan

### Stap 1: Pas het laden van 3DS-bestanden aan

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

### Stap 2: Pas het laden van OBJ-bestanden aan

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Stap 3: Pas het laden van STL-bestanden aan

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Stap 4: Pas het laden van U3D-bestanden aan

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Stap 5: Pas het laden van glTF-bestanden aan

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Stap 6: Pas het laden van PLY-bestanden aan

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Stap 7: Pas het laden van X-bestanden aan

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Stap 8: Pas het laden van FBX-bestanden aan (optioneel)

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

## Conclusie

Door het laden van 3D-bestanden in Java aan te passen met LoadOptions van Aspose.3D kunnen ontwikkelaars het importproces aanpassen aan specifieke vereisten. Of het nu gaat om het aanpassen van animatietransformaties, het omdraaien van coördinatensystemen of het omgaan met externe afhankelijkheden, Aspose.3D biedt de flexibiliteit die nodig is voor naadloze integratie.

## Veelgestelde vragen

### V1: Waar kan ik de Aspose.3D voor Java-documentatie vinden?

 A1: De documentatie is beschikbaar[hier](https://reference.aspose.com/3d/java/).

### Vraag 2: Hoe kan ik Aspose.3D voor Java downloaden?

 A2: U kunt het downloaden[hier](https://releases.aspose.com/3d/java/).

### Vraag 3: Is er een gratis proefperiode beschikbaar?

 A3: Ja, u heeft toegang tot de gratis proefperiode[hier](https://releases.aspose.com/).

### V4: Waar kan ik ondersteuning krijgen voor Aspose.3D voor Java?

 A4: Bezoek het ondersteuningsforum[hier](https://forum.aspose.com/c/3d/18).

### Vraag 5: Heb ik een tijdelijke licentie nodig om te testen?

 A5: Ja, verkrijg een tijdelijke licentie[hier](https://purchase.aspose.com/temporary-license/).