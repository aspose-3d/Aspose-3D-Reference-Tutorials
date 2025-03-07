---
title: Concaténation des quaternions
linktitle: Concaténation des quaternions
second_title: API Aspose.3D .NET
description: Explorez la puissance de la manipulation des quaternions dans les scènes 3D avec Aspose.3D pour .NET. Apprenez à concaténer les quaternions étape par étape pour des transformations immersives.
weight: 11
url: /fr/net/geometry-and-hierarchy/concatenate-quaternions/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Concaténation des quaternions

## Introduction

Bienvenue dans ce didacticiel complet sur la concaténation des quaternions dans des scènes 3D à l'aide d'Aspose.3D pour .NET ! Si vous êtes un développeur ou un passionné de 3D souhaitant améliorer vos compétences en manipulation de quaternions, vous êtes au bon endroit. Ce didacticiel vous guidera étape par étape tout au long du processus, garantissant une expérience d'apprentissage fluide.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous que les conditions préalables suivantes sont remplies :

-  Aspose.3D pour la bibliothèque .NET : téléchargez et installez la bibliothèque à partir du[Site Aspose](https://releases.aspose.com/3d/net/).
- Environnement de développement : assurez-vous de disposer d'un environnement de développement fonctionnel pour .NET.

## Importer des espaces de noms

Dans votre projet .NET, incluez les espaces de noms nécessaires pour tirer parti de la puissance d'Aspose.3D :

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
```

## Étape 1 : Créer une scène

Commencez par créer une scène 3D à l'aide de la bibliothèque Aspose.3D. La scène servira de canevas pour la manipulation des quaternions.

```csharp
Scene scene = new Scene();
```

## Étape 2 : Définir les quaternions

 Définir trois quaternions,`q1`, `q2` , et`q3`, chacun représentant une rotation spécifique.

```csharp
Quaternion q1 = Quaternion.FromEulerAngle(Math.PI * 0.5, 0, 0);
Quaternion q2 = Quaternion.FromAngleAxis(-Math.PI * 0.5, Vector3.XAxis);
Quaternion q3 = q1.Concat(q2);
```

## Étape 3 : Créer des cylindres

Créez trois cylindres, chacun représentant un quaternion. Définissez les propriétés de rotation et de translation en fonction des quaternions définis.

```csharp
Node cylinder = scene.RootNode.CreateChildNode("cylinder-q1", new Cylinder(0.1, 1, 2));
cylinder.Transform.Rotation = q1;
cylinder.Transform.Translation = new Vector3(-5, 2, 0);

// Répétez pour q2 et q3
```

## Étape 4 : Enregistrer dans un fichier

Enregistrez la scène dans un fichier, en spécifiant le format de sortie et le nom du fichier.

```csharp
var output = "Your Output Directory" + "test_out.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```

## Étape 5 : Afficher le message de réussite

Imprimez un message de réussite avec le chemin du fichier une fois les quaternions concaténés et le fichier enregistré.

```csharp
Console.WriteLine("\nQuaternions concatenated successfully.\nFile saved at " + output);
```

## Conclusion

Toutes nos félicitations! Vous avez appris avec succès comment concaténer des quaternions dans des scènes 3D à l'aide d'Aspose.3D pour .NET. Expérimentez avec différentes combinaisons de quaternions pour réaliser des transformations uniques dans vos projets.

## FAQ

### Q1 : Que sont les quaternions dans les graphiques 3D ?

A1 : Les quaternions sont des entités mathématiques utilisées pour représenter les rotations dans l'espace 3D, offrant des avantages par rapport aux autres représentations de rotation.

### Q2 : Puis-je utiliser Aspose.3D pour .NET avec d’autres bibliothèques .NET ?

A2 : Oui, Aspose.3D pour .NET est conçu pour fonctionner de manière transparente avec d'autres bibliothèques .NET.

### Q3 : Existe-t-il un essai gratuit disponible pour Aspose.3D pour .NET ?

A3 : Oui, vous pouvez accéder à un essai gratuit[ici](https://releases.aspose.com/).

### Q4 : Comment puis-je obtenir du support pour Aspose.3D pour .NET ?

 A4 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le soutien et les discussions de la communauté.

### Q5 : Puis-je utiliser une licence temporaire pour Aspose.3D pour .NET ?

 A5 : Oui, vous pouvez obtenir une licence temporaire[ici](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
