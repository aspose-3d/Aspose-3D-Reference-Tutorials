---
title: Transformez des nœuds 3D avec des matrices de transformation à l'aide d'Aspose.3D
linktitle: Transformez des nœuds 3D avec des matrices de transformation en Java à l'aide d'Aspose.3D
second_title: API Java Aspose.3D
description: Explorez le monde des graphiques 3D en Java avec Aspose.3D. Apprenez à transformer des nœuds sans effort à l'aide de matrices de transformation.
type: docs
weight: 21
url: /fr/java/geometry/transform-3d-nodes-with-matrices/
---
## Introduction

Bienvenue dans ce guide étape par étape sur la transformation de nœuds 3D avec des matrices de transformation en Java à l'aide d'Aspose.3D. Si vous êtes un développeur Java cherchant à améliorer vos compétences en graphisme et en modélisation 3D, vous êtes au bon endroit. Dans ce didacticiel, nous allons plonger dans le processus d'application de transformations aux nœuds 3D dans le framework Aspose.3D.

## Conditions préalables

Avant de commencer, assurez-vous d'avoir les prérequis suivants :

- Connaissance de base de la programmation Java.
-  Bibliothèque Aspose.3D installée. Vous pouvez le télécharger depuis[ici](https://releases.aspose.com/3d/java/).
- Un environnement de développement intégré (IDE) fonctionnel pour le développement Java.

## Importer des packages

Dans votre projet Java, importez les packages nécessaires depuis Aspose.3D. Assurez-vous que votre projet est correctement configuré pour utiliser la bibliothèque Aspose.3D. Voici un exemple d'instruction d'importation :

```java
import com.aspose.threed.*;

```

## Transformation des nœuds 3D

### Étape 1 : initialiser l'objet de scène

Commencez par initialiser un objet de scène, qui sert de conteneur aux éléments 3D.

```java
Scene scene = new Scene();
```

### Étape 2 : initialiser l'objet de classe de nœud

Créez un objet de classe Node, tel qu'un cube, qui subira une transformation.

```java
Node cubeNode = new Node("cube");
```

### Étape 3 : Créer un maillage à l'aide de Polygon Builder

Utilisez la classe Common pour créer un maillage à l'aide de la méthode de création de polygones. Ceci définit l'instance de maillage pour le cube.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

### Étape 4 : Pointer le nœud vers la géométrie du maillage

Attribuez le maillage créé au nœud du cube.

```java
cubeNode.setEntity(mesh);
```

### Étape 5 : Définir une matrice de traduction personnalisée

Appliquez une matrice de traduction personnalisée au nœud de cube. Cet exemple définit une matrice de transformation pour la traduction.

```java
cubeNode.getTransform().setTransformMatrix(new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
));
```

### Étape 6 : ajouter un cube à la scène

Incluez le nœud cube dans le nœud racine de la scène.

```java
scene.getRootNode().addChildNode(cubeNode);
```

### Étape 7 : Enregistrer la scène 3D

Spécifiez le répertoire et le nom de fichier pour enregistrer la scène 3D dans les formats de fichiers pris en charge, tels que FBX.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Conclusion

Toutes nos félicitations! Vous avez appris avec succès comment transformer des nœuds 3D à l'aide d'Aspose.3D en Java. Expérimentez avec différentes matrices et explorez les possibilités infinies des graphiques 3D.

## FAQ

### Q1 : Puis-je appliquer plusieurs transformations à un seul nœud 3D ?

A1 : Oui, vous pouvez concaténer plusieurs matrices de transformation pour des transformations complexes.

### Q2 : Comment puis-je faire pivoter un objet 3D dans Aspose.3D ?

A2 : Utilisez la matrice de rotation appropriée dans la matrice de transformation pour la rotation souhaitée.

### Q3 : Y a-t-il une limite à la taille des scènes 3D que je peux créer ?

A3 : La taille de vos scènes 3D peut être limitée par les ressources système, mais Aspose.3D est conçu pour être efficace.

### Q4 : Où puis-je trouver des exemples et de la documentation supplémentaires ?

 A4 : Visitez le[Documentation Aspose.3D](https://reference.aspose.com/3d/java/) pour plus d'exemples et de détails.

### Q5 : Comment puis-je obtenir une licence temporaire pour Aspose.3D ?

 A5 : Vous pouvez obtenir une licence temporaire[ici](https://purchase.aspose.com/temporary-license/).