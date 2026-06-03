---
date: 2026-06-03
description: Apprenez comment exporter la scène au format FBX et créer des modèles
  primitifs 3D tels que le cylindre, le cube et d’autres, en utilisant Aspose.3D for
  Java.
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
linktitle: Création de modèles primitifs 3D avec Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-06-03'
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  type: TechArticle
- description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
  type: HowTo
- questions:
  - answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
    question: Is Aspose.3D suitable for complex 3D modeling tasks?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
    question: Where can I find additional help and support?
  - answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
    question: Can I try Aspose.3D before purchasing?
  - answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: Exporter la scène au format FBX et créer un cylindre avec Aspose.3D Java
url: /fr/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Exporter la scène au format FBX et créer un cylindre avec Aspose.3D Java

## Introduction

Si vous avez déjà eu besoin de **créer un cylindre 3D** (ou toute autre forme de base) directement depuis du code Java, Aspose.3D rend la tâche indolore. Dans ce tutoriel, nous parcourrons l’ensemble du flux de travail — de la configuration de l’environnement à **l’exportation de la scène au format FBX** — afin que vous puissiez commencer à générer de la géométrie 3D programmatiquement dès maintenant. Vous verrez comment la bibliothèque gère les primitives, comment les organiser dans un graphe de scène, et comment enregistrer le résultat dans un format lisible par Unity, Blender ou tout autre outil 3D.

## Réponses rapides
- **Quelle bibliothèque me permet de créer un cylindre 3D en Java ?** Aspose.3D for Java.  
- **Quel format puis‑je exporter la scène ?** FBX (ASCII 7500) en utilisant `FileFormat.FBX7500ASCII`.  
- **Ai‑je besoin d’une licence pour le développement ?** Un essai gratuit suffit pour les tests ; une licence permanente est requise pour la production.  
- **Quelles sont les principales primitives prises en charge ?** Box, Cylinder, Sphere, Cone, et plus de 10 formes supplémentaires.  
- **Le code est‑il compatible avec Java 8 et versions ultérieures ?** Oui, Aspose.3D cible JDK 8+.

## Qu’est‑ce qu’une primitive cylindre 3D ?

Une primitive cylindre est une forme géométrique de base définie par un rayon et une hauteur. Dans de nombreux pipelines 3D, elle sert de bloc de construction pour des modèles plus complexes tels que des tuyaux, des roues ou des colonnes architecturales. Aspose.3D fournit une classe `Cylinder` prête à l’emploi, vous n’avez donc pas à calculer les sommets manuellement.

## Pourquoi utiliser Aspose.3D pour Java ?

Aspose.3D for Java offre un moteur 3D complet, pure‑Java, qui élimine le besoin de bibliothèques natives, ce qui le rend idéal pour le développement multiplateforme. Il prend en charge un large éventail de formats d’importation et d’exportation, fournit un graphe de scène robuste pour l’organisation hiérarchique, et inclut des primitives intégrées qui vous permettent de créer de la géométrie avec un minimum de code. Ces fonctionnalités accélèrent le développement et réduisent la charge de maintenance.

- **Moteur 3D complet** – prend en charge l’import/export de **plus de 30** formats populaires (FBX, OBJ, STL, GLTF, 3DS, etc.).  
- **API Java pure** – aucune dépendance native, parfait pour les projets multiplateformes.  
- **Graphe de scène robuste** – vous permet d’organiser les objets hiérarchiquement, facilitant la gestion de scènes volumineuses.  
- **Licence facile** – commencez avec un essai gratuit, puis passez à une licence permanente lorsque vous passez en production.

## Prérequis

Avant de plonger dans le code, assurez‑vous d’avoir :

