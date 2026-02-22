---
date: 2026-02-22
description: Lär dig hur du ställer in riktning i linjär extrudering och exporterar
  3D-modell OBJ med Aspose.3D för Java. Följ vår steg‑för‑steg‑guide.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Hur man anger riktning i linjär extrudering med Aspose.3D för Java
url: /sv/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hur du ställer in riktning i linjär extrudering med Aspose.3D för Java

## Introduktion

I den här omfattande handledningen kommer du att upptäcka **hur man ställer in riktning** när du utför en linjär extrudering med Aspose.3D för Java. Oavsett om du bygger ett CAD‑liknande verktyg eller genererar geometri för en spelmotor, låter kontroll av extruderingsriktningen dig skapa exakt den form du behöver. Vi går igenom varje steg, från att initiera en profil till att spara resultatet som en OBJ‑fil, så att du också kan **exportera 3d-modell obj**‑filer direkt från Java.

## Snabba svar
- **Vad är huvudklassen för linjär extrudering?** `LinearExtrusion`
- **Vilken metod definierar extruderingsriktning?** `setDirection(Vector3 direction)`
- **Kan jag exportera resultatet som OBJ?** Ja, med `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Behöver jag en licens för utveckling?** En gratis provversion finns tillgänglig; en licens krävs för produktion.
- **Vilken Java-IDE fungerar bäst?** IntelliJ IDEA eller Eclipse stöds fullt ut.

## Vad är linjär extrudering?

Linjär extrudering tar en 2‑D‑profil (t.ex. en rektangel eller cirkel) och förlänger den längs en rak linje för att skapa ett 3‑D‑solid. Som standard följer extruderingen den positiva Z‑axeln, men Aspose.3D låter dig ändra den vägen med egenskapen `setDirection`.

## Varför ställa in riktning i linjär extrudering?

Att ange en anpassad riktning är användbart när du:
- Justerar geometri med befintliga objekt i en scen.
- Skapar snedställda eller vinklade delar utan extra transformationssteg.
- Exporterar modeller som måste matcha ett specifikt koordinatsystem (t.ex. för 3‑D‑utskrift eller spelmotorer).

## Förutsättningar

Innan vi dyker ner, se till att du har:

- Grundläggande kunskaper i Java.
- Aspose.3D‑biblioteket installerat. Du kan ladda ner det från [här](https://releases.aspose.com/3d/java/).
- En IDE såsom Eclipse eller IntelliJ IDEA.

## Importera paket

Först importerar du de namnrymder som tillhandahåller de centrala 3‑D‑klasserna och verktygstyporna.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Steg 1: Initiera basprofil

Skapa formen som ska extruderas. I detta exempel använder vi en `RectangleShape` med en liten avrundningsradie för att ge kanterna ett mjukt utseende.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Steg 2: Skapa en scen

Ett `Scene`‑objekt fungerar som en behållare för alla 3‑D‑noder, ljus, kameror och material.

```java
Scene scene = new Scene();
```

## Steg 3: Skapa noder

Lägg till två barnnoder i scenroten — en för vänster‑handsextruderingen och en för höger‑handsextruderingen. Den högra noden flyttas så att de två objekten inte överlappar.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Steg 4: Utför linjär extrudering på vänster nod

Extrudera profilen på den vänstra noden med standard‑Z‑axelriktning. Vi lägger också till en full 360°‑vridning och ökar antalet skivor för ett jämnare mesh.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Steg 5: Utför linjär extrudering på höger nod med riktning

Här **ställer vi in riktning**. Genom att skicka en anpassad `Vector3` till `setDirection` följer extruderingen vektorn (0.3, 0.2, 1), vilket ger en snedställd form.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Steg 6: Spara 3D-scen

Slutligen exporterar du scenen till Wavefront OBJ‑formatet. Detta steg visar hur du **sparar obj‑fil java**‑projekt och gör det enkelt att visa resultatet i någon 3‑D‑visare.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Vanliga problem och lösningar

| Problem | Varför det händer | Lösning |
|---------|-------------------|--------|
| OBJ-fil visas tom | Profilen lades inte till i en nod | Se till att `createChildNode` anropas på en giltig nod |
| Riktningen verkar oförändrad | `setDirection` anropades efter att extruderingen redan konstruerats | Ställ in riktning i `LinearExtrusion`‑initialiseraren som visas |
| Lågupplöst mesh | `setSlices`‑värdet är för lågt | Öka antalet skivor (t.ex. 100 eller mer) |

## Slutsats

Du vet nu **hur man ställer in riktning** i en linjär extrudering, hur du justerar vridning och skivinställningar, och hur du **exporterar 3d-modell obj**‑filer med Aspose.3D för Java. Dessa tekniker ger dig fin kontroll över geometrisk skapelse och gör det enkelt att integrera 3‑D‑tillgångar i större pipelines.

## Vanliga frågor

### Q1: Kan jag använda Aspose.3D med andra programmeringsspråk?

A1: Aspose.3D stöder olika programmeringsspråk, inklusive .NET och Java.

### Q2. Finns det en gratis provversion för Aspose.3D?

A2: Ja, du kan utforska funktionerna i Aspose.3D med en gratis provversion [här](https://releases.aspose.com/).

### Q3: Var kan jag hitta detaljerad dokumentation för Aspose.3D för Java?

A3: Den omfattande dokumentationen finns tillgänglig [här](https://reference.aspose.com/3d/java/).

### Q4: Hur kan jag få support för Aspose.3D?

A4: Besök [Aspose.3D forum](https://forum.aspose.com/c/3d/18) för hjälp eller frågor.

### Q5: Finns tillfälliga licenser tillgängliga för Aspose.3D?

A5: Ja, du kan erhålla en tillfällig licens [här](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Senast uppdaterad:** 2026-02-22  
**Testad med:** Aspose.3D för Java (senaste release)  
**Författare:** Aspose