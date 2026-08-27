---
date: 2026-07-27
description: Lär dig hur du ändrar sfärens radie i Java och exporterar OBJ‑fil i Java
  med Aspose.3D, det ledande Java‑3D‑biblioteket för att konvertera 3D till OBJ.
keywords:
- modify sphere radius java
- export obj file java
- aspose 3d java
lastmod: 2026-07-27
linktitle: 'Ändra sfärens radie i Java: Konvertera 3D till OBJ med Aspose.3D'
og_description: Ändra sfärens radie i Java och exportera OBJ‑fil i Java med Aspose.3D.
  Denna handledning visar steg‑för‑steg hur du lägger till en sfär, ändrar dess storlek
  och sparar som OBJ.
og_image_alt: 'Guide: modify sphere radius Java and export OBJ using Aspose.3D'
og_title: Ändra sfärens radie i Java – Konvertera 3D till OBJ med Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-07-27'
  description: Learn how to modify sphere radius Java and export OBJ file Java using
    Aspose.3D, the leading Java 3D library for converting 3D to OBJ.
  headline: 'Modify Sphere Radius Java: Convert 3D to OBJ with Aspose.3D'
  type: TechArticle
- description: Learn how to modify sphere radius Java and export OBJ file Java using
    Aspose.3D, the leading Java 3D library for converting 3D to OBJ.
  name: 'Modify Sphere Radius Java: Convert 3D to OBJ with Aspose.3D'
  steps:
  - name: Initialize a Scene
    text: '**Definition anchor:** The `Scene` class is Aspose.3D''s top‑level container
      that holds geometry, lights, and cameras for a 3D model. Creating a `Scene`
      gives you a workspace where you can add and manipulate objects. Creating a `Scene`
      gives you a container for all geometry, lights, and cameras. This'
  - name: Initialize a Sphere
    text: '**Definition anchor:** The `Sphere` class represents a geometric sphere
      primitive with a configurable radius, center, and material. By default it starts
      with a radius of 1.0. A `Sphere` object starts with a default radius of 1.0.
      Think of it as a blank canvas for the shape you want to export.'
  - name: Set the Desired Radius
    text: The `setRadius(double)` method updates the sphere’s size by assigning a
      new radius value in the same units used by the scene. Here we **write obj file
      java**‑style code that sets the exact radius. Replace `10` with any `double`
      value that matches your design requirements.
  - name: Add Sphere to the Scene
    text: This line **adds sphere to scene** by creating a child node under the root
      node. It’s the moment the geometry becomes part of the scene graph.
  - name: Export the Model as OBJ
    text: The `save(String, FileFormat)` method writes the entire scene to the specified
      file using the chosen format, such as OBJ. Calling `scene.save` **exports obj
      file java**‑style, effectively **save scene as obj**. The generated `sphere.obj`
      can be opened in any standard 3D viewer.
  type: HowTo
