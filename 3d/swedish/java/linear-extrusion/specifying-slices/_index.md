---
date: 2026-05-24
description: Lär dig hur du skapar 3D extrusion med skivor med hjälp av Aspose.3D
  for Java. Denna steg‑för‑steg‑guide täcker linjär extrusion, sätta avrundningsradie
  och export av OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Skapa 3D Extrusion med skivor – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Skapa 3D Extrusion med skivor – Aspose.3D for Java
url: /sv/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Skapa 3D-extrudering med skivor – Aspose.3D för Java

## Introduktion

Om du behöver **skapa 3d extrusion**‑objekt som ser släta och precisa ut, är kontrollen av antalet skivor nyckeln. I den här handledningen går vi igenom hur du anger skivor när du utför en linjär extrudering med Aspose.3D för Java. Du får se varför skivantalet är viktigt, hur du ställer in en avrundningsradie och hur du exporterar resultatet som en OBJ‑fil som kan användas i vilken 3‑D‑pipeline som helst.

## Snabba svar
- **Vad styr “slices”?** Antalet mellankorssektioner som används för att approximera extruderingsytan.  
- **Vilken metod anger skivantalet?** `LinearExtrusion.setSlices(int)`  
- **Kan jag ändra avrundningsradien på profilen?** Ja, via `RectangleShape.setRoundingRadius(double)`  
- **Vilket filformat används i detta exempel?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Behöver jag en licens för att köra koden?** En gratis provversion fungerar för utvärdering; en kommersiell licens krävs för produktion.

`LinearExtrusion.setSlices(int)` anger hur många mellanskivor extruderingen ska generera.  
`RectangleShape.setRoundingRadius(double)` definierar hörnradien för en rektangulär profil.

## Hur skapar man 3d extrusion java med skivor?

Läs in din 2‑D‑profil, välj ett skivantal, ställ in avrundningsradien och anropa `save` – hela arbetsflödet ryms i några få rader. Aspose.3D för Java hanterar geometrisk skapelse, skivinterpolering och OBJ‑export automatiskt, så att du kan fokusera på visuell kvalitet snarare än lågnivå‑mesh‑beräkningar.

## Vad är en linjär extrudering med skivor?

En linjär extrudering med skivor förvandlar en plan 2‑D‑form till ett 3‑D‑solid genom att svepa den längs en rak linje samtidigt som ett konfigurerbart antal mellankorssektioner genereras. Skivantalet påverkar direkt hur jämnt krökta kanter, såsom avrundade hörn, återges.

## Varför använda Aspose.3D för Java för att skapa 3d extrusion?

Aspose.3D erbjuder **fullt programatiskt kontroll** över varje extruderingsparameter, stödjer **50+ in‑ och utdataformat** (inklusive OBJ, FBX, STL och GLTF) och kan bearbeta **modeller med hundratals sidor** utan att ladda hela filen i minnet. Det körs på alla Java‑aktiverade plattformar, kräver inga inhemska DLL‑filer och garanterar deterministiska resultat på Windows, Linux och macOS.

## Förutsättningar

1. **Java Development Kit** – JDK 8 eller högre installerat.  
2. **Aspose.3D för Java** – Ladda ner biblioteket från den officiella sidan [här](https://releases.aspose.com/3d/java/).  
3. En IDE eller textredigerare du föredrar.

## Importera paket

Lägg till Aspose.3D‑namnutrymmet i ditt projekt så att du kan komma åt 3‑D‑modellklasserna.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Steg‑för‑steg guide

### Steg 1: Ställ in scenen och definiera profilen

`RectangleShape` är en klass som definierar en 2‑D‑rektangelprofil.  
Först skapar vi ett `RectangleShape` och ger det en **avrundningsradie** så att hörnen blir släta.  
`Scene` är rotbehållaren för alla noder och geometrier.  
Sedan initierar vi en ny `Scene` som kommer att hålla all geometri.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Steg 2: Skapa underordnade nodobjekt för varje extrudering

`Node` representerar ett element i scengrafen som kan hålla geometri och transformationer.  
Varje geometridel lever under en `Node`. Här genererar vi två syskon‑noder – en för en låg‑skivextrudering och en för en hög‑skivextrudering – och flyttar den vänstra noden lite åt sidan så att resultaten blir enkla att jämföra.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Steg 3: Utför linjär extrudering och ange skivor

`LinearExtrusion` är klassen som skapar ett solid genom att svepa en profil linjärt.  
`LinearExtrusion` är Aspose.3D:s klass som genererar ett solid genom att extrudera en 2‑D‑profil längs en rak linje. Med en **anonymous inner class** anropar vi `setSlices` för att kontrollera slätheten. Den vänstra noden får bara 2 skivor (grov), medan den högra noden får 10 skivor (slät).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Steg 4: Exportera OBJ – spara scenen

Till sist skriver vi scenen till en Wavefront OBJ‑fil, ett format som brett stöds av 3‑D‑redigerare och spelmotorer. Detta demonstrerar **export OBJ Java**‑kapaciteten i Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Vanliga problem och lösningar

| Problem | Varför det händer | Åtgärd |
|-------|----------------|-----|
| **Extruderingen ser platt ut** | Skivantalet är satt till 1 eller 0 | Se till att `setSlices` anropas med ett värde ≥ 2. |
| **Avrundade hörn ser hackiga ut** | Avrundningsradien är för liten i förhållande till skivantalet | Öka antingen radien eller skivantalet för mjukare kurvor. |
| **Filen hittas inte vid sparning** | `MyDir` pekar på en icke‑existerande mapp | Skapa katalogen i förväg eller använd en absolut sökväg. |

## Vanliga frågor

**Q: Hur kan jag ladda ner Aspose.3D för Java?**  
A: Du kan ladda ner biblioteket [här](https://releases.aspose.com/3d/java/).

**Q: Var hittar jag dokumentationen för Aspose.3D?**  
A: Se dokumentationen [här](https://reference.aspose.com/3d/java/).

**Q: Finns det en gratis provversion?**  
A: Ja, du kan utforska en gratis provversion [här](https://releases.aspose.com/).

**Q: Hur får jag support för Aspose.3D?**  
A: Besök supportforumet [här](https://forum.aspose.com/c/3d/18).

**Q: Kan jag köpa en tillfällig licens?**  
A: Ja, en tillfällig licens kan erhållas [här](https://purchase.aspose.com/temporary-license/).

---

**Senast uppdaterad:** 2026-05-24  
**Testad med:** Aspose.3D för Java 24.11 (senaste vid skrivtillfället)  
**Författare:** Aspose

## Relaterade handledningar

- [Skapa 3D-extrudering Java med Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Hur man anger riktning i linjär extrudering med Aspose.3D för Java](/3d/java/linear-extrusion/setting-direction/)
- [Skapa 3D-scen med vridning i linjär extrudering – Aspose.3D för Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}