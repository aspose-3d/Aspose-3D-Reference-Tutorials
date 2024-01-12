---
title: Cylindre supérieur décalé personnalisé
linktitle: Cylindre supérieur décalé personnalisé
second_title: API Aspose.3D .NET
description: Explorez les merveilles des graphiques 3D avec Aspose.3D pour .NET. Apprenez à créer sans effort des cylindres supérieurs décalés personnalisés. Améliorez votre expérience de codage maintenant !
type: docs
weight: 11
url: /fr/net/working-with-cylinder/customized-offset-top-cylinder/
---
## Introduction
Bienvenue dans le monde de la manipulation graphique 3D avec Aspose.3D pour .NET ! Dans ce didacticiel, nous vous guiderons tout au long du processus de création d'un cylindre supérieur décalé personnalisé à l'aide d'Aspose.3D, une puissante bibliothèque permettant de travailler avec des scènes, des objets et des formats 3D dans des applications .NET.
## Conditions préalables
Avant de plonger dans le didacticiel, assurez-vous de disposer des prérequis suivants :
- Connaissance de base du langage de programmation C#.
- Visual Studio installé sur votre ordinateur.
- Bibliothèque Aspose.3D pour .NET téléchargée et référencée dans votre projet.
Maintenant, commençons avec le guide étape par étape !
## Importer des espaces de noms
Tout d’abord, assurez-vous d’importer les espaces de noms nécessaires dans votre code C# :
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
```csharp
// Créer une scène
Scene scene = new Scene();
```
Cela initialise une nouvelle scène 3D à l'aide d'Aspose.3D.
## Étape 2 : initialiser le cylindre
```csharp
// Initialiser le cylindre
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
Ici, nous créons un cylindre avec des paramètres spécifiques tels que le rayon, la hauteur et les tranches.
## Étape 3 : Définir OffsetTop pour le premier cylindre
```csharp
// Définir le décalage supérieur
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
Cela définit un dessus décalé personnalisé pour le premier cylindre.
## Étape 4 : Créer un ChildNode pour le premier cylindre
```csharp
// Créer un nœud enfant
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
Nous ajoutons le premier cylindre en tant que nœud enfant à la scène, en ajustant sa position.
## Étape 5 : initialiser le deuxième cylindre
```csharp
// Initialiser le deuxième cylindre sans OffsetTop personnalisé
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
Un deuxième cylindre est initialisé sans dessus décalé personnalisé.
## Étape 6 : Créer un ChildNode pour le deuxième cylindre
```csharp
// Créer un nœud enfant
scene.RootNode.CreateChildNode(cylinder2);
```
Nous ajoutons le deuxième cylindre en tant que nœud enfant à la scène.
## Étape 7 : Enregistrez la scène
```csharp
// Sauvegarder
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
Cela enregistre la scène 3D, y compris le cylindre supérieur décalé personnalisé, au format Wavefront OBJ.
Vous avez maintenant créé avec succès un cylindre supérieur décalé personnalisé à l'aide d'Aspose.3D pour .NET !
## Conclusion
Dans ce didacticiel, nous avons exploré les bases de l'utilisation d'Aspose.3D pour .NET pour créer un cylindre supérieur décalé personnalisé. Cette bibliothèque ouvre des possibilités infinies pour la manipulation graphique 3D au sein de vos applications .NET.
## FAQ
### Q : Où puis-je trouver la documentation d'Aspose.3D pour .NET ?
 R : La documentation est disponible[ici](https://reference.aspose.com/3d/net/).
### Q : Comment puis-je télécharger Aspose.3D pour .NET ?
 R : Vous pouvez le télécharger[ici](https://releases.aspose.com/3d/net/).
### Q : Existe-t-il un essai gratuit disponible pour Aspose.3D pour .NET ?
 R : Oui, vous pouvez bénéficier d'un essai gratuit[ici](https://releases.aspose.com/).
### Q : Où puis-je obtenir de l'assistance pour Aspose.3D pour .NET ?
 R : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le soutien.
### Q : Puis-je obtenir une licence temporaire pour Aspose.3D pour .NET ?
 R : Oui, vous pouvez obtenir une licence temporaire[ici](https://purchase.aspose.com/temporary-license/).