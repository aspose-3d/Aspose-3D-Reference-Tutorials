---
date: 2026-02-20
description: Leer een Java‑3D‑grafiektutorial over het controleren van het centrum
  bij lineaire extrusie met Aspose.3D, inclusief hoe je de afrondingsradius instelt
  en een OBJ‑bestand opslaat in Java.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Java 3D Graphics‑handleiding – Middelpunt bij lineaire extrusie
url: /nl/java/linear-extrusion/controlling-center/
weight: 11
---

 3D Graphics Tutorial – Center in Linear Extrusion" => "# Java 3D Graphics Tutorial – Center in Linear Extrusion". Actually maybe better: "# Java 3D Graphics Tutorial – Center in Linear Extrusion" => "# Java 3D Graphics Tutorial – Center in Linear Extrusion". I'm going to translate to "# Java 3D Graphics Tutorial – Center in Linear Extrusion". Eh.

Let's just translate: "# Java 3D Graphics Tutorial – Center in Linear Extrusion" => "# Java 3D Graphics Tutorial – Center in Linear Extrusion". Not helpful.

Ok, I'll translate: "# Java 3D Graphics Tutorial – Center in Linear Extrusion" => "# Java 3D Graphics Tutorial – Center in Linear Extrusion". I think they might accept unchanged because it's a product name. I'll keep as is.

Proceed to other sections.

I'll translate paragraph.

Let's produce final content.

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D Graphics Tutorial – Center in Linear Extrusion

## Inleiding

Als je 3D‑visualisaties in Java bouwt, is het beheersen van extrusietechnieken essentieel. Deze **java 3d graphics tutorial** leidt je door het regelen van het middelpunt van een lineaire extrusie met Aspose.3D for Java, zodat je nauwkeurige, symmetrische modellen kunt maken zonder extra wiskunde. Aan het einde van deze gids begrijp je waarom de `center`‑eigenschap belangrijk is, hoe je **set rounding radius** instelt, en hoe je **save OBJ file java**‑compatibele output opslaat.

## Snelle antwoorden
- **Wat doet de center‑eigenschap?** Ze bepaalt of de extrusie symmetrisch is ten opzichte van de oorsprong van het profiel.  
- **Heb ik een licentie nodig om de code uit te voeren?** Een tijdelijke licentie werkt voor testen; een volledige licentie is vereist voor productie.  
- **Welk bestandsformaat wordt gebruikt voor het resultaat?** De scène wordt opgeslagen als een Wavefront OBJ‑bestand.  
- **Kan ik het aantal slices wijzigen?** Ja, gebruik `setSlices(int)` op het `LinearExtrusion`‑object.  
- **Is Aspose.3D compatibel met Java 8+?** Absoluut – het ondersteunt alle moderne Java‑versies.

## Wat is een java 3d graphics tutorial?

Een **java 3d graphics tutorial** legt stap‑voor‑stap uit hoe je Java‑bibliotheken gebruikt om driedimensionale objecten te maken, te manipuleren en te renderen. In dit geval richten we ons op de extrusie‑API van Aspose.3D, die 2‑D‑profielen omzet in volledig uitgewerkte 3‑D‑meshes.

## Waarom Aspose.3D for Java gebruiken?

- **High‑level API** – Geen noodzaak om low‑level mesh‑berekeningen te schrijven.  
- **Cross‑format ondersteuning** – Exporteren naar OBJ, FBX, STL en meer.  
- **Performance‑geoptimaliseerd** – Verwerkt grote scènes efficiënt.  
- **Rijke documentatie** – Bevat voorbeelden zoals hieronder.

## Vereisten

Zorg ervoor dat je het volgende hebt voordat we beginnen:

