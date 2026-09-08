---
date: 2026-09-08
description: Apprenez comment définir les unités et exporter une scène au format FBX
  en Java en utilisant Aspose.3D. Ce guide étape par étape montre comment définir
  le nom de l'application, les unités de mesure et récupérer les informations de la
  scène 3D.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Comment enregistrer le FBX et récupérer les informations de la scène 3D
  en Java
og_description: Apprenez comment définir les unités et exporter une scène au format
  FBX en Java avec Aspose.3D. Le guide couvre la définition du nom de l'application,
  les unités de mesure et la récupération des informations de la scène 3D en quelques
  étapes.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Comment définir les unités et exporter la scène au format FBX en Java
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Comment définir les unités et exporter la scène au format FBX en Java
url: /fr/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment définir les unités et exporter la scène au format FBX en Java

## Introduction

Si vous cherchez un guide clair et pratique sur **comment définir les unités** et **exporter une scène au format FBX** tout en extrayant des métadonnées utiles de vos scènes 3D, vous êtes au bon endroit. Dans ce tutoriel, nous passerons en revue chaque étape en utilisant la bibliothèque **Aspose.3D for Java** : de la création d'une scène, **définir le nom de l'application**, **définir les unités de mesure**, jusqu'à **exporter la scène au format FBX**. À la fin, vous disposerez d'un fichier FBX prêt à l'emploi contenant les informations d'actif dont vous avez besoin pour les pipelines en aval.

## Réponses rapides

- **Quel est l'objectif principal ?** Exporter une scène au format FBX contenant des informations d'actif personnalisées.  
- **Quelle bibliothèque est utilisée ?** Aspose.3D for Java.  
- **Ai-je besoin d'une licence ?** Un essai gratuit suffit pour le développement ; une licence commerciale est requise pour la production.  
- **Puis-je changer les unités de mesure ?** Oui – utilisez `setUnitName` et `setUnitScaleFactor`.  
- **Où la sortie est‑elle enregistrée ?** Dans le chemin que vous spécifiez dans `scene.save(...)`.  

## Prérequis

Avant de commencer, assurez-vous d'avoir :

