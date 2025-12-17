---
date: 2025-12-17
description: Lär dig hur du ställer in licens i Aspose.3D för Java och hur du använder
  offentliga och privata nycklar för mätbaserad licensiering.
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Hur man ställer in licens i Aspose.3D för Java – Komplett guide
url: /sv/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hur man anger licens i Aspose.3D för Java

## Introduktion

Välkommen! I den här steg‑för‑steg‑handledningen kommer du att upptäcka **hur man anger licens** för Aspose.3D i en Java‑applikation och även lära dig **hur man använder offentliga och privata nycklar** för mätbaserad licensiering. Aspose.3D är ett kraftfullt Java‑bibliotek som förenklar arbete med 3D‑filformat, och en giltig licens låser upp hela funktionaliteten. I slutet av den här guiden kommer du att kunna integrera licensiering sömlöst i vilket Java‑projekt som helst.

## Snabba svar
- **Vad är det primära sättet att ange en licens?** Använd `License`‑klassen och anropa `setLicense` med en filsökväg eller en ström.  
- **Kan jag läsa in licensen från en ström?** Ja – en `FileInputStream` fungerar perfekt.  
- **Vad är offentliga/privata nycklar för?** De möjliggör mätbaserad licensiering via `Metered`‑klassen.  
- **Behöver jag en licens för utveckling?** En tillfällig eller provlicens räcker för testning; en fullständig licens krävs för produktion.  
- **Vilka Java‑versioner stöds?** Aspose.3D fungerar med Java 6 och senare.

## Förutsättningar

Innan vi börjar, se till att du har:

- Grundläggande kunskaper i Java‑programmering.
- Aspose.3D‑biblioteket tillagt i ditt projekt. Ladda ner det från [release‑sidan](https://releases.aspose.com/3d/java/).
- En giltig `.lic`‑fil eller dina offentliga och privata mätnycklar.

## Importera paket

Lägg till de nödvändiga importerna i din Java‑källfil. Se till att Aspose.3D‑JAR‑filen finns på klassvägen.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Så här anger du licens med en fil

### Steg 1: Skapa ett licensobjekt

Instansiera `License`‑klassen – detta objekt kommer att hålla licensinformationen.

```java
License license = new License();
```

### Steg 2: Ange licens från fil

Ange den relativa eller absoluta sökvägen till din `.lic`‑fil och tillämpa den.

```java
license.setLicense("Aspose._3D.lic");
```

> **Proffstips:** Förvara licensfilen utanför din källkontrollsmapp för att undvika oavsiktlig exponering.

## Så här anger du licens med en ström

### Steg 1: Skapa ett licensobjekt

Som tidigare, börja med en ny `License`‑instans.

```java
License license = new License();
```

### Steg 2: Ange licens från en ström

Läs licensfilen in i en `FileInputStream` och skicka strömmen till `setLicense`. `try‑with‑resources`‑blocket garanterar att strömmen stängs automatiskt.

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## Hur man använder offentliga och privata nycklar för mätbaserad licensiering

### Steg 1: Initiera ett Metered‑licensobjekt

Skapa en instans av `Metered`‑klassen, som hanterar mätbaserad (pay‑as‑you‑go) licensiering.

```java
Metered metered = new Metered();
```

### Steg 2: Ange offentliga och privata nycklar

Tillhandahåll de nycklar du fått från Aspose. Dessa nycklar gör det möjligt för biblioteket att rapportera användning tillbaka till licensservern.

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

> **Varning:** Koda aldrig din privata nyckel hårdkodat i en offentligt distribuerad JAR. Överväg att läsa in den från en säker plats eller miljövariabel.

## Vanliga användningsområden

- **Enterprise 3D‑renderingspipelines** – lås upp högpresterande API:er efter att licensen har angetts.
- **Automatiserade testmiljöer** – använd en tillfällig licens (se FAQ) för att validera funktionalitet utan att köpa en full licens.
- **Mätbaserade SaaS‑lösningar** – integrera offentliga/privata nycklar för att fakturera kunder baserat på faktisk användning.

## Slutsats

Grattis! Du vet nu **hur man anger licens** för Aspose.3D i Java med en fil, en ström, och hur man **använder offentliga och privata nycklar** för mätbaserad licensiering. Med dessa steg kan du tryggt integrera Aspose.3D i vilken Java‑applikation som helst och utnyttja dess 3D‑bearbetningsmöjligheter fullt ut.

## Vanliga frågor

**Q1: Är Aspose.3D kompatibel med alla Java‑versioner?**  
A1: Ja, Aspose.3D fungerar med Java 6 och senare versioner.

**Q2: Var kan jag hitta ytterligare dokumentation?**  
A2: Du kan hänvisa till dokumentationen [här](https://reference.aspose.com/3d/java/).

**Q3: Kan jag prova Aspose.3D innan jag köper?**  
A3: Ja, du kan utforska en gratis provversion [här](https://releases.aspose.com/).

**Q4: Hur kan jag få support för Aspose.3D?**  
A4: Besök [Aspose.3D‑forumet](https://forum.aspose.com/c/3d/18) för gemenskap och officiell support.

**Q5: Behöver jag en tillfällig licens för testning?**  
A5: Ja, skaffa en tillfällig licens [här](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**Senast uppdaterad:** 2025-12-17  
**Testad med:** Aspose.3D 24.11 för Java  
**Författare:** Aspose  

---