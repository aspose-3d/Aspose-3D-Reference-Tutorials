---
title: Application de torsion dans l'extrusion linéaire avec Aspose.3D pour Java
linktitle: Application de torsion dans l'extrusion linéaire avec Aspose.3D pour Java
second_title: API Java Aspose.3D
description: Apprenez à ajouter une touche à vos modèles 3D à l'aide d'Aspose.3D pour Java. Suivez notre guide étape par étape pour des effets d'extrusion linéaire améliorés.
type: docs
weight: 14
url: /fr/java/linear-extrusion/applying-twist/
---
## Introduction

Bienvenue dans ce didacticiel étape par étape sur l'application d'une torsion dans l'extrusion linéaire à l'aide d'Aspose.3D pour Java. Aspose.3D est une puissante bibliothèque Java qui permet aux développeurs de travailler avec des formats de fichiers 3D, offrant des fonctionnalités robustes pour créer, manipuler et restituer des scènes 3D. Dans ce didacticiel, nous explorerons comment appliquer un effet de torsion lors du processus d'extrusion linéaire pour améliorer vos modèles 3D.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous que les conditions préalables suivantes sont remplies :

- Environnement de développement Java : assurez-vous que Java est installé sur votre système.
-  Bibliothèque Aspose.3D : téléchargez et installez la bibliothèque Aspose.3D pour Java à partir du[lien de téléchargement](https://releases.aspose.com/3d/java/).
-  Documentation : reportez-vous au[Documentation Aspose.3D](https://reference.aspose.com/3d/java/) pour des conseils complets.

## Importer des packages

Avant de commencer le processus de codage, importez les packages nécessaires dans votre projet Java. Voici un exemple de la façon de procéder :

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Étape 1 : Définir le répertoire des documents

Commencez par définir le répertoire de documents dans lequel votre scène 3D sera enregistrée.

```java
// ExStart : SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd : SetDocumentDirectory
```

## Étape 2 : initialiser le profil de base

Initialisez le profil de base à extruder. Dans cet exemple, nous utilisons une forme rectangulaire avec un rayon d'arrondi.

```java
// ExStart : Initialiser le profil de base
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd : Initialiser le profil de base
```

## Étape 3 : Créer une scène

Créez une scène 3D pour héberger les nœuds extrudés.

```java
// ExStart : Créer une scène
Scene scene = new Scene();
// ExEnd : Créer une scène
```

## Étape 4 : Créer des nœuds

Créez des nœuds gauche et droit dans la scène. Ajustez la translation du nœud gauche.

```java
// ExStart : Créer des nœuds
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd : Créer des nœuds
```

## Étape 5 : Effectuer une extrusion linéaire avec Twist

Effectuez une extrusion linéaire sur les nœuds gauche et droit, en appliquant les propriétés de torsion et de tranches.

```java
// ExStart :ExtrusionLinéaireAvecTorsion
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd :ExtrusionLinéaireAvecTorsion
```

## Étape 6 : Enregistrer la scène 3D

Enregistrez la scène 3D au format de fichier Wavefront OBJ.

```java
// ExDémarrer : Enregistrer la scène 3DS
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
//ExEnd : Save3DScene
```

## Conclusion

Toutes nos félicitations! Vous avez appliqué avec succès une torsion dans une extrusion linéaire à l'aide d'Aspose.3D pour Java. Ce didacticiel fournit un guide détaillé, étape par étape, pour vous aider à améliorer vos capacités de modélisation 3D.

## FAQ

### Q1 : Puis-je utiliser Aspose.3D pour Java pour travailler avec d’autres formats de fichiers 3D ?

A1 : Oui, Aspose.3D prend en charge différents formats de fichiers 3D, vous permettant d'importer, d'exporter et de manipuler divers types de fichiers.

### Q2 : Où puis-je trouver du support pour Aspose.3D pour Java ?

 A2 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le soutien et les discussions de la communauté.

### Q3 : Existe-t-il un essai gratuit disponible pour Aspose.3D pour Java ?

 A3 : Oui, vous pouvez accéder à la version d'essai gratuite à partir de[ici](https://releases.aspose.com/).

### Q4 : Comment puis-je obtenir une licence temporaire pour Aspose.3D pour Java ?

 A4 : Obtenez une licence temporaire auprès du[page de licence temporaire](https://purchase.aspose.com/temporary-license/).

### Q5 : Où puis-je acheter Aspose.3D pour Java ?

 A5 : Achetez Aspose.3D pour Java sur le site[page d'achat](https://purchase.aspose.com/buy).