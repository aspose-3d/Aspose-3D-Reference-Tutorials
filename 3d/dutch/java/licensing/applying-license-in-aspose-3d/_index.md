---
date: 2026-05-24
description: Leer hoe u de aspose 3d licentie in Java instelt, een license file toepast,
  deze streamt, of gebruikmaakt van metered licensing met public en private keys.
keywords:
- set aspose 3d license
- aspose 3d java licensing
- metered licensing java
linktitle: Hoe de Aspose-licentie in Aspose.3D voor Java instellen
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to set aspose 3d license in Java, apply a license file, stream
    it, or use metered licensing with public and private keys.
  headline: How to Set Aspose 3D License in Java (set aspose 3d license)
  type: TechArticle
- description: Learn how to set aspose 3d license in Java, apply a license file, stream
    it, or use metered licensing with public and private keys.
  name: How to Set Aspose 3D License in Java (set aspose 3d license)
  steps:
  - name: Create a `License` object
    text: Instantiate the `License` class; this prepares the runtime to accept a license
      file.
  - name: Apply the license file
    text: Provide the absolute or relative path to your `.lic` file and call `setLicense`.
      The method returns `void`, and the license is cached after the first successful
      call, so subsequent calls are inexpensive.
  - name: Create a `License` object
    text: As before, start by creating an instance of the `License` class.
  - name: Load the license via `FileInputStream`
    text: Open a `FileInputStream` pointing to your `.lic` file (or any `InputStream`)
      and pass it to `setLicense`. The stream is read once and then closed automatically.
  - name: Initialize a `Metered` license object
    text: The `Metered` class represents a cloud‑based license that validates usage
      against Aspose’s metering server.
  - name: Set public and private keys
    text: Call `setMeteredKey(publicKey, privateKey)` with the keys you received when
      you purchased a metered license. The library contacts the server once to verify
      the keys and then caches the result.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports Java 6 through Java 21, covering more than 15
      major releases.
    question: Is Aspose.3D compatible with all Java versions?
  - answer: You can refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find additional documentation?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Can I try Aspose.3D before purchasing?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for support.
    question: How can I get support for Aspose.3D?
  - answer: Yes, obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).
    question: Do I need a temporary license for testing?
  type: FAQPage
second_title: Aspose.3D Java API
title: Hoe de Aspose 3D-licentie in Java instellen (set aspose 3d license)
url: /nl/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe Aspose 3D-licentie in Java instellen (set aspose 3d license)

## Introductie

In deze uitgebreide tutorial ontdek je **hoe je een Aspose 3D-licentie** instelt voor Aspose.3D in een Java‑omgeving. Of je nu de voorkeur geeft aan het laden van een licentiebestand, het streamen ervan, of het gebruik van metered licensering met openbare en privé‑sleutels, we lopen elke benadering stap‑voor‑stap door zodat je snel en zelfverzekerd de volledige functionaliteit van Aspose.3D kunt ontgrendelen. Het correct instellen van de licentie verwijdert evaluatiewatermerken, maakt premium 3D‑formaten beschikbaar en zorgt voor volledige naleving van het licentiemodel van Aspose.

## Snelle antwoorden
- **Wat is de primaire manier om een Aspose.3D‑licentie in te stellen?** Gebruik de `License`‑klasse en roep `setLicense` aan met een bestandspad of stream.  
- **Kan ik de licentie vanuit een stream laden?** Ja – wikkel het `.lic`‑bestand in een `FileInputStream` en geef het door aan `setLicense`.  
- **Wat als ik een metered‑licentie nodig heb?** Initialiseert een `Metered`‑object en roep `setMeteredKey` aan met je openbare en privé‑sleutels.  
- **Heb ik een licentie nodig voor ontwikkel‑builds?** Een proef‑ of tijdelijke licentie is vereist voor elke niet‑evaluatiesituatie.  
- **Welke Java‑versies worden ondersteund?** Aspose.3D werkt met Java 6 tot en met Java 21, meer dan 15 hoofdreleases.

