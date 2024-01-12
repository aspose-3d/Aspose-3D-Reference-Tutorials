---
title: Tranches en extrusion linéaire
linktitle: Tranches en extrusion linéaire
second_title: API Aspose.3D .NET
description: Explorez le monde de la conception 3D avec Aspose.3D pour .NET. Créez de superbes modèles à l’aide de notre didacticiel d’extrusion linéaire.
type: docs
weight: 13
url: /fr/net/linear-extrusion/slices-in-linear-extrusion/
---
## Introduction

Bienvenue dans le monde de la conception 3D avec Aspose.3D pour .NET ! Que vous soyez un développeur chevronné ou que vous débutiez tout juste, ce didacticiel vous guidera tout au long du processus de création de superbes visualisations 3D à l'aide de la puissante bibliothèque Aspose.3D.

## Conditions préalables

Avant de plonger dans le monde de la conception 3D avec Aspose.3D, assurez-vous d'avoir les prérequis suivants :

-  Aspose.3D pour la bibliothèque .NET : assurez-vous que la bibliothèque Aspose.3D est installée. Vous pouvez le télécharger depuis[ici](https://releases.aspose.com/3d/net/).

- Environnement de développement intégré (IDE) : utilisez n'importe quel IDE préféré compatible avec le développement .NET.

- Compréhension de base de C# : Familiarisez-vous avec les principes fondamentaux du langage de programmation C#.

- Désir d'explorer le design 3D : Une passion pour la création de modèles 3D visuellement époustouflants !

## Importer des espaces de noms

Pour commencer votre parcours de conception 3D avec Aspose.3D, vous devrez importer les espaces de noms nécessaires. Cela garantit que votre code peut accéder aux classes et fonctionnalités requises.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Extrusion linéaire - Tranches en extrusion linéaire

Passons maintenant à un exemple pratique : l'extrusion linéaire avec des tranches. Cette technique vous permet de créer des modèles 3D complexes avec différents niveaux de détail.

### Étape 1 : initialiser le profil de base

```csharp
// ExStart : Initialiser le profil de base
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd : Initialiser le profil de base
```

### Étape 2 : Créer une scène 3D

```csharp
// ExStart : Créer une scène 3DS
Scene scene = new Scene();
// ExEnd : Créer une scène 3DS
```

### Étape 3 : Créer des nœuds gauche et droit

```csharp
// ExStart : Créer des nœuds gauche-droite
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd : Créer des nœuds gauche-droite
```

### Étape 4 : effectuer une extrusion linéaire sur le nœud gauche

```csharp
// ExStart : LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd : LinearExtrusionLeftNode
```

### Étape 5 : Effectuer une extrusion linéaire sur le nœud droit

```csharp
// ExStart : LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd : LinearExtrusionRightNode
```

### Étape 6 : Enregistrer la scène 3D

```csharp
// ExDémarrer : Enregistrer la scène 3DS
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd : Save3DScene
```

## Conclusion

Toutes nos félicitations! Vous avez appris avec succès comment effectuer une extrusion linéaire avec des tranches à l'aide d'Aspose.3D pour .NET. Ce n'est que le début de votre parcours de conception 3D avec Aspose.3D : libérez votre créativité et explorez les possibilités infinies !

## FAQ

### Q1 : Puis-je utiliser Aspose.3D pour .NET avec d’autres langages de programmation ?

A1 : Aspose.3D est principalement conçu pour .NET, mais vous pouvez explorer les options d'interopérabilité avec des langages comme Python à l'aide des liaisons .NET.

### Q2 : Où puis-je trouver une documentation détaillée pour Aspose.3D pour .NET ?

 A2 : Se référer à la documentation[ici](https://reference.aspose.com/3d/net/) pour des informations détaillées sur les capacités et l'utilisation d'Aspose.3D.

### Q3 : Existe-t-il un essai gratuit disponible pour Aspose.3D pour .NET ?

 A3 : Oui, vous pouvez profiter de votre essai gratuit[ici](https://releases.aspose.com/) pour explorer les fonctionnalités de la bibliothèque avant de faire un achat.

### Q4 : Comment puis-je obtenir une assistance technique pour Aspose.3D pour .NET ?

 A4 : Visitez le forum Aspose.3D[ici](https://forum.aspose.com/c/3d/18) demander de l’aide et s’engager auprès de la communauté.

### Q5 : Puis-je utiliser une licence temporaire pour Aspose.3D pour .NET ?

 A5 : Oui, obtenez un permis temporaire[ici](https://purchase.aspose.com/temporary-license/) à des fins d’évaluation.