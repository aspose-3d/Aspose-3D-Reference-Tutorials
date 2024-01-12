---
title: Direction dans l'extrusion linéaire
linktitle: Direction dans l'extrusion linéaire
second_title: API Aspose.3D .NET
description: Débloquez le monde de la modélisation 3D avec Aspose.3D pour .NET. Apprenez l’extrusion linéaire directionnelle, stimulez la créativité et créez des applications immersives sans effort.
type: docs
weight: 11
url: /fr/net/linear-extrusion/direction-in-linear-extrusion/
---
## Introduction

Dans le monde dynamique du développement logiciel, créer des modèles 3D immersifs est une compétence indispensable. Aspose.3D pour .NET fournit aux développeurs un ensemble d'outils robustes pour exploiter le potentiel de la modélisation 3D dans leurs applications. Dans ce didacticiel, nous plongerons dans le monde fascinant de l'extrusion linéaire et explorerons les nuances de la fonctionnalité « Direction dans l'extrusion linéaire ».

## Conditions préalables

Avant de nous lancer dans ce voyage passionnant, assurez-vous d’avoir les conditions préalables suivantes en place :

-  Aspose.3D pour .NET : téléchargez et installez la bibliothèque à partir de[Documentation Aspose.3D .NET](https://reference.aspose.com/3d/net/).

- Environnement de développement : assurez-vous d'avoir configuré un environnement de développement .NET fonctionnel.

## Importer des espaces de noms

Dans votre projet .NET, importez les espaces de noms nécessaires pour accéder aux fonctionnalités d'Aspose.3D. Ajoutez les lignes suivantes au début de votre code :

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Étape 1 : initialiser le profil de base

Commencez par initialiser le profil de base à extruder. Dans cet exemple, nous créons une forme rectangulaire avec un rayon d'arrondi de 0,3.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Étape 2 : Créer une scène 3D

Construisez les bases de votre chef-d'œuvre 3D en créant une scène.

```csharp
Scene scene = new Scene();
```

## Étape 3 : Créer des nœuds

Générez des nœuds dans la scène pour représenter différents composants de votre environnement 3D.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## Étape 4 : Extrusion linéaire sans direction

 Effectuez une extrusion linéaire sur le nœud gauche à l'aide de la touche`Twist` et`Slices` propriétés.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Étape 5 : Extrusion linéaire avec direction

 Étendez les capacités d'extrusion en incorporant le`Direction` propriété dans le nœud droit.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## Étape 6 : Enregistrez la scène 3D

 Préservez votre création en enregistrant la scène 3D. Remplacer`"Your Output Directory"` avec le répertoire souhaité.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Toutes nos félicitations! Vous avez implémenté avec succès l'extrusion linéaire avec Aspose.3D pour .NET, en explorant à la fois les approches traditionnelles et directionnelles.

## Conclusion

Dans ce didacticiel, nous avons parcouru le domaine fascinant de la modélisation 3D à l'aide d'Aspose.3D pour .NET. L'extrusion linéaire, avec ou sans direction, ouvre des possibilités infinies aux développeurs cherchant à créer des applications visuellement époustouflantes. Avec Aspose.3D, la puissance de la modélisation 3D est à portée de main.

## FAQ

### Q1 : Comment puis-je obtenir une licence temporaire pour Aspose.3D pour .NET ?

 A1 : Visite[Asposer une licence temporaire](https://purchase.aspose.com/temporary-license/) pour obtenir un permis temporaire.

### Q2 : Où puis-je trouver de l'assistance pour Aspose.3D ?

 A2 : Rejoignez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour demander de l'aide et entrer en contact avec la communauté.

### Q3 : Existe-t-il un essai gratuit disponible ?

 A3 : Oui, explorez les fonctionnalités avec un essai gratuit sur[Versions d'Aspose.3D](https://releases.aspose.com/).

### Q4 : Comment puis-je acheter Aspose.3D pour .NET ?

 A4 : Accédez au[Page d'achat Aspose](https://purchase.aspose.com/buy) pour les options de licence et les détails d’achat.

### Q5 : Où puis-je trouver une documentation détaillée pour Aspose.3D pour .NET ?

 A5 : Reportez-vous au document complet[Documentation Aspose.3D .NET](https://reference.aspose.com/3d/net/) pour des informations détaillées.