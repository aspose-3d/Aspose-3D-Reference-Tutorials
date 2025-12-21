---
date: 2025-12-21
description: Apprenez à enregistrer un fichier 3D Java avec Aspose.3D SaveOptions
  – optimisez les performances, activez le pretty‑print, personnalisez la sortie HTML5,
  et plus encore.
linktitle: Save 3D File Java – Optimize 3D Saving with Aspose.3D SaveOptions
second_title: Aspose.3D Java API
title: Enregistrer un fichier 3D Java – Optimiser la sauvegarde 3D avec Aspose.3D
  SaveOptions
url: /fr/java/load-and-save/optimize-3d-file-saving/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Enregistrer un fichier 3D Java – Optimiser l'enregistrement 3D avec Aspose.3D SaveOptions

## Introduction

Si vous devez **enregistrer des fichiers 3d java** rapidement et efficacement, Aspose.3D pour Java vous offre un ensemble puissant d'options pour affiner la sortie. Dans ce tutoriel, nous passerons en revue les paramètres `SaveOptions` les plus utiles, vous montrerons comment améliorer les performances et démontrerons des scénarios concrets tels que le pretty‑printing de fichiers GLTF ou la génération de visionneuses HTML5 autonomes.

## Quick Answers
- **Quelle est la classe principale pour l'enregistrement ?** `Scene.save()` avec une sous‑classe spécifique de `*SaveOptions`.  
- **Quelle option rend les fichiers GLTF lisibles par l'homme ?** `GltfSaveOptions.setPrettyPrint(true)`.  
- **Puis‑je intégrer les ressources dans une exportation GLTF ?** Oui – utilisez `GltfSaveOptions.setEmbedAssets(true)`.  
- **Comment désactiver l'interface utilisateur dans une exportation HTML5 ?** Définissez `Html5SaveOptions.setShowUI(false)`.  
- **Ai‑je besoin d'une licence pour la production ?** Une licence commerciale est requise pour tout usage non‑évaluation.

## Prérequis

Avant de plonger dans le tutoriel, assurez‑vous d’avoir les prérequis suivants :

