---
date: 2026-11-17
description: Hur man minskar 3D-modellens storlek genom att generera ett sfärnät i
  Java och komprimera det med Google Draco via Aspose.3D. Lär dig hela arbetsflödet
  på några minuter.
images:
- /java/3d-mesh-data/compress-meshes-google-draco/og-image.png
keywords:
- create sphere mesh
- how to compress 3d
- reduce 3d model size
- aspose 3d java
- compress 3d mesh
lastmod: 2026-11-17
linktitle: Hur man minskar 3D-modellens storlek – Skapa sfärnät i Java med Google
  Draco
og_description: Skapa sfärnät och komprimera 3D-modell med Java med hjälp av Aspose.3D
  och Google Draco. Denna handledning visar hur man genererar en sfär, exporterar
  till .drc och uppnår upp till 95 % minskning av storleken på några minuter.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Skapa sfärnät och komprimera 3D-modell med Java och Draco
schemas:
- author: Aspose
  dateModified: '2026-11-17'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: Hur man minskar 3D-modellens storlek med ett Java-sfärnät och Draco
url: /sv/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hur man minskar 3d-modellens storlek med ett Java-sfärnät och Draco

## Introduktion

Aspose.3D for Java är ett bibliotek som möjliggör skapande, manipulering och konvertering av 3‑D-modeller direkt från Java‑kod. Om du letar efter ett snabbt sätt att **minska 3d-modellens storlek** samtidigt som du levererar högkvalitativ geometri, har du hamnat på rätt plats. I den här handledningen går vi igenom hur man genererar ett sfärnät med **Aspose.3D for Java** och sedan komprimerar nätet med **Google Draco**. I slutet har du en färdig `.drc`‑fil som är dramatiskt mindre än originalet, vilket gör den perfekt för webbaserade visare, mobilspel eller någon bandbreddsbegränsad Java‑applikation.

## Snabba svar
- **Vad täcker den här handledningen?** Skapa ett sfärnät i Java och komprimera det med Google Draco via Aspose.3D.  
- **Primärt bibliotek?** Aspose.3D for Java (används för både nätgenerering och Draco‑export).  
- **Typisk implementeringstid?** Ungefär 10‑15 minuter för en grundläggande sfär.  
- **Viktig förutsättning?** En Java‑utvecklingsmiljö med Aspose.3D‑JAR‑filer på classpath.  
- **Resultat?** En `.drc`‑fil som **minskar 3d-modellens storlek** med upp till 95 % jämfört med ett okomprimerat nät.

## Hur man minskar 3d-modellens storlek?

Läs in din sfär och komprimera den i två enkla steg. Först **skapar du ett sfärnät** med `new Sphere(1.0, 32, 32)`. Sedan exporterar du scenen direkt till Draco med `scene.save("sphere.drc", SaveFormat.Draco)`. Aspose.3D hanterar geometrikvantisering och vertex‑deduplicering automatiskt och levererar filer som vanligtvis är 80‑95 % mindre samtidigt som den visuella kvaliteten bevaras.

`Sphere`‑klassen är Aspose.3D:s inbyggda geometrigenerator som skapar ett triangulerat sfärnät. Den accepterar en radie och tessellationsparametrar, vilket låter dig styra detaljnivån före komprimering.

## Vad betyder “minska 3d-modellens storlek” i sammanhanget av 3d‑utveckling?

**Minska 3d-modellens storlek** betyder att krympa mängden geometridata som måste överföras eller lagras, utan att märkbart försämra den visuella kvaliteten. Draco uppnår detta genom att koda vertex‑positioner, normaler och andra attribut i ett mycket kompakt binärt format. När det kombineras med Aspose.3D hålls hela arbetsflödet inom Java, så du behöver inte hantera inhemska binärer.

## Varför använda Google Draco‑nätkomprimering med Aspose.3D?

Google Draco kombinerat med Aspose.3D ger en effektiv pipeline som dramatiskt minskar nätfiler samtidigt som de är enkla att integrera i Java‑projekt. Biblioteket hanterar all låg‑nivå‑kodning, så utvecklare kan fokusera på geometrisk skapelse utan att behöva hantera inhemska Draco‑binärer, vilket resulterar i snabbare utveckling och mindre resurser för webb och mobila.

- **Massiv storleksreduktion:** Draco kan minska nätdata med upp till 95 % för typiska modeller, vilket omvandlar en 5 MB OBJ till en 0,3 MB `.drc`.  
- **Snabb avkodning vid körning:** Motorer som Unity, Unreal och three.js avkodar Draco nativt, vilket ger snabbare laddningstider.  
- **Sömlös Java‑integration:** Aspose.3D abstraherar det inhemska Draco‑biblioteket, så du kan stanna i Java‑ekosystemet.  
- **All‑till‑en Aspose 3D‑export:** Samma API som du använder för att skapa geometri hanterar även exporten, vilket förenklar pipelinen.  

Aspose.3D stöder **50+ in‑ och utdataformat** — inklusive OBJ, FBX, STL, GLTF och många fler — och kan bearbeta modeller med hundratals sidor utan att ladda in hela filen i minnet.

## Förutsättningar

