---
date: 2025-12-17
description: Leer hoe u een gedraaid 3D‑model maakt met Aspose.3D voor Java, met lineaire
  extrusie‑draai, en een OBJ‑bestand exporteert. Volg onze stapsgewijze handleiding.
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Maak een gedraaid 3D‑model – Toepassen van draaiing in lineaire extrusie met
  Aspose.3D voor Java
url: /nl/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Toepassen van draaiing bij lineaire extrusie met Aspose.3D voor Java

## Inleiding

Welkom bij deze stap‑voor‑stap‑handleiding over **hoe je een gedraaid 3D‑model maakt** door een draaiing toe te passen tijdens lineaire extrusie met Aspose.3D voor Java. Of je nu architecturale visualisaties, game‑assets of engineering‑prototypes bouwt, een draaiing kan je geometrie een dynamisch, spiraalvormig uiterlijk geven met slechts een paar regels code.

## Snelle antwoorden
- **Wat betekent “draaiing” bij extrusie?** Het roteert het profiel rond de extrusie‑as terwijl de vorm wordt uitgerekt.  
- **Welke API‑klasse behandelt de draaiing?** `LinearExtrusion` biedt de `setTwist`‑methode.  
- **Heb ik een licentie nodig om het voorbeeld uit te voeren?** Een gratis proefversie werkt voor evaluatie; een commerciële licentie is vereist voor productie.  
- **Kan ik het resultaat exporteren als OBJ?** Ja, gebruik `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Welke Java‑versie is vereist?** Java 8 of hoger wordt volledig ondersteund.

## Voorvereisten

Voordat je aan de tutorial begint, zorg dat je de volgende zaken hebt:

- Java‑ontwikkelomgeving: Zorg dat Java op je systeem is geïnstalleerd.  
- Aspose.3D‑bibliotheek: Download en installeer de Aspose.3D‑bibliotheek voor Java vanaf de [download‑link](https://releases.aspose.com/3d/java/).  
- Documentatie: Raadpleeg de [Aspose.3D‑documentatie](https://reference.aspose.com/3d/java/) voor uitgebreide begeleiding.

## Pakketten importeren

Voordat je begint met coderen, importeer je de benodigde pakketten in je Java‑project. Hieronder een voorbeeld hoe je dit doet:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Documentdirectory instellen

Definieer eerst waar het gegenereerde 3D‑bestand wordt opgeslagen.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Basisprofiel initialiseren

Maak vervolgens de vorm die geëxtrudeerd zal worden. In dit voorbeeld gebruiken we een rechthoek met een kleine afrondingsstraal.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Een Scene maken

Een `Scene`‑object fungeert als de container voor alle 3D‑nodes.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Nodes maken

Voeg twee child‑nodes toe aan de scene – één blijft recht, de andere krijgt de draaiing.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Lineaire extrusie‑draaiing

Nu voeren we **lineaire extrusie‑draaiing** uit op beide nodes. De linkse node krijgt een draaiing van 0° (recht), terwijl de rechtse node een draaiing van 90° krijgt, waardoor een spiraalvorm ontstaat. We stellen ook het aantal slices in om een gladde geometrie te garanderen.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## OBJ‑bestand exporteren Java

Sla tenslotte de scene op in het breed ondersteunde OBJ‑formaat. Dit demonstreert de **export OBJ‑bestand Java**‑functionaliteit van Aspose.3D.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Waarom dit belangrijk is

Het maken van een gedraaid 3D‑model geeft je een krachtig visueel effect zonder externe modellerings‑tools. Het is vooral nuttig voor:

- **Mechanische onderdelen** die helicale kenmerken vereisen (bijv. veren, schroeven).  
- **Artistieke ontwerpen** waarbij een subtiele spiraal visuele interesse toevoegt.  
- **Game‑assets** die profiteren van low‑poly, procedureel gegenereerde geometrie.

## Veelvoorkomende problemen & tips

| Probleem | Oplossing |
|----------|-----------|
| Draaiing lijkt plat of ontbreekt | Zorg dat `setSlices` hoog genoeg is (bijv. 100) voor een soepele rotatie. |
| OBJ‑bestand opent niet in viewer | Controleer of het uitvoerpad (`MyDir`) correct is en of het bestand schrijfrechten heeft. |
| Onverwachte schaalverandering | Controleer het eenheidssysteem van je bronprofiel; Aspose.3D werkt standaard in meters. |

## Veelgestelde vragen

**V: Kan ik Aspose.3D voor Java gebruiken met andere 3D‑bestandsformaten?**  
A: Ja, Aspose.3D ondersteunt een breed scala aan formaten zoals FBX, STL, 3MF en meer.

**V: Waar vind ik ondersteuning voor Aspose.3D voor Java?**  
A: Bezoek het [Aspose.3D‑forum](https://forum.aspose.com/c/3d/18) voor community‑hulp en officiële assistentie.

**V: Is er een gratis proefversie beschikbaar?**  
A: Ja, je kunt een proefversie downloaden via [hier](https://releases.aspose.com/).

**V: Hoe verkrijg ik een tijdelijke licentie voor testen?**  
A: Haal een tijdelijke licentie op via de [pagina voor tijdelijke licenties](https://purchase.aspose.com/temporary-license/).

**V: Waar kan ik een volledige licentie aanschaffen?**  
A: Koop Aspose.3D voor Java via de [aankoop‑pagina](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Laatst bijgewerkt:** 2025-12-17  
**Getest met:** Aspose.3D 24.11 for Java  
**Auteur:** Aspose  

---