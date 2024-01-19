---
title: Création de cylindres avec fond cisaillé dans Aspose.3D pour Java
linktitle: Création de cylindres avec fond cisaillé dans Aspose.3D pour Java
second_title: API Java Aspose.3D
description: Apprenez à créer des cylindres personnalisés avec des fonds cisaillés à l'aide d'Aspose.3D pour Java. Améliorez vos compétences en modélisation 3D avec ce guide étape par étape.
type: docs
weight: 12
url: /fr/java/cylinders/creating-cylinders-with-sheared-bottom/
---
## Introduction

Bienvenue dans ce guide étape par étape sur la création de cylindres à fond cisaillé à l'aide d'Aspose.3D pour Java. Aspose.3D est une puissante bibliothèque Java qui vous permet de travailler avec des fichiers 3D sans effort. Dans ce didacticiel, nous allons plonger dans la création de cylindres personnalisés avec des fonds cisaillés, vous offrant ainsi une expérience pratique de l'utilisation d'Aspose.3D pour améliorer vos compétences en modélisation 3D.

## Conditions préalables

Avant de commencer, assurez-vous que les conditions préalables suivantes sont remplies :
- Kit de développement Java (JDK) installé sur votre système.
-  Bibliothèque Aspose.3D pour Java téléchargée et ajoutée à votre projet. Vous pouvez trouver le lien de téléchargement[ici](https://releases.aspose.com/3d/java/).

## Importer des packages

Pour commencer, importez les packages nécessaires pour travailler avec Aspose.3D dans votre application Java :
```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Étape 1 : Créer une scène

Commencez par créer une scène 3D dans laquelle vous ajouterez et manipulerez vos cylindres :
```java
// ExDébut : 3
// Créer une scène
Scene scene = new Scene();
// ExFin : 3
```

## Étape 2 : Créer le cylindre 1

Créons maintenant le premier cylindre avec un fond cisaillé :
```java
// ExDébut : 4
// Créer le cylindre 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Fond de cisaillement personnalisé pour cylindre 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Cisaillement de 47,5 degrés dans le plan xy (axe z)
// Ajouter le cylindre 1 à la scène
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExFin : 4
```

## Étape 3 : Créer le cylindre 2

Ajoutons ensuite un deuxième cylindre sans fond cisaillé à la scène :
```java
// ExDébut : 5
// Créer le cylindre 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Ajouter le cylindre 2 sans ShearBottom à la scène
scene.getRootNode().createChildNode(cylinder2);
// ExFin : 5
```

## Étape 4 : Enregistrez la scène

Enregistrez la scène avec les cylindres personnalisés dans votre répertoire de documents :
```java
// ExDébut : 6
// Enregistrer la scène
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExFin : 6
```

Toutes nos félicitations! Vous avez créé avec succès des cylindres avec des fonds cisaillés à l'aide d'Aspose.3D pour Java.

## Conclusion

Dans ce didacticiel, nous avons exploré comment exploiter Aspose.3D pour Java pour améliorer vos projets de modélisation 3D. La création de cylindres personnalisés avec des fonds cisaillés ajoute une touche unique à vos conceptions et Aspose.3D simplifie le processus.

## FAQ

### Q1 : Puis-je utiliser Aspose.3D pour Java avec d’autres bibliothèques Java 3D ?

A1 : Aspose.3D pour Java est conçu pour fonctionner de manière indépendante. Bien que vous puissiez l'intégrer à d'autres bibliothèques, il est suffisamment puissant pour gérer seul la plupart des tâches de modélisation 3D.

### Q2 : Aspose.3D est-il adapté aux débutants en modélisation 3D ?

A2 : Oui, Aspose.3D fournit une API conviviale, ce qui la rend adaptée aussi bien aux développeurs débutants qu'expérimentés en modélisation 3D.

### Q3 : Où puis-je trouver une assistance supplémentaire pour Aspose.3D pour Java ?

 A3 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le soutien et les discussions de la communauté.

### Q4 : Comment puis-je obtenir une licence temporaire pour Aspose.3D ?

 A4 : Vous pouvez obtenir une licence temporaire[ici](https://purchase.aspose.com/temporary-license/).

### Q5 : Puis-je acheter Aspose.3D pour Java ?

 A5 : Oui, vous pouvez acheter Aspose.3D pour Java[ici](https://purchase.aspose.com/buy).