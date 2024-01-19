---
title: Centre de contrôle en extrusion linéaire avec Aspose.3D pour Java
linktitle: Centre de contrôle en extrusion linéaire avec Aspose.3D pour Java
second_title: API Java Aspose.3D
description: Explorez le monde des graphiques 3D en Java avec Aspose.3D. Contrôlez le centre en extrusion linéaire sans effort.
type: docs
weight: 11
url: /fr/java/linear-extrusion/controlling-center/
---
## Introduction

Dans le monde du graphisme 3D et de la programmation Java, le contrôle du centre en extrusion linéaire joue un rôle crucial pour obtenir les effets souhaités dans vos projets. Aspose.3D pour Java fournit une boîte à outils puissante pour gérer ces tâches de manière transparente. Dans ce didacticiel, nous allons plonger dans le processus de contrôle du centre en extrusion linéaire à l'aide d'Aspose.3D pour Java, en décomposant chaque étape pour garantir une compréhension fluide et complète.

## Conditions préalables

Avant de nous lancer dans ce didacticiel, assurez-vous d'avoir les conditions préalables suivantes en place :

1. Environnement de développement Java : assurez-vous qu'un environnement de développement Java est configuré sur votre ordinateur.

2.  Aspose.3D pour Java : téléchargez et installez la bibliothèque Aspose.3D. Vous pouvez retrouver la bibliothèque et sa documentation[ici](https://reference.aspose.com/3d/java/).

3. Répertoire de documents : créez un répertoire pour stocker vos documents Java. Appelons-le « Votre répertoire de documents ».

## Importer des packages

Dans votre environnement de développement Java, importez les packages nécessaires pour Aspose.3D. Cela garantit que votre code a accès aux fonctionnalités fournies par la bibliothèque.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Étape 1 : configurer le profil de base

Initialisez le profil de base à extruder. Dans cet exemple, nous utiliserons une forme rectangulaire avec un rayon d'arrondi de 0,3.

```java
// Le chemin d'accès au répertoire des documents.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Étape 2 : Créer une scène 3D

Construisez les bases de votre monde 3D en créant une scène.

```java
Scene scene = new Scene();
```

## Étape 3 : Créer des nœuds gauche et droit

Établissez des nœuds gauche et droit dans votre scène. Ces nœuds servent de canevas pour vos objets 3D.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Étape 4 : Extrusion linéaire avec la propriété Centre

Effectuez une extrusion linéaire sur le nœud gauche sans centrage et définissez le nombre de tranches sur 3.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Étape 5 : Définir le plan de sol pour référence

Améliorez la représentation visuelle en ajoutant un plan de sol au nœud gauche.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Étape 6 : Extrusion linéaire avec la propriété Centre (nœud droit)

Effectuez une extrusion linéaire sur le nœud droit, en centrant cette fois l'extrusion, puis définissez à nouveau le nombre de tranches sur 3.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Étape 7 : Définir le plan de sol pour référence (nœud droit)

Semblable au nœud gauche, ajoutez un plan de sol au nœud droit pour référence.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Étape 8 : Enregistrez la scène 3D

Enregistrez votre scène 3D au format Wavefront OBJ.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusion

Le contrôle du centre en extrusion linéaire avec Aspose.3D pour Java ouvre des possibilités passionnantes dans le développement graphique 3D. En suivant ce guide étape par étape, vous avez appris à manipuler la propriété center, vous permettant ainsi d'obtenir les effets visuels souhaités dans vos projets Java.

## FAQ

### Q1 : Puis-je utiliser Aspose.3D pour Java dans des projets commerciaux ?

 R1 : Oui, Aspose.3D pour Java est disponible pour un usage commercial. Pour plus de détails sur les licences, visitez[ici](https://purchase.aspose.com/buy).

### Q2 : Existe-t-il un essai gratuit ?

 A2 : Oui, vous pouvez explorer un essai gratuit d'Aspose.3D pour Java[ici](https://releases.aspose.com/).

### Q3 : Où puis-je trouver du support pour Aspose.3D pour Java ?

 A3 : Le forum communautaire Aspose.3D est un endroit idéal pour rechercher de l'aide et partager vos expériences. Visitez le forum[ici](https://forum.aspose.com/c/3d/18).

### Q4 : Ai-je besoin d’une licence temporaire pour tester ?

A4 : Oui, si vous avez besoin d'une licence temporaire à des fins de test, vous pouvez en obtenir une.[ici](https://purchase.aspose.com/temporary-license/).

### Q5 : Où puis-je trouver la documentation ?

 A5 : La documentation d'Aspose.3D pour Java est disponible[ici](https://reference.aspose.com/3d/java/).