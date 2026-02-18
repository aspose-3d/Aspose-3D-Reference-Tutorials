---
date: 2026-02-17
description: Apprenez à convertir un maillage en FBX tout en définissant la couleur
  du matériau et en partageant les données de géométrie du maillage en Java 3D avec
  Aspose.3D.
linktitle: Convert Mesh to FBX and Set Material Color in Java 3D
second_title: Aspose.3D Java API
title: Convertir le maillage en FBX et définir la couleur du matériau dans Java 3D
url: /fr/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Convertir un maillage en FBX et définir la couleur du matériau en Java 3D

## Introduction

Si vous développez une application 3D basée sur Java, vous aurez souvent besoin de réutiliser la même géométrie sur plusieurs objets tout en donnant à chaque instance un aspect unique. Dans ce tutoriel, vous apprendrez **comment convertir un maillage en FBX**, partager la géométrie du maillage sous‑jacent entre plusieurs nœuds, et **définir une couleur de matériau différente pour chaque nœud**. À la fin, vous disposerez d’une scène FBX prête à être exportée que vous pourrez intégrer dans n’importe quel moteur ou visualiseur.

## Réponses rapides
- **Quel est l'objectif principal ?** Convertir le maillage en FBX, partager la géométrie du maillage et définir une couleur de matériau distincte pour chaque nœud.
- **Quelle bibliothèque est requise?** Aspose.3D pour Java.
- **Comment exporter le résultat?** Enregistrer la scène sous forme de fichier FBX en utilisant `FileFormat.FBX7400ASCII`.
- **Ai‑je besoin d’une licence?** Une licence temporaire ou complète est requise pour une utilisation en production.
- **Quelle version de Java fonctionne ?** Tout environnement Java8+.

## Qu'est-ce que **convertir le maillage en FBX** ?

`convert mesh to fbx` est le processus consistant à prendre un objet maillage créé ou manipulé en mémoire et à l'écrire au format de fichier FBX, largement supporté par les outils 3D tels que Maya, Blender et Unity. Aspose.3D se charge du travail lourd, vous n’avez donc qu’à appeler `scene.save(...)` avec le `FileFormat` approprié.

## Pourquoi partager des données de géométrie de maillage ?

Partager la géométrie réduit la consommation de mémoire et accélère le rendu car les tampons de sommets sous‑jacents ne sont stockés qu’une seule fois. Cette technique est idéale pour les scènes contenant de nombreux objets dupliqués — pensez aux forêts, aux foules ou à l’architecture modulaire — où chaque instance ne diffère que par sa transformation ou son matériau.

## Prérequis

Avant de Sous-marin dans le tutoriel, assurez-vous d’avoir les prérequis suivants en place :

- **Environnement de développement Java** – tout IDE ou configuration en ligne de commande avec Java8 ou supérieur.
- **Bibliothèque Aspose.3D** – téléchargez le dernier JAR depuis le site officiel : [ici](https://releases.aspose.com/3d/java/).

## Importer des packages

Commencez par importer les packages nécessaires dans votre projet Java. Cette étape est cruciale pour les fonctionnalités fournies par la bibliothèque Aspose.3D.

```java
import com.aspose.threed.*;
```

## Étape 1 : Initialiser l’objet Scene (initialize scene java)

Commençons le processus en initialisant un objet scène. Celui‑ci servira de toile où notre magie 3D se déroulera.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Étape 2 : Définir les vecteurs de couleur

Dans cette étape, nous définissons un tableau de vecteurs de couleur qui seront appliqués aux différents éléments de notre scène 3D.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Étape 3 : Créer un maillage 3D Java en utilisant Polygon Builder (create 3d mesh java)

Utilisez la classe Common pour créer un maillage à l’aide de la méthode polygon builder. Ce maillage sera la base de nos éléments 3D.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Comment définir la couleur du matériau pour chaque nœud ?

Parcourez les vecteurs de couleur, créez des nœuds cube et définissez des attributs tels que le matériau, **set material color**, et la translation. C’est le cœur du contrôle de l’apparence visuelle de chaque instance de maillage.

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

## Étape 5 : Enregistrer la scène 3D (save scene fbx, convert mesh to fbx)

Spécifiez le répertoire et le nom de fichier pour enregistrer la scène 3D dans le format de fichier pris en charge, dans ce cas FBX7400ASCII. Cette étape montre également **convert mesh to FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Écueils courants & Conseils

- **Problèmes de chemin** – Assurez‑vous que le chemin du répertoire se termine par un séparateur de fichier (`/` ou `\\`) avant d’ajouter le nom de fichier.  
- **Initialisation de la licence** – Si vous oubliez de définir la licence Aspose.3D avant d’appeler `scene.save`, la bibliothèque fonctionnera en mode d’essai et pourra intégrer un filigrane.  
- **Écrasement de matériau** – Réutiliser la même instance `LambertMaterial` pour plusieurs nœuds entraînera le partage de la même couleur par tous les nœuds. Créez toujours un nouveau matériau à chaque itération, comme montré ci‑dessus.  
- **Grands maillages** – Pour les maillages contenant des millions de sommets, envisagez d’utiliser `MeshBuilder` avec des polygones indexés afin de garder la taille du fichier FBX gérable.

## Questions supplémentaires fréquemment posées

**Q1 : Puis‑je utiliser Aspose.3D avec d’autres frameworks Java ?**  
R1 : Oui, Aspose.3D est conçu pour fonctionner de manière transparente avec divers frameworks Java.

**Q2 : Existe‑t‑il des options de licence pour Aspose.3D ?**  
R2 : Oui, vous pouvez explorer les options de licence [ici](https://purchase.aspose.com/buy).

**Q3 : Comment obtenir du support pour Aspose.3D ?**  
R3 : Visitez le [forum](https://forum.aspose.com/c/3d/18) Aspose.3D pour le support et les discussions.

**Q4 : Un essai gratuit est‑il disponible ?**  
R4 : Oui, vous pouvez obtenir un essai gratuit [ici](https://releases.aspose.com/).

**Q5 : Comment obtenir une licence temporaire pour Aspose.3D ?**  
R5 : Vous pouvez obtenir une licence temporaire [ici](https://purchase.aspose.com/temporary-license/).

## Conclusion

Félicitations ! Vous avez réussi à **convertir un maillage en FBX**, à partager les données de géométrie du maillage entre plusieurs nœuds, et à définir des couleurs de matériau individuelles en utilisant Aspose.3D pour Java. Ce flux de travail vous offre une architecture de maillage légère et réutilisable qui peut être exportée vers n’importe quel pipeline compatible FBX.

---

**Dernière mise à jour :** 2026-02-17  
**Testé avec :** Aspose.3D 24.11 for Java  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}