## Wat is de `License`‑klasse?
De `License`‑klasse is het kernlicentie‑object van Aspose.3D dat een `.lic`‑bestand in het geheugen laadt, de licentie‑informatie valideert, en zodra deze is geïnstantieerd, de licentie globaal toepast voor het JVM‑proces, zodat alle daaropvolgende Aspose.3D‑bewerkingen onder de gelicentieerde modus draaien zonder evaluatiebeperkingen.

## Waarom de Aspose 3D‑licentie instellen?
Een geldige licentie inschakelen maakt **meer dan 50 premium 3D‑bestandsformaten** beschikbaar (inclusief FBX, OBJ, STL en GLTF) en verwijdert het “Evaluation”‑watermerk van gerenderde afbeeldingen. Het verwijdert ook limieten op de scenegrootte, waardoor modellen met **tot 1 miljoen vertices** verwerkt kunnen worden zonder prestatieverlies.

## Vereisten

Voordat we beginnen, zorg dat je de volgende zaken gereed hebt:

- Basiskennis van Java‑programmeren.  
- Aspose.3D‑bibliotheek geïnstalleerd. Je kunt deze downloaden van de [release‑pagina](https://releases.aspose.com/3d/java/).  

## Pakketten importeren

Om te beginnen, importeer de benodigde pakketten in je Java‑project. Zorg ervoor dat Aspose.3D aan je classpath is toegevoegd. Hieronder een voorbeeld:

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

De `License`‑klasse is verantwoordelijk voor het laden van een `.lic`‑bestand en het globaal toepassen ervan, terwijl de `Metered`‑klasse cloud‑gebaseerde metered licensering mogelijk maakt door openbare en privé‑sleutels te valideren tegen de licentieserver van Aspose.

## Hoe een licentie toepassen vanuit een bestand?

Laad je licentie direct vanuit een `.lic`‑bestand op schijf. Deze methode is de meest eenvoudige aanpak voor desktop‑ of on‑premises‑applicaties, en zorgt ervoor dat de licentie één keer bij het opstarten wordt gelezen en gedurende de levensduur van de JVM wordt gecached, waardoor er geen runtime‑overhead meer is na de initiële lading.

### Stap 1: Maak een `License`‑object
Instantieer de `License`‑klasse; dit bereidt de runtime voor om een licentiebestand te accepteren.

### Stap 2: Pas het licentiebestand toe
Geef het absolute of relatieve pad naar je `.lic`‑bestand op en roep `setLicense` aan. De methode retourneert `void`, en de licentie wordt gecached na de eerste succesvolle aanroep, zodat latere aanroepen weinig kosten.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Hoe een licentie toepassen vanuit een stream?

Het streamen van een licentie is handig wanneer het bestand is ingebed als resource, opgeslagen op een veilige locatie, of opgehaald wordt van een externe service tijdens runtime. Door een `InputStream` te gebruiken, vermijd je het blootleggen van het fysieke bestandspad en kun je de licentie‑gegevens versleuteld of verpakt in je JAR houden, wat de beveiliging verhoogt terwijl de bibliotheek nog steeds de licentie‑bytes kan lezen.

### Stap 1: Maak een `License`‑object
Zoals eerder, begin met het creëren van een instantie van de `License`‑klasse.

### Stap 2: Laad de licentie via `FileInputStream`
Open een `FileInputStream` die naar je `.lic`‑bestand (of een willekeurige `InputStream`) wijst en geef deze door aan `setLicense`. De stream wordt één keer gelezen en daarna automatisch gesloten.

```java
License license = new License();
```

## Hoe openbare en privé‑sleutels gebruiken voor metered licensering?

Metered licensering laat je Aspose.3D activeren zonder een fysiek `.lic`‑bestand, met behulp van sleutels die door de cloudservice van Aspose zijn uitgegeven. Deze aanpak is ideaal voor SaaS‑ of cloud‑gebaseerde implementaties waarbij het beheren van licentiebestanden op elke instantie onpraktisch is; de bibliotheek neemt één keer contact op met de metering‑server van Aspose om de sleutels te valideren en cachet vervolgens het resultaat voor de sessie.

### Stap 1: Initialiseer een `Metered` licentie‑object
De `Metered`‑klasse vertegenwoordigt een cloud‑gebaseerde licentie die gebruik valideert tegen de metering‑server van Aspose.

### Stap 2: Stel openbare en privé‑sleutels in
Roep `setMeteredKey(publicKey, privateKey)` aan met de sleutels die je hebt ontvangen bij de aankoop van een metered licentie. De bibliotheek neemt één keer contact op met de server om de sleutels te verifiëren en cachet vervolgens het resultaat.

```java
license.setLicense("Aspose._3D.lic");
```

## Veelvoorkomende problemen & tips

- **Bestand niet gevonden** – Controleer of het pad naar het `.lic`‑bestand correct is ten opzichte van de werkdirectory of gebruik een absoluut pad.  
- **Stream te vroeg gesloten** – Houd het `License`‑object levend gedurende de levensduur van de applicatie; de licentie wordt gecached na de eerste succesvolle aanroep.  
- **Metered‑sleutel komt niet overeen** – Controleer of de openbare en privé‑sleutels bij dezelfde metered licentie horen; een typefout veroorzaakt een runtime‑exception.  
- **Pro‑tip:** Plaats het licentiebestand op een veilige locatie buiten de source‑tree en laad het via een omgevingsvariabele om te voorkomen dat het in versiebeheer terechtkomt.

## Conclusie

Gefeliciteerd! Je hebt nu geleerd **hoe je een Aspose 3D‑licentie** in Java instelt met drie betrouwbare methoden: een licentie vanuit een bestand toepassen, deze streamen, en metered licensering configureren met openbare en privé‑sleutels. Met de licentie op zijn plaats kun je Aspose.3D naadloos integreren in je Java‑applicaties, alle premium 3D‑verwerkingsfuncties ontgrendelen en voldoen aan de licentie‑vereisten van Aspose.

## Veelgestelde vragen

**V: Is Aspose.3D compatibel met alle Java‑versies?**  
A: Ja, Aspose.3D ondersteunt Java 6 tot en met Java 21, meer dan 15 hoofdreleases.

**V: Waar kan ik extra documentatie vinden?**  
A: Je kunt de documentatie raadplegen [hier](https://reference.aspose.com/3d/java/).

**V: Kan ik Aspose.3D eerst uitproberen voordat ik koop?**  
A: Ja, je kunt een gratis proefversie verkennen [hier](https://releases.aspose.com/).

**V: Hoe krijg ik ondersteuning voor Aspose.3D?**  
A: Bezoek het [Aspose.3D‑forum](https://forum.aspose.com/c/3d/18) voor ondersteuning.

**V: Heb ik een tijdelijke licentie nodig voor testen?**  
A: Ja, verkrijg een tijdelijke licentie [hier](https://purchase.aspose.com/temporary-license/).

**V: Wat is het verschil tussen een bestandslicentie en een metered licentie?**  
A: Een bestandslicentie is een statisch `.lic`‑bestand gekoppeld aan een specifieke productversie, terwijl een metered licentie gebruik valideert tegen de cloud‑gebaseerde metering‑service van Aspose met openbare/privé‑sleutels.

**V: Kan ik de licentieladercode in een statische initializer plaatsen?**  
A: Absoluut – het plaatsen van de `License`‑initialisatie in een static‑block zorgt ervoor dat de licentie één keer wordt toegepast wanneer de klasse voor het eerst wordt geladen.

```java
License license = new License();
```
```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```
```java
Metered metered = new Metered();
```
```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

{{< blocks/products/products-backtop-button >}}

## Gerelateerde tutorials

- [Stap‑voor‑stap licentiegids voor Aspose.3D Java](/3d/java/licensing/)
- [3D‑scene maken in Java met Aspose 3D Java](/3d/java/3d-scenes-and-models/)
- [3D‑kubus maken, PBR‑materialen toepassen in Java met Aspose.3D](/3d/java/geometry/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}