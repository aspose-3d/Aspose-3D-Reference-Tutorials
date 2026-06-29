---
date: 2026-06-29
description: Apprenez comment utiliser une licence Aspose 3D pour créer une scène
  3D avec une extrusion linéaire à décalage de torsion en Java et l'exporter au format
  Wavefront OBJ.
keywords:
- aspose 3d license
- wavefront obj export
- linear extrusion twist
- java 3d modeling
linktitle: Utiliser le décalage de torsion dans l'extrusion linéaire avec Aspose.3D
  pour Java
schemas:
- author: Aspose
  dateModified: '2026-06-29'
  description: Learn how to use an Aspose 3D license to create a 3D scene with twist
    offset linear extrusion in Java and export it as a Wavefront OBJ file.
  headline: Using Aspose 3D License for Twist Offset Extrusion in Java
  type: TechArticle
- description: Learn how to use an Aspose 3D license to create a 3D scene with twist
    offset linear extrusion in Java and export it as a Wavefront OBJ file.
  name: Using Aspose 3D License for Twist Offset Extrusion in Java
  steps:
  - name: Set Up the Environment
    text: Begin by setting up your Java development environment and ensuring that
      Aspose.3D for Java is correctly installed. This step is essential for any **java
      3d modeling** work.
  - name: Initialize the Base Profile
    text: '`RectangleShape` is a class representing a rectangular 2‑D shape used as
      an extrusion profile. Create a base profile for extrusion, in this case, a `RectangleShape`
      with a rounding radius of 0.3. The profile defines the cross‑section that will
      be swept along the extrusion path.'
  - name: Create a 3D Scene
    text: '`Scene` is the container that holds all nodes, lights, and cameras for
      your model. Building the scene first gives you a place to attach the extruded
      geometry.'
  - name: Create Nodes
    text: Generate nodes within the scene to represent different entities. Here we
      create two sibling nodes—one for a plain extrusion and another that uses a twist
      offset.
  - name: Perform Linear Extrusion with Twist and Twist Offset
    text: Apply linear extrusion on both nodes. The left node demonstrates a basic
      twist, while the right node adds a twist offset to illustrate the extra control
      you get with this feature. `setSlices(int)` sets the number of slices (segments)
      used to approximate the twist, controlling mesh resolution. > **Pr
  - name: Save the 3D Scene (Export 3d scene)
    text: '`save(String, FileFormat)` writes the scene to a file in the specified
      format. Finally, export the assembled scene to an OBJ file so you can view it
      in any standard 3D viewer or import it into other pipelines. CODE_BLOCK_PLACEHOLDER_6_END
      When the code runs successfully, you’ll find `TwistOffsetInLi'
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D for Java can be used in both commercial and non‑commercial
      projects. Check the [licensing options](https://purchase.aspose.com/buy) for
      more details.
    question: Can I use Aspose.3D for Java in non‑commercial projects?
  - answer: Visit the [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18)
      to get assistance and connect with the community.
    question: Where can I find support for Aspose.3D for Java?
  - answer: Yes, you can explore a free trial version from the [releases page](https://releases.aspose.com/).
    question: Is there a free trial available for Aspose.3D for Java?
  - answer: Get a temporary license for your project by visiting [this link](https://purchase.aspose.com/temporary-license/).
    question: How do I obtain a temporary license for Aspose.3D for Java?
  - answer: Yes, refer to the [documentation](https://reference.aspose.com/3d/java/)
      for more examples and in‑depth tutorials.
    question: Are there additional examples and tutorials available?
  type: FAQPage
second_title: Aspose.3D Java API
title: Utiliser la licence Aspose 3D pour l'extrusion linéaire à décalage de torsion
  en Java
url: /fr/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utilisation de la licence Aspose 3D pour l'extrusion à décalage de torsion en Java

## Introduction

Créer une scène 3D en Java devient beaucoup plus puissant lorsque vous combinez une **licence Aspose 3D** avec les fonctionnalités de torsion d'extrusion linéaire et de décalage de torsion. Ce tutoriel vous guide à travers chaque étape nécessaire pour **créer une scène 3D**, appliquer un décalage de torsion, et enfin **exporter la scène 3D** au format Wavefront OBJ. Avec une version sous licence, vous débloquez la génération de maillage en pleine résolution, une taille de fichier illimitée et des performances de niveau commercial.

## Réponses rapides
- **Que fait le décalage de torsion ?** Il décale le point de départ de la torsion, vous permettant de décaler la rotation le long du chemin d'extrusion.  
- **Quelle classe effectue l'extrusion linéaire ?** `LinearExtrusion` – vous pouvez définir la torsion, les tranches et le décalage de torsion dessus.  
- **Puis-je exporter le résultat ?** Oui, appelez `scene.save(..., FileFormat.WAVEFRONTOBJ)` pour exporter la scène 3D.  
- **Ai-je besoin d'une licence Aspose 3D pour le développement ?** Une licence temporaire fonctionne pour les tests ; une **licence Aspose 3D** complète est requise pour la production et pour supprimer les filigranes d'évaluation.  
- **Quelle version de Java est prise en charge ?** Tout runtime Java 8+ fonctionne avec la dernière bibliothèque Aspose.3D.

## Qu'est-ce que « créer une scène 3D » dans Aspose.3D ?

`Scene` est l'objet de niveau supérieur d'Aspose.3D représentant un environnement 3D complet. Créer une scène 3D dans Aspose.3D signifie instancier un objet `Scene`, ajouter des nœuds enfants contenant la géométrie, les lumières ou les caméras, puis enregistrer la hiérarchie dans un format de fichier tel que OBJ. Le `Scene` sert de conteneur racine pour tout le contenu 3D de votre application Java.

## Pourquoi utiliser la torsion d'extrusion linéaire avec un décalage de torsion ?

`LinearExtrusion` est la classe d'Aspose.3D pour balayer un profil 2D le long d'une ligne droite afin de générer une géométrie 3D. L'utiliser avec une torsion ajoute un composant de rotation, et le décalage de torsion vous permet de déplacer le point de départ de cette rotation, vous offrant un contrôle précis sur les formes en spirale telles que les colonnes hélicoïdales, les poignées décoratives ou les ressorts mécaniques. Ce contrôle supplémentaire est particulièrement précieux dans le **modélisation 3D Java** pour les pièces mécaniques et les conceptions artistiques.

## Prérequis

- **Environnement Java :** Assurez-vous d'avoir un environnement de développement Java configuré sur votre système.  
- **Aspose.3D pour Java :** Téléchargez et installez la bibliothèque Aspose.3D depuis le [lien de téléchargement](https://releases.aspose.com/3d/java/).  
- **Documentation :** Familiarisez‑vous avec la [documentation Aspose.3D pour Java](https://reference.aspose.com/3d/java/).  

## Importer les packages

Dans votre projet Java, importez les packages nécessaires pour commencer à utiliser Aspose.3D pour Java. Assurez‑vous d'inclure les bibliothèques requises pour une intégration fluide.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Comment créer une scène 3D – Guide étape par étape

Pour créer une scène 3D avec une extrusion linéaire à décalage de torsion en Java, vous devez d'abord configurer votre environnement de développement, puis définir un profil rectangulaire, instancier un `Scene`, ajouter deux nœuds enfants, appliquer `LinearExtrusion` avec et sans décalage de torsion, et enfin enregistrer la scène au format Wavefront OBJ. Suivez les sections étape par étape ci‑dessous pour obtenir les extraits de code exacts.

### Étape 1 : Configurer l'environnement
Commencez par configurer votre environnement de développement Java et vous assurer qu'Aspose.3D pour Java est correctement installé. Cette étape est essentielle pour tout travail de **modélisation 3D Java**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Étape 2 : Initialiser le profil de base
`RectangleShape` est une classe représentant une forme 2D rectangulaire utilisée comme profil d'extrusion. Créez un profil de base pour l'extrusion, dans ce cas, un `RectangleShape` avec un rayon d'arrondi de 0,3. Le profil définit la section transversale qui sera balayée le long du chemin d'extrusion.

```java
// Create a scene
Scene scene = new Scene();
```

### Étape 3 : Créer une scène 3D
`Scene` est le conteneur qui regroupe tous les nœuds, lumières et caméras de votre modèle. Construire la scène d'abord vous donne un endroit où attacher la géométrie extrudée.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Étape 4 : Créer des nœuds
Générez des nœuds au sein de la scène pour représenter différentes entités. Ici, nous créons deux nœuds frères — un pour une extrusion simple et un autre qui utilise un décalage de torsion.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

### Étape 5 : Effectuer une extrusion linéaire avec torsion et décalage de torsion
Appliquez l'extrusion linéaire sur les deux nœuds. Le nœud de gauche montre une torsion de base, tandis que le nœud de droite ajoute un décalage de torsion pour illustrer le contrôle supplémentaire offert par cette fonctionnalité. `setSlices(int)` définit le nombre de tranches (segments) utilisées pour approximer la torsion, contrôlant la résolution du maillage.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

> **Astuce :** Ajustez `setSlices()` pour augmenter la résolution du maillage lorsque vous avez besoin d'une courbure plus lisse.

### Étape 6 : Enregistrer la scène 3D (Exporter la scène 3D)
`save(String, FileFormat)` écrit la scène dans un fichier au format spécifié. Enfin, exportez la scène assemblée vers un fichier OBJ afin de pouvoir la visualiser dans n'importe quel visualiseur 3D standard ou l'importer dans d'autres pipelines.

CODE_BLOCK_PLACEHOLDER_6_END

Lorsque le code s'exécute avec succès, vous trouverez `TwistOffsetInLinearExtrusion.obj` dans le répertoire spécifié, prêt à être ouvert dans des outils tels que Blender, MeshLab ou tout logiciel de CAO.

## Problèmes courants et solutions
| Issue | Why it Happens | Fix |
|-------|----------------|-----|
| **La scène s'enregistre comme fichier vide** | `MyDir` chemin incorrect ou permissions d'écriture manquantes. | Vérifiez que le répertoire existe et est accessible en écriture, ou utilisez un chemin absolu. |
| **La torsion semble plate** | `setSlices()` est trop bas, ce qui entraîne un maillage grossier. | Augmentez le nombre de tranches (par ex., 200) pour des torsions plus lisses. |
| **Le décalage de torsion n'a aucun effet** | Le vecteur de décalage est colinéaire avec la direction d'extrusion. | Utilisez une composante X ou Y non nulle pour voir le décalage. |

## Questions fréquentes

**Q : Puis‑je utiliser Aspose.3D pour Java dans des projets non commerciaux ?**  
R : Oui, Aspose.3D pour Java peut être utilisé dans des projets commerciaux et non commerciaux. Consultez les [options de licence](https://purchase.aspose.com/buy) pour plus de détails.

**Q : Où puis‑je trouver du support pour Aspose.3D pour Java ?**  
R : Visitez le [forum Aspose.3D pour Java](https://forum.aspose.com/c/3d/18) pour obtenir de l'aide et rejoindre la communauté.

**Q : Existe‑t‑il une version d'essai gratuite pour Aspose.3D pour Java ?**  
R : Oui, vous pouvez explorer une version d'essai gratuite depuis la [page des releases](https://releases.aspose.com/).

**Q : Comment obtenir une licence temporaire pour Aspose.3D pour Java ?**  
R : Obtenez une licence temporaire pour votre projet en visitant [ce lien](https://purchase.aspose.com/temporary-license/).

**Q : Existe‑t‑il d'autres exemples et tutoriels disponibles ?**  
R : Oui, consultez la [documentation](https://reference.aspose.com/3d/java/) pour plus d'exemples et de tutoriels approfondis.

---

**Dernière mise à jour :** 2026-06-29  
**Testé avec :** Aspose.3D pour Java 24.11 (dernière version)  
**Auteur :** Aspose

{{< blocks/products/products-backtop-button >}}

## Tutoriels associés

- [Créer une extrusion 3D Java avec Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Créer une scène 3D avec torsion dans l'extrusion linéaire – Aspose.3D pour Java](/3d/java/linear-extrusion/applying-twist/)
- [Comment définir la direction dans l'extrusion linéaire avec Aspose.3D pour Java](/3d/java/linear-extrusion/setting-direction/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}