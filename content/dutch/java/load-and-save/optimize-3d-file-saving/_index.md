---
title: Optimaliseer het opslaan van 3D-bestanden in Java met Aspose.3D SaveOptions
linktitle: Optimaliseer het opslaan van 3D-bestanden in Java met Aspose.3D SaveOptions
second_title: Aspose.3D Java-API
description: Leer hoe u het opslaan van 3D-bestanden in Java kunt optimaliseren met Aspose.3D SaveOptions. Verbeter de prestaties en pas de uitvoer moeiteloos aan.
type: docs
weight: 16
url: /nl/java/load-and-save/optimize-3d-file-saving/
---
## Invoering

Aspose.3D is een Java-bibliotheek boordevol functies waarmee ontwikkelaars naadloos met 3D-modellen kunnen werken. Als het gaat om het opslaan van 3D-bestanden, biedt de klasse SaveOptions een overvloed aan instellingen om de uitvoer te verfijnen volgens uw vereisten. In deze zelfstudie onderzoeken we verschillende opslagopties en hoe deze kunnen worden gebruikt om het proces te optimaliseren.

## Vereisten

Voordat we ingaan op de tutorial, zorg ervoor dat je aan de volgende vereisten voldoet:

-  Aspose.3D voor Java: Zorg ervoor dat de Aspose.3D-bibliotheek in uw Java-project is geïntegreerd. Je kunt het downloaden[hier](https://releases.aspose.com/3d/java/).

- Java-ontwikkelomgeving: Zorg ervoor dat er een functionele Java-ontwikkelomgeving op uw machine is geïnstalleerd.

- Documentmap: maak een map waarin u uw 3D-bestanden wilt opslaan en noteer het pad voor later gebruik.

## Pakketten importeren

 Importeer in uw Java-project de benodigde pakketten om met Aspose.3D te werken. Dit omvat de`Scene` klasse en verschillende SaveOptions-klassen. Hieronder vindt u een eenvoudig voorbeeld:

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

Laten we nu elk voorbeeld in meerdere stappen opsplitsen om het gebruik van verschillende SaveOptions te demonstreren.

## Stap 1: Mooie afdruk in GLTF SaveOption

 De`prettyPrintInGltfSaveOption` Met de methode kunt u een GLTF-bestand genereren met ingesprongen JSON-inhoud voor menselijke leesbaarheid.

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // Initialiseer de 3D-scène
    Scene scene = new Scene(new Sphere());
    
    // Initialiseer GLTFSaveOptions
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // Schakel mooie afdrukken in voor een betere leesbaarheid
    opt.setPrettyPrint(true);
    
    // 3D-scène opslaan
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## Stap 2: HTML5 SaveOption

 De`html5SaveOption` methode laat zien hoe u een 3D-scène opslaat als een HTML5-bestand, inclusief aanpassingsopties.

```java
public static void html5SaveOption() throws IOException {
    // Initialiseer een scène
    Scene scene = new Scene();
    
    // Maak een onderliggend knooppunt met een cilinder
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //Stel eigenschappen in voor het onderliggende knooppunt
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // Voeg een licht toe aan de scène
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // Initialiseer HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // Opties aanpassen (bijvoorbeeld het raster en de gebruikersinterface uitschakelen)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // Sla de scène op als een HTML5-bestand
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

 Ga verder met soortgelijke uitsplitsingen voor andere SaveOptions-methoden, zoals`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` , En`drcSaveOptions`.

## Conclusie

Door deze uitgebreide tutorial te volgen, hebt u geleerd hoe u het opslaan van 3D-bestanden in Java kunt optimaliseren met behulp van Aspose.3D SaveOptions. Of u nu geïnteresseerd bent in het mooi afdrukken van GLTF-bestanden of het aanpassen van HTML5-uitvoer, Aspose.3D voorziet u van de tools om uw 3D grafische workflow te verbeteren.

## Veelgestelde vragen

### Vraag 1: Hoe kan ik assets insluiten in een glTF-bestand?

 A1: Om assets in te sluiten, gebruikt u de`setEmbedAssets(true)` methode in de`GltfSaveOptions` klas.

###  Vraag 2: Wat is het doel van de`setPositionBits` method in `DracoSaveOptions`?

 A2: De`setPositionBits` -methode stelt de kwantiseringsbits in voor de positie in het Draco-compressie-algoritme.

### Vraag 3: Kan ik normale gegevens in een U3D-bestand exporteren?

 A3: Ja, u kunt normale gegevens exporteren door in te stellen`setExportNormals(true)` in de`U3dSaveOptions` klas.

### V4: Hoe verwijder ik opgeslagen materiaalbestanden in een OBJ-export?

A4: Gebruik de`setFileSystem(new DummyFileSystem())` methode in de`ObjSaveOptions` klasse om materiële bestanden te verwijderen.

### Vraag 5: Is er een manier om afhankelijkheden op te slaan in een lokale map in een OBJ-bestand?

 A5: Ja, gebruik de`setFileSystem(new LocalFileSystem(MyDir))` methode in de`ObjSaveOptions` klasse om afhankelijkheden lokaal op te slaan.