- **Java Development Kit (JDK)** – version 8 eller senare.  
- **Aspose.3D for Java** – ladda ner de senaste JAR‑filerna från **[Aspose 3D Java releases page](https://releases.aspose.com/3d/java/)**.  
- **Grundläggande kunskap om Google Draco** – du kommer att använda Aspose.3D:s omslag, så ingen inhemsk Draco‑installation krävs.

## Importera paket

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Steg‑för‑steg‑guide

### Steg 1: konfigurera projektet

Skapa ett nytt Java‑projekt (valfri IDE fungerar) och lägg till alla Aspose.3D‑JAR‑filer i classpath. Håll dina källfiler i ett paket som t.ex. `com.example.draco` för tydlighet.

### Steg 2: hur man skapar ett sfärnät i Java

`Sphere`‑klassen är Aspose.3D:s inbyggda geometrigenerator som skapar ett triangulerat sfärnät.  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **Proffstips:** `Sphere`‑klassen genererar ett triangulerat nät med standardradien 1.0. Du kan ange anpassad radie, tessellation eller materialparametrar om du behöver en annan detaljnivå före komprimering.

### Steg 3: exportera nätet till Draco‑format

`Scene`‑klassen representerar en komplett 3‑D‑scen som kan innehålla nät, ljus och kameror. `DracoCompressionOptions`‑klassen låter dig anpassa Draco‑komprimeringsinställningar såsom kvantisering och komprimeringsnivå. Efter att sfären har lagts till i ett `Scene`‑objekt, anropa `scene.save("sphere.drc", SaveFormat.Draco)`. Aspose.3D väljer automatiskt optimala komprimeringsinställningar, men du kan finjustera dem genom att justera `DracoCompressionOptions` om du behöver den minsta möjliga filen. `DracoCompressionOptions` låter dig

### Steg 4: verifiera resultatet

`DRACOLoader` är ett three.js‑verktyg som laddar Draco‑komprimerade `.drc`‑filer och konverterar dem till WebGL‑kompatibel geometri. Öppna den genererade `.drc`‑filen med en Draco‑visare (t.ex. three.js `DRACOLoader`) för att säkerställa att geometrin renderas korrekt. Du kommer att märka en dramatisk minskning av filstorleken — ofta en faktor tio eller mer.

## Vanliga användningsfall

| Scenario | Varför minska modellens storlek? | Hur den här handledningen hjälper |
|----------|----------------------------------|-----------------------------------|
| Webbaserade produktkonfiguratorer | Snabbare sidladdning på långsamma anslutningar | Draco‑komprimerade `.drc`‑filer laddas på sekunder |
| Mobila AR/VR‑appar | Mindre minnesavtryck på enheter | Mindre nät håller appen responsiv |
| Molnrenderade scener | Minska bandbreddskostnader | Export med ett klick från Aspose.3D till Draco |

## Vanliga problem och lösningar

| Problem | Orsak | Lösning |
|---------|-------|---------|
| **`NoClassDefFoundError` for Draco classes** | Aspose.3D JAR-filer är inte på classpath | Verifiera att *alla* Aspose.3D JAR‑filer är inkluderade och att versionen matchar dokumentationen. |
| **Output file is empty** | `MyDir` pekar på en icke‑existerande mapp | Skapa katalogen programatiskt (`Files.createDirectories(Paths.get(MyDir))`) innan filen skrivs. |
| **Compressed mesh looks distorted** | Användning av låg komprimeringsnivå eller otillräcklig tessellation | Byt till `DracoCompressionLevel.OPTIMAL` och öka sfärens tessellation (t.ex. `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` väljer den högsta komprimeringskvaliteten för Draco‑utdata. |

## Vanliga frågor

**Q: Är Aspose.3D kompatibel med olika 3d‑filformat?**  
A: Ja, Aspose.3D stöder OBJ, FBX, STL, GLTF och många fler, vilket gör det till ett mångsidigt val för **Aspose 3d export**‑pipelines.

**Q: Kan jag använda Google Draco för komprimering i andra programmeringsspråk?**  
A: Absolut. Draco erbjuder inhemska bibliotek för C++, Python och JavaScript. Denna handledning fokuserar på Java, men koncepten gäller för alla språk.

**Q: Var kan jag hitta ytterligare Aspose.3D‑dokumentation?**  
A: Besök **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)** för fullständiga API‑referenser och fler exempel.

**Q: Hur får jag en tillfällig licens för Aspose.3D?**  
A: Utforska tillfälliga licensalternativ på **[Aspose temporary license page](https://purchase.aspose.com/temporary-license/)**.

**Q: Finns det ett community‑forum för Aspose.3D‑support?**  
A: Ja, gå med i diskussionen på **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.

## Slutsats

I den här guiden demonstrerade vi hur man **minskar 3d-modellens storlek** genom att skapa ett sfärnät i Java och sedan komprimera det med Google Draco via Aspose.3D. Genom att följa dessa koncisa steg kan du kraftigt krympa nätfiler, förbättra laddningstider och hålla dina Java‑baserade 3d‑applikationer responsiva och bandbredds‑vänliga.

---

**Last Updated:** 2026-11-17  
**Tested With:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose

## Relaterade handledningar

- [Minska 3D-filstorlek – Komprimera scener med Aspose.3D för Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Generera ett Draco-punktmoln från sfärer med Aspose.3D för Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Lär dig att triangulera nät för optimerad rendering i Java med Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}