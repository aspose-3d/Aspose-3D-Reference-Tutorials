---
date: 2026-02-12
description: Lär dig hur du exporterar en scen till FBX och hämtar 3D‑sceninformations
  med Aspose.3D för Java. Denna steg‑för‑steg‑guide täcker hur du anger applikationsnamnet,
  definierar måttenheter och exporterar scenen till FBX.
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: Hur man exporterar scen till FBX och hämtar 3D‑scenin­formation i Java
url: /sv/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hur man exporterar scen till FBX och hämtar 3D‑sceninformations i Java

## Introduktion

Om du letar efter en tydlig, praktisk guide om **how to export scene to FBX** medan du extraherar användbar metadata från dina 3D‑scener, har du kommit till rätt ställe. I den här handledningen går vi igenom varje steg med **Aspose.3D Java**‑biblioteket: från att skapa en scen, **setting the application name**, **defining measurement units**, till slut att **exportera scenen till FBX**. I slutet har du en färdig‑att‑använda FBX‑fil som innehåller den asset‑information du behöver för efterföljande pipelines.

## Snabba svar
- **Vad är det primära målet?** Exportera en scen till FBX som innehåller anpassad asset‑information.  
- **Vilket bibliotek används?** Aspose.3D for Java.  
- **Behöver jag en licens?** En gratis provversion fungerar för utveckling; en kommersiell licens krävs för produktion.  
- **Kan jag ändra mätenheterna?** Ja – använd `setUnitName` och `setUnitScaleFactor`.  
- **Var sparas utdata?** Till den sökväg du anger i `scene.save(...)`.

## Förutsättningar

Innan vi börjar, se till att du har:

- En solid förståelse för grundläggande Java‑syntax.  
- **Aspose.3D for Java** nedladdat och tillagt i ditt projekt (du kan hämta det från den officiella) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Din favoritte Java‑IDE (IntelliJ IDEA, Eclipse, NetBeans, etc.) korrekt konfigurerad.

## Importera paket

I din Java‑källfil, importera Aspose.3D‑klasserna som tillhandahåller scenhantering och filformatstöd.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tip:** Håll importlistan minimal för att undvika onödiga beroenden och förbättra kompileringstider.

## Vad är processen för att spara en FBX‑fil?

Nedan är en kortfattad, steg‑för‑steg‑genomgång som visar **how to add asset information** till en scen och sedan **export the scene to FBX**.

### Steg 1: Initiera en 3D‑scen

Först, skapa ett tomt `Scene`‑objekt. Detta blir behållaren för all geometri, ljus, kameror och asset‑metadata.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Steg 2: Ange applikations‑ och leverantörsinformation

Att lägga till anpassad metadata hjälper efterföljande verktyg att identifiera filens källa. Här **set the application name** och leverantör med `AssetInfo`‑objektet.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Why this matters:** Många pipelines filtrerar eller taggar assets baserat på den ursprungliga applikationen, vilket gör detta steg viktigt för stora projekt.

### Steg 3: Definiera mätenheter

Aspose.3D låter dig ange enhetssystemet som din scen använder. I detta exempel använder vi en gammal egyptisk enhet kallad “pole” med en anpassad skalningsfaktor.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Justera `unitScaleFactor` för att matcha den verkliga storleken på dina modeller; 1.0 representerar en 1‑till‑1‑mappning med den valda enheten.

### Steg 4: Exportera scen till FBX

Nu när asset‑informationen är bifogad sparar vi scenen som en FBX‑fil. `FileFormat.FBX7500ASCII`‑alternativet producerar en mänskligt läsbar ASCII‑FBX, vilket är praktiskt för felsökning.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Remember:** Ersätt `"Your Document Directory"` med en absolut sökväg eller en sökväg relativ till ditt projekts arbetskatalog.

### Steg 5: Skriv ut framgångsmeddelande

Ett enkelt konsolutskrift bekräftar att operationen lyckades och talar om var filen skrevs.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Varför exportera scen till FBX med Aspose.3D?

Att exportera till FBX är ett vanligt krav eftersom FBX stöds brett av spelmotorer, DCC‑verktyg och AR/VR‑pipelines. Aspose.3D ger dig full kontroll över den exporterade filen—metadata, enheter och geometri—utan att behöva ett tungt 3D‑authoringsprogram. Detta gör automatiserad asset‑generering, batch‑bearbetning och server‑sidiga konverteringar snabba och pålitliga.

## Vanliga användningsfall

- **Game asset pipelines** – bädda in skaparinformation direkt i FBX‑filer för versionsspårning.  
- **Architectural visualization** – lagra projektspecifika enheter för att undvika skalningsfel vid import till renderingsmotorer.  
- **Automated reporting** – generera FBX‑filer i farten med metadata som efterföljande analysverktyg kan läsa.  
- **Cloud‑based 3D services** – programatiskt skapa och exportera scener utan ett GUI, perfekt för SaaS‑plattformar.

## Felsökning & tips

| Issue | Solution |
|-------|----------|
| **Fil ej hittad efter sparning** | Verifiera att `MyDir` pekar på en befintlig mapp och att din applikation har skrivbehörighet. |
| **Enheter visas felaktigt i extern visare** | Dubbelkolla `unitScaleFactor`; vissa visare förväntar sig meter som basenhet. |
| **Asset‑metadata saknas** | Se till att du anropar `scene.getAssetInfo()` **före** sparning; ändringar gjorda efter `save()` kommer inte att sparas. |
| **Prestandaflaskhals på stora scener** | Använd `scene.optimize()` före sparning för att minska minnesanvändning. |
| **ASCII FBX är för stor** | Byt till binär FBX genom att använda `FileFormat.FBX7500` (se FAQ). |

## Vanliga frågor

**Q: Hur ändrar jag utdataformatet till binär FBX?**  
A: Ersätt `FileFormat.FBX7500ASCII` med `FileFormat.FBX7500` när du anropar `scene.save(...)`.

**Q: Kan jag lägga till anpassad användardefinierad metadata utöver de inbyggda asset‑fälten?**  
A: Ja, använd `scene.getUserData().add("Key", "Value")` för att bädda in ytterligare nyckel‑värde‑par.

**Q: Stöder Aspose.3D andra exportformat som OBJ eller GLTF?**  
A: Ja. Ändra helt enkelt `FileFormat`‑enum till `OBJ` eller `GLTF2` efter behov.

**Q: Vilken version av Java krävs?**  
A: Aspose.3D för Java stöder Java 8 och senare.

**Q: Är det möjligt att ladda en befintlig FBX, ändra dess asset‑info och spara igen?**  
A: Absolut. Läs in filen med `new Scene("input.fbx")`, ändra `scene.getAssetInfo()`, och spara sedan.

## Slutsats

Du har nu ett komplett, produktionsklart arbetsflöde för **exporting a scene to FBX** samtidigt som du inbäddar värdefull asset‑information såsom applikationsnamn, leverantör och anpassade mätenheter. Detta tillvägagångssätt förenklar asset‑hantering, minskar manuellt pappersarbete och säkerställer att efterföljande verktyg får all den kontext de behöver. Känn dig fri att utforska andra exportformat, lägga till anpassad användardata eller integrera denna kod i större automatiseringspipelines.

---

**Senast uppdaterad:** 2026-02-12  
**Testad med:** Aspose.3D for Java 24.11  
**Författare:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}