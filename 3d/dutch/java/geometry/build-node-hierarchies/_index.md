---
date: 2026-04-12
description: Leer hoe u kindknooppunten maakt, een mesh aan een knooppunt toevoegt
  en FBX exporteert met de Aspose.3D Java API voor robuuste 3D‑scènegraphen.
keywords:
- create child nodes
- how to export fbx
- add mesh to node
- java 3d scene graph
- save scene fbx
linktitle: Bouw knooppunthiërarchieën in 3D‑scènes met Java en Aspose.3D
second_title: Aspose.3D Java API
title: Maak onderliggende knooppunten en exporteer FBX in Java met Aspose.3D
url: /nl/java/geometry/build-node-hierarchies/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}  
{{< blocks/products/pf/main-container >}}  
{{< blocks/products/pf/tutorial-page-section >}}  

# Hoe FBX te exporteren en knooppunt‑hiërarchieën te bouwen in Java met Aspose.3D  

## Introductie  

Als je op zoek bent naar een duidelijke, stapsgewijze handleiding over **create child nodes**, **add mesh to node** en **how to export FBX** vanuit een Java‑applicatie, dan ben je hier aan het juiste adres. In deze tutorial lopen we stap voor stap door het bouwen van een **java 3d scene graph**, het koppelen van meshes, het toepassen van transformaties, en uiteindelijk het opslaan van de scène als een FBX‑bestand met behulp van de Aspose.3D Java‑API. Of je nu een eenvoudige demo prototype of een productie‑klaar 3D‑engine ontwikkelt, het beheersen van deze concepten geeft je volledige controle over je scène‑hiërarchie en export‑workflow.  

## Snelle antwoorden  
- **Wat is het primaire doel van deze tutorial?** Demonstreren hoe **create child nodes**, meshes toe te voegen en **export FBX** uit te voeren na het bouwen van een knooppunt‑hiërarchie.  
- **Welke bibliotheek wordt gebruikt?** Aspose.3D for Java.  
- **Heb ik een licentie nodig?** Een gratis proefversie werkt voor ontwikkeling; een commerciële licentie is vereist voor productie.  
- **Welk bestandsformaat wordt geproduceerd?** FBX (ASCII 7500).  
- **Kan ik knooppunt‑transformaties aanpassen?** Ja – translatie, rotatie en schaalvergroting worden allemaal ondersteund.  

## Wat betekent “create child nodes” in de context van Aspose.3D?  

Het creëren van child nodes betekent het toevoegen van ondergeschikte `Node`‑objecten aan een ouder‑node in de scène‑graph. Deze hiërarchische structuur stelt je in staat om een transformatie één keer op het ouder‑niveau toe te passen en deze automatisch op alle kinderen te laten gelden, wat essentieel is voor realistische objectrelaties zoals een autokarrosserie met roterende wielen.  

## Waarom knooppunt‑hiërarchieën bouwen vóór het exporteren?  

Een goed gestructureerde hiërarchie vermindert code‑duplicatie, vereenvoudigt animatie en weerspiegelt relaties uit de echte wereld. Wanneer je later **convert scene fbx** (of een ander formaat) uitvoert, blijft de hiërarchie behouden, zodat downstream‑tools zoals Blender, Maya of Unity de ouder‑kindrelaties precies begrijpen zoals jij ze hebt ontworpen.  

## Veelvoorkomende gebruikssituaties voor knooppunt‑hiërarchieën  

| Gebruikssituatie | Waarom een hiërarchie helpt | Typisch resultaat |
|------------------|-----------------------------|-------------------|
| **Mechanische assemblages** (bijv. robotarm) | Het roteren van een basis‑node verplaatst alle gekoppelde segmenten | Eenvoudige animatie van complexe mechanismen |
| **Karakter‑rigs** | Skeletbotten zijn child nodes van een root | Consistente pose‑transformaties |
| **Scène‑organisatie** | Groeperen van statische props onder een “props”‑node | Nettere scène‑beheer en selectieve export |
| **Level‑of‑detail (LOD) schakeling** | Parent‑node schakelt de zichtbaarheid van child meshes | Geoptimaliseerde weergave voor verschillende hardware |

## Vereisten  