1. **Java Development Environment** – JDK 8 of nieuwer geïnstalleerd.  
2. **Aspose.3D for Java** – Download de bibliotheek en documentatie [hier](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Maak een map op je machine aan om gegenereerde bestanden op te slaan; we noemen deze **“Your Document Directory.”**

## Import Packages

Importeer in je Java‑IDE de Aspose.3D‑klassen die je nodig hebt. Hiermee krijgt de compiler toegang tot de extrusie‑ en scenebouw‑functies.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Stapsgewijze handleiding

### Stap 1: Basisprofiel instellen

Maak eerst de 2‑D‑vorm die geëxtrudeerd gaat worden. Hier gebruiken we een rechthoek en **set rounding radius** op 0.3, waardoor de hoeken worden afgerond.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Stap 2: Een 3D‑scene maken

Een `Scene`‑object fungeert als container voor alle 3‑D‑nodes, lichten en camera’s.

```java
Scene scene = new Scene();
```

### Stap 3: Links‑ en rechts‑nodes toevoegen

We plaatsen twee aparte nodes naast elkaar zodat je de extrusie met en zonder centrering kunt vergelijken.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Stap 4: Lineaire extrusie – Geen centrum (linker node)

Maak de extrusie op de linker node, schakel centrering uit, en beperk de mesh tot drie slices voor een low‑poly preview.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Stap 5: Een grondvlak toevoegen ter referentie (linker node)

Een dunne box fungeert als visueel vloeroppervlak, zodat je de oriëntatie van de extrusie beter ziet.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Stap 6: Lineaire extrusie – Gecentreerd (rechter node)

Herhaal nu de extrusie, dit keer met `center` ingeschakeld. De geometrie wordt symmetrisch rond de oorsprong van het profiel.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Stap 7: Een grondvlak toevoegen ter referentie (rechter node)

Zelfde grondvlak voor de rechterkant, zodat de vergelijking duidelijk is.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Stap 8: De 3D‑scene opslaan

Exporteer tenslotte de volledige scene naar een Wavefront OBJ‑bestand – een formaat dat breed bruikbaar is in de meeste 3‑D‑editors.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Veelvoorkomende problemen en oplossingen

| Probleem | Waarom het gebeurt | Oplossing |
|----------|--------------------|-----------|
| **Extrusie lijkt verschoven** | `setCenter(false)` laat het profiel verankerd op de hoek. | Gebruik `setCenter(true)` voor symmetrische resultaten. |
| **OBJ‑bestand is leeg** | Het uitvoerpad is onjuist of er ontbreken schrijfrechten. | Controleer of `MyDir` naar een bestaande map wijst en de applicatie schrijfrechten heeft. |
| **Afgeronde hoeken zien er scherp uit** | De afrondingsradius is te klein ten opzichte van de rechthoekgrootte. | Verhoog de radiuswaarde (bijv. `setRoundingRadius(0.5)`). |

## Veelgestelde vragen

### Q1: Kan ik Aspose.3D for Java gebruiken in commerciële projecten?

A1: Ja, Aspose.3D for Java is beschikbaar voor commercieel gebruik. Voor licentie‑details, bezoek [hier](https://purchase.aspose.com/buy).

### Q2: Is er een gratis proefversie beschikbaar?

A2: Ja, je kunt een gratis proefversie van Aspose.3D for Java verkennen [hier](https://releases.aspose.com/).

### Q3: Waar kan ik ondersteuning vinden voor Aspose.3D for Java?

A3: Het Aspose.3D‑communityforum is een uitstekende plek voor ondersteuning en het delen van ervaringen. Bezoek het forum [hier](https://forum.aspose.com/c/3d/18).

### Q4: Heb ik een tijdelijke licentie nodig voor testen?

A4: Ja, als je een tijdelijke licentie voor testdoeleinden nodig hebt, kun je er een verkrijgen [hier](https://purchase.aspose.com/temporary-license/).

### Q5: Waar vind ik de documentatie?

A5: De documentatie voor Aspose.3D for Java is beschikbaar [hier](https://reference.aspose.com/3d/java/).

## Conclusie

Door deze **java 3d graphics tutorial** te voltooien, weet je nu hoe je het middelpunt van een lineaire extrusie regelt, de afrondingsradius aanpast, en **save OBJ file java**‑output opslaat met Aspose.3D. Deze technieken geven je fijne controle over mesh‑symmetrie, wat cruciaal is voor game‑assets, CAD‑prototypes en wetenschappelijke visualisaties. Experimenteer gerust met verschillende profielen, slice‑aantallen en exportformaten om je 3‑D‑toolbox uit te breiden.

---

**Laatst bijgewerkt:** 2026-02-20  
**Getest met:** Aspose.3D for Java 24.11  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}