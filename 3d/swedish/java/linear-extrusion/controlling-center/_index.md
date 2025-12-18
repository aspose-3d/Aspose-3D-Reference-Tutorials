---
date: 2025-12-18
description: Lär dig hur du lägger till ett markplan och ställer in center‑egenskapen
  i linjär extrusion med Aspose.3D för Java, med steg‑för‑steg kodexempel.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Hur man lägger till markplan och kontrollcenter i linjär extrusion med Aspose.3D
  för Java
url: /sv/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Styrning av centrum i linjär extrusion med Aspose.3D för Java

## Introduktion

När du bygger 3D‑scener i Java kan förmågan att **add ground plane** samtidigt som du exakt **set center property** på en linjär extrusion göra skillnaden mellan en platt prototyp och en polerad visualisering. I den här handledningen går vi igenom hela processen för att kontrollera extrusionens centrum och lägga till ett markplan med Aspose.3D för Java. Du får se varför det är viktigt, hur du ställer in det och får ett färdigt kodexempel som du kan anpassa till dina egna projekt.

## Snabba svar
- **What does “add ground plane” do?** Det skapar en tunn referensgeometri som hjälper dig att se extrusionens position i förhållande till världens axlar.  
- **How do I set the center of a linear extrusion?** Använd metoden `setCenter(boolean)` på `LinearExtrusion`‑objektet.  
- **Do I need a license to run the sample?** En tillfällig licens fungerar för testning; en full licens krävs för produktion.  
- **Which file format is used for saving?** Exemplet sparar till Wavefront OBJ (`.obj`).  
- **What Java version is required?** Java 8 eller senare räcker.

## Vad är “add ground plane” i en 3D-scen?

Att lägga till ett markplan innebär att infoga en tunn rektangulär geometri (ofta en låda med minimal tjocklek) som ligger i X‑Z‑planet. Det fungerar som ett visuellt golv, vilket gör det enklare att bedöma höjd och inriktning av andra objekt, särskilt när du experimenterar med extrusionens centrum.

## Varför ställa in centrumegenskapen på en linjär extrusion?

Som standard startar en linjär extrusion från profilens origo. Genom att sätta centrumegenskapen (`setCenter(true)`) flyttas profilen så att extrusionen centreras kring origo, vilket är användbart för symmetriska designer eller när du behöver konsekvent inriktning över flera objekt.

## Förutsättningar

Innan vi påbörjar den här handledningen, se till att du har följande förutsättningar på plats:

1. **Java Development Environment** – Säkerställ att du har en Java‑utvecklingsmiljö installerad på din maskin.  
2. **Aspose.3D for Java** – Ladda ner och installera Aspose.3D‑biblioteket. Du kan hitta biblioteket och dess dokumentation [here](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Skapa en katalog för att lagra dina Java‑dokument. Låt oss kalla den “Your Document Directory.”

## Importera paket

I din Java‑utvecklingsmiljö, importera de nödvändiga paketen för Aspose.3D. Detta säkerställer att din kod har åtkomst till de funktioner som biblioteket tillhandahåller.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Steg 1: Ställ in basprofilen

Initiera basprofilen som ska extruderas. I detta exempel använder vi en rektangel med en avrundningsradie på 0,3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Steg 2: Skapa en 3D-scen

Bygg grunden för din 3D‑värld genom att skapa en scen.

```java
Scene scene = new Scene();
```

## Steg 3: Skapa vänstra och högra noder

Skapa vänstra och högra noder i din scen. Dessa noder fungerar som en duk för dina 3D‑objekt.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Steg 4: Linjär extrusion med centrumegenskap (vänster nod)

Utför linjär extrusion på den vänstra noden **utan centrering** och sätt antalet skivor till 3. Observera anropet `setCenter(false)` – här **set center property** sätts till *false*.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Steg 5: Lägg till markplan för referens (vänster nod)

Förbättra den visuella representationen genom att **add ground plane** till den vänstra noden. Den tunna lådan fungerar som ett golv så att du tydligt kan se extrusionens höjd.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Steg 6: Linjär extrusion med centrumegenskap (höger nod)

Nu utför du linjär extrusion på den högra noden, den här gången **centrerar extrusionen**. Anropet `setCenter(true)` demonstrerar hur du **set center property** till *true*.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Steg 7: Lägg till markplan för referens (höger nod)

Precis som på vänster sida, lägg till ett markplan till den högra noden för en konsekvent visuell baslinje.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Steg 8: Spara 3D-scenen

Spara din 3D-scen i Wavefront OBJ‑format så att du kan visa den i någon standard 3D‑visare.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Vanliga problem och lösningar

| Problem | Varför det händer | Lösning |
|---------|-------------------|---------|
| Markplanet syns inte | Lådans tjocklek är för liten för visarens skala. | Öka tjockleken (första parametern i `Box`) eller zooma ut i visaren. |
| Extrusionen är förskjuten | `setCenter`‑värdet är inte satt som avsett. | Dubbelkolla det booleska värdet som skickas till `setCenter`. |
| Filen sparas inte | Fel katalogsökväg eller saknade skrivbehörigheter. | Verifiera att `MyDir` pekar på en befintlig mapp med skrivrättigheter. |

## Vanliga frågor

**Q1: Kan jag använda Aspose.3D för Java i kommersiella projekt?**  
A1: Ja, Aspose.3D för Java är tillgängligt för kommersiell användning. För licensinformation, besök [here](https://purchase.aspose.com/buy).

**Q2: Finns det en gratis provversion?**  
A2: Ja, du kan prova en gratis version av Aspose.3D för Java [here](https://releases.aspose.com/).

**Q3: Var kan jag hitta support för Aspose.3D för Java?**  
A3: Aspose.3D‑community‑forumet är en utmärkt plats för att söka support och dela dina erfarenheter. Besök forumet [here](https://forum.aspose.com/c/3d/18).

**Q4: Behöver jag en tillfällig licens för testning?**  
A4: Ja, om du behöver en tillfällig licens för teständamål kan du skaffa en [here](https://purchase.aspose.com/temporary-license/).

**Q5: Var kan jag hitta dokumentationen?**  
A5: Dokumentationen för Aspose.3D för Java finns [here](https://reference.aspose.com/3d/java/).

## Slutsats

Att kontrollera centrum i linjär extrusion **och** lära sig hur man **add ground plane** med Aspose.3D för Java öppnar spännande möjligheter inom 3D‑grafikutveckling. Genom att följa stegen ovan har du nu ett återanvändbart mönster för att skapa centrerade extrusioner, visuella referensplan och exportera resultatet till OBJ. Känn dig fri att experimentera med olika profiler, skivantal och transformationer för att passa just ditt projekt.

---

**Last Updated:** 2025-12-18  
**Tested With:** Aspose.3D 24.11 för Java (senaste vid skrivtillfället)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}