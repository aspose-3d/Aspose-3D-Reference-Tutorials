---
date: 2026-01-17
description: Apprenez à appliquer un matériau PBR à une boîte en utilisant Aspose.3D
  pour .NET, créez un matériau PBR et exportez des fichiers STL ASCII avec un rendu
  basé sur la physique.
linktitle: Applying PBR Material to Box
second_title: Aspose.3D .NET API
title: Comment appliquer un matériau PBR à une boîte
url: /fr/net/geometry-and-hierarchy/apply-pbr-material-to-box/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment appliquer un matériau PBR à une boîte

## Introduction

Bienvenue dans le monde fascinant des graphiques 3D ! Dans ce guide étape par étape, vous apprendrez **comment appliquer un matériau pbr** à une boîte en utilisant Aspose.3D pour .NET. Nous parcourrons la création d'un matériau PBR, son ajout à un maillage, et enfin **l'exportation STL ASCII** afin que vous puissiez utiliser le modèle dans n'importe quel flux de travail en aval. Que vous construisiez un prototype de jeu ou une visualisation de produit, maîtriser ce flux de travail ouvre la porte au rendu réaliste basé sur la physique (PBR) dans vos applications .NET.

## Réponses rapides
- **Quel est l'objectif principal ?** Appliquer un matériau PBR à une boîte et l'exporter en STL ASCII.  
- **Quelle bibliothèque est utilisée ?** Aspose.3D pour .NET (comment utiliser aspose).  
- **Ai-je besoin d'une licence ?** Oui, une licence temporaire ou complète est requise pour la production.  
- **Format de sortie pris en charge ?** STL ASCII (export stl ascii) et de nombreux autres formats 3D.  
- **Combien de temps cela prend‑il ?** Environ 10‑15 minutes pour une implémentation de base.

## Qu'est‑ce qu'un matériau PBR ?

Le rendu basé sur la physique (Physically Based Rendering, PBR) est un modèle d'ombrage qui simule la façon dont la lumière interagit avec les surfaces du monde réel. En ajustant des propriétés telles que les facteurs métallique et rugosité, vous pouvez obtenir des résultats très réalistes sans devoir régler manuellement des shaders complexes.

## Pourquoi utiliser le rendu basé sur la physique (PBR) ?

- **Réalité :** Les matériaux réagissent à l'éclairage d'une manière qui correspond à la physique réelle.  
- **Cohérence :** Le même matériau apparaît correctement sous n'importe quel environnement d'éclairage.  
- **Efficacité :** Les GPU modernes sont optimisés pour les calculs PBR, vous offrant des performances gratuites.

## Prérequis

Avant de plonger dans le code, assurez‑vous d'avoir les éléments suivants :

### Download and Install Aspose.3D for .NET
Visitez la [documentation Aspose.3D pour .NET](https://reference.aspose.com/3d/net/) pour des instructions détaillées sur le téléchargement et l'installation de la bibliothèque.

### Acquire a License
Pour libérer tout le potentiel d'Aspose.3D, obtenez une licence valide. Vous pouvez obtenir une licence temporaire [ici](https://purchase.aspose.com/temporary-license/) ou acheter une licence complète [ici](https://purchase.aspose.com/buy).

## Importer les espaces de noms
Tout d'abord, assurez‑vous d'importer les espaces de noms nécessaires pour exploiter les capacités d'Aspose.3D pour .NET :

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Étape 1 : Initialiser une scène
Commencez par initialiser une scène 3D en utilisant le fragment de code suivant :

```csharp
Scene scene = new Scene();
```

## Étape 2 : Créer un matériau PBR
Nous allons maintenant **créer un matériau pbr** qui donnera à notre boîte un aspect réaliste :

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Étape 3 : Définir les propriétés du matériau
Ajustez finement les propriétés du matériau, le rendant presque métallique et très rugueux — parfait pour une boîte en métal brossé :

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Étape 4 : Créer une boîte
Générez une boîte à laquelle le matériau PBR sera appliqué :

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Étape 5 : Ajouter le matériau PBR à la boîte
Attribuez le **add pbr material** précédemment configuré au nœud de boîte créé :

```csharp
boxNode.Material = mat;
```

## Étape 6 : Enregistrer la scène 3D au format STL ASCII
Enfin, **export stl ascii** afin que le modèle puisse être ouvert dans n'importe quel visualiseur 3D standard ou trancheur :

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Félicitations ! Vous avez appliqué avec succès un matériau PBR à une boîte dans une scène 3D en utilisant Aspose.3D pour .NET.

## Pièges courants et astuces
- **Licence non trouvée :** Assurez‑vous que le fichier de licence est chargé avant tout appel à Aspose ; sinon, la bibliothèque fonctionne en mode d'évaluation.  
- **Chemin de fichier incorrect :** Utilisez `Path.Combine` pour éviter les séparateurs de chemin manquants sur différents systèmes d'exploitation.  
- **Rugosité vs. Métallique :** Régler les deux facteurs trop haut peut rendre la surface plate ; expérimentez avec des valeurs entre 0,5‑0,9 pour un rendu équilibré.

## Conclusion
Se lancer dans les graphiques 3D avec Aspose.3D pour .NET ouvre des portes à d'innombrables possibilités créatives. Avec son API intuitive et ses fonctionnalités robustes, créer des scènes visuellement époustouflantes devient une expérience agréable pour les développeurs. Ensuite, essayez de remplacer la boîte par un maillage plus complexe ou expérimentez avec différentes textures PBR pour voir comment l'éclairage réagit.

## Questions fréquemment posées

**Q1 : Aspose.3D est‑il compatible avec d'autres formats de fichiers 3D ?**  
R1 : Oui, Aspose.3D prend en charge divers formats de fichiers 3D, assurant une flexibilité dans vos projets.

**Q2 : Puis‑je utiliser Aspose.3D pour des applications commerciales ?**  
R2 : Absolument ! Aspose.3D propose des licences commerciales pour une intégration fluide dans vos applications.

**Q3 : Existe‑t‑il une version d'essai disponible ?**  
R3 : Oui, vous pouvez explorer les capacités d'Aspose.3D en téléchargeant l'essai gratuit [ici](https://releases.aspose.com/).

**Q4 : Où puis‑je trouver du support communautaire et des discussions ?**  
R4 : Rejoignez la communauté Aspose.3D sur les [Forums Aspose.3D](https://forum.aspose.com/c/3d/18) pour obtenir du support et participer aux discussions.

**Q5 : Comment obtenir une licence temporaire pour Aspose.3D ?**  
R5 : Vous pouvez obtenir une licence temporaire [ici](https://purchase.aspose.com/temporary-license/) à des fins d'évaluation.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Dernière mise à jour :** 2026-01-17  
**Testé avec :** Aspose.3D 24.11 for .NET  
**Auteur :** Aspose  

---