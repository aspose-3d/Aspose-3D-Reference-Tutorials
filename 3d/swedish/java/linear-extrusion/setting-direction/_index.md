---
date: 2026-08-02
description: Lär dig hur du ändrar extruderingsriktning i linjär extrudering och exporterar
  OBJ-filer med Aspose.3D för Java. Följ vår step‑by‑step guide.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Ändra extruderingsriktning – Aspose.3D Java
og_description: Ändra extruderingsriktning i linjär extrudering med Aspose.3D för
  Java och exportera OBJ-filer. Denna guide visar step‑by‑step kod och tips för utvecklare.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Ändra extruderingsriktning – Aspose.3D Java‑handledning
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Ändra extruderingsriktning i 3D-modeller – Aspose.3D Java
url: /sv/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Ändra extruderingsriktning i 3D-modeller – Aspose.3D Java

## Introduktion

I den här omfattande handledningen kommer du att upptäcka **hur man ändrar extruderingsriktning** när du utför en linjär extrudering med Aspose.3D för Java. Oavsett om du bygger ett CAD‑liknande verktyg, förbereder resurser för en spelmotor eller genererar delar för 3‑D‑utskrift, låter kontrollen av extruderingsriktningen dig skapa exakt den form du behöver. Vi går igenom varje steg, från att initiera en profil till att spara resultatet som en OBJ‑fil, så att du också kan **exportera 3D‑modell OBJ**‑filer direkt från Java.

## Snabba svar
- **Vilken klass utför linjär extrudering?** `LinearExtrusion`
- **Vilken metod sätter extruderingsvektorn?** `setDirection(Vector3 direction)`
- **Kan resultatet sparas som OBJ?** Ja—använd `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Krävs en licens för produktion?** En gratis provversion finns tillgänglig; en licens är obligatorisk för kommersiell användning.
- **Vilken IDE fungerar bäst med Aspose.3D?** IntelliJ IDEA och Eclipse stöds fullt ut.

## Vad är linjär extrudering?

Linjär extrudering är processen att förlänga en 2‑D‑skiss (såsom en rektangel eller cirkel) längs en rak linje för att generera ett 3‑D‑solid. Som standard följer extruderingen den positiva Z‑axeln, men Aspose.3D låter dig ändra den vägen med egenskapen `setDirection`, vilket ger dig full kontroll över den slutliga geometrin.

## Varför ändra extruderingsriktning i linjär extrudering?

Att ändra extruderingsriktningen låter dig anpassa ny geometri med befintliga objekt, skapa vinklade komponenter utan extra transformationer och generera modeller som matchar koordinatsystemet som krävs av efterföljande pipelines (t.ex. 3‑D‑skrivare eller spelmotorer). Detta eliminerar behovet av efterbearbetningssteg och minskar filstorleksöverhead med upp till 15 % när du använder riktningsvektorer som undviker onödiga rotationer.

## Förutsättningar

- Grundläggande kunskap i Java.
- Aspose.3D‑biblioteket installerat. Du kan ladda ner det från [here](https://releases.aspose.com/3d/java/). Du kan också bläddra bland alla Aspose‑utgåvor på huvudsidan [here](https://releases.aspose.com/).
- En IDE såsom Eclipse eller IntelliJ IDEA.

## Importera paket

`com.aspose.threed`‑namnrymden tillhandahåller de centrala 3‑D‑klasserna och verktygstyparna.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Steg 1: Initiera basprofil

`RectangleShape`‑klassen skapar den 2‑D‑profil som ska extruderas. En liten avrundningsradie ger kanterna ett mjukt utseende.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Steg 2: Skapa en scen

`Scene`‑klassen är Aspose.3D:s överordnade behållare som håller alla 3‑D‑noder, ljus, kameror och material.

```java
Scene scene = new Scene();
```

## Steg 3: Skapa noder

En `Node` representerar ett objekt i scen‑grafen, vilket gör att du kan fästa geometri, transformationer och andra egenskaper.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Steg 4: Utför linjär extrudering på vänstra noden

`LinearExtrusion` utför extruderingsoperationen och omvandlar en 2‑D‑profil till ett 3‑D‑nät.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Steg 5: Utför linjär extrudering på högra noden med riktning

Här **ändrar vi extruderingsriktning**. Genom att skicka en anpassad `Vector3` till `setDirection` följer extruderingen vektorn (0.3, 0.2, 1), vilket ger en snedställd form som anpassas till scenens koordinatsystem.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Steg 6: Spara 3D-scen

`save`‑metoden skriver scenen till en fil i det angivna formatet.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Vanliga problem och lösningar

| Problem | Varför det händer | Lösning |
|---------|-------------------|--------|
| OBJ‑filen är tom | Profilen lades inte till i en nod | Se till att `createChildNode` anropas på en giltig nod |
| Riktningen verkar oförändrad | `setDirection` anropades efter att extruderingen redan hade konstruerats | Ange riktning i `LinearExtrusion`‑initialiseraren som visat |
| Lågupplöst mesh | `setSlices`‑värdet är för lågt | Öka antalet skivor (t.ex. 100 eller mer) |

## Slutsats

Du vet nu **hur man ändrar extruderingsriktning** i en linjär extrudering, hur du justerar twist‑ och slice‑inställningar, och hur du **exporterar 3D‑modell OBJ**‑filer med Aspose.3D för Java. Dessa tekniker ger dig fin‑granulerad kontroll över geometrisk skapelse och gör det enkelt att integrera 3‑D‑resurser i större pipelines.

## Vanliga frågor

**Q:** Kan jag använda Aspose.3D med andra programmeringsspråk?  
**A:** Ja—Aspose.3D tillhandahåller API:er för .NET och Java, vilket möjliggör plattformsoberoende utveckling.

**Q:** Finns det en gratis provversion av Aspose.3D?  
**A:** Absolut. Du kan utforska hela funktionsuppsättningen med en gratis provversion [here](https://releases.aspose.com/).

**Q:** Var kan jag hitta detaljerad dokumentation för Aspose.3D för Java?  
**A:** Den omfattande referensen finns tillgänglig [here](https://reference.aspose.com/3d/java/).

**Q:** Hur får jag support för Aspose.3D?  
**A:** Besök det officiella [Aspose.3D forum](https://forum.aspose.com/c/3d/18) för hjälp från communityn och produktteamet.

**Q:** Finns tillfälliga licenser för testning?  
**A:** Ja—tillfälliga licenser kan erhållas [here](https://purchase.aspose.com/temporary-license/).

---

**Senast uppdaterad:** 2026-08-02  
**Testad med:** Aspose.3D för Java (senaste utgåva)  
**Författare:** Aspose

{{< blocks/products/products-backtop-button >}}

## Relaterade handledningar

- [Hur man extruderar form - Skapa 3D-modeller med linjär extrudering i Java](/3d/java/linear-extrusion/)
- [Skapa 3D-extrudering Java med Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Java 3D-grafikhandledning – Centrum i linjär extrudering](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}