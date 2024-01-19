---
title: Knooppunthiërarchie in 3D-scènes begrijpen
linktitle: Knooppunthiërarchie in 3D-scènes begrijpen
second_title: Aspose.3D .NET-API
description: Ontgrendel de kracht van Aspose.3D voor .NET! Duik in de manipulatie van knooppunthiërarchieën met deze stapsgewijze handleiding. Creëer moeiteloos verbluffende 3D-scènes.
type: docs
weight: 16
url: /nl/net/geometry-and-hierarchy/node-hierarchy/
---
## Invoering

Welkom in de wereld van Aspose.3D voor .NET, een krachtige bibliotheek waarmee ontwikkelaars naadloos kunnen werken met 3D-scènes en -modellen in hun .NET-toepassingen. In deze tutorial zullen we dieper ingaan op de fijne kneepjes van het begrijpen van de knooppunthiërarchie in 3D-scènes met behulp van Aspose.3D. Aan het einde van deze handleiding zult u goed begrijpen hoe u de structuur van 3D-scènes via knooppunten kunt manipuleren, waardoor u verbluffende visuele ervaringen kunt creëren.

## Vereisten

Voordat we aan deze 3D-reis beginnen, moet u ervoor zorgen dat u aan de volgende vereisten voldoet:

-  Aspose.3D voor .NET-bibliotheek: Zorg ervoor dat de Aspose.3D-bibliotheek in uw .NET-project is geïntegreerd. Als je dit nog niet hebt gedaan, ga dan naar de[documentatie](https://reference.aspose.com/3d/net/) voor begeleiding.

-  Download de bibliotheek: Als u de Aspose.3D-bibliotheek niet hebt gedownload, download dan de nieuwste versie van de[download link](https://releases.aspose.com/3d/net/)en volg de installatie-instructies in de documentatie.

-  Verkrijg een licentie: om het volledige potentieel van Aspose.3D te benutten, hebt u een geldige licentie nodig. Als u er geen heeft, kunt u deze verkrijgen[hier](https://purchase.aspose.com/buy) of kies voor een[gratis proefperiode](https://releases.aspose.com/) om zijn mogelijkheden te verkennen.

-  Ondersteuning en gemeenschap: Sluit u aan bij de Aspose.3D-gemeenschap op de[Helpforum](https://forum.aspose.com/c/3d/18)om in contact te komen met andere ontwikkelaars, hulp te zoeken en op de hoogte te blijven van de nieuwste ontwikkelingen.

-  Tijdelijke licentie (optioneel): Als u Aspose.3D verkent voordat u een aankoop doet, overweeg dan om een[tijdelijke licentie](https://purchase.aspose.com/temporary-license/) voor uitgebreide toegang.

Nu we onze tools gereed hebben, gaan we duiken in de opwindende wereld van manipulatie van de 3D-knoophiërarchie met behulp van Aspose.3D.

## Naamruimten importeren

Zorg ervoor dat u in uw .NET-project de benodigde naamruimten importeert om gebruik te kunnen maken van de functionaliteit van Aspose.3D. Voeg de volgende regels toe aan uw code:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Deze naamruimten geven u toegang tot essentiële klassen en methoden voor het werken met 3D-scènes.

## Stap 1: Initialiseer het scèneobject

```csharp
Scene scene = new Scene();
```

 Begin met het maken van een nieuwe 3D-scène met behulp van de`Scene` klas.

## Stap 2: Maak onderliggende knooppunten

```csharp
Node top = scene.RootNode.CreateChildNode();
Node cube1 = top.CreateChildNode("cube1");
Node cube2 = top.CreateChildNode("cube2");
```

 Breng een hiërarchische structuur tot stand door ouder-kindrelaties tussen knooppunten te creëren. In dit voorbeeld`cube1` En`cube2` zijn onderliggende knooppunten van de`top` knooppunt.

## Stap 3: Mesh maken en toewijzen

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
cube1.Entity = mesh;
cube2.Entity = mesh;
```

 Genereer een mesh met behulp van een geschikte methode (hier,`CreateMeshUsingPolygonBuilder`) en wijs het toe aan de onderliggende knooppunten.

## Stap 4: Stel vertalingen in

```csharp
cube1.Transform.Translation = new Vector3(-10, 0, 0);
cube2.Transform.Translation = new Vector3(10, 0, 0);
```

Definieer vertalingen voor elk kubusknooppunt en positioneer ze in de 3D-ruimte.

## Stap 5: Pas rotatie toe op het bovenliggende knooppunt

```csharp
top.Transform.Rotation = Quaternion.FromEulerAngle(Math.PI, 4, 0);
```

Roteer het bovenliggende knooppunt (`top`), en kijk hoe deze transformatie alle onderliggende knooppunten beïnvloedt.

## Stap 6: Sla de 3D-scène op

```csharp
string output = "Your Output Directory" + "NodeHierarchy.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Geef de uitvoermap op en sla de 3D-scène op in het gewenste bestandsformaat (hier FBX7500ASCII).

## Stap 7: Succesbericht weergeven

```csharp
Console.WriteLine("\nNode hierarchy added successfully to document.\nFile saved at " + output);
```

Informeer de gebruiker over de succesvolle toevoeging van de knooppunthiërarchie en de opgeslagen bestandslocatie.

## Conclusie

Gefeliciteerd! U heeft met succes door de ingewikkelde wereld van de 3D-knooppunthiërarchie in Aspose.3D voor .NET genavigeerd. Met deze tutorial beschikt u over de kennis om eenvoudig 3D-scènes te maken, manipuleren en op te slaan. Terwijl u uw reis voortzet, ontdekt u meer functies en ontketent u het volledige potentieel van Aspose.3D in uw .NET-projecten.

## Veelgestelde vragen

### V1: Kan ik Aspose.3D voor .NET gebruiken zonder licentie?

A1: Hoewel een licentie alle functies ontgrendelt, kunt u Aspose.3D met beperkte mogelijkheden verkennen met behulp van de gratis proefperiode.

### Vraag 2: Zijn er andere ondersteunde bestandsformaten voor het opslaan van 3D-scènes?

A2: Ja, Aspose.3D ondersteunt verschillende formaten; Raadpleeg de documentatie voor een uitgebreide lijst.

### Vraag 3: Hoe kan ik bijdragen aan de Aspose.3D-gemeenschap?

A3: Sluit u aan bij het ondersteuningsforum, deel uw ervaringen en draag bij door anderen te helpen met hun vragen.

### Vraag 4: Is Aspose.3D geschikt voor game-ontwikkeling?

A4: Absoluut! Aspose.3D is veelzijdig en kan worden geïntegreerd in game-ontwikkelingsprojecten.

### V5: Wat is het verschil tussen een tijdelijke licentie en een volledige licentie?

A5: Een tijdelijke licentie biedt toegang op korte termijn voor evaluatiedoeleinden, terwijl een volledige licentie onbeperkt gebruik biedt.