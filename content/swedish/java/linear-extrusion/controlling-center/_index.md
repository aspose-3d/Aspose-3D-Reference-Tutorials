---
title: Kontrollcenter i linjär extrudering med Aspose.3D för Java
linktitle: Kontrollcenter i linjär extrudering med Aspose.3D för Java
second_title: Aspose.3D Java API
description: Utforska en värld av 3D-grafik i Java med Aspose.3D. Styr mitten i linjär extrudering utan ansträngning.
type: docs
weight: 11
url: /sv/java/linear-extrusion/controlling-center/
---
## Introduktion

en värld av 3D-grafik och Java-programmering spelar kontroll av mitten i linjär extrudering en avgörande roll för att uppnå önskade effekter i dina projekt. Aspose.3D för Java tillhandahåller en kraftfull verktygslåda för att hantera sådana uppgifter sömlöst. I den här handledningen kommer vi att dyka ner i processen att styra centret i linjär extrudering med Aspose.3D för Java, och bryta ner varje steg för att säkerställa en smidig och heltäckande förståelse.

## Förutsättningar

Innan vi ger oss ut på denna handledningsresa, se till att du har följande förutsättningar på plats:

1. Java-utvecklingsmiljö: Se till att du har en Java-utvecklingsmiljö inställd på din maskin.

2.  Aspose.3D för Java: Ladda ner och installera Aspose.3D-biblioteket. Du hittar biblioteket och dess dokumentation[här](https://reference.aspose.com/3d/java/).

3. Dokumentkatalog: Skapa en katalog för att lagra dina Java-dokument. Låt oss kalla det "Din dokumentkatalog."

## Importera paket

Importera nödvändiga paket för Aspose.3D i din Java-utvecklingsmiljö. Detta säkerställer att din kod har tillgång till funktionerna som tillhandahålls av biblioteket.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Steg 1: Ställ in basprofilen

Initiera basprofilen som ska extruderas. I det här exemplet använder vi en rektangelform med en avrundningsradie på 0,3.

```java
// Sökvägen till dokumentkatalogen.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Steg 2: Skapa en 3D-scen

Bygg grunden för din 3D-värld genom att skapa en scen.

```java
Scene scene = new Scene();
```

## Steg 3: Skapa vänster och höger noder

Etablera vänster och höger noder inom din scen. Dessa noder fungerar som arbetsytan för dina 3D-objekt.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Steg 4: Linjär extrudering med Center Property

Utför linjär extrudering på vänster nod utan centrering och ställ in antalet skivor till 3.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Steg 5: Ställ in markplan för referens

Förbättra den visuella representationen genom att lägga till ett jordplan till den vänstra noden.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Steg 6: Linjär strängsprutning med mittegenskap (höger nod)

Utför linjär extrudering på höger nod, denna gång centrera extruderingen och ställ återigen in antalet skivor till 3.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Steg 7: Ställ in jordplan för referens (höger nod)

I likhet med den vänstra noden, lägg till ett jordplan till den högra noden som referens.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Steg 8: Spara 3D-scenen

Spara din 3D-scen i Wavefront OBJ-format.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Slutsats

Att styra centrum i linjär extrudering med Aspose.3D för Java öppnar upp spännande möjligheter inom 3D-grafikutveckling. Genom att följa denna steg-för-steg-guide har du lärt dig hur du manipulerar centeregenskapen, så att du kan uppnå önskade visuella effekter i dina Java-projekt.

## FAQ's

### F1: Kan jag använda Aspose.3D för Java i kommersiella projekt?

 S1: Ja, Aspose.3D för Java är tillgänglig för kommersiellt bruk. För licensinformation, besök[här](https://purchase.aspose.com/buy).

### F2: Finns det en gratis provperiod?

 S2: Ja, du kan utforska en gratis testversion av Aspose.3D för Java[här](https://releases.aspose.com/).

### F3: Var kan jag hitta stöd för Aspose.3D för Java?

 S3: Gemenskapsforumet Aspose.3D är ett bra ställe att söka stöd och dela med sig av dina erfarenheter på. Besök forumet[här](https://forum.aspose.com/c/3d/18).

### F4: Behöver jag en tillfällig licens för att testa?

S4: Ja, om du behöver en tillfällig licens för teständamål kan du få en[här](https://purchase.aspose.com/temporary-license/).

### F5: Var kan jag hitta dokumentationen?

 S5: Dokumentationen för Aspose.3D för Java finns tillgänglig[här](https://reference.aspose.com/3d/java/).