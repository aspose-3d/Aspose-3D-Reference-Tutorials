---
title: Utilisation du décalage de torsion dans l'extrusion linéaire avec Aspose.3D pour Java
linktitle: Utilisation du décalage de torsion dans l'extrusion linéaire avec Aspose.3D pour Java
second_title: API Java Aspose.3D
description: Améliorez vos compétences en modélisation 3D avec Aspose.3D pour Java. Apprenez à utiliser le décalage de torsion dans l'extrusion linéaire dans ce didacticiel complet.

weight: 15
url: /fr/java/linear-extrusion/using-twist-offset/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utilisation du décalage de torsion dans l'extrusion linéaire avec Aspose.3D pour Java

## Introduction

Dans le monde dynamique du graphisme 3D, maîtriser l’art de l’extrusion linéaire change la donne. Avec Aspose.3D pour Java, vous pouvez améliorer vos compétences en modélisation 3D en incorporant la fonction Twist Offset dans votre processus d'extrusion linéaire. Ce didacticiel vous guidera à travers les étapes d'utilisation du Twist Offset dans l'extrusion linéaire à l'aide d'Aspose.3D pour Java, vous fournissant les outils nécessaires pour créer de superbes scènes 3D.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous que les conditions préalables suivantes sont remplies :

- Environnement Java : assurez-vous d'avoir configuré un environnement de développement Java sur votre système.
-  Aspose.3D pour Java : téléchargez et installez la bibliothèque Aspose.3D à partir du[lien de téléchargement](https://releases.aspose.com/3d/java/).
-  Documentation : Familiarisez-vous avec le[Documentation Aspose.3D pour Java](https://reference.aspose.com/3d/java/).

## Importer des packages

Dans votre projet Java, importez les packages nécessaires pour commencer à utiliser Aspose.3D pour Java. Assurez-vous d’inclure les bibliothèques requises pour une intégration transparente.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Étape 1 : configurer l'environnement

Commencez par configurer votre environnement de développement Java et assurez-vous qu'Aspose.3D for Java est correctement installé.

## Étape 2 : initialiser le profil de base

Créez un profil de base pour l'extrusion, dans ce cas, un RectangleShape avec un rayon d'arrondi de 0,3.

```java
// Le chemin d'accès au répertoire des documents.
String MyDir = "Your Document Directory";
// Initialiser le profil de base à extruder
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Étape 3 : Créer une scène 3D

Créez une scène 3D pour héberger vos objets extrudés.

```java
// Créer une scène
Scene scene = new Scene();
```

## Étape 4 : Créer des nœuds

Générez des nœuds dans la scène pour représenter différentes entités.

```java
// Créer le nœud gauche
Node left = scene.getRootNode().createChildNode();
// Créer le bon nœud
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Étape 5 : Effectuer une extrusion linéaire

Utilisez l'extrusion linéaire sur les nœuds gauche et droit avec diverses propriétés.

```java
// Effectuer une extrusion linéaire sur le nœud gauche à l'aide des propriétés twist et slices
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Effectuer une extrusion linéaire sur le nœud droit à l'aide des propriétés twist, twist offset et slices
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Étape 6 : Enregistrez la scène 3D

Enregistrez votre scène 3D nouvellement créée avec le format de fichier spécifié.

```java
// Enregistrer la scène 3D
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusion

Toutes nos félicitations! Vous avez implémenté avec succès le décalage de torsion dans l'extrusion linéaire à l'aide d'Aspose.3D pour Java. Cette fonctionnalité puissante ouvre un monde de possibilités pour vos projets de modélisation 3D, vous permettant de créer des scènes complexes et captivantes.

## FAQ

### Q1 : Puis-je utiliser Aspose.3D pour Java dans des projets non commerciaux ?

 A1 : Oui, Aspose.3D pour Java peut être utilisé dans des projets commerciaux et non commerciaux. Vérifier la[options de licence](https://purchase.aspose.com/buy) pour plus de détails.

### Q2 : Où puis-je trouver du support pour Aspose.3D pour Java ?

 A2 : Visitez le[Forum Aspose.3D pour Java](https://forum.aspose.com/c/3d/18) pour obtenir de l'aide et entrer en contact avec la communauté.

### Q3 : Existe-t-il un essai gratuit disponible pour Aspose.3D pour Java ?

 A3 : Oui, vous pouvez explorer une version d'essai gratuite à partir du[page des versions](https://releases.aspose.com/).

### Q4 : Comment puis-je obtenir une licence temporaire pour Aspose.3D pour Java ?

 A4 : Obtenez une licence temporaire pour votre projet en visitant[ce lien](https://purchase.aspose.com/temporary-license/).

### Q5 : Existe-t-il des exemples et des didacticiels supplémentaires disponibles ?

 A5 : Oui, reportez-vous au[Documentation](https://reference.aspose.com/3d/java/) pour plus d’exemples et des tutoriels approfondis.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