- questions:
  - answer: You can refer to the [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/)
      for comprehensive guidance.
    question: Where can I find the documentation for Aspose.3D for Java?
  - answer: 'Download the library from the releases page: [Download Aspose.3D for
      Java](https://releases.aspose.com/3d/java/).'
    question: How do I download Aspose.3D for Java?
  - answer: Yes, explore the features with a free trial by visiting [Aspose.3D Free
      Trial](https://releases.aspose.com/).
    question: Is there a free trial available for Aspose.3D for Java?
  - answer: Join the Aspose community at [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18)
      for assistance and discussions.
    question: Where can I get support for Aspose.3D for Java?
  - answer: Get a temporary license by visiting [Temporary License](https://purchase.aspose.com/temporary-license/).
    question: How can I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- modify sphere radius
- export OBJ
- aspose.3d
- java 3d
- 3d conversion
title: 'Ändra sfärens radie i Java: Konvertera 3D till OBJ med Aspose.3D'
url: /sv/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Konvertera 3D till OBJ: Lägg till sfär & ändra radie i Java

## Introduktion

Om du snabbt och programatiskt behöver **modifiera sfärens radie i Java**, visar den här guiden exakt hur du lägger till en sfär i en scen, ändrar dess radie och skriver den resulterande OBJ‑filen med hjälp av **Aspose.3D Java library**. Vi går igenom varje kodrad, förklarar varför varje steg är viktigt och ger dig tips för att undvika vanliga fallgropar—så att du kan integrera arbetsflödet i spel, CAD‑verktyg eller vetenskapliga visualiseringar med förtroende.

## Snabba svar
- **Vad är huvudmålet med den här handledningen?** Att demonstrera hur man konverterar 3D till OBJ genom att skapa en sfär, justera dess radie och exportera modellen i Java.  
- **Vilket bibliotek tillhandahåller 3D‑funktionaliteten?** Aspose.3D, en full‑featured **java 3d library tutorial**.  
- **Hur ändrar jag sfärens storlek?** Anropa `sphere.setRadius(double)` på `Sphere`‑instansen.  
- **Kan jag skriva OBJ‑filen direkt från Java?** Ja—använd `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.  
- **Behöver jag en licens för produktion?** En gratis provversion räcker för utveckling; en permanent licens krävs för kommersiell användning.

## Vad är Aspose.3D för Java?

Aspose.3D för Java är ett omfattande **java 3d library** som gör det möjligt för utvecklare att skapa, redigera och konvertera 3D‑filer utan externa beroenden. Det stöder mer än **50 in‑ och utdataformat**—inklusive OBJ, FBX, STL och GLTF—vilket möjliggör sömlös integration i vilken 3‑D‑pipeline som helst.

## Varför konvertera 3D till OBJ?

Att konvertera till OBJ ger en universellt läsbar, ren‑text representation av geometri som kan inspekteras, redigeras och importeras av praktiskt taget alla 3D‑applikationer, vilket gör den idealisk för snabb prototypframtagning och plattformsoberoende tillgångsutbyte.

- **Universell kompatibilitet** – OBJ stöds av praktiskt taget varje 3D‑visare, spelmotor och modelleringsprogram.  
- **Lättviktig export** – OBJ lagrar geometri i ett ren‑textformat, vilket är enkelt att inspektera och felsöka.  
- **Arbetsflödesflexibilitet** – Du kan generera OBJ‑filer i farten från server‑sidig Java‑kod, vilket möjliggör automatiserade pipelines för skapande av tillgångar.

## Förutsättningar

- Grundläggande kunskaper i Java‑programmering.  
- Aspose.3D‑biblioteket installerat – ladda ner det från den [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  
- JDK 8 eller senare installerat på din utvecklingsmaskin.

## Importera paket

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Hur man ändrar sfärens radie i Java?

Läs in `Sphere`‑objektet, anropa `setRadius` med önskat värde och spara sedan scenen som OBJ—detta hela arbetsflöde kan utföras i fem koncisa steg. Metoden fungerar för vilken numerisk radie som helst och garanterar att den exporterade OBJ‑filen återspeglar exakt den storlek du anger.

### Steg 1: Initiera en scen

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

**Definition anchor:** `Scene`‑klassen är Aspose.3D:s översta behållare som innehåller geometri, ljus och kameror för en 3D‑modell. Att skapa en `Scene` ger dig ett arbetsutrymme där du kan lägga till och manipulera objekt.

Att skapa en `Scene` ger dig en behållare för all geometri, ljus och kameror. Detta är där vi senare kommer att **lägga till en sfär i scenen**.

### Steg 2: Initiera en sfär

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

**Definition anchor:** `Sphere`‑klassen representerar en geometrisk sfär‑primitiv med en konfigurerbar radie, centrum och material. Som standard startar den med en radie på 1,0.

Ett `Sphere`‑objekt startar med en standardradie på 1,0. Tänk på det som en tom duk för den form du vill exportera.

### Steg 3: Ställ in önskad radie

`setRadius(double)`‑metoden uppdaterar sfärens storlek genom att tilldela ett nytt radievärde i samma enheter som scenen använder.

```java
// set radius
sphere.setRadius(10);
```

Här skriver vi **write obj file java**‑stil kod som sätter den exakta radien. Ersätt `10` med vilket `double`‑värde som helst som matchar dina designkrav.

### Steg 4: Lägg till sfär i scenen

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Denna rad **lägger till en sfär i scenen** genom att skapa en barnnod under rot‑noden. Det är ögonblicket då geometrin blir en del av scen‑grafen.

### Steg 5: Exportera modellen som OBJ

`save(String, FileFormat)`‑metoden skriver hela scenen till den angivna filen med det valda formatet, såsom OBJ.

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Att anropa `scene.save` **exporterar obj file java**‑stil, effektivt **save scene as obj**. Den genererade `sphere.obj` kan öppnas i vilken standard 3D‑visare som helst.

## Vanliga problem och lösningar

| Problem | Lösning |
|-------|----------|
| **Sphere appears too small in the viewer** | Verifiera att radievärdet är korrekt inställt; kom ihåg att enheter är godtyckliga om du inte applicerar en skalnings‑transform. |
| **Exported OBJ has no material** | Aspose.3D skriver endast geometri; lägg till ett material på sfären om du behöver texturer (`sphere.setMaterial(...)`). |
| **License exception at runtime** | Se till att du har en temporär eller permanent licensfil laddad innan du skapar `Scene`. |

## Vanliga frågor

**Q: Var kan jag hitta dokumentationen för Aspose.3D för Java?**  
A: Du kan hänvisa till den [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) för omfattande vägledning.

**Q: Hur laddar jag ner Aspose.3D för Java?**  
A: Ladda ner biblioteket från releases‑sidan: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

**Q: Finns det en gratis provversion av Aspose.3D för Java?**  
A: Ja, utforska funktionerna med en gratis provversion genom att besöka [Aspose.3D Free Trial](https://releases.aspose.com/).

**Q: Var kan jag få support för Aspose.3D för Java?**  
A: Gå med i Aspose‑gemenskapen på [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) för hjälp och diskussioner.

**Q: Hur kan jag skaffa en temporär licens för Aspose.3D?**  
A: Skaffa en temporär licens genom att besöka [Temporary License](https://purchase.aspose.com/temporary-license/).

**Q: Kan jag använda denna kod med andra 3D‑format som STL?**  
A: Absolut – byt bara `FileFormat`‑enum när du anropar `scene.save`, t.ex. `FileFormat.STL`.

---

**Senast uppdaterad:** 2026-07-27  
**Testad med:** Aspose.3D for Java 24.11  
**Författare:** Aspose

## Relaterade handledningar

- [Hur man sätter normaler på 3D‑objekt i Java med Aspose.3D Java API](/3d/java/geometry/set-up-normals-on-3d-objects/)
- [Hur man bäddar in textur i FBX med Java – Applicera material på 3D‑objekt med Aspose.3D](/3d/java/geometry/apply-materials-to-3d-objects/)
- [Hur man ändrar planorientering och exporterar OBJ i Java](/3d/java/3d-scenes-and-models/change-plane-orientation/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}