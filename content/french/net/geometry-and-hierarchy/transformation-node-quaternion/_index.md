---
title: Transformation de nœud par Quaternion dans des scènes 3D
linktitle: Transformation de nœud par Quaternion dans des scènes 3D
second_title: API Aspose.3D .NET
description: Apprenez à transformer des nœuds 3D avec des quaternions à l'aide d'Aspose.3D pour .NET. Guide étape par étape pour les débutants.
type: docs
weight: 20
url: /fr/net/geometry-and-hierarchy/transformation-node-quaternion/
---
## Introduction

Bienvenue dans un guide étape par étape sur la transformation d'un nœud par quaternion dans des scènes 3D à l'aide d'Aspose.3D pour .NET. Dans ce didacticiel, nous explorerons les puissantes fonctionnalités d'Aspose.3D pour .NET et passerons en revue le processus d'ajout de transformations à un nœud 3D à l'aide de quaternions.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous que les conditions préalables suivantes sont remplies :

-  Aspose.3D pour .NET : assurez-vous que la bibliothèque Aspose.3D est installée. Vous pouvez le télécharger depuis le[page de sortie](https://releases.aspose.com/3d/net/).

- Environnement de développement : configurez votre environnement de développement .NET avec les outils et configurations nécessaires.

- Compréhension de base des concepts 3D : une connaissance des graphiques et des concepts 3D sera utile.

## Importer des espaces de noms

Dans votre projet .NET, incluez les espaces de noms requis pour Aspose.3D :

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Étape 1 : initialiser l'objet de scène

```csharp
// ExStart : AddTransformationToNodeByQuaternion
// Initialiser l'objet de scène
Scene scene = new Scene();
```

## Étape 2 : initialiser l'objet de classe de nœud

```csharp
// Initialiser l'objet de classe Node
Node cubeNode = new Node("cube");
```

## Étape 3 : Créer un maillage à l'aide de Polygon Builder

```csharp
// Appelez la classe Common pour créer un maillage à l'aide de la méthode de création de polygones pour définir l'instance de maillage
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Étape 4 : Pointer le nœud vers la géométrie du maillage

```csharp
// Pointer le nœud vers la géométrie du maillage
cubeNode.Entity = mesh;
```

## Étape 5 : Définir la rotation à l’aide du Quaternion

```csharp
// Définir la rotation
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## Étape 6 : Définir la traduction

```csharp
// Définir la traduction
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## Étape 7 : ajouter un cube à la scène

```csharp
// Ajouter un cube à la scène
scene.RootNode.ChildNodes.Add(cubeNode);
```

## Étape 8 : Enregistrer la scène 3D

```csharp
// Le chemin d'accès au répertoire des documents.
var output = "Your Output Directory" + "TransformationToNode.fbx";

//Enregistrez la scène 3D dans les formats de fichiers pris en charge
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd : AddTransformationToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## Conclusion

Toutes nos félicitations! Vous avez appris avec succès comment transformer un nœud par quaternion dans des scènes 3D à l'aide d'Aspose.3D pour .NET. Explorez plus de fonctionnalités et de possibilités en vous référant au[Documentation](https://reference.aspose.com/3d/net/).

## FAQ

### Q1 : Qu'est-ce qu'un quaternion dans les graphiques 3D ?

A1 : Les quaternions sont des entités mathématiques utilisées pour représenter les rotations dans l'espace 3D.

### Q2 : Comment puis-je télécharger Aspose.3D pour .NET ?

 A2 : Vous pouvez télécharger la bibliothèque à partir du[page de sortie](https://releases.aspose.com/3d/net/).

### Q3 : Existe-t-il un essai gratuit disponible pour Aspose.3D pour .NET ?

 A3 : Oui, vous pouvez bénéficier d'un essai gratuit auprès de[ici](https://releases.aspose.com/).

### Q4 : Où puis-je trouver du support pour Aspose.3D pour .NET ?

 A4 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour du soutien et des discussions.

### Q5 : Comment puis-je obtenir une licence temporaire pour Aspose.3D ?

 A5 : Obtenez un permis temporaire[ici](https://purchase.aspose.com/temporary-license/).
