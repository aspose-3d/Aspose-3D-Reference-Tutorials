---
title: Création de modèles 3D primitifs
linktitle: Création de modèles 3D primitifs
second_title: API Aspose.3D .NET
description: Explorez le monde de la modélisation 3D avec Aspose.3D pour .NET. Créez de superbes modèles primitifs sans effort.
type: docs
weight: 10
url: /fr/net/3d-modeling/primitive-3d-models/
---
## Introduction

Bienvenue dans le monde passionnant de la modélisation 3D avec Aspose.3D pour .NET ! Dans ce didacticiel complet, nous explorerons étape par étape le processus de création de modèles 3D primitifs à l'aide d'Aspose.3D. Que vous soyez un développeur chevronné ou un débutant curieux, ce guide vous aidera à exploiter la puissance d'Aspose.3D pour créer des éléments 3D visuellement époustouflants pour vos projets.

## Conditions préalables

Avant de plonger dans le domaine fascinant de la modélisation 3D, assurez-vous d’avoir les prérequis suivants en place :

-  Aspose.3D pour .NET : téléchargez et installez la bibliothèque Aspose.3D pour .NET à partir du[lien de téléchargement](https://releases.aspose.com/3d/net/).

- Environnement de développement : mettre en place un environnement de développement .NET, garantissant la compatibilité avec Aspose.3D.

Maintenant que vous avez l'essentiel, commençons notre voyage pour créer des modèles 3D primitifs étape par étape.

## Importer des espaces de noms

Commencez par importer les espaces de noms nécessaires pour accéder aux fonctionnalités fournies par Aspose.3D :

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

Une fois ces espaces de noms en place, vous êtes prêt à libérer la puissance d'Aspose.3D dans votre application .NET.

## Étape 1 : initialiser un objet de scène

```csharp
//Initialiser un objet Scene
Scene scene = new Scene();
```

Créez un nouvel objet de scène, qui servira de canevas à votre chef-d'œuvre 3D.

## Étape 2 : Créer un modèle de boîte

```csharp
// Créer un modèle de boîte
scene.RootNode.CreateChildNode("box", new Box());
```

Ajoutez un modèle de boîte à la racine de votre scène. Personnalisez les dimensions et les propriétés de la boîte selon votre vision créative.

## Étape 3 : Créer un modèle de cylindre

```csharp
// Créer un modèle de cylindre
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

Améliorez votre scène en introduisant un modèle de cylindre. Ajustez ses paramètres pour obtenir la forme et la taille souhaitées.

## Étape 4 : Enregistrer le dessin au format FBX

```csharp
// Enregistrer le dessin au format FBX
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Enregistrez votre chef-d'œuvre 3D au format FBX. Choisissez un répertoire de sortie et un nom de fichier appropriés pour votre création.

## Étape 5 : Afficher le message de réussite

```csharp
// Afficher le message de réussite
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

Célébrez votre réussite ! La scène est construite avec succès à partir de modèles 3D primitifs et le fichier est enregistré.

## Conclusion

 Toutes nos félicitations! Vous avez créé avec succès de superbes modèles 3D à l'aide d'Aspose.3D pour .NET. Ce guide couvre les bases, mais les possibilités sont illimitées. Explore le[Documentation](https://reference.aspose.com/3d/net/) pour des fonctionnalités et des techniques plus avancées.

## FAQ

### Q1 : Puis-je utiliser Aspose.3D pour .NET avec d’autres langages de programmation ?

A1 : Aspose.3D prend principalement en charge .NET, mais il existe d'autres versions disponibles pour Java et d'autres plates-formes.

### Q2 : Existe-t-il un essai gratuit ?

 A2 : Oui, vous pouvez explorer les capacités d'Aspose.3D avec un[essai gratuit](https://releases.aspose.com/).

### Q3 : Où puis-je trouver du support pour Aspose.3D pour .NET ?

 A3 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le soutien et les discussions de la communauté.

### Q4 : Comment puis-je obtenir une licence temporaire ?

 A4 : Vous pouvez obtenir un permis temporaire[ici](https://purchase.aspose.com/temporary-license/).

### Q5 : Existe-t-il des exemples de didacticiels disponibles ?

 A5 : Oui, explorez davantage de didacticiels et d'exemples dans le[Documentation](https://reference.aspose.com/3d/net/).