1. **Java Development Kit (JDK)** – JDK 8 ou version supérieure installé sur votre machine.  
2. **Bibliothèque Aspose.3D for Java** – téléchargez‑la et installez‑la depuis la [page de téléchargement](https://releases.aspose.com/3d/java/).  

## Importer les packages

Commencez par importer l’espace de noms principal d’Aspose.3D. Cela vous donne accès à `Scene`, `Box`, `Cylinder` et aux constantes de format de fichier.

```java
import com.aspose.threed.*;
```

Maintenant que la bibliothèque est référencée, créons une scène et ajoutons de la géométrie primitive.

## Comment exporter la scène au format FBX et créer des primitives 3D ?

Chargez un nouvel objet `Scene`, ajoutez des nœuds primitifs (Box, Cylinder, etc.), puis appelez `save` avec le format FBX7500ASCII. En quelques lignes seulement, vous obtenez un fichier FBX complet qui peut être ouvert dans n’importe quel éditeur 3D majeur, permettant une intégration fluide avec les moteurs de jeu, les pipelines de rendu ou les applications AR/VR.

### Étape 1 : Initialiser un objet Scene

La classe `Scene` est le conteneur de haut niveau d’Aspose.3D qui contient en mémoire tous les nœuds, lumières, caméras et matériaux.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Étape 2 : Construire un modèle de boîte 3D

La classe `Box` représente un prisme rectangulaire et est utile pour tester le système de coordonnées. L’ajouter comme enfant du nœud racine de la scène le place à l’origine.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Étape 3 : Créer un modèle de cylindre 3D

La classe `Cylinder` est la primitive cylindre intégrée d’Aspose.3D. Elle possède des dimensions par défaut (rayon = 1, hauteur = 2) mais vous pouvez les personnaliser via son constructeur.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Étape 4 : Enregistrer le dessin au format FBX

Après avoir assemblé la scène, exportez‑la afin que d’autres outils (par ex., Unity, Blender) puissent la lire. Nous utilisons le format `FBX7500ASCII`, largement supporté et lisible par l’homme.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Problèmes courants et solutions

| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| **Fichier non trouvé** lors de l'enregistrement | `myDir` pointe vers un dossier inexistant | Assurez‑vous que le répertoire existe ou créez‑le avec `new File(myDir).mkdirs();` |
| **Scène vide** après l'exportation | Aucun nœud n'a été ajouté avant d'appeler `save` | Vérifiez que les appels `createChildNode` sont exécutés (déboguez avec `scene.getRootNode().getChildCount()` ) |
| **Exception de licence** | Exécution sans licence valide en production | Appliquez une licence temporaire ou permanente en utilisant `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## Questions fréquemment posées

**Q : Puis‑je utiliser Aspose.3D pour Java avec d’autres langages de programmation ?**  
**R :** Aspose.3D prend principalement en charge Java, mais des versions existent également pour .NET et C++.

**Q : Aspose.3D est‑il adapté aux tâches de modélisation 3D complexes ?**  
**R :** Absolument. Il fournit un ensemble complet de fonctionnalités — y compris la manipulation de maillages, l’attribution de matériaux et l’animation — le rendant adapté tant aux primitives simples qu’aux modèles détaillés.

**Q : Où puis‑je trouver de l’aide et du support supplémentaires ?**  
**R :** Consultez le [Forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le support communautaire et les discussions.

**Q : Puis‑je essayer Aspose.3D avant d’acheter ?**  
**R :** Oui, vous pouvez explorer un [essai gratuit](https://releases.aspose.com/) avant de prendre votre décision d’achat.

**Q : Comment obtenir une licence temporaire pour Aspose.3D ?**  
**R :** Vous pouvez obtenir une [licence temporaire](https://purchase.aspose.com/temporary-license/) pour Aspose.3D via le site web.

## Conclusion

Vous avez maintenant appris comment **exporter la scène au format FBX**, et comment **créer un cylindre 3D**, une boîte et d’autres modèles primitifs en utilisant Aspose.3D for Java. N’hésitez pas à expérimenter avec des primitives supplémentaires telles que Sphere, Cone ou Torus, et à explorer l’attribution de matériaux pour donner à vos modèles un aspect réaliste. Une fois à l’aise, vous pouvez intégrer les fichiers FBX générés dans des moteurs de jeu, des pipelines AR/VR ou tout autre flux de travail 3D en aval.

---

**Dernière mise à jour :** 2026-06-03  
**Testé avec :** Aspose.3D for Java 24.11 (dernière version au moment de la rédaction)  
**Auteur :** Aspose

## Tutoriels associés

- [Comment exporter une scène au format FBX et récupérer les informations d’une scène 3D en Java](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Comment exporter du FBX et créer des hiérarchies de nœuds en Java](/3d/java/geometry/build-node-hierarchies/)
- [Comment créer des modèles de cylindre avec Aspose.3D for Java](/3d/java/cylinders/)

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}