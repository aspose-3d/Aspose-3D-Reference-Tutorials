---
date: 2025-12-12
description: Apprenez à définir la couleur du matériau tout en partageant les données
  de géométrie du maillage et en enregistrant la scène au format FBX dans Java 3D
  à l’aide d’Aspose.3D.
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: Définir la couleur du matériau et partager les données de géométrie du maillage
  en Java 3D avec Aspose.3D
url: /fr/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Définir la couleur du matériau et partager les données de géométrie de maillage en Java 3D avec Aspose.3D

## Introduction

S'embarquer dans le domaine de Java 3D avec Aspose.3D ouvre un monde de possibilités pour créer des visualisations époustouflantes et des expériences immersives. Dans ce tutoriel, nous vous guiderons à travers **comment partager les données de maillage** en Java 3D à l'aide d'Aspose.3D, et nous vous montrerons exactement **comment définir la couleur du matériau** pour chaque instance de maillage. Suivez chaque étape attentivement, et à la fin, vous échangerez sans problème les données de maillage entre plusieurs nœuds tout en contrôlant les couleurs et en exportant vers FBX.

## Quick Answers
- **Quel est l'objectif principal ?** Définir la couleur du matériau pour chaque nœud et partager les données de géométrie du maillage.  
- **Quelle bibliothèque est requise ?** Aspose.3D pour Java.  
- **Comment exporter le résultat ?** Enregistrer la scène en tant que fichier FBX (FBX7400ASCII).  
- **Ai-je besoin d'une licence ?** Une licence temporaire ou complète est requise pour une utilisation en production.  
- **Quelle version de Java fonctionne ?** Tout environnement Java 8+.

## Prérequis

Avant de plonger dans le tutoriel, assurez-vous d'avoir les prérequis suivants en place :

- Environnement de développement Java : Assurez-vous d'avoir un environnement de développement Java configuré sur votre système.  
- Bibliothèque Aspose.3D : Téléchargez et installez la bibliothèque Aspose.3D. Vous pouvez trouver la bibliothèque [ici](https://releases.aspose.com/3d/java/).

## Import Packages

Commencez par importer les packages nécessaires dans votre projet Java. Cette étape est cruciale pour accéder aux fonctionnalités fournies par la bibliothèque Aspose.3D.

```java
import com.aspose.threed.*;
```

## Step 1: Initialize Scene Object (initialize scene java)

Lançons le processus en initialisant un objet scène. Cela servira de toile où notre magie 3D se déroulera.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Step 2: Define Color Vectors

Dans cette étape, nous définissons un tableau de vecteurs de couleur qui seront appliqués aux différents éléments de notre scène 3D.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Step 3: Create 3D Mesh Java Using Polygon Builder (create 3d mesh java)

Utilisez la classe Common pour créer un maillage à l'aide de la méthode polygon builder. Ce maillage sera la base de nos éléments 3D.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## How to set material color for each node?

Itérez à travers les vecteurs de couleur, créez des nœuds cube, et définissez des attributs tels que le matériau, **set material color**, et la translation. C’est le cœur du contrôle de l’apparence visuelle de chaque instance de maillage.

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## Step 5: Save the 3D Scene (save scene fbx, convert mesh to fbx)

Spécifiez le répertoire et le nom de fichier pour enregistrer la scène 3D dans le format de fichier pris en charge, dans ce cas FBX7400ASCII. Cette étape montre également **convert mesh to FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Conclusion

Félicitations ! Vous avez réussi à **set material color**, partagé les données de géométrie de maillage entre plusieurs nœuds, et exporté le résultat sous forme de fichier FBX en utilisant Aspose.3D pour Java. Cela ouvre d'innombrables possibilités pour créer des applications 3D visuellement impressionnantes et interactives.

## FAQ's

### Q1: Can I use Aspose.3D with other Java frameworks?

A1: Yes, Aspose.3D is designed to work seamlessly with various Java frameworks.

### Q2: Are there any licensing options available for Aspose.3D?

A2: Yes, you can explore licensing options [here](https://purchase.aspose.com/buy).

### Q3: How can I get support for Aspose.3D?

A3: Visit the Aspose.3D [forum](https://forum.aspose.com/c/3d/18) for support and discussions.

### Q4: Is there a free trial available?

A4: Yes, you can get a free trial [here](https://releases.aspose.com/).

### Q5: How do I obtain a temporary license for Aspose.3D?

A5: You can get a temporary license [here](https://purchase.aspose.com/temporary-license/).

## Additional Frequently Asked Questions

**Q: Can I export the scene to other formats besides FBX?**  
A: Yes, Aspose.3D supports OBJ, STL, 3MF, and more. Just change the `FileFormat` enum in the `save` call.

**Q: What if I need to change the material after the scene is created?**  
A: Retrieve the node, modify its `LambertMaterial` (e.g., `setDiffuseColor`), and re‑save the scene.

**Q: Does the library handle large meshes efficiently?**  
A: Aspose.3D uses optimized data structures; however, for extremely large meshes consider streaming or splitting the scene.

**Q: Is there a way to animate the color change?**  
A: Yes, you can animate material properties using the `AnimationController` API.

---

**Last Updated:** 2025-12-12  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}