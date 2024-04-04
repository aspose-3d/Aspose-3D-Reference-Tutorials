---
title: Animation de propriétés à documenter dans des scènes 3D
linktitle: Animation de propriétés à documenter dans des scènes 3D
second_title: API Aspose.3D .NET
description: Apprenez à animer des propriétés 3D avec Aspose.3D pour .NET. Guide étape par étape pour créer des scènes dynamiques.
type: docs
weight: 10
url: /fr/net/animation/property-to-document/
---
## Introduction

Si vous plongez dans le domaine de la création et de l'animation de scènes 3D dans .NET, Aspose.3D est votre boîte à outils incontournable. Dans ce guide étape par étape, nous explorerons le processus d'animation de propriétés dans des scènes 3D à l'aide d'Aspose.3D pour .NET. À la fin, vous disposerez des connaissances nécessaires pour donner vie à vos projets 3D.

## Conditions préalables

Avant de nous lancer dans cette aventure passionnante, assurez-vous d’avoir les conditions préalables suivantes en place :

-  Aspose.3D pour .NET : assurez-vous que la bibliothèque est installée. Vous pouvez le télécharger depuis le[Site Aspose.3D](https://releases.aspose.com/3d/net/).

- Connaissance de C# : La connaissance du langage de programmation C# est essentielle pour comprendre et mettre en œuvre les exemples.

- Environnement de développement intégré (IDE) : utilisez votre IDE préféré, tel que Visual Studio, pour le codage avec les exemples.

- Concepts de base des scènes 3D : Une compréhension des concepts de base des scènes 3D facilitera votre parcours d’apprentissage.

## Importer des espaces de noms

Dans votre code C#, assurez-vous d'importer les espaces de noms nécessaires pour Aspose.3D. Voici un exemple :

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## Étape 1 : initialiser l'objet de scène

```csharp
Scene scene = new Scene();
```

## Étape 2 : Créer un maillage à l'aide de Polygon Builder

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Étape 3 : Créer des nœuds de cube

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Étape 4 : Rechercher la propriété de traduction

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Étape 5 : Créer un point de liaison

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Étape 6 : Lier la courbe d'animation sur le composant X

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Étape 7 : Lier la courbe d'animation sur le composant Z

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Étape 8 : Enregistrer la scène 3D

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Étape 9 : Afficher le message de réussite

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Conclusion

Toutes nos félicitations! Vous venez de maîtriser l'art de l'animation de propriétés dans des scènes 3D à l'aide d'Aspose.3D pour .NET. Maintenant, laissez libre cours à votre créativité pendant que vous donnez vie à vos créations 3D.

## Questions fréquemment posées

### Q1 : Où puis-je trouver la documentation Aspose.3D ?

 A1 : La documentation est disponible[ici](https://reference.aspose.com/3d/net/).

### Q2 : Comment télécharger Aspose.3D pour .NET ?

 A2 : Vous pouvez le télécharger à partir du[page de sortie](https://releases.aspose.com/3d/net/).

### Q3 : Existe-t-il un essai gratuit disponible ?

 A3 : Oui, vous pouvez bénéficier d'un essai gratuit[ici](https://releases.aspose.com/).

### Q4 : Où puis-je obtenir de l'aide pour Aspose.3D ?

 A4 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le soutien.

### Q5 : Puis-je obtenir une licence temporaire ?

 A5 : Oui, vous pouvez obtenir une licence temporaire[ici](https://purchase.aspose.com/temporary-license/).