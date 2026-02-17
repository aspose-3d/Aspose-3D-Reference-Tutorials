---
date: 2026-01-27
description: Apprenez la modélisation 3D en Java en créant des cylindres avec un fond
  cisaillé à l'aide d'Aspose.3D pour Java. Ce tutoriel 3D pour débutants montre comment
  installer Aspose 3D, appliquer une transformation de cisaillement et exporter un
  fichier OBJ en Java.
linktitle: Java 3D Modeling – Sheared Bottom Cylinders with Aspose.3D
second_title: Aspose.3D Java API
title: Modélisation 3D Java – Cylindres à base cisaillée avec Aspose.3D
url: /fr/java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Modélisation 3D Java – Cylindres à base inclinée avec Aspose.3D

## Introduction

Bienvenue dans ce **java 3d modeling** ! Dans ce guide étape par étape, nous allons créer un cylindre dont la base est inclinée, en utilisant la bibliothèque Aspose.3D pour Java. Que vous suiviez un **beginner 3d tutorial** ou que vous souhaitiez ajouter une transformation de cisaillement personnalisée à un modèle existant, vous verrez exactement comment configurer la scène, appliquer le cisaillement, et enfin **export OBJ file java** pour une utilisation dans d’autres outils.

## Réponses rapides
- **Quelle bibliothèque est utilisée ?** Aspose.3D for Java  
- **Puis‑je installer Aspose 3D via Maven ?** Oui – ajoutez la dépendance Aspose.3D à votre `pom.xml`  
- **Une licence est‑elle requise pour le développement ?** Une licence temporaire suffit pour les tests ; une licence complète est nécessaire pour la production  
- **Quel format de fichier est démontré ?** Wavefront OBJ (`.obj`)  
- **Combien de temps l’exemple met‑il à s’exécuter ?** Moins d’une seconde sur une station de travail typique  

## Prérequis

Avant de commencer, assurez‑vous d’avoir les éléments suivants :

- Java Development Kit (JDK) installé sur votre système.  
- **Install Aspose 3D** – téléchargez la bibliothèque depuis le site officiel [here](https://releases.aspose.com/3d/java/).  
- Un IDE ou un outil de construction (Maven/Gradle) pour gérer la dépendance Aspose.3D.  

## Importer les packages

Tout d’abord, importez les classes dont nous aurons besoin pour la scène, la géométrie et la gestion des fichiers.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Étape 1 : Créer une scène

Une scène est le conteneur de tous les objets 3‑D. Nous allons commencer par créer une scène vide.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Étape 2 : Créer le Cylindre 1 – Comment ciseler un cylindre

Nous allons maintenant créer le premier cylindre et **appliquer une transformation de cisaillement** à sa base. Cela montre **comment ciseler un cylindre** directement via l’API.

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

## Étape 3 : Créer le Cylindre 2 – Cylindre standard (sans cisaillement)

À titre de comparaison, nous ajouterons un deuxième cylindre qui **n’a pas** de base inclinée.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Étape 4 : Enregistrer la scène – Exporter le fichier OBJ Java

Enfin, nous exportons la scène vers un fichier Wavefront OBJ, illustrant l’utilisation de **export obj file java**.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Pourquoi cela est important pour la modélisation 3D Java

Ajouter un cisaillement à un primitive vous permet de créer des formes plus organiques sans recourir à des outils de modélisation externes. Cette technique est pratique pour :

- Visualisations architecturales où des bases inclinées sont requises.  
- Actifs de jeu nécessitant des empreintes personnalisées tout en gardant la géométrie légère.  
- Prototypage rapide où vous souhaitez ajuster les dimensions de manière programmatique.

## Problèmes courants & solutions

| Problème | Solution |
|----------|----------|
| **Le cisaillement apparaît trop extrême** | Ajustez les valeurs du `Vector2` ; elles représentent le facteur de cisaillement (plage 0‑1). |
| **Le fichier OBJ ne s’ouvre pas dans le visualiseur** | Vérifiez que le répertoire cible existe et que vous avez les permissions d’écriture. |
| **Exception de licence à l’exécution** | Appliquez une licence temporaire ou permanente avant de créer la scène (`License license = new License(); license.setLicense("Aspose.3D.lic");`). |

## Questions fréquentes

**Q : Puis‑je utiliser Aspose.3D pour Java avec d’autres bibliothèques Java 3D ?**  
A : Aspose.3D est conçu pour fonctionner de manière indépendante. Bien que vous puissiez l’intégrer à d’autres bibliothèques, il fournit déjà une API complète pour la plupart des tâches 3‑D.

**Q : Aspose.3D convient‑il aux débutants en modélisation 3D ?**  
A : Absolument. L’API est simple, et ce **beginner 3d tutorial** démontre les concepts de base avec un code minimal.

**Q : Où puis‑je trouver un support supplémentaire pour Aspose.3D pour Java ?**  
A : Consultez le [Aspose.3D forum](https://forum.aspose.com/c/3d/18) pour l’aide de la communauté et les réponses officielles.

**Q : Comment obtenir une licence temporaire pour Aspose.3D ?**  
A : Vous pouvez obtenir une licence temporaire [ici](https://purchase.aspose.com/temporary-license/).

**Q : Où puis‑je acheter une licence complète Aspose.3D pour Java ?**  
A : Les options d’achat sont disponibles [ici](https://purchase.aspose.com/buy).

---

**Dernière mise à jour :** 2026-01-27  
**Testé avec :** Aspose.3D 24.11 for Java  
**Auteur :** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