1. **Java Development Environment** – JDK 8+ en een IDE of build‑tool naar keuze.  
2. **Aspose.3D for Java Library** – Download en installeer de bibliotheek van de [download page](https://releases.aspose.com/3d/java/).  
3. **Document Directory** – Een map op je computer waar het gegenereerde FBX‑bestand wordt opgeslagen.  

## Pakketten importeren  

Begin met het importeren van de benodigde Aspose.3D‑klassen:  

```java
import com.aspose.threed.*;
```  

## Stap 1: Het Scene‑object initialiseren  

```java
// Initialize scene object
Scene scene = new Scene();
```  

## Stap 2: Child‑nodes maken en mesh aan node toevoegen  

In deze stap demonstreren we **how to create child nodes** en **add mesh to node** objecten.  

```java
// Get a child node object
Node top = scene.getRootNode().createChildNode();

// Create the first cube node
Node cube1 = top.createChildNode("cube1");
Mesh mesh = Common.createMeshUsingPolygonBuilder(); // Use your mesh creation method
cube1.setEntity(mesh);
cube1.getTransform().setTranslation(new Vector3(-10, 0, 0));

// Create the second cube node
Node cube2 = top.createChildNode("cube2");
cube2.setEntity(mesh);
cube2.getTransform().setTranslation(new Vector3(10, 0, 0));
```  

## Stap 3: Rotatie toepassen op de bovenste node  

Het roteren van de ouder‑node roteert automatisch al zijn kinderen, wat een kernvoordeel is van hiërarchische scènes.  

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```  

## Stap 4: De 3D‑scene opslaan – Hoe FBX te exporteren  

Nu **save scene as FBX**, waarmee de “how to export fbx” workflow voltooid is.  

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```  

### Verwacht resultaat  

Het uitvoeren van de code maakt een bestand genaamd **NodeHierarchy.fbx** aan in de opgegeven map. Open het in een willekeurige FBX‑compatibele viewer om twee kubussen te zien die links en rechts van een centraal draaipunt zijn geplaatst, en samen roteren.  

## Veelvoorkomende problemen en oplossingen  

| Probleem | Waarom het gebeurt | Oplossing |
|----------|--------------------|-----------|
| **File not found** fout bij het opslaan | `MyDir` pad is onjuist of mist een afsluitende scheidingsteken | Zorg ervoor dat de map bestaat en eindigt met een bestandsscheidingsteken (`/` of `\\`). |
| **Mesh not visible** na export | Mesh‑entity niet toegewezen of translatie verplaatst het buiten het zicht | Controleer `cube1.setEntity(mesh)` en controleer de translatie‑waarden. |
| **Rotatie ziet er verkeerd uit** | Onjuiste toepassing van radialen versus graden | `Quaternion.fromEulerAngle` verwacht radialen; pas de waarden dienovereenkomstig aan. |

## Tips voor probleemoplossing  

- **Validate the directory**: Gebruik `new File(MyDir).mkdirs();` vóór `scene.save` als de map mogelijk niet bestaat.  
- **Inspect the scene graph**: Roep `scene.getRootNode().getChildren().size()` aan om te bevestigen dat child nodes zijn toegevoegd.  
- **Check FBX version compatibility**: Sommige oudere tools ondersteunen alleen FBX 2013; je kunt het formaat wijzigen naar `FileFormat.FBX2013` indien nodig.  

## Veelgestelde vragen  

**Q: Is Aspose.3D for Java geschikt voor beginners?**  
A: Absoluut! De API is ontworpen met een schone, object‑georiënteerde aanpak die het gemakkelijk maakt om te leren, zelfs als je nieuw bent in 3D‑programmeren.  

**Q: Kan ik Aspose.3D for Java gebruiken voor commerciële projecten?**  
A: Ja, dat kan. Bezoek de [purchase page](https://purchase.aspose.com/buy) voor licentie‑details.  

**Q: Hoe kan ik ondersteuning krijgen voor Aspose.3D for Java?**  
A: Word lid van het [Aspose.3D forum](https://forum.aspose.com/c/3d/18) om hulp te krijgen van de community en het Aspose‑ondersteuningsteam.  

**Q: Is er een gratis proefversie beschikbaar?**  
A: Zeker! Verken de functies met de [free trial](https://releases.aspose.com/) voordat je een beslissing neemt.  

**Q: Waar kan ik de documentatie vinden?**  
A: Raadpleeg de [documentation](https://reference.aspose.com/3d/java/) voor gedetailleerde informatie over Aspose.3D for Java.  

## Conclusie  

Het beheersen van **create child nodes**, **add mesh to node** en **how to export FBX** zijn essentiële stappen om geavanceerde 3D‑applicaties in Java te bouwen. Met Aspose.3D krijg je een krachtige, licentie‑vriendelijke oplossing die low‑level details abstraheert terwijl je volledige controle over de scène‑graph behoudt. Experimenteer met verschillende meshes, transformaties en exportformaten om nog meer mogelijkheden te ontgrendelen.  

---  

**Laatst bijgewerkt:** 2026-04-12  
**Getest met:** Aspose.3D for Java 24.11  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}  

{{< /blocks/products/pf/main-container >}}  
{{< /blocks/products/pf/main-wrap-class >}}  

{{< blocks/products/products-backtop-button >}}