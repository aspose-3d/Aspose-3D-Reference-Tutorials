---
date: 2025-12-09
description: Apprenez à utiliser Aspose pour créer des cylindres personnalisés avec
  des bases cisaillées en Java, parfaits pour la modélisation 3D Java et l’enregistrement
  de scènes au format OBJ.
language: fr
linktitle: 'How to Use Aspose: Create Cylinders with Sheared Bottom in Java'
second_title: Aspose.3D Java API
title: 'Comment utiliser Aspose : créer des cylindres avec une base cisaillée en Java'
url: /java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment utiliser Aspose : créer des cylindres avec une base cisaille en Java

## Introduction

Dans ce tutoriel pratique, vous découvrirez **comment utiliser Aspose** pour créer un cylindre dont la base est cisaille – une technique souvent requise dans les projets de *modélisation 3d java*. Nous parcourrons chaque étape, de la configuration de la scène à l’enregistrement du modèle final au format OBJ. À la fin, vous disposerez d’un extrait de code réutilisable que vous pourrez intégrer à n’importe quelle application 3D basée sur Java.

## Réponses rapides
- **Que signifie « shear bottom » ?** Cela incline la base du cylindre d’un angle spécifié dans le plan XY.  
- **Quelle bibliothèque gère les calculs 3D ?** Aspose.3D for Java fournit les classes `Cylinder` et `Vector2`.  
- **Ai‑je besoin d’une licence pour exécuter l’exemple ?** Une licence temporaire suffit pour l’évaluation ; une licence complète est requise en production.  
- **Puis‑je exporter le modèle vers d’autres formats ?** Oui – utilisez `scene.save(..., FileFormat.WAVEFRONTOBJ)` pour obtenir un fichier OBJ.  
- **Quelle version de Java est requise ?** JDK 8 ou supérieur est suffisant.

## Qu’est‑ce que « how to use aspose » dans le contexte de la modélisation 3D ?

Aspose.3D for Java est une API de haut niveau qui abstrait les complexités de la géométrie 3D, des formats de fichiers et des transformations. Au lieu de manipuler des tampons de sommets de bas niveau, vous appelez des méthodes intuitives comme `new Cylinder(...)` et laissez Aspose gérer le travail lourd.

## Pourquoi utiliser Aspose pour la modélisation 3D Java ?

- **Développement rapide :** Créez des formes complexes en quelques lignes de code.  
- **Large prise en charge des formats :** Exportez vers OBJ, STL, FBX, et plus encore.  
- **Multiplateforme :** Fonctionne sur tout OS supportant Java.  
- **API cohérente :** Le même code fonctionne sur desktop, serveur ou Android.

## Prérequis

Avant de commencer, assurez‑vous d’avoir :

- **Java Development Kit (JDK) 8+** installé et configuré dans votre IDE.  
- **Bibliothèque Aspose.3D for Java** ajoutée au classpath de votre projet. Vous pouvez la télécharger depuis le site officiel [ici](https://releases.aspose.com/3d/java/).  
- **Une licence temporaire ou complète** (facultatif pour les essais).

## Importer les packages

Pour commencer, importez les classes essentielles d’Aspose.3D et les utilitaires Java :

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Étape 1 : créer une scène

Une *scene* est le conteneur qui regroupe tous les objets 3D, les lumières et les caméras. Pensez‑y comme la scène où vous placerez vos cylindres.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Étape 2 : créer le Cylindre 1 (base cisaille)

Nous allons maintenant créer le premier cylindre et appliquer une transformation de cisaillement à sa base. La méthode `setShearBottom` accepte un `Vector2` où le composant X représente le facteur de cisaillement selon l’axe X et le composant Y selon l’axe Y.

```java
// ExStart:4
// Create cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Customized shear bottom for cylinder 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Shear 47.5deg in the xy plane (z-axis)
// Add cylinder 1 to the scene
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

> **Astuce :** Le facteur de cisaillement `0.83` correspond à environ 47,5° ; ajustez cette valeur pour obtenir l’angle exact souhaité.

## Étape 3 : créer le Cylindre 2 (standard)

À titre de comparaison, nous ajoutons un deuxième cylindre sans cisaillement. Cela vous permet de voir la différence visuelle directement dans le fichier OBJ exporté.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Étape 4 : enregistrer la scène (Comment enregistrer la scène au format OBJ)

Enfin, nous persistons la scène sur le disque. La constante `FileFormat.WAVEFRONTOBJ` indique à Aspose d’écrire un fichier OBJ, largement supporté par les éditeurs 3D comme Blender et Maya.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Remarque :** Remplacez `"Your Document Directory"` par un chemin absolu ou relatif adapté à votre environnement.

## Problèmes courants et solutions

| Problème | Cause | Solution |
|----------|-------|----------|
| **Le cylindre apparaît plat** | Facteur de cisaillement incorrect (hors de la plage 0‑1) | Utilisez une valeur comprise entre 0 et 1 ; ajustez progressivement tout en prévisualisant. |
| **Le fichier OBJ ne se charge pas dans le visualiseur** | Définitions de matériaux manquantes | Ajoutez un matériau simple à chaque nœud ou exportez en STL pour un test uniquement géométrique. |
| **LicenseException à l’exécution** | Aucun fichier de licence valide | Placez `Aspose.3D.lic` à la racine du projet ou utilisez la classe `License` pour le charger programmatique. |

## Questions fréquentes

### Q1 : Puis‑je utiliser Aspose.3D for Java avec d’autres bibliothèques 3D Java ?
**R :** Aspose.3D for Java est conçu pour fonctionner de manière autonome. Bien que vous puissiez l’intégrer à d’autres bibliothèques, il fournit un ensemble complet de fonctionnalités pour la plupart des tâches de modélisation 3D.

### Q2 : Aspose.3D convient‑il aux débutants en modélisation 3D ?
**R :** Oui, Aspose.3D propose une API conviviale qui abstrait les détails de bas niveau, la rendant accessible tant aux débutants qu’aux développeurs expérimentés### Q3 : Où puis‑je trouver un support supplémentaire pour Aspose.3D for Java ?
**R :** Consultez le [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le support communautaire, des tutoriels et des discussions.

### Q4 : Comment obtenir une licence temporaire pour Aspose.3D ?
**R :** Vous pouvez obtenir une licence temporaire [ici](https://purchase.aspose.com/temporary-license/).

### Q5 : Puis‑je acheter Aspose.3D for Java ?
**R :** Oui, vous pouvez acheter Aspose.3D for Java [ici](https://purchase.aspose.com/buy).

## Conclusion

Nous avons parcouru **comment utiliser Aspose** pour créer deux cylindres — l’un avec une base cisaille et l’autre standard — puis enregistré le résultat au format OBJ. Cette technique constitue une base pour des modèles 3D plus sophistiqués, tels que des pièces personnalisées, des éléments architecturaux ou des actifs de jeu. N’hésitez pas à expérimenter avec différentes valeurs de cisaillement, rayons et hauteurs pour répondre aux besoins de votre projet.

---

**Dernière mise à jour :** 2025-12-09  
**Testé avec :** Aspose.3D for Java 24.11 (dernière version au moment de la rédaction)  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}