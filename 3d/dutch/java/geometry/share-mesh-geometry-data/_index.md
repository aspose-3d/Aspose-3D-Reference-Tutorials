---
date: 2025-12-12
description: Leer hoe je de materiaalkleur instelt terwijl je mesh‑geometriegegevens
  deelt en de scène opslaat als FBX in Java 3D met Aspose.3D.
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: Stel materiaalkleur in en deel mesh‑geometriegegevens in Java 3D met Aspose.3D
url: /nl/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Materiaalkleur instellen en mesh‑geometriegegevens delen in Java 3D met Aspose.3D

## Introductie

Een reis beginnen in de wereld van Java 3D met Aspose.3D opent een scala aan mogelijkheden voor het creëren van verbluffende visualisaties en meeslepende ervaringen. In deze tutorial laten we je zien **hoe je mesh‑geometrie** kunt delen in Java 3D met Aspose.3D, en we laten je precies zien **hoe je materiaalkleur** instelt voor elke mesh‑instantie. Volg elke stap zorgvuldig, en aan het einde kun je mesh‑gegevens naadloos uitwisselen tussen meerdere nodes, kleuren beheren en exporteren naar FBX.

## Snelle antwoorden
- **Wat is het hoofddoel?** Materiaalkleur instellen voor elke node en mesh‑geometriegegevens delen.  
- **Welke bibliotheek is vereist?** Aspose.3D voor Java.  
- **Hoe exporteer ik het resultaat?** Sla de scène op als een FBX‑bestand (FBX7400ASCII).  
- **Heb ik een licentie nodig?** Een tijdelijke of volledige licentie is vereist voor productiegebruik.  
- **Welke Java‑versie werkt?** Elke Java 8+ omgeving.

## Vereisten

Voordat we aan de tutorial beginnen, zorg ervoor dat je de volgende zaken gereed hebt:

- Java‑ontwikkelomgeving: Zorg dat je een Java‑ontwikkelomgeving op je systeem hebt geïnstalleerd.  
- Aspose.3D‑bibliotheek: Download en installeer de Aspose.3D‑bibliotheek. Je kunt de bibliotheek vinden **[hier](https://releases.aspose.com/3d/java/)**.

## Pakketten importeren

Begin met het importeren van de benodigde pakketten in je Java‑project. Deze stap is cruciaal om toegang te krijgen tot de functionaliteiten die de Aspose.3D‑bibliotheek biedt.

```java
import com.aspose.threed.*;
```

## Stap 1: Scene‑object initialiseren (initialize scene java)

Laten we het proces starten door een scene‑object te initialiseren. Dit dient als het canvas waarop onze 3D‑magie zich zal ontv.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Stap 2 Kleurvectoren definiëren

In deze stap definiëren we een array van kleurvectoren die op verschillende elementen van onze 3D‑scene worden toegepast.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Stap 3: 3D‑mesh maken in Java met Polygon Builder (create 3d mesh java)

Gebruik de Common‑klasse om een mesh te maken met de polygon‑builder‑methode. Deze mesh vormt de basis voor onze 3D‑elementen.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Hoe materiaalkleur instellen voor elke node?

Itereer door de kleurvectoren, maak kubus‑nodes aan en stel attributen in zoals materiaal, **materiaalkleur instellen**, en translatie. Dit is de kern van het regelen van het visuele uiterlijk van elke mesh‑instantie.

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## Stap 5: 3D‑scene opslaan (save scene fbx, convert mesh to fbx)

Geef de map en bestandsnaam op voor het opslaan van de 3D‑scene in het ondersteunde bestandsformaat, in dit geval FBX7400ASCII. Deze stap toont ook **mesh naar FBX converteren**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Conclusie

Gefeliciteerd! Je hebt met succes **materiaalkleur ingesteld**, mesh‑geometriegegevens gedeeld tussen meerdere nodes, en het resultaat geëxporteerd als een FBX‑bestand met Aspose.3D voor Java. Dit opent eindeloze mogelijkheden voor het creëren van visueel verbluffende en interactieve 3D‑applicaties.

## Veelgestelde vragen

### Q1: Kan ik Aspose.3D gebruiken met andere Java‑frameworks?

A1: Ja, Aspose.3D is ontworpen om naadloos te werken met diverse Java‑frameworks.

### Q2: Zijn er licentie‑opties beschikbaar voor Aspose.3D?

A2: Ja, je kunt licentie‑opties verkennen **[hier](https://purchase.aspose.com/buy)**.

### Q3: Hoe krijg ik ondersteuning voor Aspose.3D?

A3: Bezoek het Aspose.3D **[forum](https://forum.aspose.com/c/3d/18)** voor ondersteuning en discussies.

### Q4: Is er een gratis proefversie beschikbaar?

A4: Ja, je kunt een gratis proefversie krijgen **[hier](https://releases.aspose.com/)**.

### Q5: Hoe verkrijg ik een tijdelijke licentie voor Aspose.3D?

A5: Je kunt een tijdelijke licentie krijgen **[hier](https://purchase.aspose.com/temporary-license/)**.

## Extra veelgestelde vragen

**V: Kan ik de scène exporteren naar andere formaten dan FBX?**  
A: Ja, Aspose.3D ondersteunt OBJ, STL, 3MF en meer. Pas gewoon de `FileFormat`‑enum aan in de `save`‑aanroep.

**V: Wat als ik het materiaal moet wijzigen nadat de scène is aangemaakt?**  
A: Haal de node op, wijzig zijn `LambertMaterial` (bijv. `setDiffuseColor`), en sla de scène opnieuw op.

**V: Handelt de bibliotheek grote meshes efficiënt af?**  
A: Aspose.3D gebruikt geoptimaliseerde datastructuren; bij extreem grote meshes kun je overwegen te streamen of de scène op te splitsen.

**V: Is er een manier om de kleurverandering te animeren?**  
A: Ja, je kunt materiaaleigenschappen animeren met de `AnimationController`‑API.

---

**Laatst bijgewerkt:** 2025-12-12  
**Getest met:** Aspose.3D 24.11 voor Java  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}