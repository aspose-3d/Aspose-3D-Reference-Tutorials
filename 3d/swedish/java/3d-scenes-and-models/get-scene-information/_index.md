---
date: 2026-09-08
description: Lär dig hur du definierar enheter och exporterar en scen till FBX i Java
  med Aspose.3D. Denna steg‑för‑steg‑guide visar hur du ställer in application name,
  measurement units och hämtar 3D scene information.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Hur man sparar FBX och hämtar 3D Scene Info i Java
og_description: Lär dig hur du definierar enheter och exporterar en scen till FBX
  i Java med Aspose.3D. Guiden täcker hur du ställer in application name, measurement
  units och hämtar 3D scene info i några steg.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Hur man definierar enheter och exporterar scen till FBX i Java
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Hur man definierar enheter och exporterar scen till FBX i Java
url: /sv/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hur man definierar enheter och exporterar scen till FBX i Java

## Introduktion

Om du letar efter en tydlig, praktisk guide om **hur man definierar enheter** och **exporterar en scen till FBX** samtidigt som du extraherar användbar metadata från dina 3D‑scener, har du kommit till rätt ställe. I den här handledningen går vi igenom varje steg med **Aspose.3D for Java**‑biblioteket: från att skapa en scen, **ange applikationsnamnet**, **definiera mätenheter**, till slut **exportera scenen till FBX**. I slutet har du en färdig‑använd FBX‑fil som innehåller den asset‑information du behöver för efterföljande pipelines.

## Snabba svar
- **Vad är huvudmålet?** Exportera en scen till FBX som innehåller anpassad asset‑information.  
- **Vilket bibliotek används?** Aspose.3D for Java.  
- **Behöver jag en licens?** En gratis provversion fungerar för utveckling; en kommersiell licens krävs för produktion.  
- **Kan jag ändra mätenheterna?** Ja – använd `setUnitName` och `setUnitScaleFactor`.  
- **Var sparas utdata?** Till den sökväg du anger i `scene.save(...)`.  

## Förutsättningar

Innan vi börjar, se till att du har:

- En solid förståelse för grundläggande Java‑syntax.  
- **Aspose.3D for Java** nedladdat och tillagt i ditt projekt (du kan hämta det från den officiella) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Din favorit‑Java‑IDE (IntelliJ IDEA, Eclipse, NetBeans, etc.) korrekt konfigurerad.

## Importera paket

I din Java‑källfil importerar du Aspose.3D‑klasserna som tillhandahåller scenhantering och filformatstöd.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tip:** Håll importlistan minimal för att undvika onödiga beroenden och förbättra kompileringstider.

## Vad är processen för att spara en FBX‑fil?

För att spara en scen som en FBX‑fil skapar du ett `Scene`, anger önskad asset‑metadata, definierar mätenheten och anropar sedan `scene.save(path, FileFormat.FBX7500ASCII)`. Denna sekvens skriver geometri, material och metadata till en ASCII‑FBX som kan inspekteras eller importeras av efterföljande verktyg.

### Steg 1: initiera en 3D‑scen

`Scene`‑klassen är Aspose.3D:s översta behållare som representerar en hel 3D‑scen, inklusive geometri, ljus, kameror och metadata. Skapa först ett tomt `Scene`‑objekt. Detta blir behållaren för all geometri, ljus, kameror och asset‑metadata.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Hur man anger applikationsnamn i Java

`AssetInfo`‑objektet lagrar metadata såsom applikationsnamn, leverantör och version för scenen. Att lägga till anpassad metadata hjälper efterföljande verktyg att identifiera filens källa. Använd `AssetInfo`‑objektet för att **ange applikationsnamnet** (och leverantören) innan du sparar filen.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Why this matters:** Många pipelines filtrerar eller taggar assets baserat på den ursprungliga applikationen, vilket gör detta steg avgörande för stora projekt.

### Steg 3: definiera mätenheter

Enhetssystemet bestämmer den verkliga skalan för scenen; Aspose.3D låter dig ange ett enhetsnamn och en skalningsfaktor i förhållande till meter. I det här exemplet använder vi en gammal egyptisk enhet kallad “pole” med en anpassad skalningsfaktor.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Justera `unitScaleFactor` så att den matchar den verkliga storleken på dina modeller; 1.0 representerar en 1‑till‑1‑mappning med den valda enheten.

### Steg 4: exportera scen till FBX

Nu när asset‑informationen är bifogad sparar vi scenen som en FBX‑fil. `FileFormat.FBX7500ASCII`‑alternativet producerar en mänskligt läsbar ASCII‑FBX, vilket är praktiskt för felsökning.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Remember:** Ersätt `"Your Document Directory"` med en absolut sökväg eller en sökväg relativ till ditt projekts arbetskatalog.

## Varför exportera scen till FBX med Aspose.3D?

Aspose.3D stödjer **50+ in‑ och utdataformat** och kan bearbeta scener med hundratals sidor utan att ladda in hela filen i minnet, vilket ger dig full kontroll över den exporterade filen—metadata, enheter och geometri—utan att behöva ett tungt 3D‑authoringsprogram. Detta gör automatiserad asset‑generering, batch‑bearbetning och server‑sidiga konverteringar snabba och pålitliga.

## Vanliga användningsfall

- **Spel‑asset‑pipelines** – bädda in skaparinformation direkt i FBX‑filer för versionsspårning.  
- **Arkitektonisk visualisering** – lagra projektspecifika enheter för att undvika skalningsfel vid import till renderingsmotorer.  
- **Automatiserad rapportering** – generera FBX‑filer i farten med metadata som efterföljande analysverktyg kan läsa.  
- **Molnbaserade 3D‑tjänster** – programatiskt skapa och exportera scener utan ett GUI, perfekt för SaaS‑plattformar.

## Felsökning & tips

| Problem | Lösning |
|-------|----------|
| **Fil ej funnen efter sparning** | Verifiera att `MyDir` pekar på en befintlig mapp och att din applikation har skrivrättigheter. |
| **Enheter visas felaktigt i extern visare** | Dubbelkolla `unitScaleFactor`; vissa visare förväntar sig meter som basenhet. |
| **Asset‑metadata saknas** | Se till att du anropar `scene.getAssetInfo()` **innan** sparning; ändringar gjorda efter `save()` kommer inte att sparas. |
| **Prestandaflaskhals på stora scener** | Använd `scene.optimize()` innan sparning för att minska minnesanvändning. |
| **ASCII‑FBX är för stor** | Byt till binär FBX genom att använda `FileFormat.FBX7500` (se FAQ). |

## Vanliga frågor

**Q: Hur ändrar jag utdataformatet till binär FBX?**  
A: Ersätt `FileFormat.FBX7500ASCII` med `FileFormat.FBX7500` när du anropar `scene.save(...)`.

**Q: Kan jag lägga till anpassad användardefinierad metadata utöver de inbyggda asset‑fälten?**  
A: Ja, använd `scene.getUserData().add("Key", "Value")` för att bädda in ytterligare nyckel‑värde‑par.

**Q: Stöder Aspose.3D andra exportformat som OBJ eller GLTF?**  
A: Det gör den. Ändra helt enkelt `FileFormat`‑enum till `OBJ` eller `GLTF2` efter behov.

**Q: Vilken version av Java krävs?**  
A: Aspose.3D for Java stödjer Java 8 och senare.

**Q: Är det möjligt att ladda en befintlig FBX, ändra dess asset‑info och spara igen?**  
A: Absolut. Ladda filen med `new Scene("input.fbx")`, ändra `scene.getAssetInfo()`, och spara sedan.

---

**Senast uppdaterad:** 2026-09-08  
**Testat med:** Aspose.3D for Java 24.11  
**Författare:** Aspose

## Relaterade handledningar

- [Minska 3D‑filstorlek – komprimera scener med Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Hur man sätter vector3‑färg java: Ändra Diffuse Color och hantera 3D‑egenskaper i Java‑scener med Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}