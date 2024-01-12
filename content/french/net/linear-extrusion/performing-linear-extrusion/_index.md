---
title: Exécution d'une extrusion linéaire
linktitle: Exécution d'une extrusion linéaire
second_title: API Aspose.3D .NET
description: Explorez le monde des graphiques 3D avec Aspose.3D pour .NET. Réalisation d'une extrusion linéaire dans ce guide étape par étape.
type: docs
weight: 12
url: /fr/net/linear-extrusion/performing-linear-extrusion/
---
## Introduction:

Embarquez pour un voyage passionnant dans le domaine des graphiques 3D avec Aspose.3D pour .NET, une centrale qui élève votre jeu de développement. Dans ce didacticiel, nous approfondirons les subtilités de l'extrusion linéaire, une technique fascinante qui donne vie aux profils 2D statiques, les propulsant dans le monde dynamique de la 3D. Ouvrons la porte à la créativité et à l'innovation avec Aspose.3D !

## Conditions préalables:

Avant de plonger dans le monde enchanteur de la manipulation 3D, assurez-vous d’avoir les prérequis suivants en place :

1. Installation d'Aspose.3D :
   -  Commencez par télécharger et installer Aspose.3D pour .NET à partir de[ici](https://releases.aspose.com/3d/net/).
   -  Suivez les instructions d'installation fournies dans la documentation[ici](https://reference.aspose.com/3d/net/).

2. Configuration de votre environnement de développement :
   - Assurez-vous que votre environnement de développement est correctement configuré avec les espaces de noms requis pour Aspose.3D.

Maintenant que vous êtes prêt, passons à la magie d’Aspose.3D !

## Importer des espaces de noms :

Incluez les espaces de noms essentiels pour démarrer votre aventure 3D :

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Ces espaces de noms jettent les bases de votre parcours de codage 3D, donnant accès aux outils nécessaires à une intégration transparente des fonctionnalités Aspose.3D.

## Exécution d'une extrusion linéaire :

Créons un objet 3D fascinant grâce à l'extrusion linéaire à l'aide d'Aspose.3D. Suivez ces étapes:

## Étape 1 : initialiser le profil de base
```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Cette étape définit le profil 2D qui servira de base à notre chef-d'œuvre 3D. Ajustez les paramètres si nécessaire pour obtenir la forme souhaitée.

## Étape 2 : Extrusion linéaire
```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

Ici, l'extrusion linéaire est réalisée, en prenant le profil 2D et en l'étendant dans la troisième dimension. Expérimentez avec des paramètres tels que « Tranches » et « Torsion » pour façonner votre création.

## Étape 3 : Créer une scène
```csharp
Scene scene = new Scene();
```

Une toile vierge est créée – une scène où votre objet 3D prendra vie.

## Étape 4 : ajouter une extrusion à la scène
```csharp
scene.RootNode.CreateChildNode(extrusion);
```

Votre chef-d'œuvre extrudé est ajouté en tant que nœud enfant à la scène.

## Étape 5 : Enregistrez la scène 3D
```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Enfin, enregistrez votre création au format souhaité. Dans cet exemple, il est enregistré en tant que fichier Wavefront OBJ.

Maintenant, voici votre merveille 3D !

## Conclusion:

Toutes nos félicitations! Vous venez d'effleurer la surface du potentiel d'Aspose.3D. Ce didacticiel fait simplement allusion au vaste paysage qui attend votre exploration. Plongez dans la documentation, expérimentez différentes formes et débloquez tout le spectre des possibilités avec Aspose.3D pour .NET.

## FAQ :

### Q1 : Aspose.3D convient-il aux débutants ?

A1 : Absolument ! Aspose.3D offre un environnement convivial et notre didacticiel vous guide à travers les bases.

### Q2 : Puis-je utiliser Aspose.3D pour des projets commerciaux ?

 A2 : Oui, Aspose.3D est livré avec des options de licence pour un usage personnel et commercial. Vérifier[ici](https://purchase.aspose.com/buy) pour plus de détails.

### Q3 : Comment puis-je obtenir des licences temporaires pour les tests ?

 A3 : Visite[ce lien](https://purchase.aspose.com/temporary-license/) pour obtenir des licences temporaires à des fins de tests.

### Q4 : Où puis-je trouver le soutien de la communauté ?

 A4 : Rejoignez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour se connecter avec une communauté dynamique et demander de l’aide.

### Q5 : Existe-t-il un essai gratuit ?

 A5 : Certainement ! Téléchargez la version d'essai gratuite[ici](https://releases.aspose.com/) pour découvrir les capacités d'Aspose.3D.