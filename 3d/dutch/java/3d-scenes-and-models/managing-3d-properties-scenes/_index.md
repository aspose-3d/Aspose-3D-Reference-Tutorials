---
date: 2025-12-01
description: Leer hoe u de textuurkleur wijzigt, materiaaleigenschappen benadert,
  Vector3‑waarden instelt en eigenschappen op naam opvraagt in Java‑scènes met Aspose.3D
  – een volledige Aspose 3D‑tutorial.
language: nl
linktitle: Change texture color and manage 3D properties in Java scenes using Aspose.3D
second_title: Aspose.3D Java API
title: Verander textuurkleur en beheer 3D‑eigenschappen in Java‑scènes met Aspose.3D
url: /java/3d-scenes-and-models/managing-3d-properties-scenes/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Verander textuurkleur en beheer 3D‑eigenschappen in Java‑scènes met Aspose.3D

## Inleiding

In deze **Aspose 3D‑tutorial** ontdekt u hoe u **textuurkleur** kunt wijzigen en kunt werken met 3D‑eigenschappen en aangepaste gegevens binnen Java‑scènes. Of u nu een spel, een productvisualisatie of een wetenschappelijke viewer bouwt, het kunnen aanpassen van materiaaleigenschappen tijdens runtime geeft u volledige artistieke controle. Laten we stap‑voor‑stap door het proces lopen, van het laden van een scène tot het aanpassen van de *Diffuse*-kleur met een `Vector3`‑waarde.

## Snelle antwoorden
- **Wat kan ik aanpassen?** U kunt textuurkleur, doorzichtigheid, glans en elke aangepaste eigenschap die aan een materiaal is gekoppeld wijzigen.  
- **Welke klasse bevat de gegevens?** `Material` en zijn `PropertyCollection`.  
- **Hoe stel ik een nieuwe kleur in?** Gebruik `props.set("Diffuse", new Vector3(r, g, b))`.  
- **Heb ik een licentie nodig?** Een tijdelijke licentie werkt voor evaluatie; een volledige licentie is vereist voor productie.  
- **Ondersteunde formaten?** FBX, OBJ, STL, GLTF en nog veel meer.

## Voorvereisten

