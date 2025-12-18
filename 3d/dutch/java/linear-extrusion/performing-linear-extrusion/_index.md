---
date: 2025-12-18
description: Leer hoe je een vorm extrudeert in Java met Aspose.3D, maak een 3D‑scène
  en exporteer moeiteloos Wavefront OBJ‑bestanden.
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: Hoe een vorm extruderen in Java met Aspose.3D lineaire extrusie
url: /nl/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Uitvoeren van lineaire extrusie in Aspose.3D voor Java

## Introductie

Welkom bij deze uitgebreide tutorial over **how to extrude shape** in Aspose.3D voor Java! Als je je 3D-modelleringsvaardigheden met Java wilt verbeteren, ben je hier op de juiste plek. We leiden je door het maken van een 3D‑scene, het uitvoeren van lineaire extrusie en het exporteren van het resultaat als een Wavefront OBJ‑bestand — allemaal met duidelijke, stap‑voor‑stap code‑voorbeelden.

## Snelle antwoorden
- **Wat is lineaire extrusie?** Een 2D‑profiel langs een rechte pad uitbreiden om een 3D‑solid te creëren.  
- **Welke bibliotheek behandelt dit in Java?** Aspose.3D voor Java.  
- **Kan ik exporteren naar OBJ?** Ja, met de Wavefront OBJ‑exportfunctie.  
- **Heb ik een licentie nodig voor ontwikkeling?** Een gratis proefversie werkt voor testen; een licentie is vereist voor productie.  
- **Welke Java‑versie is vereist?** Java 1.6 of hoger.

## Wat is “how to extrude shape”?
Lineaire extrusie is een fundamentele techniek in **3d modeling java** die een plat profiel — zoals een rechthoek — omzet in een volumineus object door het over een gedefinieerde afstand te trekken. Deze methode wordt veel gebruikt voor het maken van mechanische onderdelen, architecturale elementen en decoratieve modellen.

## Waarom Aspose.3D gebruiken voor lineaire extrusie?
- **Volledige controle** over geometrie (slices, twist, offset).  
- **Naadloze integratie** met Java‑projecten — geen native afhankelijkheden.  
- **Ingebouwde exporters** voor populaire formaten, inclusief Wavefront OBJ, waardoor het eenvoudig is om **generate 3d model**‑bestanden te maken voor downstream‑pijplijnen.

## Voorvereisten

Voordat je aan de tutorial begint, zorg ervoor dat je de volgende voorvereisten hebt:

1. **Java Development Environment** – een JDK (1.6 of nieuwer) en je favoriete IDE.  
2. **Aspose.3D Library** – download en installeer de bibliotheek vanaf de officiële site **[here](https://releases.aspose.com/3d/java/)**.

## Importeer pakketten

Zodra je je ontwikkelomgeving hebt opgezet en de Aspose.3D‑bibliotheek hebt geïnstalleerd, importeer je het benodigde pakket:

```java
import com.aspose.threed.*;
```

### Stap 1: Stel documentmap in

Definieer de map waarin de gegenereerde bestanden worden opgeslagen:

```java
String MyDir = "Your Document Directory";
```

> Dit zorgt ervoor dat de **generate 3d model**‑operatie het OBJ‑bestand naar een bekende locatie schrijft.

### Stap 2: Initialiseert basisvorm

Maak een rechthoek die dient als het extrusie‑profiel:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Je kunt de afrondingsradius aanpassen om afgeronde hoeken te krijgen of deze op `0` zetten voor een perfecte rechthoek.

### Stap 3: Voer lineaire extrusie uit

Nu extruderen we de rechthoek langs de Z‑as, voegen slices toe, schakelen centrering in en passen een draai met een offset toe:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Extrusielengte** – `10` eenheden.  
- **Slices** – `100` voor gladde geometrie.  
- **Twist** – `360°` creëert een volledige rotatie.  
- **Twist offset** – verplaatst de draai‑origin naar `(10, 0, 0)`.

### Stap 4: Maak 3D‑scene

Maak een scene‑container en voeg de extrusie toe als een kind‑node. Deze stap **creates 3d scene** die meerdere objecten kan bevatten:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### Stap 5: Sla 3D‑scene op

Exporteer de scene naar een Wavefront OBJ‑bestand. Dit demonstreert de mogelijkheden van **wavefront obj export** en **save 3d obj**:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Na het uitvoeren van de code vind je `LinearExtrusion.obj` in de map die je hebt opgegeven, klaar om geopend te worden in elke 3D‑viewer of verder verwerkt te worden.

## Veelvoorkomende problemen en oplossingen

| Probleem | Reden | Oplossing |
|----------|-------|-----------|
| OBJ‑bestand is leeg | Pad van de uitvoermap is onjuist of niet beschrijfbaar | Controleer of `MyDir` naar een bestaande map met schrijfrechten wijst. |
| Twist niet toegepast | `setCenter(true)` weggelaten | Zorg ervoor dat centrering is ingeschakeld of pas de waarden van `setTwistOffset` aan. |
| Compilatiefout op `LinearExtrusion` | Gebruik van een oudere Aspose.3D‑versie | Update naar de nieuwste Aspose.3D‑release. |

## Veelgestelde vragen

**Q: Is Aspose.3D compatibel met alle Java‑versies?**  
A: Aspose.3D werkt met Java 1.6 en hoger.

**Q: Kan ik Aspose.3D gebruiken voor commerciële projecten?**  
A: Ja, commercieel gebruik is toegestaan met een geldige licentie. Je kunt er een verkrijgen **[here](https://purchase.aspose.com/buy)**.

**Q: Waar kan ik ondersteuning krijgen als ik problemen ondervind?**  
A: Bezoek het **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** voor community‑hulp of koop een **[temporary license](https://purchase.aspose.com/temporary-license/)** voor premium‑ondersteuning.

**Q: Welke andere 3D‑modelleermogelijkheden biedt Aspose.3D?**  
A: De bibliotheek bevat mesh‑manipulatie, Boolean‑operaties, texture‑mapping en meer. Zie de volledige lijst **[here](https://reference.aspose.com/3d/java/)**.

**Q: Is er een gratis proefversie beschikbaar?**  
A: Ja, je kunt een proefversie downloaden **[here](https://releases.aspose.com/)**.

## Conclusie

Je hebt nu geleerd **how to extrude shape** te gebruiken met Aspose.3D voor Java, een 3D‑scene gemaakt en het resultaat geëxporteerd als een Wavefront OBJ‑bestand. Deze techniek opent de deur naar een breed scala aan **3d modeling java**‑projecten — van eenvoudige onderdelen tot complexe assemblages. Verken extra functies zoals Boolean‑operaties of texture‑mapping om je modellen verder te verrijken.

---

**Laatst bijgewerkt:** 2025-12-18  
**Getest met:** Aspose.3D 24.11 for Java  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## DOELKEYWORDS:

**Primaire zoekterm (HOOGSTE PRIORITEIT):**
how to extrude shape

**Secundaire zoektermen (ONDERSTEUNEND):**
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj