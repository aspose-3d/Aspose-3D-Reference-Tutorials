---
title: Transformation du nœud par matrice de transformation
linktitle: Transformation du nœud par matrice de transformation
second_title: API Aspose.3D .NET
description: Transformez les nœuds sans effort dans des scènes 3D à l'aide d'Aspose.3D pour .NET. Apprenez les transformations de nœuds étape par étape avec le didacticiel.
type: docs
weight: 21
url: /fr/net/geometry-and-hierarchy/transformation-node-matrix/
---
## Introduction

Dans le domaine dynamique des graphiques et des visualisations 3D, la capacité de manipuler des objets au sein d’une scène est un aspect crucial. Aspose.3D pour .NET permet aux développeurs de transformer de manière transparente les nœuds à l'aide de matrices de transformation, ajoutant ainsi une couche de créativité et de contrôle aux scènes 3D. Ce didacticiel vous guidera étape par étape dans le processus de transformation d'un nœud en scène 3D.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous que les conditions préalables suivantes sont remplies :

1.  Bibliothèque Aspose.3D pour .NET : assurez-vous que la bibliothèque Aspose.3D est installée dans votre projet .NET. Vous pouvez le télécharger[ici](https://releases.aspose.com/3d/net/).

2. Environnement de développement : configurez un environnement de développement .NET fonctionnel et, si ce n'est pas déjà fait, créez un nouveau projet dans lequel vous implémenterez les transformations.

## Importer des espaces de noms

Commencez par importer les espaces de noms nécessaires dans votre projet .NET. Ces espaces de noms fournissent les classes et méthodes essentielles à la manipulation de scènes 3D.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Maintenant que nous avons couvert les bases, décomposons le processus de transformation en un guide étape par étape.

## Étape 1 : initialiser la scène

```csharp
// ExStart : AddTransformationToNodeByTransformationMatrix
// Initialiser l'objet de scène
Scene scene = new Scene();

```

Dans cette étape, nous créons une nouvelle scène 3D vide.

## Étape 2 : créer un maillage et l'attacher à la scène

```csharp
// Appelez la classe Common pour créer un maillage à l'aide de la méthode de création de polygones pour définir l'instance de maillage
Mesh mesh = (new Box()).ToMesh();

// Créez un nœud conteneur pour le maillage.
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

Ici, nous générons un maillage à l'aide de la méthode de création de polygones et l'attribuons au nœud, établissant ainsi la géométrie de notre cube.

## Étape 3 : Définir une matrice de traduction personnalisée

```csharp
// Définir une matrice de traduction personnalisée
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Définissez une matrice de traduction personnalisée pour déterminer la transformation spécifique appliquée au nœud. Ajustez les valeurs de la matrice selon vos besoins pour la transformation souhaitée.

Incluez le nœud de cube dans la scène, en l'intégrant à l'environnement 3D global.

## Étape 4 : Enregistrez la scène

```csharp
// Le chemin d'accès au répertoire des documents.
var output = "TransformationToNode.fbx";

// Enregistrez la scène 3D dans les formats de fichiers pris en charge
scene.Save(output);
// ExEnd : AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Spécifiez le répertoire de sortie et le nom du fichier, puis enregistrez la scène 3D au format de fichier souhaité. Dans cet exemple, nous l'enregistrons au format FBX7500ASCII.

## Conclusion

Toutes nos félicitations! Vous avez réussi à transformer un nœud à l'aide d'une matrice de transformation dans une scène 3D avec Aspose.3D pour .NET. Cette capacité ouvre les portes à des applications 3D diverses et visuellement captivantes.

## FAQ

### Q1 : Qu'est-ce qu'une matrice de transformation dans les graphiques 3D ?

A1 : Une matrice de transformation est une représentation mathématique utilisée pour appliquer diverses transformations (translation, rotation, mise à l'échelle) à des objets dans l'espace 3D.

### Q2 : Puis-je appliquer plusieurs transformations à un seul nœud ?

A2 : Oui, vous pouvez combiner plusieurs transformations en multipliant leurs matrices respectives et en appliquant le résultat au nœud.

### Q3 : Existe-t-il d'autres formats de fichiers pris en charge pour enregistrer des scènes 3D ?

 A3 : Aspose.3D pour .NET prend en charge divers formats de fichiers, notamment STL, GLTF, OBJ, etc. Se référer au[Documentation](https://reference.aspose.com/3d/net/) pour une liste complète.

### Q4 : Comment puis-je obtenir une licence temporaire pour Aspose.3D pour .NET ?

 A4 : Visitez le[page de licence temporaire](https://purchase.aspose.com/temporary-license/)sur le site Aspose pour obtenir une licence temporaire à des fins d'évaluation.

### Q5 : Où puis-je demander de l'aide ou me connecter à la communauté Aspose.3D ?

 A5 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour poser des questions, partager des expériences et vous connecter avec d'autres développeurs utilisant Aspose.3D.