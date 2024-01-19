---
title: Création d'un cylindre de ventilateur
linktitle: Création d'un cylindre de ventilateur
second_title: API Aspose.3D .NET
description: Débloquez le monde de la conception 3D avec Aspose.3D pour .NET ! Créez sans effort de superbes cylindres de ventilateur et non-ventilateur. Téléchargez votre essai maintenant.
type: docs
weight: 10
url: /fr/net/working-with-cylinder/create-fan-cylinder/
---
## Introduction
Bienvenue dans le monde de la modélisation et de la visualisation 3D avec Aspose.3D pour .NET ! Dans ce guide étape par étape, nous explorerons comment créer un cylindre de ventilateur captivant à l'aide d'Aspose.3D pour .NET. Aspose.3D est une bibliothèque puissante qui offre des fonctionnalités étendues pour travailler avec du contenu 3D dans les applications .NET.
## Conditions préalables
Avant de plonger dans le monde passionnant de la modélisation 3D, assurez-vous de disposer des prérequis suivants :
- Une compréhension de base de la programmation .NET.
- Visual Studio installé sur votre ordinateur.
-  Bibliothèque Aspose.3D pour .NET, que vous pouvez télécharger[ici](https://releases.aspose.com/3d/net/).
- Un réel intérêt à libérer votre créativité grâce à la conception 3D.
## Importer des espaces de noms
Commençons par importer les espaces de noms nécessaires pour rendre la fonctionnalité Aspose.3D disponible dans votre projet .NET.
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Importer les espaces de noms Aspose.3D
```
Maintenant que nous sommes tous installés, décomposons le processus de création d'un cylindre de ventilateur en étapes gérables.
## Étape 1 : Créer une scène
```csharp
// Créer une scène
Scene scene = new Scene();
```
Commencez par initialiser une nouvelle scène 3D. Cela sert de toile sur laquelle notre cylindre de ventilateur prendra vie.
## Étape 2 : Créer un cylindre de ventilateur
```csharp
// Créer un cylindre
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
Définissez les caractéristiques de votre cylindre de ventilateur, en spécifiant des paramètres tels que le rayon, la hauteur et la résolution.
## Étape 3 : Personnaliser les propriétés du cylindre de ventilateur
```csharp
// Définissez GenerateFanCylinder sur vrai
fan.GenerateFanCylinder = true;
// Définir la longueur thêta
fan.ThetaLength = MathUtils.ToRadian(270);
```
Personnalisez votre cylindre de ventilateur en activant la génération de la partie ventilateur et en ajustant le balayage angulaire à l'aide de ThetaLength.
## Étape 4 : Positionner le cylindre du ventilateur dans la scène
```csharp
// Créer un nœud enfant
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
Ajoutez le cylindre du ventilateur en tant que nœud enfant au nœud racine de la scène et positionnez-le dans l'espace 3D.
## Étape 5 : Créer un cylindre sans ventilateur
```csharp
// Créer un cylindre sans ventilateur
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
Explorez la flexibilité d'Aspose.3D en créant un cylindre sans la partie ventilateur.
## Étape 6 : Personnaliser les propriétés du cylindre sans ventilateur
```csharp
// Définir GenerateFanCylinder sur false
nonfan.GenerateFanCylinder = false;
// Définir la longueur thêta
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
Distinguer le cylindre non ventilateur en désactivant la génération de la partie ventilateur.
## Étape 7 : Positionner le cylindre sans ventilateur dans la scène
```csharp
// Créer un nœud enfant
scene.RootNode.CreateChildNode(nonfan);
```
De même, ajoutez le cylindre non-ventilateur en tant que nœud enfant au nœud racine de la scène.
## Étape 8 : Enregistrez la scène
```csharp
// Enregistrer la scène
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
Enregistrez votre chef-d'œuvre au format et à l'emplacement souhaités. Vous avez maintenant créé avec succès un cylindre avec ventilateur et sans ventilateur à l'aide d'Aspose.3D pour .NET !
## Conclusion
Félicitations pour avoir terminé ce guide pratique sur la modélisation 3D avec Aspose.3D pour .NET ! Vous avez libéré votre créativité dans le domaine numérique, en créant facilement des cylindres avec et sans ventilateur.
## Questions fréquemment posées
### Puis-je utiliser Aspose.3D pour .NET avec d’autres frameworks .NET ?
Oui, Aspose.3D est compatible avec divers frameworks .NET, offrant une polyvalence dans vos projets de développement.
### Existe-t-il un essai gratuit disponible pour Aspose.3D pour .NET ?
 Oui, vous pouvez explorer un essai gratuit[ici](https://releases.aspose.com/).
### Où puis-je trouver une documentation détaillée pour Aspose.3D pour .NET ?
 La documentation est disponible[ici](https://reference.aspose.com/3d/net/).
### Comment puis-je obtenir du support pour Aspose.3D pour .NET ?
 Visitez le forum d'assistance[ici](https://forum.aspose.com/c/3d/18)pour obtenir l’aide de la communauté et des experts Aspose.
### Des licences temporaires sont-elles disponibles pour Aspose.3D pour .NET ?
 Oui, des licences temporaires peuvent être obtenues[ici](https://purchase.aspose.com/temporary-license/).