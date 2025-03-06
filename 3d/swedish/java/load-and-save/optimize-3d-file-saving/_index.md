---
title: Optimera 3D-fillagring i Java med Aspose.3D SaveOptions
linktitle: Optimera 3D-fillagring i Java med Aspose.3D SaveOptions
second_title: Aspose.3D Java API
description: Lär dig hur du optimerar 3D-filsparande i Java med Aspose.3D SaveOptions. Förbättra prestanda och anpassa utgångar utan ansträngning.
weight: 16
url: /sv/java/load-and-save/optimize-3d-file-saving/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Optimera 3D-fillagring i Java med Aspose.3D SaveOptions

## Introduktion

Aspose.3D är ett funktionsrikt Java-bibliotek som ger utvecklare möjlighet att arbeta med 3D-modeller sömlöst. När det gäller att spara 3D-filer erbjuder klassen SaveOptions en uppsjö av inställningar för att finjustera utdata enligt dina krav. I den här handledningen kommer vi att utforska olika sparalternativ och hur de kan utnyttjas för att optimera processen.

## Förutsättningar

Innan vi dyker in i handledningen, se till att du har följande förutsättningar på plats:

-  Aspose.3D för Java: Se till att du har Aspose.3D-biblioteket integrerat i ditt Java-projekt. Du kan ladda ner den[här](https://releases.aspose.com/3d/java/).

- Java-utvecklingsmiljö: Ha en fungerande Java-utvecklingsmiljö inställd på din maskin.

- Dokumentkatalog: Skapa en katalog där du vill spara dina 3D-filer och notera sökvägen för senare användning.

## Importera paket

 I ditt Java-projekt, importera de nödvändiga paketen för att arbeta med Aspose.3D. Detta inkluderar`Scene` klass och olika SaveOptions-klasser. Nedan följer ett grundläggande exempel:

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

Låt oss nu dela upp varje exempel i flera steg för att demonstrera användningen av olika SaveOptions.

## Steg 1: Pretty Print i GLTF SaveOption

 De`prettyPrintInGltfSaveOption` metoden låter dig generera en GLTF-fil med indraget JSON-innehåll för mänsklig läsbarhet.

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // Initiera 3D-scen
    Scene scene = new Scene(new Sphere());
    
    // Initiera GLTFSaveOptions
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // Aktivera snygg utskrift för bättre läsbarhet
    opt.setPrettyPrint(true);
    
    // Spara 3D-scen
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## Steg 2: HTML5 SaveOption

 De`html5SaveOption` Metoden visar hur man sparar en 3D-scen som en HTML5-fil, inklusive anpassningsalternativ.

```java
public static void html5SaveOption() throws IOException {
    // Initiera en scen
    Scene scene = new Scene();
    
    // Skapa en barnnod med en cylinder
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //Ställ in egenskaper för den underordnade noden
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // Lägg till ett ljus till scenen
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // Initiera HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // Anpassa alternativ (t.ex. stäng av rutnät och användargränssnitt)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // Spara scenen som en HTML5-fil
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

 Fortsätt med liknande uppdelningar för andra SaveOptions-metoder som t.ex`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` , och`drcSaveOptions`.

## Slutsats

Genom att följa den här omfattande handledningen har du lärt dig hur du optimerar 3D-filsparandet i Java med Aspose.3D SaveOptions. Oavsett om du är intresserad av snygga utskrifter av GLTF-filer eller anpassa HTML5-utdata, utrustar Aspose.3D dig med verktygen för att förbättra ditt 3D-grafikarbetsflöde.

## FAQ's

### F1: Hur kan jag bädda in tillgångar i en glTF-fil?

 S1: För att bädda in tillgångar, använd`setEmbedAssets(true)` metod i`GltfSaveOptions` klass.

###  F2: Vad är syftet med`setPositionBits` method in `DracoSaveOptions`?

 A2: Den`setPositionBits` metoden ställer in kvantiseringsbitarna för position i Draco-komprimeringsalgoritmen.

### F3: Kan jag exportera normal data i en U3D-fil?

 S3: Ja, du kan exportera normal data genom att ställa in`setExportNormals(true)` i`U3dSaveOptions` klass.

### F4: Hur kasserar jag sparade materialfiler i en OBJ-export?

A4: Använd`setFileSystem(new DummyFileSystem())` metod i`ObjSaveOptions` klass för att kassera materialfiler.

### F5: Finns det något sätt att spara beroenden till en lokal katalog i en OBJ-fil?

 A5: Ja, använd`setFileSystem(new LocalFileSystem(MyDir))` metod i`ObjSaveOptions` klass för att spara beroenden lokalt.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