- Aspose.3D pour Java : assurez‑vous que la bibliothèque Aspose.3D est intégrée à votre projet Java. Vous pouvez la télécharger [ici](https://releases.aspose.com/3d/java/).

- Environnement de développement Java : disposez d’un environnement de développement Java fonctionnel installé sur votre machine.

- Répertoire de documents : créez un répertoire où vous souhaitez enregistrer vos fichiers 3D et notez son chemin pour une utilisation ultérieure.

## Import Packages

Dans votre projet Java, importez les packages nécessaires pour travailler avec Aspose.3D. Cela inclut la classe `Scene` et diverses classes `SaveOptions`. Voici un exemple de base :

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## How to Save 3D File Java Using Aspose.3D SaveOptions

Ci‑dessous, nous détaillons les configurations `SaveOptions` les plus courantes. Chaque extrait est suivi d’une courte explication afin que vous compreniez **pourquoi** le paramètre est important.

### Step 1: Pretty Print in GLTF SaveOption

La méthode `prettyPrintInGltfSaveOption` vous permet de générer un fichier GLTF avec du JSON indenté pour une lisibilité humaine.

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // Initialize 3D scene
    Scene scene = new Scene(new Sphere());
    
    // Initialize GLTFSaveOptions
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // Enable pretty print for better readability
    opt.setPrettyPrint(true);
    
    // Save 3D Scene
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

### Step 2: HTML5 SaveOption

La méthode `html5SaveOption` montre comment enregistrer une scène 3D sous forme de fichier HTML5, avec des options de personnalisation.

```java
public static void html5SaveOption() throws IOException {
    // Initialize a scene
    Scene scene = new Scene();
    
    // Create a child node with a cylinder
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    // Set properties for the child node
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // Add a light to the scene
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // Initialize HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // Customize options (e.g., turn off grid and user interface)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // Save the scene as an HTML5 file
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

Continuez avec des découpages similaires pour les autres méthodes `SaveOptions` telles que `colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` et `drcSaveOptions`. Chaque exemple suit le même schéma : créez une scène, configurez l’objet `*SaveOptions` approprié, puis appelez `scene.save()`.

## Common Pitfalls & Tips

- **Intégration des ressources** – N’oubliez pas d’appeler `setEmbedAssets(true)` sur `GltfSaveOptions` lorsque vous avez besoin d’un fichier autonome unique.  
- **Performance** – Pour les scènes volumineuses, envisagez de réduire la complexité du maillage avant l’enregistrement ou d’utiliser la compression Draco (`DracoSaveOptions`).  
- **Gestion du système de fichiers** – Lors de l’exportation de fichiers OBJ, vous pouvez contrôler la création du fichier matériel avec `setFileSystem(new DummyFileSystem())` afin d’éviter les fichiers secondaires indésirables.  
- **Éléments d’interface** – Les exportations HTML5 incluent une UI par défaut ; désactivez‑la avec `setShowUI(false)` pour obtenir un visionneur épuré.

## Conclusion

En suivant ce tutoriel complet, vous avez appris à **enregistrer des fichiers 3d java** de manière efficace en utilisant les `SaveOptions` d’Aspose.3D. Que vous ayez besoin de fichiers GLTF pretty‑printed, de visionneuses HTML5 légères ou de sorties Draco fortement compressées, ces options vous offrent un contrôle total sur votre flux de travail graphique 3D.

## FAQ's

### Q1 : Comment intégrer les ressources dans un fichier glTF ?

R1 : Pour intégrer les ressources, utilisez la méthode `setEmbedAssets(true)` de la classe `GltfSaveOptions`.

### Q2 : Quel est le but de la méthode `setPositionBits` dans `DracoSaveOptions` ?

R2 : La méthode `setPositionBits` définit le nombre de bits de quantification pour la position dans l’algorithme de compression Draco.

### Q3 : Puis‑je exporter les normales dans un fichier U3D ?

R3 : Oui, vous pouvez exporter les normales en définissant `setExportNormals(true)` dans la classe `U3dSaveOptions`.

### Q4 : Comment ignorer l’enregistrement des fichiers matériels lors d’une exportation OBJ ?

R4 : Utilisez la méthode `setFileSystem(new DummyFileSystem())` de la classe `ObjSaveOptions` pour ne pas créer les fichiers matériels.

### Q5 : Existe‑t‑il un moyen d’enregistrer les dépendances dans un répertoire local lors d’une exportation OBJ ?

R5 : Oui, utilisez la méthode `setFileSystem(new LocalFileSystem(MyDir))` de la classe `ObjSaveOptions` pour enregistrer les dépendances localement.

## Frequently Asked Questions

**Q : Puis‑je utiliser ces SaveOptions dans un environnement serveur sans interface graphique ?**  
R : Absolument. Toutes les `SaveOptions` fonctionnent sans UI, ce qui les rend idéales pour les pipelines de traitement en arrière‑plan.

**Q : Aspose.3D prend‑il en charge l’enregistrement au format glTF 2.0 ?**  
R : Oui. Utilisez `GltfSaveOptions(FileFormat.GLTF2)` pour cibler la spécification glTF 2.0.

**Q : Comment contrôler le niveau de détail lors de l’exportation vers OBJ ?**  
R : Simplifiez le maillage avant l’enregistrement ou utilisez `ObjSaveOptions` pour définir la précision des sommets.

**Q : Existe‑t‑il un moyen de prévisualiser le fichier enregistré sans l’écrire sur le disque ?**  
R : Vous pouvez enregistrer dans un `ByteArrayOutputStream`, puis transmettre les octets à un visionneur ou à un client.

**Q : Quelle licence est requise pour une utilisation en production ?**  
R : Une licence commerciale Aspose.3D est nécessaire pour tout déploiement non‑évaluation.

---

**Dernière mise à jour :** 2025-12-21  
**Testé avec :** Aspose.3D pour Java 24.12 (dernière version au moment de la rédaction)  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}