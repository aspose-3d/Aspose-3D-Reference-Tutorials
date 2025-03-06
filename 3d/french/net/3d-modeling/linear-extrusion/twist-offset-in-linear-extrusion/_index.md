---
title: Décalage de torsion dans l'extrusion linéaire
linktitle: Décalage de torsion dans l'extrusion linéaire
second_title: API Aspose.3D .NET
description: Explorez la magie d'Aspose.3D pour .NET avec notre guide étape par étape sur le décalage de torsion dans l'extrusion linéaire. Élevez vos projets 3D sans effort.
weight: 15
url: /fr/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Décalage de torsion dans l'extrusion linéaire

## Introduction

Bienvenue dans le monde d'Aspose.3D pour .NET, une bibliothèque polyvalente permettant aux développeurs de gérer facilement la manipulation 3D. Dans ce didacticiel, nous aborderons l'une des fonctionnalités les plus intéressantes : le "décalage de torsion dans l'extrusion linéaire". Si vous êtes prêt à améliorer vos compétences en programmation 3D, allons-y !

## Conditions préalables

Avant de nous lancer dans ce voyage passionnant, assurez-vous d’avoir les conditions préalables suivantes en place :

-  Aspose.3D pour la bibliothèque .NET : téléchargez et installez la bibliothèque à partir du[page de sortie](https://releases.aspose.com/3d/net/).

- Votre environnement de développement : assurez-vous que votre environnement de développement est configuré et prêt à fonctionner.

## Importer des espaces de noms

Commencez par importer les espaces de noms nécessaires pour accéder aux fonctionnalités fournies par Aspose.3D pour .NET. Dans votre code, cela pourrait ressembler à :

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Maintenant, décomposons l'exemple en étapes gérables pour maîtriser le décalage de torsion dans l'extrusion linéaire :

## Étape 1 : initialiser le profil de base

Commencez par créer un profil de base, illustré ici par une forme de rectangle avec un rayon d'arrondi spécifié.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Étape 2 : Créer une scène

Générez une scène 3D pour héberger vos nœuds et formes.

```csharp
Scene scene = new Scene();
```

## Étape 3 : Créer des nœuds

Construisez des nœuds dans la scène, à gauche et à droite.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## Étape 4 : Extrusion linéaire sur le nœud gauche

Effectuez une extrusion linéaire sur le nœud gauche à l'aide de la propriété twist et slices.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Étape 5 : Extrusion linéaire sur le nœud droit avec décalage de torsion

Sur le nœud de droite, effectuez une extrusion linéaire à l'aide des propriétés twist, twist offset et slices.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## Étape 6 : Enregistrer la scène 3D

Enregistrez la scène 3D dans le répertoire de sortie souhaité, en spécifiant le format de fichier comme WavefrontOBJ.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Toutes nos félicitations! Vous avez implémenté avec succès le décalage de torsion dans l'extrusion linéaire à l'aide d'Aspose.3D pour .NET.

## Conclusion

Dans ce didacticiel, nous avons exploré les puissantes capacités d'Aspose.3D pour .NET, en nous concentrant spécifiquement sur le décalage de torsion dans l'extrusion linéaire. Grâce à ces nouvelles compétences, vous êtes bien équipé pour insuffler du dynamisme à vos projets 3D.

## FAQ

### Q1 : Puis-je utiliser Aspose.3D pour .NET avec d’autres langages de programmation ?

A1 : Aspose.3D prend principalement en charge les langages .NET, mais Aspose fournit des bibliothèques similaires pour Java et d'autres plates-formes.

### Q2 : Comment puis-je obtenir une licence temporaire pour Aspose.3D pour .NET ?

 A2 : Visite[ce lien](https://purchase.aspose.com/temporary-license/)pour acquérir une licence temporaire à des fins de tests.

### Q3 : Existe-t-il un forum communautaire pour Aspose.3D pour .NET ?

 A3 : Absolument ! Rejoignez la communauté sur[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour interagir avec d’autres développeurs et demander de l’aide.

### Q4 : Existe-t-il des exemples et de la documentation supplémentaires disponibles ?

 A4 : Explorez le[Documentation](https://reference.aspose.com/3d/net/) pour des guides et des exemples détaillés.

### Q5 : Où puis-je acheter Aspose.3D pour .NET ?

 A5 : Dirigez-vous vers[ce lien](https://purchase.aspose.com/buy) pour effectuer un achat et libérer tout le potentiel d’Aspose.3D.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
