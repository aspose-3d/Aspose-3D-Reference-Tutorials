---
title: Définition de la direction dans l'extrusion linéaire avec Aspose.3D pour Java
linktitle: Définition de la direction dans l'extrusion linéaire avec Aspose.3D pour Java
second_title: API Java Aspose.3D
description: Maîtrisez l'extrusion linéaire avec Aspose.3D pour Java ! Suivez notre guide pour une programmation 3D fluide. Téléchargez maintenant pour une expérience captivante.
type: docs
weight: 12
url: /fr/java/linear-extrusion/setting-direction/
---
## Introduction

Bienvenue dans notre guide étape par étape sur la définition de la direction dans l'extrusion linéaire à l'aide d'Aspose.3D pour Java. Aspose.3D est une puissante bibliothèque Java qui permet aux développeurs de travailler de manière transparente avec des fichiers et des scènes 3D. Dans ce didacticiel, nous nous concentrerons sur la tâche spécifique consistant à définir la direction de l'extrusion linéaire, améliorant ainsi vos compétences en programmation 3D.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous que les conditions préalables suivantes sont remplies :

- Connaissance de base du langage de programmation Java.
-  Bibliothèque Aspose.3D installée. Vous pouvez le télécharger depuis[ici](https://releases.aspose.com/3d/java/).
- Un environnement de développement intégré (IDE) pour Java, tel qu'Eclipse ou IntelliJ.

## Importer des packages

Assurez-vous d'importer les packages nécessaires pour démarrer votre projet :

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Étape 1 : initialiser le profil de base

 Commencez par initialiser le profil de base à extruder. Dans cet exemple, nous utilisons un`RectangleShape` avec un rayon d'arrondi de 0,3 :

```java
// Le chemin d'accès au répertoire des documents.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Étape 2 : Créer une scène

Créez ensuite une scène 3D pour contenir les objets extrudés :

```java
Scene scene = new Scene();
```

## Étape 3 : Créer des nœuds

Créez des nœuds gauche et droit dans la scène :

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Étape 4 : effectuer une extrusion linéaire sur le nœud gauche

 Effectuez une extrusion linéaire sur le nœud gauche à l'aide de la touche`LinearExtrusion`classe avec des paramètres spécifiés tels que twist et slices :

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Étape 5 : Effectuer une extrusion linéaire sur le nœud droit avec direction

 Effectuez une extrusion linéaire sur le nœud droit, en introduisant le`setDirection` propriété pour définir la direction de l'extrusion :

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Étape 6 : Enregistrer la scène 3D

Enregistrez la scène 3D au format de fichier souhaité. Dans cet exemple, nous l'enregistrons sous forme de fichier Wavefront OBJ :

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusion

Toutes nos félicitations! Vous avez appris avec succès comment définir la direction d'une extrusion linéaire à l'aide d'Aspose.3D pour Java. Ce tutoriel améliore vos compétences en programmation 3D et ouvre de nouvelles possibilités pour des projets créatifs.

## FAQ

### Q1 : Puis-je utiliser Aspose.3D avec d’autres langages de programmation ?

A1 : Aspose.3D prend en charge divers langages de programmation, notamment .NET et Java.

### Q2. Existe-t-il un essai gratuit disponible pour Aspose.3D ?

 A2 : Oui, vous pouvez explorer les fonctionnalités d'Aspose.3D avec un essai gratuit[ici](https://releases.aspose.com/).

### Q3 : Où puis-je trouver une documentation détaillée pour Aspose.3D pour Java ?

 A3 : La documentation complète est disponible[ici](https://reference.aspose.com/3d/java/).

### Q4 : Comment puis-je obtenir de l'aide pour Aspose.3D ?

 A4 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour toute aide ou question.

### Q5 : Des licences temporaires sont-elles disponibles pour Aspose.3D ?

 A5 : Oui, vous pouvez obtenir une licence temporaire[ici](https://purchase.aspose.com/temporary-license/).