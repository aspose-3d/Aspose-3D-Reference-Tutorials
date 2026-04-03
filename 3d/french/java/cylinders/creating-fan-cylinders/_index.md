---
date: 2026-04-03
description: Apprenez à créer une forme d’éventail cylindrique en Java avec Aspose.3D.
  Ce guide couvre la modélisation 3D en Java et les techniques Java pour enregistrer
  un fichier OBJ.
keywords:
- create cylinder fan shape
- save obj file java
- aspose 3d export obj
linktitle: Comment créer une forme d’éventail cylindrique avec Aspose.3D pour Java
second_title: Aspose.3D Java API
title: Comment créer une forme d’éventail cylindrique avec Aspose.3D pour Java
url: /fr/java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment créer une forme d'éventail cylindrique avec Aspose.3D pour Java

## Introduction

Prêt à maîtriser **la création d'une forme d'éventail cylindrique** dans un environnement Java ? Dans ce tutoriel, nous parcourrons chaque étape— de la configuration de la scène à l'exportation d'un fichier Wavefront OBJ— en utilisant Aspose.3D. Que vous créiez un élément de jeu, un prototype CAO ou que vous expérimentiez simplement avec la géométrie 3D, vous verrez à quel point la modélisation 3D Java peut être simple avec cette bibliothèque puissante.

## Réponses rapides
- **Quel est l'objectif principal ?** Créez un cylindre à forme d'éventail personnalisable et enregistrez‑le au format OBJ.  
- **Quelle bibliothèque est utilisée ?** Aspose.3D pour Java.  
- **Ai‑je besoin d'une licence ?** Un essai gratuit suffit pour le développement ; une licence commerciale est requise pour la production.  
- **Quels sont les prérequis ?** JDK installé et le package Aspose.3D Java ajouté à votre projet.  
- **Puis‑je exporter d'autres formats ?** Oui—Aspose.3D prend en charge de nombreux formats ; cet exemple utilise Wavefront OBJ.

## Qu'est‑ce qu'un cylindre éventail ?

Un cylindre éventail est un cylindre à surface partielle où un secteur de la base circulaire est omis, créant une ouverture en forme d'« éventail ». Cette géométrie est utile pour visualiser des tranches, des tableaux de bord ou des pièces mécaniques personnalisées.

## Pourquoi utiliser Aspose.3D pour la modélisation 3D Java ?

Aspose.3D offre une API propre et orientée objet qui abstrait les mathématiques de bas niveau des graphiques 3D. Vous pouvez vous concentrer sur la conception plutôt que sur les particularités des formats de fichiers, et la bibliothèque gère automatiquement les opérations **save obj file java**.

## Prérequis

Avant de commencer, assurez‑vous d'avoir :

- **Java Development Kit (JDK)** – téléchargez‑le [ici](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – obtenez le dernier JAR depuis le [lien de téléchargement](https://releases.aspose.com/3d/java/).  

Ajoutez le JAR Aspose.3D au classpath de votre projet.

## Importer les packages

Commencez par importer les classes nécessaires. Cela vous donne accès à la scène 3D, aux primitives géométriques et aux méthodes utilitaires.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Étape 1 : Créer une scène

Tout d'abord, nous créons une nouvelle instance de `Scene`. Considérez une scène comme le conteneur qui regroupe tous vos objets 3D, lumières et caméras.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Étape 2 : Créer un cylindre éventail (comment créer un cylindre)

Nous construisons maintenant le cylindre éventail lui‑même. Les paramètres du constructeur définissent le rayon, la hauteur, la tessellation et si la géométrie est générée sous forme d'éventail.

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

> **Astuce :** Ajustez `setThetaLength` pour modifier l'angle d'ouverture. 270° crée un éventail de trois quarts ; 180° donnerait un demi‑cylindre.

## Étape 3 : Positionner le cylindre éventail

Ensuite, nous ajoutons le cylindre éventail à la scène et le déplaçons à un emplacement pratique. Les coordonnées de translation sont dans l'ordre (X, Y, Z).

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Étape 4 : Créer un cylindre sans éventail (comparaison de modélisation 3D Java)

Pour illustrer la flexibilité d'Aspose.3D, nous créons également un cylindre standard sans ouverture d'éventail.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Étape 5 : Enregistrer la scène (enregistrement OBJ Java)

Enfin, nous exportons la scène complète vers un fichier Wavefront OBJ. Ce format est largement pris en charge par la plupart des éditeurs 3D et moteurs de jeu.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Note :** Remplacez "Your Document Directory" par un chemin absolu ou relatif où vous avez les droits d'écriture.

## Comment enregistrer un fichier OBJ en Java avec Aspose 3D

La méthode `Scene.save` d'Aspose.3D gère automatiquement le processus **aspose 3d export obj**. Vous devez simplement spécifier le nom du fichier cible et la valeur d'énumération `FileFormat.WAVEFRONTOBJ`, comme illustré à l'étape précédente.

## Problèmes courants et solutions

| Problème | Raison | Solution |
|----------|--------|----------|
| Le fichier OBJ est vide | Scène non enregistrée ou chemin incorrect | Vérifiez que le répertoire de sortie existe et possède les droits d'écriture. |
| L'ouverture de l'éventail est incorrecte | Valeur `ThetaLength` incorrecte | Utilisez `MathUtils.toRadian(degrees)` pour définir l'angle exact dont vous avez besoin. |
| Erreurs de compilation | JAR Aspose.3D manquant dans le classpath | Ajoutez le JAR dans le dossier `libs` de votre projet et incluez‑le dans le chemin de construction. |

## Questions fréquemment posées

**Q : Aspose.3D est‑il compatible avec d'autres bibliothèques Java 3D ?**  
A : Oui, Aspose.3D peut coexister avec des bibliothèques comme Java 3D ou jMonkeyEngine, vous permettant d'intégrer une géométrie personnalisée dans des pipelines plus vastes.

**Q : Puis‑je personnaliser davantage l'apparence du cylindre éventail ?**  
A : Absolument. Vous pouvez appliquer des matériaux, des textures et de l'éclairage en accédant aux collections `Material` et `Light` du nœud.

**Q : Où puis‑je obtenir un support supplémentaire ?**  
A : Visitez le [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour obtenir de l'aide de la communauté et des réponses officielles.

**Q : Une version d'essai gratuite est‑elle disponible ?**  
A : Oui, vous pouvez explorer Aspose.3D avec un [essai gratuit](https://releases.aspose.com/) avant d'acheter.

**Q : Comment obtenir une licence temporaire pour les tests ?**  
A : Obtenez‑en une [ici](https://purchase.aspose.com/temporary-license/) pour débloquer toutes les fonctionnalités pendant le développement.

---

**Dernière mise à jour :** 2026-04-03  
**Testé avec :** Aspose.3D 24.11 pour Java  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}