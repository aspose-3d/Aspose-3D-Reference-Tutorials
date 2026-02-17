---
date: 2026-02-07
description: Apprenez à créer des modèles de cylindre avec des sommets décalés dans
  Aspose.3D pour Java, ajoutez des étapes de nœud enfant en Java et exportez facilement
  des fichiers OBJ de modèles 3D.
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Comment créer un cylindre avec un haut décalé dans Aspose.3D pour Java
url: /fr/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment créer un cylindre avec un sommet décalé dans Aspose.3D pour Java

## Introduction

Si vous cherchez à **comment créer un cylindre** avec un sommet décalé personnalisé dans une scène 3D basée sur Java, Aspose.3D rend le processus simple. Dans ce tutoriel, nous parcourrons chaque étape — de la configuration de la scène à l’exportation du modèle final au format OBJ— afin que vous puissiez intégrer des cylindres à sommet décalé dans vos applications en toute confiance. À la fin du guide, vous maîtriserez la création de formes cylindriques avec des décalages personnalisés en quelques lignes de code seulement.

## Réponses rapides
- **Quelle bibliothèque est utilisée ?** Aspose.3D for Java  
- **Puis-je décaler le sommet d'un cylindre ?** Oui, en utilisant `setOffsetTop`  
- **Comment ajouter un nœud enfant en Java ?** Appelez `createChildNode` sur le nœud racine  
- **Quel format puis-je exporter ?** Wavefront OBJ (`export 3d model obj`)  
- **Ai-je besoin d'une licence pour les tests ?** Une licence temporaire est disponible pour l'évaluation  

## Qu’est‑ce que « comment créer un cylindre » avec un sommet décalé ?

Créer un cylindre avec un sommet décalé signifie que la face circulaire supérieure est déplacée par rapport à la base, vous permettant de modéliser des formes coniques ou asymétriques sans manipulation manuelle des sommets. Aspose.3D fournit un constructeur dédié et une propriété `OffsetTop` pour y parvenir en quelques lignes de code seulement.

## Pourquoi utiliser Aspose.3D pour Java ?

- **API de haut niveau :** Pas besoin de gérer les données de maillage de bas niveau.  
- **Cross‑platform :** Fonctionne sur tout environnement compatible JVM.  
- **Exportateurs intégrés :** Enregistrement direct en OBJ, STL, FBX, etc.  
- **Extensible :** Ajoutez facilement des nœuds enfants, appliquez des transformations et intégrez d’autres bibliothèques Java.  

## Prérequis

- **Java Development Kit (JDK)** – une version compatible installée.  
- **Aspose.3D for Java library** – téléchargez le dernier JAR depuis le site officiel [here](https://releases.aspose.com/3d/java/).  
- Un IDE de votre choix (Eclipse, IntelliJ IDEA, NetBeans, etc.).

## Importer les packages

Tout d’abord, importez les classes dont nous aurons besoin. Placez ces instructions en haut de votre fichier Java :

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Guide étape par étape

### Étape 1 : Créer une scène

Une scène agit comme le conteneur pour tous les objets 3D.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Étape 2 : Initialiser le cylindre avec un sommet décalé

Ici nous répondons à **comment créer un cylindre** avec un décalage personnalisé. Le constructeur définit le rayon, la hauteur, les tranches, les piles, et si le cylindre est fermé. Ensuite, nous décalons le sommet à l'aide de `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Étape 3 : Comment **add child node Java** – Attacher le premier cylindre

Nous créons un nœud enfant sous le nœud racine de la scène et déplaçons le cylindre à l'emplacement souhaité.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Étape 4 : Initialiser un deuxième cylindre (sans décalage)

À titre de comparaison, nous ajoutons un cylindre standard sans décalage.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Étape 5 : Comment **add child node Java** – Attacher le deuxième cylindre

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Étape 6 : Comment **export OBJ** – Enregistrer la scène au format OBJ

Enfin, nous exportons toute la scène (les deux cylindres) en tant que fichier Wavefront OBJ, largement pris en charge par les outils 3D.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Lorsque vous exécutez le programme, vous trouverez `CustomizedOffsetTopCylinder.obj` dans le répertoire spécifié, prêt à être ouvert dans Blender, Maya ou tout autre visualiseur compatible OBJ.

## Pourquoi cela importe – Cas d’utilisation réels

- **Visualisation architecturale :** Les cylindres à sommet décalé sont parfaits pour modéliser des colonnes qui s’effilent vers le plafond.  
- **Pièces mécaniques :** Créez des pistons ou des carters d’engrenages où la surface supérieure est intentionnellement décalée.  
- **Assets de jeu :** Générez rapidement des formes de piliers variées sans créer manuellement les maillages.  

## Comment exporter OBJ – Enregistrer la scène au format OBJ

La capacité d’exportation OBJ d’Aspose 3D vous permet de partager vos modèles avec pratiquement n’importe quel pipeline 3D. En utilisant la méthode `scene.save(..., FileFormat.WAVEFRONTOBJ)`, vous **comment exporter obj** des fichiers directement depuis Java, éliminant le besoin de convertisseurs tiers.

## Comment ajouter un nœud enfant Java – Attacher la géométrie

L’ajout de nœuds enfants est la méthode standard pour organiser un graphe de scène. Chaque appel à `createChildNode` renvoie un nœud qui peut être transformé indépendamment, ce qui explique pourquoi le modèle **add child node java** apparaît deux fois dans ce tutoriel.

## Exporter le modèle 3D OBJ – Utiliser l’export OBJ d’Aspose 3D

Si vous devez distribuer vos modèles aux designers, la fonctionnalité **export 3d model obj** fournit une représentation légère, basée sur du texte, qui fonctionne avec toutes les principales applications 3D. Le même appel API utilisé à l’Étape 6 illustre le flux de travail **aspose 3d export obj**.

## Problèmes courants et solutions

| Problème | Raison | Solution |
|----------|--------|----------|
| **Le fichier OBJ est vide** | Scène non enregistrée correctement ou chemin incorrect. | Vérifiez que le répertoire de sortie existe et que vous avez les permissions d’écriture. |
| **Décalage non appliqué** | Utilisation d’une version plus ancienne d’Aspose.3D. | Mettez à jour vers la dernière bibliothèque où `setOffsetTop` est pris en charge. |
| **Nœud enfant non visible** | Transformation non appliquée. | Assurez‑vous d’appeler `getTransform().setTranslation` après la création du nœud enfant. |

## Foire aux questions

**Q : Aspose.3D est‑il compatible avec différents IDE Java ?**  
R : Oui, il fonctionne parfaitement avec Eclipse, IntelliJ IDEA, NetBeans et d’autres IDE.

**Q : Puis‑je appliquer des textures aux objets 3D créés ?**  
R : Absolument ! Utilisez la classe `Material` pour assigner des textures et des propriétés de surface.

**Q : Existe‑t‑il des options de licence pour Aspose.3D ?**  
R : Divers modèles de licence sont disponibles ; vous pouvez les explorer [ici](https://purchase.aspose.com/buy).

**Q : Comment puis‑je obtenir de l’aide ou partager des expériences ?**  
R : Rejoignez le forum communautaire Aspose.3D [ici](https://forum.aspose.com/c/3d/18) pour le support et les discussions.

**Q : Une licence temporaire est‑elle disponible pour les tests ?**  
R : Oui, une licence temporaire peut être obtenue pour l’évaluation [ici](https://purchase.aspose.com/temporary-license/).

---

**Dernière mise à jour :** 2026-02-07  
**Testé avec :** Aspose.3D for Java 24.12 (latest)  
**Auteur :** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}