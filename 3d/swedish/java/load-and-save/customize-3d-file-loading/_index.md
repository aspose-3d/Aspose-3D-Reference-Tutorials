---
title: Anpassa 3D-filladdning i Java med Aspose.3D LoadOptions
linktitle: Anpassa 3D-filladdning i Java med Aspose.3D LoadOptions
second_title: Aspose.3D Java API
description: Förbättra din 3D-filladdning i Java med Aspose.3D anpassningsbara LoadOptions. Lär dig steg-för-steg-anpassning för 3DS, OBJ, STL, U3D, glTF, PLY, X och valfri FBX.
type: docs
weight: 12
url: /sv/java/load-and-save/customize-3d-file-loading/
---
## Introduktion

det ständigt föränderliga landskapet av 3D-design och -utveckling är effektiv hantering av 3D-filformat avgörande. Aspose.3D för Java tillhandahåller en kraftfull lösning för att anpassa laddningen av olika 3D-filformat. Denna handledning guidar dig genom processen att anpassa 3D-filladdning i Java med Aspose.3Ds LoadOptions.

## Förutsättningar

Innan du dyker in i anpassningsprocessen, se till att du har följande:

- Grundläggande förståelse för Java-programmering.
- Installerat Java Development Kit (JDK).
-  Aspose.3D för Java-bibliotek nedladdat. Du kan få det[här](https://releases.aspose.com/3d/java/).
- Bekantskap med 3D-filformat som 3DS, OBJ, STL, U3D, glTF, PLY, X och FBX.

## Importera paket

Se till att importera de nödvändiga Aspose.3D-paketen i ditt Java-projekt:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Anpassa 3D-filladdning

### Steg 1: Anpassa 3DS-filladdning

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

### Steg 2: Anpassa OBJ-filladdning

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Steg 3: Anpassa STL-filladdning

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Steg 4: Anpassa U3D-filladdning

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Steg 5: Anpassa glTF-filladdning

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Steg 6: Anpassa PLY-filladdning

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Steg 7: Anpassa X File Loading

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Steg 8: Anpassa FBX-filladdning (valfritt)

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

## Slutsats

Anpassning av 3D-filladdning i Java med Aspose.3Ds LoadOptions ger utvecklare möjlighet att skräddarsy importprocessen efter specifika krav. Oavsett om det handlar om att justera animationstransformationer, vända koordinatsystem eller hantera externa beroenden, ger Aspose.3D den flexibilitet som behövs för sömlös integration.

## Vanliga frågor

### F1: Var kan jag hitta dokumentationen för Aspose.3D för Java?

 S1: Dokumentationen finns tillgänglig[här](https://reference.aspose.com/3d/java/).

### F2: Hur kan jag ladda ner Aspose.3D för Java?

 A2: Du kan ladda ner det[här](https://releases.aspose.com/3d/java/).

### F3: Finns det en gratis provperiod?

 A3: Ja, du kan komma åt den kostnadsfria provperioden[här](https://releases.aspose.com/).

### F4: Var kan jag få support för Aspose.3D för Java?

 S4: Besök supportforumet[här](https://forum.aspose.com/c/3d/18).

### F5: Behöver jag en tillfällig licens för att testa?

 A5: Ja, skaffa en tillfällig licens[här](https://purchase.aspose.com/temporary-license/).