- Une bonne maîtrise de la syntaxe Java de base.  
- **Aspose.3D for Java** téléchargé et ajouté à votre projet (vous pouvez le récupérer depuis le site officiel) [Page de téléchargement Aspose 3D](https://releases.aspose.com/3d/java/).  
- Votre IDE Java préféré (IntelliJ IDEA, Eclipse, NetBeans, etc.) correctement configuré.

## Importer les packages

Dans votre fichier source Java, importez les classes Aspose.3D qui offrent la gestion de scènes et la prise en charge des formats de fichiers.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Conseil pro :** Gardez la liste d'importations minimale pour éviter les dépendances inutiles et améliorer les temps de compilation.

## Quel est le processus pour enregistrer un fichier FBX ?

Pour enregistrer une scène au format FBX, vous créez un `Scene`, définissez les métadonnées d'actif souhaitées, spécifiez l'unité de mesure, puis appelez `scene.save(path, FileFormat.FBX7500ASCII)`. Cette séquence écrit la géométrie, les matériaux et les métadonnées dans un FBX ASCII qui peut être inspecté ou importé par les outils en aval.

### Étape 1 : initialiser une scène 3D

La classe `Scene` est le conteneur de niveau supérieur d'Aspose.3D qui représente une scène 3D complète, incluant la géométrie, les lumières, les caméras et les métadonnées. Tout d'abord, créez un objet `Scene` vide. Ce sera le conteneur pour toute la géométrie, les lumières, les caméras et les métadonnées d'actif.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Comment définir le nom de l'application en Java

L'objet `AssetInfo` stocke des métadonnées telles que le nom de l'application, le fournisseur et la version pour la scène. Ajouter des métadonnées personnalisées aide les outils en aval à identifier la source du fichier. Utilisez l'objet `AssetInfo` pour **définir le nom de l'application** (et le fournisseur) avant d'enregistrer le fichier.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Pourquoi c'est important :** De nombreux pipelines filtrent ou étiquettent les actifs en fonction de l'application d'origine, rendant cette étape essentielle pour les grands projets.

### Étape 3 : définir les unités de mesure

Le système d'unités détermine l'échelle réelle de la scène ; Aspose.3D vous permet de spécifier un nom d'unité et un facteur d'échelle relatif aux mètres. Dans cet exemple, nous utilisons une unité égyptienne antique appelée « pole » avec un facteur d'échelle personnalisé.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Conseil :** Ajustez `unitScaleFactor` pour correspondre à la taille réelle de vos modèles ; 1,0 représente une correspondance 1 à 1 avec l'unité choisie.

### Étape 4 : exporter la scène au format FBX

Maintenant que les informations d'actif sont attachées, nous enregistrons la scène au format FBX. L'option `FileFormat.FBX7500ASCII` produit un FBX ASCII lisible par l'homme, ce qui est pratique pour le débogage.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Rappel :** Remplacez `"Your Document Directory"` par un chemin absolu ou un chemin relatif au répertoire de travail de votre projet.

## Pourquoi exporter une scène au format FBX avec Aspose.3D ?

Aspose.3D prend en charge **plus de 50 formats d'entrée et de sortie** et peut traiter des scènes de plusieurs centaines de pages sans charger le fichier complet en mémoire, vous offrant un contrôle total sur le fichier exporté — métadonnées, unités et géométrie — sans nécessiter d'application d'authoring 3D lourde. Cela rend la génération automatisée d'actifs, le traitement par lots et les conversions côté serveur rapides et fiables.

## Cas d'utilisation courants

- **Pipelines d'actifs de jeu** – intégrer les informations du créateur directement dans les fichiers FBX pour le suivi des versions.  
- **Visualisation architecturale** – stocker les unités spécifiques au projet pour éviter les erreurs d'échelle lors de l'importation dans les moteurs de rendu.  
- **Reporting automatisé** – générer des fichiers FBX à la volée avec des métadonnées que les outils d'analyse en aval peuvent lire.  
- **Services 3D basés sur le cloud** – créer et exporter des scènes programmatiquement sans interface graphique, parfait pour les plateformes SaaS.  

## Dépannage et astuces

| Problème | Solution |
|----------|----------|
| **Fichier introuvable après l'enregistrement** | Vérifiez que `MyDir` pointe vers un dossier existant et que votre application dispose des permissions d'écriture. |
| **Les unités apparaissent incorrectes dans le visualiseur externe** | Vérifiez à nouveau `unitScaleFactor` ; certains visualiseurs attendent les mètres comme unité de base. |
| **Métadonnées d'actif manquantes** | Assurez‑vous d’appeler `scene.getAssetInfo()` **avant** l’enregistrement ; les modifications effectuées après `save()` ne seront pas conservées. |
| **Goulot d'étranglement de performance sur les grandes scènes** | Utilisez `scene.optimize()` avant l’enregistrement pour réduire l’utilisation de la mémoire. |
| **Le FBX ASCII est trop volumineux** | Passez au FBX binaire en utilisant `FileFormat.FBX7500` (voir FAQ). |

## Questions fréquentes

**Q : Comment changer le format de sortie en FBX binaire ?**  
R : Remplacez `FileFormat.FBX7500ASCII` par `FileFormat.FBX7500` lors de l’appel à `scene.save(...)`.

**Q : Puis‑je ajouter des métadonnées personnalisées définies par l'utilisateur au‑delà des champs d'actif intégrés ?**  
R : Oui, utilisez `scene.getUserData().add("Key", "Value")` pour intégrer des paires clé‑valeur supplémentaires.

**Q : Aspose.3D prend‑il en charge d'autres formats d'exportation comme OBJ ou GLTF ?**  
R : Oui. Il suffit de changer l'énumération `FileFormat` en `OBJ` ou `GLTF2` selon les besoins.

**Q : Quelle version de Java est requise ?**  
R : Aspose.3D for Java prend en charge Java 8 et versions ultérieures.

**Q : Est‑il possible de charger un FBX existant, de modifier ses informations d'actif et de le réenregistrer ?**  
R : Absolument. Chargez le fichier avec `new Scene("input.fbx")`, modifiez `scene.getAssetInfo()`, puis enregistrez.

---

**Dernière mise à jour :** 2026-09-08  
**Testé avec :** Aspose.3D for Java 24.11  
**Auteur :** Aspose

## Tutoriels associés

- [Réduire la taille des fichiers 3D – Compresser les scènes avec Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Comment définir la couleur vector3 en Java : changer la couleur diffuse et gérer les propriétés 3D dans les scènes Java avec Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}