- Java Development Kit (JDK) 8 of nieuwer geïnstalleerd.  
- Aspose.3D for Java‑bibliotheek (download van de [Aspose‑website](https://releases.aspose.com/3d/java/)).  
- Basiskennis van Java‑syntaxis en object‑georiënteerde concepten.

## Importeer pakketten

Voordat u enige logica schrijft, importeert u de klassen die u toegang geven tot materiaaleigenschappen en vectormanipulatie.

```java
import java.io.IOException;

import com.aspose.threed.Material;
import com.aspose.threed.Property;
import com.aspose.threed.PropertyCollection;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;
```

### Waarom deze klassen importeren?

- `Scene` laadt en vertegenwoordigt het 3D‑bestand.  
- `Material` geeft u de oppervlakdefinitie (texturen, kleuren, enz.).  
- `PropertyCollection` is een dictionary‑achtige container die u **toegang tot materiaaleigenschappen** per naam geeft.  
- `Vector3` is het datatype dat wordt gebruikt voor kleuren en andere vectoren met drie componenten.

## Stap 1: Initialiseer de scène

```java
String dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
```

We maken een `Scene`‑object aan door een FBX‑bestand te laden dat al een textuur bevat. Dit is het canvas waarop we **textuurkleur** zullen wijzigen.

## Stap 2: Toegang tot materiaaleigenschappen

```java
Material material = scene.getRootNode().getChildNodes().get(0).getMaterial();
PropertyCollection props = material.getProperties();
```

Hier **benaderen we materiaaleigenschappen** van de eerste mesh in de scène. Het `Material`‑object bevat een `PropertyCollection` die elke configureerbare eigenschap opslaat, zoals *Diffuse*, *Specular* en aangepaste gebruikersdata.

## Stap 3: Lijst alle eigenschappen

```java
for (Property prop : props) {
    System.out.println("Name" + prop.getName() + " Value = " + prop.getValue());
}
```

Itereren over `props` print elke eigenschapsnaam en de huidige waarde. Deze snelle inventaris helpt u ontdekken welke sleutels u later kunt wijzigen, bijvoorbeeld `"Diffuse"` voor de basiskleur.

## Stap 4: Stel Vector3‑waarde in om textuurkleur te wijzigen

```java
props.set("Diffuse", new Vector3(1, 0, 1));
```

**Pro tip:** De `Vector3`‑constructor neemt drie kommagetallen die respectievelijk de **rode, groene en blauwe** componenten (bereik 0‑1) vertegenwoordigen. Het instellen van `(1, 0, 1)` verandert de basiskleur van de textuur naar magenta, waardoor u effectief **de textuurkleur van het model** wijzigt.

## Stap 5: Eigenschap ophalen op naam

```java
Object diffuse = (Vector3) props.get("Diffuse");
System.out.println(diffuse);
```

Dit toont **het ophalen van een eigenschap op naam**. We casten het geretourneerde `Object` naar `Vector3` om programmatisch met de kleur te werken.

## Stap 6: Toegang tot eigenschapsinstantie

```java
Property pdiffuse = props.findProperty("Diffuse");
System.out.println(pdiffuse);
```

`findProperty` retourneert het volledige `Property`‑object, waardoor u toegang krijgt tot metadata zoals het type van de eigenschap, het label en eventuele gekoppelde aangepaste data.

## Stap 7: Doorloop sub‑eigenschappen van eigenschap

```java
for (Property pp : pdiffuse.getProperties()) {
    System.out.println("Diffuse. " + pp.getName() + " = " + pp.getValue());
}
```

Sommige eigenschappen zijn hiërarchisch. Het doorlopen van `pdiffuse.getProperties()` laat u eventuele geneste attributen zien (bijv. textuurcoördinaten, animatiesleutels) die bij de *Diffuse*‑entry horen.

## Veelvoorkomende problemen & oplossingen

| Probleem | Waarom het gebeurt | Oplossing |
|----------|--------------------|-----------|
| **`NullPointerException` op `material`** | Het knooppunt heeft mogelijk geen toegewezen materiaal. | Roep `node.setMaterial(new Material())` aan voordat u eigenschappen benadert. |
| **Kleur verandert niet** | Het model gebruikt een textuur die de *Diffuse*-kleur overschrijft. | Schakel de textuur uit of wijzig de textuurafbeelding direct. |
| **`ClassCastException` bij ophalen** | Er wordt geprobeerd een niet‑Vector3‑eigenschap te casten. | Controleer het type van de eigenschap met `pdiffuse.getValue().getClass()` voordat u cast. |

## Veelgestelde vragen

**Q: Hoe kan ik de Aspose.3D‑bibliotheek in mijn Java‑project installeren?**  
A: Download de JAR van de [Aspose‑website](https://releases.aspose.com/3d/java/) en voeg deze toe aan de classpath van uw project of aan de Maven/Gradle‑dependencies.

**Q: Zijn er gratis proefopties beschikbaar voor Aspose.3D?**  
A: Ja, een volledig functionele 30‑daagse proefversie is verkrijgbaar via de [Aspose‑proefpagina](https://releases.aspose.com/).

**Q: Waar vind ik gedetailleerde documentatie voor Aspose.3D in Java?**  
A: De officiële API‑referentie staat op [Aspose.3D‑documentatie](https://reference.aspose.com/3d/java/).

**Q: Is er een ondersteuningsforum voor Aspose.3D waar ik vragen kan stellen?**  
A: Zeker—bezoek het [Aspose.3D‑ondersteuningsforum](https://forum.aspose.com/c/3d/18) om in contact te komen met de community en experts.

**Q: Hoe kan ik een tijdelijke licentie voor Aspose.3D verkrijgen?**  
A: Vraag er een aan via de [tijdelijke licentie‑pagina](https://purchase.aspose.com/temporary-license/) op de Aspose‑site.

**Q: Kan ik andere materiaaleigenschappen dan kleur wijzigen?**  
A: Ja, eigenschappen zoals `Specular`, `Opacity` en aangepaste gebruikersdata kunnen worden aangepast met hetzelfde `props.set`‑patroon.

## Conclusie

U heeft nu geleerd hoe u **textuurkleur** kunt wijzigen, **materiaaleigenschappen** kunt benaderen, een **Vector3‑waarde** kunt instellen en **eigenschappen op naam** kunt ophalen in een Java‑scene met Aspose.3D. Deze technieken geven u fijnmazige controle over elk 3D‑object, waardoor dynamische visuele effecten en runtime‑aanpassingen in uw toepassingen mogelijk worden.

---

**Laatst bijgewerkt:** 2025-12-01  
**Getest met:** Aspose.3D for Java 24.11  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}