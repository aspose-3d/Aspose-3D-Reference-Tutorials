---
date: 2025-12-17
description: Leer hoe u een licentie instelt in Aspose.3D voor Java en hoe u publieke
  en private sleutels gebruikt voor metered licenties.
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Hoe licentie instellen in Aspose.3D voor Java – Complete gids
url: /nl/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe een licentie instellen in Aspose.3D voor Java

## Introductie

Welkom! In deze stapsgewijze tutorial ontdek je **hoe je een licentie instelt** voor Aspose.3D in een Java‑applicatie en leer je ook **hoe je openbare en privésleutels gebruikt** voor meter‑licenties. Aspose.3D is een krachtige Java‑bibliotheek die het werken met 3D‑bestandsformaten vereenvoudigt, en een geldige licentie ontgrendelt de volledige functionaliteit. Aan het einde van deze gids kun je licenties naadloos integreren in elk Java‑project.

## Snelle antwoorden
- **Wat is de primaire manier om een licentie in te stellen?** Gebruik de `License`‑klasse en roep `setLicense` aan met een bestandspad of stream.  
- **Kan ik de licentie vanuit een stream laden?** Ja – een `FileInputStream` werkt perfect.  
- **Waar zijn openbare/privésleutels voor?** Ze maken meter‑licenties mogelijk via de `Metered`‑klasse.  
- **Heb ik een licentie nodig voor ontwikkeling?** Een tijdelijke of proeflicentie is voldoende voor testen; een volledige licentie is vereist voor productie.  
- **Welke Java‑versies worden ondersteund?** Aspose.3D werkt met Java 6 en hoger.

## Voorvereisten

Voordat we beginnen, zorg ervoor dat je het volgende hebt:

- Een basiskennis van Java‑programmeren.
- De Aspose.3D‑bibliotheek toegevoegd aan je project. Download deze van de [release‑pagina](https://releases.aspose.com/3d/java/).
- Een geldig `.lic`‑bestand of je openbare en privésleutels voor meter‑licenties.

## Importeer pakketten

Voeg de benodigde imports toe aan je Java‑bronbestand. Zorg ervoor dat de Aspose.3D‑JAR op de classpath staat.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Hoe een licentie instellen met een bestand

### Stap 1: Maak een licentie‑object

Instantieer de `License`‑klasse – dit object bevat de licentie‑informatie.

```java
License license = new License();
```

### Stap 2: Licentie instellen vanuit een bestand

Geef het relatieve of absolute pad naar je `.lic`‑bestand op en pas het toe.

```java
license.setLicense("Aspose._3D.lic");
```

> **Pro tip:** Houd het licentiebestand buiten je source‑control‑map om onbedoelde blootstelling te voorkomen.

## Hoe een licentie instellen met een stream

### Stap 1: Maak een licentie‑object

Zoals eerder, begin met een nieuwe `License`‑instantie.

```java
License license = new License();
```

### Stap 2: Licentie instellen vanuit een stream

Lees het licentiebestand in een `FileInputStream` en geef de stream door aan `setLicense`. Het try‑with‑resources‑blok zorgt ervoor dat de stream automatisch wordt gesloten.

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## Hoe openbare en privésleutels te gebruiken voor meter‑licenties

### Stap 1: Initialiseert een Metered‑licentie‑object

Maak een instantie van de `Metered`‑klasse, die meter‑licenties (pay‑as‑you‑go) afhandelt.

```java
Metered metered = new Metered();
```

### Stap 2: Stel openbare en privésleutels in

Geef de sleutels die je van Aspose hebt ontvangen. Deze sleutels stellen de bibliotheek in staat om gebruik te rapporteren aan de licentieserver.

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

> **Waarschuwing:** Code je privésleutel nooit hard‑coded in een publiek verspreide JAR. Overweeg deze te laden vanuit een veilige locatie of een omgevingsvariabele.

## Veelvoorkomende gebruikssituaties

- **Enterprise 3D‑rendering‑pijplijnen** – ontgrendel high‑performance API's na het instellen van de licentie.
- **Geautomatiseerde testomgevingen** – gebruik een tijdelijke licentie (zie de FAQ) om functionaliteit te valideren zonder een volledige licentie aan te schaffen.
- **Metered SaaS‑oplossingen** – integreer openbare/privésleutels om klanten te factureren op basis van daadwerkelijk gebruik.

## Conclusie

Gefeliciteerd! Je weet nu **hoe je een licentie instelt** voor Aspose.3D in Java met een bestand, een stream, en hoe je **openbare en privésleutels gebruikt** voor meter‑licenties. Met deze stappen kun je Aspose.3D vol vertrouwen integreren in elke Java‑applicatie en volledig profiteren van de 3D‑verwerkingsmogelijkheden.

## Veelgestelde vragen

**Q1: Is Aspose.3D compatibel met alle Java‑versies?**  
A1: Ja, Aspose.3D werkt met Java 6 en latere versies.

**Q2: Waar kan ik extra documentatie vinden?**  
A2: Je kunt de documentatie raadplegen [hier](https://reference.aspose.com/3d/java/).

**Q3: Kan ik Aspose.3D uitproberen voordat ik koop?**  
A3: Ja, je kunt een gratis proefversie verkennen [hier](https://releases.aspose.com/).

**Q4: Hoe kan ik ondersteuning krijgen voor Aspose.3D?**  
A4: Bezoek het [Aspose.3D‑forum](https://forum.aspose.com/c/3d/18) voor community‑ en officiële ondersteuning.

**Q5: Heb ik een tijdelijke licentie nodig voor testen?**  
A5: Ja, verkrijg een tijdelijke licentie [hier](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**Laatst bijgewerkt:** 2025-12-17  
**Getest met:** Aspose.3D 24.11 voor Java  
**Auteur:** Aspose  

---