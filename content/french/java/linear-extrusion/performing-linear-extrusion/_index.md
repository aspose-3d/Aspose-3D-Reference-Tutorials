---
title: Exécution d'une extrusion linéaire dans Aspose.3D pour Java
linktitle: Exécution d'une extrusion linéaire dans Aspose.3D pour Java
second_title: API Java Aspose.3D
description: Explorez le monde de la modélisation 3D avec Aspose.3D pour Java. Apprenez à réaliser une extrusion linéaire sans effort.
type: docs
weight: 10
url: /fr/java/linear-extrusion/performing-linear-extrusion/
---
## Introduction

Bienvenue dans ce didacticiel complet sur la réalisation d'une extrusion linéaire dans Aspose.3D pour Java ! Si vous souhaitez améliorer vos compétences en modélisation 3D à l'aide de Java, vous êtes au bon endroit. Dans ce didacticiel, nous vous guiderons tout au long du processus de réalisation d'une extrusion linéaire à l'aide d'Aspose.3D, une puissante bibliothèque Java pour la modélisation 3D.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous que les conditions préalables suivantes sont remplies :

1. Environnement de développement Java : assurez-vous qu'un environnement de développement Java est configuré sur votre ordinateur.

2.  Bibliothèque Aspose.3D : téléchargez et installez la bibliothèque Aspose.3D. Vous pouvez trouver la bibliothèque[ici](https://releases.aspose.com/3d/java/).

## Importer des packages

Une fois que vous avez configuré votre environnement de développement et installé la bibliothèque Aspose.3D, il est temps d'importer les packages nécessaires. Dans votre code Java, incluez les éléments suivants :

```java
import com.aspose.threed.*;
```

Décomposons chaque étape pour assurer une compréhension claire.

## Étape 1 : Définir le répertoire des documents

Définissez le chemin d'accès à votre répertoire de documents :

```java
String MyDir = "Your Document Directory";
```

Cela garantit que le modèle 3D généré sera enregistré dans le répertoire spécifié.

## Étape 2 : initialiser la forme de base

Créez une forme de rectangle comme profil de base pour l'extrusion :

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Ajustez le rayon d'arrondi selon vos besoins pour personnaliser la forme.

## Étape 3 : Effectuer une extrusion linéaire

Effectuez une extrusion linéaire sur le profil de base :

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

Ici, nous extrudons la forme par 10 unités, définissons le nombre de tranches, activons le centrage et appliquons une torsion et un décalage de torsion.

## Étape 4 : Créer une scène 3D

Créez une scène 3D et ajoutez l'extrusion en tant que nœud enfant :

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## Étape 5 : Enregistrer la scène 3D

Enregistrez la scène 3D générée en tant que fichier Wavefront OBJ :

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Vous avez désormais réalisé avec succès une extrusion linéaire à l’aide d’Aspose.3D pour Java !

## Conclusion

Toutes nos félicitations! Vous avez appris à exploiter Aspose.3D pour Java pour effectuer une extrusion linéaire. Cette puissante bibliothèque ouvre un monde de possibilités pour vos projets de modélisation 3D.

## FAQ

### Q1 : Aspose.3D est-il compatible avec toutes les versions de Java ?

A1 : Aspose.3D est conçu pour fonctionner avec Java 1.6 et les versions ultérieures.

### Q2 : Puis-je utiliser Aspose.3D pour des projets commerciaux ?

A2 : Oui, Aspose.3D peut être utilisé pour des projets personnels et commerciaux. Vérifiez les détails de la licence[ici](https://purchase.aspose.com/buy).

### Q3 : Comment puis-je obtenir de l'aide pour Aspose.3D ?

 A3 : Visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le soutien de la communauté ou envisagez d'acheter un[permis temporaire](https://purchase.aspose.com/temporary-license/) pour un support premium.

### Q4 : Existe-t-il d'autres fonctionnalités de modélisation 3D dans Aspose.3D ?

 A4 : Absolument ! Explorez la documentation complète[ici](https://reference.aspose.com/3d/java/) pour une liste complète de fonctionnalités et d’exemples.

### Q5 : Existe-t-il un essai gratuit disponible pour Aspose.3D ?

 A5 : Oui, vous pouvez accéder à un essai gratuit[ici](https://releases.aspose.com/).