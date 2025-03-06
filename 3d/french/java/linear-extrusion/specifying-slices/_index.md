---
title: Spécification de tranches dans l'extrusion linéaire avec Aspose.3D pour Java
linktitle: Spécification de tranches dans l'extrusion linéaire avec Aspose.3D pour Java
second_title: API Java Aspose.3D
description: Apprenez à spécifier des tranches en extrusion linéaire à l'aide d'Aspose.3D pour Java. Améliorez vos compétences en modélisation 3D avec ce guide étape par étape.
weight: 13
url: /fr/java/linear-extrusion/specifying-slices/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Spécification de tranches dans l'extrusion linéaire avec Aspose.3D pour Java

## Introduction

La création de modèles 3D complexes nécessite souvent plus que de la simple créativité ; cela nécessite une compréhension approfondie des outils à votre disposition. Aspose.3D pour Java change la donne à cet égard. Dans ce didacticiel, nous nous concentrerons sur un aspect spécifique : la spécification des tranches en extrusion linéaire.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous que les conditions préalables suivantes sont remplies :

1. Environnement Java : assurez-vous qu'un environnement de développement Java est configuré sur votre système.
2.  Aspose.3D pour Java : téléchargez et installez la bibliothèque Aspose.3D. Vous pouvez trouver les packages nécessaires[ici](https://releases.aspose.com/3d/java/).

## Importer des packages

Dans votre projet Java, importez la bibliothèque Aspose.3D. Ceci est crucial pour accéder aux fonctionnalités avec lesquelles nous allons travailler. Ajoutez l'instruction d'importation suivante à votre code :

```java
import com.aspose.threed.*;

import java.io.IOException;
```

Maintenant, décomposons l'exemple en plusieurs étapes.

## Étape 1 : configurer la scène

Initialisez le profil de base à extruder, dans ce cas, un`RectangleShape` avec un rayon d'arrondi spécifié. Créez une scène 3D dans laquelle travailler.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

## Étape 2 : Créer des nœuds

Générez des nœuds gauche et droit dans la scène. Ajustez la translation du nœud gauche pour la variation spatiale.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Étape 3 : Extrusion linéaire avec des tranches

Effectuez une extrusion linéaire sur les deux nœuds, en spécifiant le nombre de tranches pour chacun. C'est là que la magie opère.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

## Étape 4 : Enregistrez la scène

Enregistrez la scène 3D au format souhaité, dans ce cas, un fichier Wavefront OBJ.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusion

Toutes nos félicitations! Vous avez appris avec succès comment spécifier des tranches dans une extrusion linéaire à l'aide d'Aspose.3D pour Java. Cette compétence ouvre de nouvelles possibilités dans votre parcours de modélisation 3D.

## FAQ

### Q1 : Comment puis-je télécharger Aspose.3D pour Java ?

 A1 : Vous pouvez télécharger la bibliothèque[ici](https://releases.aspose.com/3d/java/).

### Q2 : Où puis-je trouver la documentation d'Aspose.3D ?

 A2 : Se référer à la documentation[ici](https://reference.aspose.com/3d/java/).

### Q3 : Existe-t-il un essai gratuit disponible ?

 A3 : Oui, vous pouvez explorer un essai gratuit[ici](https://releases.aspose.com/).

### Q4 : Comment puis-je obtenir de l'aide pour Aspose.3D ?

 A4 : Visitez le forum d'assistance[ici](https://forum.aspose.com/c/3d/18).

### Q5 : Puis-je acheter une licence temporaire ?

 A5 : Oui, une licence temporaire peut être obtenue[ici](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
