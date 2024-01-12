---
title: Centre en extrusion linéaire
linktitle: Centre en extrusion linéaire
second_title: API Aspose.3D .NET
description: Explorez le monde de la modélisation 3D avec Aspose.3D pour .NET. Centrez les techniques d'extrusion linéaire, créez des designs époustouflants et libérez votre créativité.
type: docs
weight: 10
url: /fr/net/linear-extrusion/center-in-linear-extrusion/
---
## Introduction

Bienvenue dans ce guide complet sur la maîtrise de l'extrusion linéaire à l'aide d'Aspose.3D pour .NET. Si vous souhaitez améliorer vos compétences en modélisation 3D et créer de superbes extrusions, vous êtes au bon endroit. Dans ce didacticiel, nous approfondirons la technique d'extrusion linéaire, en nous concentrant spécifiquement sur l'aspect du centrage pour amener vos conceptions à un tout autre niveau.

## Conditions préalables

Avant de nous lancer dans ce voyage passionnant, assurez-vous d’avoir les conditions préalables suivantes en place :

- Compréhension de base du langage de programmation C#.
- Visual Studio installé sur votre ordinateur.
-  Bibliothèque Aspose.3D pour .NET, que vous pouvez télécharger à partir du[Documentation Aspose.3D .NET](https://reference.aspose.com/3d/net/).
-  Assurez-vous d'avoir accès au[Documentation Aspose.3D .NET](https://reference.aspose.com/3d/net/) pour référence tout au long du didacticiel.

## Importer des espaces de noms

Pour commencer, importons les espaces de noms nécessaires. Ceux-ci jetteront les bases de notre chef-d’œuvre de modélisation 3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Étape 1 : initialiser le profil de base

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Étape 2 : Créer une scène 3D

```csharp
Scene scene = new Scene();
```

## Étape 3 : Créer des nœuds gauche et droit

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Étape 4 : effectuer une extrusion linéaire sur le nœud gauche

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Étape 5 : Définir le plan de sol pour référence

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Étape 6 : Effectuer une extrusion linéaire sur le nœud droit

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Étape 7 : Définir le plan de sol pour référence (nœud droit)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Étape 8 : Enregistrer la scène 3D

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Conclusion

Toutes nos félicitations! Vous maîtrisez avec succès l'art de l'extrusion linéaire avec centrage à l'aide d'Aspose.3D pour .NET. N'hésitez pas à expérimenter différents paramètres et à explorer les vastes possibilités qu'offre cette technique.

## FAQ

### Q1 : Puis-je utiliser Aspose.3D pour .NET avec d’autres langages de programmation ?

A1 : Aspose.3D prend principalement en charge les langages .NET tels que C# et VB.NET.

### Q2 : Où puis-je trouver de l'aide pour les requêtes liées à Aspose.3D ?

 A2 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour un soutien et des discussions dédiés.

### Q3 : Existe-t-il un essai gratuit disponible pour Aspose.3D pour .NET ?

 A3 : Oui, vous pouvez accéder à l'essai gratuit[ici](https://releases.aspose.com/).

### Q4 : Comment puis-je obtenir une licence temporaire pour Aspose.3D pour .NET ?

 A4 : Vous pouvez acquérir une licence temporaire[ici](https://purchase.aspose.com/temporary-license/).

### Q5 : Où puis-je acheter la licence Aspose.3D pour .NET ?

 A5 : Achetez votre licence[ici](https://purchase.aspose.com/buy).
