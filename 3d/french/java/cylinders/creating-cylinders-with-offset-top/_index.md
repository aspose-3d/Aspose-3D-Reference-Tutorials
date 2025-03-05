---
title: Création de cylindres avec décalage supérieur dans Aspose.3D pour Java
linktitle: Création de cylindres avec décalage supérieur dans Aspose.3D pour Java
second_title: API Java Aspose.3D
description: Explorez les merveilles de la modélisation 3D en Java avec Aspose.3D. Apprenez à créer sans effort des cylindres captivants avec des sommets décalés.
type: docs
weight: 11
url: /fr/java/cylinders/creating-cylinders-with-offset-top/
---
## Introduction

Dans le domaine de la modélisation 3D basée sur Java, Aspose.3D se distingue comme un outil puissant, offrant aux développeurs la possibilité de créer facilement des scènes 3D complexes. Dans ce didacticiel, nous plongerons dans le monde fascinant d'Aspose.3D pour Java, en nous concentrant sur une tâche spécifique : créer des cylindres avec des sommets décalés. À la fin de ce guide, vous maîtriserez parfaitement le processus, vous permettant d'intégrer cette fonctionnalité de manière transparente dans vos projets 3D.

## Conditions préalables

Avant de nous lancer dans ce voyage créatif, assurez-vous d’avoir les conditions préalables suivantes en place :

- Kit de développement Java (JDK) : Aspose.3D pour Java nécessite un JDK compatible installé sur votre machine.
-  Bibliothèque Aspose.3D : Téléchargez et intégrez la bibliothèque Aspose.3D dans votre projet Java. Vous pouvez trouver la bibliothèque et la documentation détaillée[ici](https://releases.aspose.com/3d/java/).

## Importer des packages

Commençons le processus en important les packages nécessaires à notre projet Java. Dans votre code, incluez les éléments suivants :

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Étape 1 : Créer une scène

Commencez par initialiser une scène dans laquelle vous orchestrerez vos éléments 3D.

```java
// ExDébut : 1
// Créer une scène
Scene scene = new Scene();
// ExFin : 1
```

## Étape 2 : Initialiser le cylindre avec le dessus décalé

Créez ensuite un objet cylindre avec un sommet décalé personnalisé à l'aide du code suivant :

```java
// ExDébut : 2
// Initialiser le cylindre
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Définir le décalage supérieur
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExFin : 2
```

## Étape 3 : Créer un nœud enfant

Maintenant, créez un nœud enfant dans la scène et définissez la traduction pour le premier cylindre :

```java
// ExDébut : 3
// Créer un nœud enfant
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExFin : 3
```

## Étape 4 : initialiser le deuxième cylindre

Initialisons un deuxième cylindre sans dessus décalé personnalisé :

```java
// ExDébut : 4
// Initialiser le deuxième cylindre sans OffsetTop personnalisé
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExFin : 4
```

## Étape 5 : Créer un nœud enfant pour le deuxième cylindre

Créez un nœud enfant pour le deuxième cylindre de la scène :

```java
// ExDébut : 5
// Créer un nœud enfant
scene.getRootNode().createChildNode(cylinder2);
// ExFin : 5
```

## Étape 6 : Enregistrez la scène

Enfin, enregistrez la scène avec les cylindres créés sous forme de fichier Wavefront OBJ dans votre répertoire de documents :

```java
// ExDébut : 6
//Sauvegarder
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExFin : 6
```

Avec ces étapes simples, vous avez réussi à créer des cylindres 3D avec des sommets décalés en utilisant Aspose.3D pour Java !

## Conclusion

Aspose.3D pour Java permet aux développeurs de donner vie à leurs visions 3D sans effort. Dans ce didacticiel, nous nous sommes concentrés sur la création de cylindres avec des sommets décalés, mettant en valeur la polyvalence et la simplicité d'Aspose.3D. Désormais, armé de ces connaissances, vous pouvez explorer et intégrer des fonctionnalités plus avancées dans vos projets 3D basés sur Java.

## FAQ

### Q1 : Aspose.3D est-il compatible avec différents IDE Java ?

R1 : Oui, Aspose.3D s'intègre de manière transparente aux environnements de développement intégrés (IDE) Java populaires tels qu'Eclipse, IntelliJ IDEA et NetBeans.

### Q2 : Puis-je appliquer des textures aux objets 3D créés ?

A2 : Absolument ! Aspose.3D offre des fonctionnalités étendues pour appliquer des textures et des matériaux afin d'améliorer l'attrait visuel de vos modèles 3D.

### Q3 : Existe-t-il des options de licence disponibles pour Aspose.3D ?

A3 : Oui, vous pouvez explorer et choisir l'option de licence qui correspond à vos besoins.[ici](https://purchase.aspose.com/buy).

### Q4 : Comment puis-je demander de l'aide ou partager mes expériences avec Aspose.3D ?

 A4 : Rejoignez le forum de la communauté Aspose.3D[ici](https://forum.aspose.com/c/3d/18) pour vous connecter avec d'autres développeurs, demander de l'aide et partager vos idées.

### Q5 : Existe-t-il une option de licence temporaire à des fins de test ?

 A5 : Oui, vous pouvez obtenir une licence temporaire à des fins de tests et d'évaluation[ici](https://purchase.aspose.com/temporary-license/).