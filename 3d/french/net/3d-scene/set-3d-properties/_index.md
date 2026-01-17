---
date: 2026-01-17
description: Apprenez à répertorier les propriétés des matériaux, à modifier la couleur
  diffuse et à ajuster les attributs des matériaux 3D à l'aide d'Aspose.3D pour .NET.
  Des exemples de code étape par étape sont inclus.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Lister les propriétés des matériaux dans les scènes 3D avec Aspose.3D
url: /fr/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Lister les propriétés des matériaux dans les scènes 3D avec Aspose.3D

## Introduction

Si vous devez **lister les propriétés des matériaux** d’un modèle 3D puis ajuster des éléments comme la couleur diffuse, vous êtes au bon endroit. Aspose.3D for .NET vous offre une API propre, orientée objet, qui vous permet d’inspecter, de récupérer et de modifier les attributs des matériaux sans quitter votre code C#. Dans ce tutoriel, nous parcourrons le chargement d’une scène, l’énumération de ses propriétés de matériau, et la modification de valeurs telles que le composant diffuse — pour que vous puissiez donner à vos modèles l’aspect exact que vous désirez.

## Réponses rapides
- **Quel est l'objectif principal ?** Lister les propriétés des matériaux et les modifier (p. ex. couleur diffuse).  
- **Quelle bibliothèque est requise ?** Aspose.3D for .NET.  
- **Ai-je besoin d'une licence ?** Une licence temporaire ou complète est requise pour une utilisation en production.  
- **Formats de fichiers pris en charge ?** FBX, OBJ, STL, STL‑ASCII, 3MF, et plus.  
- **Temps d'implémentation typique ?** Environ 10‑15 minutes pour un script de base listant les propriétés.

## Qu'est-ce que **list material properties** ?
Lister les propriétés des matériaux signifie parcourir le `PropertyCollection` d’un matériau pour lire chaque nom de propriété et sa valeur actuelle. Cela est utile pour le débogage, l’inspection visuelle ou la création de contrôles UI permettant aux utilisateurs d’ajuster les paramètres du matériau à l’exécution.

## Pourquoi utiliser Aspose.3D pour **access material properties** ?
- **Pas de convertisseurs externes** – travaillez directement avec les objets .NET natifs.  
- **Modèle de propriétés riche** – prend en charge les attributs spécifiques FBX en plus des valeurs PBR standard.  
- **Cross‑platform** – fonctionne sur .NET Framework, .NET Core et .NET 5/6+.  

## Prérequis

- Aspose.3D for .NET installé dans votre projet. Téléchargez-le [here](https://releases.aspose.com/3d/net/).
- Un dossier sur le disque pour contenir vos fichiers source 3‑D (p. ex. un fichier FBX avec textures intégrées).

Maintenant que les bases sont en place, plongeons dans le code.

## Importer les espaces de noms

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Étape 1 : Charger la scène 3D

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Étape 2 : **Access material properties** du premier nœud

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Étape 3 : **List material properties** – voir chaque paire nom/valeur

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## Étape 4 : **How to change diffuse** – modifier la propriété Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Étape 5 : **Retrieve property by name** – obtenir une instance fortement typée

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Étape 6 : Parcourir les propriétés d'une propriété (avancé)

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## Comment **change 3d material color** au‑delà du diffuse
Si vous devez affecter les couleurs spéculaire, ambiante ou émissive, remplacez simplement `"Diffuse"` par `"Specular"` ou `"Ambient"` dans l’affectation `props["..."]` ci‑dessus. Les mêmes structures `Vector3` ou `Vector4` s’appliquent.

## Pièges courants & conseils
- **Sensibilité à la casse du nom de propriété** – les clés de propriétés Aspose.3D sont sensibles à la casse ; utilisez le nom exact affiché dans la sortie de la liste.  
- **Propriété manquante** – Tous les matériaux n'exposent pas chaque attribut PBR. Vérifiez `props.ContainsKey("Specular")` avant d'accéder.  
- **Enregistrement des modifications** – Après avoir modifié les propriétés, appelez `scene.Save("output.fbx");` pour persister les changements.

## Conclusion

Vous avez maintenant appris comment **lister les propriétés des matériaux**, **récupérer une propriété par son nom**, et **modifier la couleur diffuse** (ou tout autre attribut du matériau) en utilisant Aspose.3D for .NET. Expérimentez avec différents types de propriétés pour affiner l’apparence de vos actifs 3‑D.

## FAQ

### Q1 : Puis‑je utiliser Aspose.3D for .NET avec d’autres formats de fichiers 3D ?

A1 : Oui, Aspose.3D prend en charge divers formats de fichiers 3D, y compris FBX, STL, et bien d’autres.

### Q2 : Comment obtenir une licence temporaire pour Aspose.3D for .NET ?

A2 : Visitez [here](https://purchase.aspose.com/temporary-license/) pour obtenir une licence temporaire.

### Q3 : Existe‑t‑il un forum communautaire pour les utilisateurs d’Aspose.3D ?

A3 : Oui, vous pouvez trouver du support et des discussions sur le [Aspose.3D forum](https://forum.aspose.com/c/3d/18).

### Q4 : Où puis‑je trouver la documentation détaillée pour Aspose.3D for .NET ?

A4 : Consultez la [documentation](https://reference.aspose.com/3d/net/) pour des instructions complètes.

### Q5 : Puis‑je essayer Aspose.3D for .NET gratuitement avant d’acheter ?

A5 : Bien sûr ! Téléchargez la [free trial version](https://releases.aspose.com/) pour explorer ses fonctionnalités.

## Questions fréquemment posées

**Q : Que représente le `Vector3(1, 0, 1)` ?**  
R : Il définit la couleur diffuse en magenta (rouge = 1, vert = 0, bleu = 1) dans l’espace couleur linéaire.

**Q : Dois‑je appeler `scene.Save` après avoir changé les propriétés ?**  
R : Oui, persister la scène écrit vos modifications sur le disque ; sinon les changements restent uniquement en mémoire.

**Q : Puis‑je énumérer les attributs FBX personnalisés ?**  
R : Absolument. Le `PropertyCollection` inclura tous les attributs personnalisés, accessibles via `GetProperty("customName")`.

**Q : Existe‑t‑il un moyen de mettre à jour plusieurs matériaux en lot ?**  
R : Parcourez `scene.RootNode.ChildNodes` et répétez les étapes de modification des propriétés pour chaque matériau.

**Q : Aspose.3D prend‑il en charge .NET 6 ?**  
R : Oui, la bibliothèque est entièrement compatible avec .NET 6 et les versions ultérieures.

**Last Updated:** 2026-01-17  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}