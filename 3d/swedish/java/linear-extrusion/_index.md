---
date: 2026-05-24
description: Lär dig hur du extruderar form med Aspose.3D för Java. Denna java‑3d‑modelleringstutorial
  täcker linear extrusion, center control, direction, slices, twist och mer!
keywords:
- how to extrude shape
- java 3d geometry
- create 3d model java
- create solid from 2d
linktitle: Skapa 3D-modeller med Linear Extrusion i Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  headline: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  type: TechArticle
- description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  name: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  steps:
  - name: Define the 2‑D profile
    text: Create a `Polygon` or `Polyline` that represents the shape you want to extrude.
      *A `Polygon` represents a closed shape defined by vertices, while a `Polyline`
      is an open series of line segments.* Ready to get started? [Perform Linear Extrusion
      Now](./performing-linear-extrusion/) For a detailed tuto
  - name: Configure extrusion options
    text: 'Set the center, direction, slices, twist, and twist offset on an `Extrusion`
      object. *The `Extrusion` class encapsulates all parameters needed to generate
      a 3‑D mesh from a 2‑D profile.* Get hands‑on with center control: [Control Center
      in Linear Extrusion](./controlling-center/) Read more about cen'
  - name: Add the extrusion to the scene
    text: 'Instantiate a `Scene`, attach the extrusion mesh, and export to your desired
      format. *`Scene` is the container that holds all 3‑D objects and handles exporting
      to various file formats.* Ready to set the direction? [Explore Now](./setting-direction/)
      Learn more about direction: [Setting Direction in '
  - name: Export or render
    text: 'Use `Scene.save()` to write the model to OBJ, STL, or any supported format.
      *`Scene.save()` writes the entire scene to the specified file format, applying
      any necessary post‑processing.* Start specifying slices: [Learn More](./specifying-slices/)
      Detailed guide: [Specifying Slices in Linear Extrusio'
  type: HowTo
- questions:
  - answer: Yes, a valid Aspose license is required for production use, but a free
      trial is available for evaluation.
    question: Can I use Aspose.3D for Java in a commercial project?
  - answer: The library works with Java 8 and newer runtimes, including Java 11, 17,
      and 21.
    question: Which Java versions are supported?
  - answer: Aspose.3D handles mesh generation efficiently, but you can call `scene.dispose()`
      when you’re done with large scenes to free native resources.
    question: Do I need to manage memory for large extrusions?
  - answer: Absolutely – you can create several extrusion objects, position them independently,
      and add them to the same scene.
    question: Can I combine multiple extrusion operations in one model?
  - answer: Yes, the “Applying Twist” and “Using Twist Offset” tutorials demonstrate
      how to set both properties on the same extrusion object.
    question: Is there sample code for applying twist and twist offset together?
  type: FAQPage
second_title: Aspose.3D Java API
title: Hur man extruderar form - Skapa 3D-modeller med Linear Extrusion i Java
url: /sv/java/linear-extrusion/
weight: 23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hur man extruderar form – Skapa 3D-modeller med linjär extrusion i Java

Om du någonsin har undrat **hur man extruderar form** i en Java-applikation, är du på rätt plats. I den här handledningen går vi igenom Aspose.3D för Javas funktioner för linjär extrusion och visar hur du förvandlar enkla 2‑D-profiler till fullständiga 3‑D-modeller. Oavsett om du bygger en CAD‑liknande visare, en spelresurs‑pipeline eller bara experimenterar med geometri, kommer behärskning av linjär extrusion att ge dig förtroendet att skapa komplexa former med bara några rader kod.

## Snabba svar
- **Vad är linjär extrusion?** Att omvandla en 2‑D-skiss till ett 3‑D-solidd genom att sträcka den längs en riktning.  
- **Vilket bibliotek hjälper dig?** Aspose.3D för Java tillhandahåller ett flytande API för extruderingsuppgifter.  
- **Behöver jag en licens?** En gratis provversion fungerar för inlärning; en kommersiell licens krävs för produktion.  
- **Vilken Java-version krävs?** Java 8 eller högre.  
- **Kan jag applicera vridningar eller förskjutningar?** Ja – API:et stödjer vridvinkel och vridförskjutning direkt.  

## Vad är “hur man extruderar form” i Java?
`Extrusion`-operationen är Aspose.3D:s kärnfunktion som konverterar en plan kontur till ett volymetriskt nät. Enkelt uttryckt levererar du en 2‑D-profil (t.ex. en rektangel eller en anpassad polygon), talar om för motorn hur långt den ska dras, och biblioteket bygger 3‑D-geometrin åt dig.

## Varför använda Aspose.3D för Java?
Aspose.3D stödjer **50+ in- och utdataformat** – inklusive OBJ, STL, FBX och GLTF – och kan generera nät med upp till **10 000 vertexar per extrusion** utan att ladda in hela scenen i minnet. Dess plattformsoberoende motor körs på Windows, Linux och macOS och levererar konsekventa resultat oavsett om du arbetar på en stationär arbetsstation eller en huvudlös CI‑server.

## Förutsättningar
- Java 8 eller nyare installerat på din utvecklingsmaskin.  
- Maven eller Gradle för beroendehantering.  
- En Aspose.3D för Java-licensfil (valfri för provversion).  

## Hur fungerar linjär extrusion?
Linjär extrusion skapar ett 3‑D-solidd genom att svepa en 2‑D-profil längs en rak linje. Motorn triangulerar först profilen, replikerar den sedan vid varje skiva längs extrusionsaxeln och syr slutligen ihop skivorna för att bilda ett vattentätt nät. Denna process beräknar automatiskt normaler och UV‑koordinater, så du kan rendera resultatet utan ytterligare geometriprocessering.

## Vilka är nyckelparametrarna för en linjär extrusion?
Linjär extrusion kan anpassas med flera parametrar. **center** definierar pivotpunkten för profilen före extrusion. **direction**‑vektorn sätter extrusionsaxeln och har som standard den positiva Z‑axeln. **Slices** styr hur många mellanliggande tvärsnitt som genereras, vilket påverkar jämnheten för vridna eller avsmalnande former. **Twist angle** roterar profilen gradvis från start till slut, medan **twist offset** lägger till en linjär förskjutning längs axeln och möjliggör spiralformer.

- **Center** – Pivotpunkten runt vilken profilen placeras innan extrusion.  
- **Direction** – En vektor som definierar extrusionsaxeln; standard är den positiva Z‑axeln.  
- **Slices** – Antalet mellanliggande tvärsnitt; fler skivor ger mjukare övergångar för vridna eller avsmalnande extrusioner.  
- **Twist Angle** – Den totala rotation som appliceras på profilen från start till slut, uttryckt i grader.  
- **Twist Offset** – En linjär förskjutning som flyttar profilen längs extrusionsaxeln medan den vrids, vilket möjliggör spiralformer.

## Utföra linjär extrusion i Aspose.3D för Java
Läs in din profil, konfigurera parametrarna och låt API:et generera nätet. Följande steg beskriver det typiska arbetsflödet.

### Steg 1: Definiera 2‑D-profilen
Skapa en `Polygon` eller `Polyline` som representerar formen du vill extrudera.  
*En `Polygon` representerar en sluten form definierad av vertexar, medan en `Polyline` är en öppen sekvens av linjesegment.*  
Redo att komma igång? [Utför linjär extrusion nu](./performing-linear-extrusion/)  
För en detaljerad handledning, se [Utför linjär extrusion i Aspose.3D för Java](./performing-linear-extrusion/).

### Steg 2: Konfigurera extruderingsalternativ
Ställ in center, direction, slices, twist och twist offset på ett `Extrusion`-objekt.  
*Klassen `Extrusion` kapslar in alla parametrar som behövs för att generera ett 3‑D-nät från en 2‑D-profil.*  
Få praktisk erfarenhet av centrumkontroll: [Kontrollera centrum i linjär extrusion](./controlling-center/)  
Läs mer om centrumkontroll: [Kontroll av centrum i linjär extrusion med Aspose.3D för Java](./controlling-center/)

### Steg 3: Lägg till extrusionen i scenen
Instansiera en `Scene`, fäst extrusionsnätet och exportera till önskat format.  
*`Scene` är behållaren som håller alla 3‑D-objekt och hanterar export till olika filformat.*  
Redo att sätta riktningen? [Utforska nu](./setting-direction/)  
Läs mer om riktning: [Ställa in riktning i linjär extrusion med Aspose.3D för Java](./setting-direction/)

### Steg 4: Exportera eller rendera
Använd `Scene.save()` för att skriva modellen till OBJ, STL eller något annat stödformat.  
*`Scene.save()` skriver hela scenen till det angivna filformatet och tillämpar eventuell nödvändig efterbehandling.*  
Börja specificera skivor: [Läs mer](./specifying-slices/)  
Detaljerad guide: [Specificera skivor i linjär extrusion med Aspose.3D för Java](./specifying-slices/)

## Hur applicerar man en vridning på en extrusion?
Applicera en vridning genom att sätta `twistAngle`-egenskapen i extruderingsalternativen. Motorn roterar varje skiva proportionellt och skapar en helix-effekt. Genom att justera vinkeln kan du skapa allt från subtil torsion till fulla 360°-spiraler, användbart för dekorativa element eller funktionella fjädrar.  
Redo att vrida upp det? [Applicera vridning nu](./applying-twist/)  
Fullt exempel: [Applicera vridning i linjär extrusion med Aspose.3D för Java](./applying-twist/)

## Hur använder man vridförskjutning för spiralformer?
Vridförskjutning flyttar varje skiva längs extrusionsaxeln samtidigt som den roterar, vilket bildar en spiraltrappa eller korkskruvsgeometri. Att kombinera vridvinkel med en positiv förskjutning ger en mjuk helixramp, medan en negativ förskjutning kan skapa nedåtgående spiraler. Denna teknik är idealisk för att modellera gängor, fjädrar eller konstnärliga band.  
Förbättra dina färdigheter: [Lär dig vridförskjutning](./using-twist-offset/)  
Omfattande guide: [Använda vridförskjutning i linjär extrusion med Aspose.3D för Java](./using-twist-offset/)

## Vanliga användningsfall för linjär extrusion
- **Mekaniska delar** – Generera snabbt bultar, axlar och fästen från enkla skisser.  
- **Arkitektoniska element** – Extrudera planritningar till väggar eller pelare för BIM‑prototyper.  
- **Spelresurser** – Skapa låg‑poly rekvisita såsom staket, rör eller dekorativa räls direkt från 2‑D‑konst.  
- **Utbildningsverktyg** – Visualisera matematiska ytor genom att extrudera parametriska kurvor.

## Felsökning av vanliga problem
- **Saknade ytor** – Säkerställ att profilen är en sluten slinga; öppna konturer ger hål.  
- **Överdriven minnesanvändning** – Minska antalet `slices` eller aktivera `scene.setMemoryOptimization(true)`.  
- **Fel vridriktning** – Positiva vinklar roterar medurs när man tittar längs extrusionsriktningen; använd negativa värden för att vända.

## Vanliga frågor

**Q: Kan jag använda Aspose.3D för Java i ett kommersiellt projekt?**  
A: Ja, en giltig Aspose‑licens krävs för produktionsbruk, men en gratis provversion finns tillgänglig för utvärdering.

**Q: Vilka Java‑versioner stöds?**  
A: Biblioteket fungerar med Java 8 och nyare runtime, inklusive Java 11, 17 och 21.

**Q: Måste jag hantera minnet för stora extrusioner?**  
A: Aspose.3D hanterar mesh‑generering effektivt, men du kan anropa `scene.dispose()` när du är klar med stora scener för att frigöra inhemska resurser.

**Q: Kan jag kombinera flera extruderingsoperationer i en modell?**  
A: Absolut – du kan skapa flera extrusionsobjekt, placera dem oberoende och lägga till dem i samma scen.

**Q: Finns det exempel på kod för att applicera vridning och vridförskjutning tillsammans?**  
A: Ja, handledningarna “Applying Twist” och “Using Twist Offset” visar hur man sätter båda egenskaperna på samma extrusionsobjekt.

**Senast uppdaterad:** 2026-05-24  
**Testat med:** Aspose.3D för Java 24.11  
**Författare:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Relaterade handledningar

- [Java 3D-grafikhandledning – Centrum i linjär extrusion](/3d/java/linear-extrusion/controlling-center/)
- [Hur man ställer in riktning i linjär extrusion med Aspose.3D för Java](/3d/java/linear-extrusion/setting-direction/)
- [Skapa 3D-extrusion med skivor – Aspose.3D för Java](/3d/java/linear-extrusion/specifying-slices/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}