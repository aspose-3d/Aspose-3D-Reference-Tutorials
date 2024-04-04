---
title: Cylindre inférieur de cisaillement personnalisé
linktitle: Cylindre inférieur de cisaillement personnalisé
second_title: API Aspose.3D .NET
description: Apprenez à créer des cylindres inférieurs de cisaillement personnalisés à l'aide d'Aspose.3D pour .NET avec notre guide détaillé étape par étape. Élevez vos compétences en modélisation 3D dès aujourd'hui !
type: docs
weight: 12
url: /fr/net/3d-modeling/working-with-cylinder/
---
## Introduction
Bienvenue dans notre guide complet sur la création d'un cylindre personnalisé à l'aide d'Aspose.3D pour .NET. Si vous souhaitez améliorer vos compétences en modélisation 3D et ajouter des fonctionnalités uniques à vos projets, vous êtes au bon endroit. Dans ce didacticiel, nous vous guiderons pas à pas tout au long du processus, à l'aide d'explications claires et d'extraits de code.
## Conditions préalables
Avant de plonger dans le didacticiel, assurez-vous d'avoir les éléments suivants :
- Compréhension de base de la programmation C# et .NET.
-  Aspose.3D pour la bibliothèque .NET installée. Vous pouvez le télécharger[ici](https://releases.aspose.com/3d/net/).
- Un environnement de développement configuré pour la programmation .NET.
## Importer des espaces de noms
Dans votre code C#, commencez par importer les espaces de noms nécessaires :
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Étape 1 : Créer une scène
Commencez par créer une scène 3D à l'aide d'Aspose.3D :
```csharp
Scene scene = new Scene();
```
## Étape 2 : Créer le cylindre 1
Générez le premier cylindre et définissez ses propriétés :
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Étape 3 : Personnaliser le fond de cisaillement pour le cylindre 1
Appliquez un fond de cisaillement personnalisé au premier cylindre :
```csharp
//Cisaillement de 47,5 degrés dans le plan xy (axe z)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Définissez GenerateFanCylinder sur vrai
cylinder1.GenerateFanCylinder = true;
// Définir la longueur thêta
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Définir le décalage supérieur
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
## Étape 4 : ajouter le cylindre 1 à la scène
Ajoutez le premier cylindre à la scène et définissez sa traduction :
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Étape 5 : Créer le cylindre 2
Générez un deuxième cylindre avec des propriétés similaires :
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Étape 6 : ajouter le cylindre 2 à la scène
Ajoutez le deuxième cylindre à la scène sans paramètres personnalisés :
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Étape 7 : Enregistrez la scène
Enregistrez la scène en tant que fichier Wavefront OBJ dans votre répertoire de documents :
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Conclusion
Toutes nos félicitations! Vous avez créé avec succès un cylindre inférieur de cisaillement personnalisé à l'aide d'Aspose.3D pour .NET. Ce didacticiel visait à fournir un guide étape par étape aux utilisateurs ayant différents niveaux d'expertise en modélisation et en programmation 3D.
## Questions fréquemment posées
### Aspose.3D pour .NET convient-il aux débutants ?
Absolument! Aspose.3D pour .NET offre une interface conviviale, la rendant accessible aussi bien aux développeurs débutants qu'expérimentés.
### Puis-je appliquer différents angles de cisaillement aux cylindres ?
Oui, vous pouvez personnaliser le fond de cisaillement pour chaque cylindre individuellement, vous permettant d'obtenir des effets uniques.
### Existe-t-il une version d'essai disponible ?
 Oui, vous pouvez explorer la version d'essai gratuite[ici](https://releases.aspose.com/).
### Où puis-je trouver une assistance supplémentaire ?
 Visiter le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le soutien et les discussions de la communauté.
### Comment puis-je obtenir un permis temporaire ?
 Obtenez votre permis temporaire[ici](https://purchase.aspose.com/temporary-license/).