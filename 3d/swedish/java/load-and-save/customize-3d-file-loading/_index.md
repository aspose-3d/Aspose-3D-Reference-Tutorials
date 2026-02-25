---
date: 2026-02-25
description: Lär dig hur du vänder koordinatsystemet och anpassar 3D‑import med Aspose.3D
  LoadOptions i Java. Steg‑för‑steg‑guide för 3DS, OBJ, STL, U3D, glTF, PLY, X och
  valfritt FBX.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Vänd koordinatsystem – Anpassa 3D‑filinläsning i Java med Aspose.3D
url: /sv/java/load-and-save/customize-3d-file-loading/
weight: 12
---

.

Thus:

**Last Updated:** -> **Senast uppdaterad:**  
**Tested With:** -> **Testat med:**  
**Author:** -> **Författare:**  

Keep dates unchanged.

Now produce final content with all translations.

Check that we didn't translate any URLs or code placeholders.

Make sure we keep markdown formatting.

Now produce final answer.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vänd koordinatsystem – Anpassa 3D-filinläsning i Java med Aspose.3D

I det ständigt utvecklande landskapet för 3D-design och -utveckling är **flipping the coordinate system** när man importerar modeller ett vanligt krav. Oavsett om du konverterar resurser från ett högervridet till ett vänstervridet system eller behöver anpassa modeller till ditt motors axelkonventioner, ger Aspose.3D for Java dig finjusterad kontroll. Denna handledning guidar dig genom hur du **anpassa 3D-import** med Aspose.3D:s `LoadOptions`, och täcker de mest populära formaten såsom 3DS, OBJ, STL, U3D, glTF, PLY, X och det valfria FBX.

## Snabba svar
- **Vad gör “flip coordinate system”?** Det byter X/Y/Z-axlarna för att matcha målkoordinatkonventionen.  
- **Vilka format stödjer flipping?** Alla större format (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) exponerar ett `setFlipCoordinateSystem`-alternativ.  
- **Behöver jag extra bibliotek?** Endast Aspose.3D for Java JAR; inga externa konverterare krävs.  
- **Kan jag ladda material samtidigt?** Ja—använd `setEnableMaterials(true)` för OBJ-filer.  
- **Krävs en licens för produktion?** En giltig Aspose.3D-licens behövs för icke‑testdistributioner.

## Vad är “flip coordinate system”?
Att vända koordinatsystemet ändrar orienteringen på de axlar som den importerade modellen använder. Detta är nödvändigt när källfilen har en annan handighet (höger‑handig vs. vänster‑handig) än din renderingsmotor, vilket förhindrar att modeller visas spegelvända eller inverterade.

## Varför anpassa 3D-import?
- Bevara animationstransformeringar (`setApplyAnimationTransform`).  
- Korrigera färghantering (`setGammaCorrectedColor`).  
- Lösa externa resursvägar via `getLookupPaths()`.  
- Optimera minnesanvändning genom att bara ladda det du behöver.

## Förutsättningar

- Grundläggande förståelse för Java-programmering.  
- Installerat Java Development Kit (JDK).  
- Aspose.3D for Java-biblioteket nedladdat. Du kan hämta det [here](https://releases.aspose.com/3d/java/).  
- Bekantskap med 3D-filformat som 3DS, OBJ, STL, U3D, glTF, PLY, X och FBX.

## Importera paket

I ditt Java-projekt, se till att importera de nödvändiga Aspose.3D-paketen:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Hur man anpassar 3D-import med LoadOptions

Nedan följer steg‑för‑steg kodsnuttar som visar hur du aktiverar **flip coordinate system**-alternativet för varje stödd format. Snuttarna är redo att kopieras in i ditt projekt; ersätt bara `"Your Document Directory"` med den faktiska sökvägen till dina resurser.

### Steg 1: Anpassa 3DS-filinläsning

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

### Steg 2: Anpassa OBJ-filinläsning

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Steg 3: Anpassa STL-filinläsning

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Steg 4: Anpassa U3D-filinläsning

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Steg 5: Anpassa glTF-filinläsning

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Steg 6: Anpassa PLY-filinläsning

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Steg 7: Anpassa X-filinläsning

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Steg 8: Anpassa FBX-filinläsning (valfritt)

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

## Vanliga problem och lösningar
- **Modellen visas spegelvänd efter inläsning** – Verifiera att `setFlipCoordinateSystem(true)` är satt för rätt format.  
- **Material saknas** – För OBJ-filer, säkerställ `setEnableMaterials(true)` och att materialfilerna (.mtl) finns i någon av sökvägarna.  
- **Texturkoordinater är upp och ner** – För glTF kan du behöva `setFlipTexCoordV(true)` utöver att vända axlarna.  
- **Fil‑ej‑hittad‑fel** – Lägg till katalogen som innehåller externa resurser (texturer, hjälpfiler) till `loadOpts.getLookupPaths()`.

## Slutsats

Genom att utnyttja Aspose.3D:s `LoadOptions` kan du **flip the coordinate system** och **customize 3D import** för praktiskt taget alla större format. Denna kontrollnivå eliminerar behovet av efterbearbetningsskript och säkerställer att dina resurser renderas korrekt redan första gången.

## Vanliga frågor

### Q1: Var kan jag hitta Aspose.3D for Java-dokumentationen?
A1: Dokumentationen finns tillgänglig [here](https://reference.aspose.com/3d/java/).

### Q2: Hur kan jag ladda ner Aspose.3D for Java?
A2: Du kan ladda ner den [here](https://releases.aspose.com/3d/java/).

### Q3: Finns det en gratis provperiod tillgänglig?
A3: Ja, du kan komma åt den gratis provperioden [here](https://releases.aspose.com/).

### Q4: Var kan jag få support för Aspose.3D for Java?
A4: Besök supportforumet [here](https://forum.aspose.com/c/3d/18).

### Q5: Behöver jag en tillfällig licens för testning?
A5: Ja, skaffa en tillfällig licens [here](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Senast uppdaterad:** 2026-02-25  
**Testat med:** Aspose.3D for Java 24.11 (latest)  
**Författare:** Aspose