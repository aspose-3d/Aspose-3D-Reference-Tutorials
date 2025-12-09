---
date: 2025-12-06
description: Lär dig hur du sparar FBX‑filer och hämtar sceninformation med Aspose.3D
  för Java. Denna steg‑för‑steg‑guide täcker hur du anger programnamn, definierar
  måttenheter och exporterar scenen till FBX.
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: Hur man sparar FBX och hämtar 3D-sceninformation i Java
url: /sv/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Så sparar du FBX och hämtar 3D-sceninformation i Java

## Introduktion

Om du letar efter en tydlig, praktisk guide om **hur man sparar fbx**‑filer samtidigt som du extraherar användbar metadata från dina 3D‑scener, har du kommit rätt. I den här handledningen går vi igenom varje steg med **Aspose.3D Java**‑biblioteket: från att skapa en scen, **ange applikationsnamn**, **definiera mätenheter**, till slut att **exportera scenen till FBX**. När du är klar har du en färdig FBX‑fil som bär den tillgångsinformation du behöver för efterföljande pipelines.

## Snabba svar
- **Vad är huvudmålet?** Spara en FBX‑fil som innehåller anpassad tillgångsinformation.  
- **Vilket bibliotek används?** Aspose.3D for Java.  
- **Behöver jag en licens?** En gratis provversion fungerar för utveckling; en kommersiell licens krävs för produktion.  
- **Kan jag ändra mätenheterna?** Ja – använd `setUnitName` och `setUnitScaleFactor`.  
- **Var sparas utdata?** Till sökvägen du anger i `scene.save(...)`.

## Förutsättningar

Innan vi börjar, se till att du har:

- God förståelse för grundläggande Java‑syntax.  
- **Aspose.3D for Java** hämtad och tillagd i ditt projekt (du kan få den från den officiella) [Aspose 3D nedladdningssida](https://releases.aspose.com/3d/java/).  
- Din favorit‑Java‑IDE (IntelliJ IDEA, Eclipse, NetBeans, etc.) korrekt konfigurerad.

## Importera paket

I din Java‑källfil importerar du Aspose.3D‑klasserna som hanterar scenhantering och filformatstöd.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Proffstips:** Håll importlistan minimal för att undvika onödiga beroenden och förbättra kompileringstider.

## Vad är processen för att spara en FBX‑fil?

Nedan följer en kortfattad, steg‑för‑steg‑genomgång som visar **hur man lägger till tillgångsinformation** i en scen och sedan **exporterar scenen till FBX**.

### Steg 1: Initiera en 3D‑scen

Först skapar du ett tomt `Scene`‑objekt. Detta blir behållaren för all geometri, ljus, kameror och tillgångsmetadata.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Steg 2: Ange applikations‑ och leverantörsinformation

Att lägga till anpassad metadata hjälper efterföljande verktyg att identifiera filens källa. Här **anger vi applikationsnamnet** och leverantören med hjälp av `AssetInfo`‑objektet.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Varför detta är viktigt:** Många pipelines filtrerar eller taggar tillgångar baserat på den ursprungliga applikationen, vilket gör detta steg avgörande för stora projekt.

### Steg 3: Definiera mätenheter

Aspose.3D låter dig specificera enhetssystemet som din scen använder. I detta exempel använder vi en gammal egyptisk enhet kallad “pole” med en anpassad skalningsfaktor.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Justera `unitScaleFactor` så att den matchar den verkliga storleken på dina modeller; 1.0 representerar en 1‑till‑1‑mappning med den valda enheten.

### Steg 4: Exportera scenen till FBX

Nu när tillgångsinformationen är bifogad sparar vi scenen som en FBX‑fil. Alternativet `FileFormat.FBX7500ASCII` skapar en mänskligt läsbar ASCII‑FBX, vilket är praktiskt för felsökning.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Kom ihåg:** Ersätt `"Your Document Directory"` med en absolut sökväg eller en sökväg relativ till ditt projekts arbetskatalog.

### Steg 5: Skriv ut framgångsmeddelande

Ett enkelt konsolutskrift bekräftar att operationen lyckades och talar om var filen skrevs.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Vanliga användningsområden

- **Spel‑tillgångspipelines** – bädda in skaparinformation direkt i FBX‑filer för versionsspårning.  
- **Arkitektonisk visualisering** – lagra projektspecifika enheter för att undvika skalningsfel vid import till renderingsmotorer.  
- **Automatiserad rapportering** – generera FBX‑filer i farten med metadata som nedströmsanalysverktyg kan läsa.

## Felsökning & tips

| Problem | Lösning |
|-------|----------|
| **Filen hittas inte efter sparning** | Verifiera att `MyDir` pekar på en befintlig mapp och att din applikation har skrivbehörighet. |
| **Enheter visas felaktiga i extern visare** | Dubbelkolla `unitScaleFactor`; vissa visare förväntar sig meter som basenhet. |
| **Tillgångsmetadata saknas** | Se till att du anropar `scene.getAssetInfo()` **innan** sparning; ändringar gjorda efter `save()` kommer inte att sparas. |

## Vanliga frågor

### Q1: Är Aspose.3D kompatibel med alla Java-IDE:er?

A1: Ja, Aspose.3D är designat för att fungera sömlöst med alla större Java-IDE:er.

### Q2: Kan jag använda Aspose.3D för kommersiella projekt?

A2: Absolut. Aspose.3D erbjuder kommersiella licenser för utvecklare, vilket säkerställer att du följer licenskraven.

### Q3: Var kan jag hitta ytterligare support för Aspose.3D?

A3: För frågor eller hjälp, besök [Aspose.3D-forum](https://forum.aspose.com/c/3d/18).

### Q4: Finns det en gratis provversion av Aspose.3D?

A4: Ja, du kan utforska funktionerna med en gratis provversion tillgänglig [här](https://releases.aspose.com/).

### Q5: Hur kan jag skaffa en tillfällig licens för Aspose.3D?

A5: Skaffa en tillfällig licens för teständamål [här](https://purchase.aspose.com/temporary-license/).

## Vanliga frågor

**Q: Hur ändrar jag utdataformatet till binär FBX?**  
A: Ersätt `FileFormat.FBX7500ASCII` med `FileFormat.FBX7500` när du anropar `scene.save(...)`.

**Q: Kan jag lägga till anpassad användardefinierad metadata utöver de inbyggda tillgångsfälten?**  
A: Ja, använd `scene.getUserData().add("Key", "Value")` för att bädda in ytterligare nyckel‑värde‑par.

**Q: Stöder Aspose.3D andra exportformat som OBJ eller GLTF?**  
A: Det gör den. Ändra helt enkelt `FileFormat`‑enum till `OBJ` eller `GLTF2` efter behov.

**Q: Vilken version av Java krävs?**  
A: Aspose.3D for Java stödjer Java 8 och senare.

**Q: Är det möjligt att ladda en befintlig FBX, ändra dess tillgångsinformation och spara igen?**  
A: Absolut. Ladda filen med `new Scene("input.fbx")`, ändra `scene.getAssetInfo()`, och spara sedan.

---

**Senast uppdaterad:** 2025-12-06  
**Testad med:** Aspose.3D for Java 24.11  
**Författare:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}