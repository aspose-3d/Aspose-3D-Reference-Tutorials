---
date: 2026-02-20
description: Apprenez un tutoriel Java de graphisme 3D sur le contrôle du centre lors
  d’une extrusion linéaire avec Aspose.3D, y compris comment définir le rayon d’arrondi
  et enregistrer un fichier OBJ en Java.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Tutoriel Java 3D – Centre dans l’extrusion linéaire
url: /fr/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tutoriel Java 3D Graphics – Centre dans l’extrusion linéaire

## Introduction

Si vous créez des visualisations 3D en Java, maîtriser les techniques d’extrusion est essentiel. Ce **java 3d graphics tutorial** vous guide dans le contrôle du centre d’une extrusion linéaire à l’aide d’Aspose.3D for Java, afin que vous puissiez créer des modèles précis et symétriques sans calculs supplémentaires. À la fin de ce guide, vous comprendrez pourquoi la propriété `center` est importante, comment **définir le rayon d’arrondi**, et comment **enregistrer le fichier OBJ compatible java**.

## Réponses rapides
- **Que fait la propriété center ?** Elle détermine si l’extrusion est symétrique autour de l’origine du profil.  
- **Ai‑je besoin d’une licence pour exécuter le code ?** Une licence temporaire suffit pour les tests ; une licence complète est requise en production.  
- **Quel format de fichier est utilisé pour le résultat ?** La scène est enregistrée au format Wavefront OBJ.  
- **Puis‑je modifier le nombre de tranches ?** Oui, utilisez `setSlices(int)` sur l’objet `LinearExtrusion`.  
- **Aspose.3D est‑il compatible avec Java 8+ ?** Absolument – il prend en charge toutes les versions modernes de Java.

## Qu’est‑ce qu’un java 3d graphics tutorial ?

Un **java 3d graphics tutorial** explique pas à pas comment utiliser les bibliothèques Java pour créer, manipuler et rendre des objets tridimensionnels. Dans ce cas, nous nous concentrons sur l’API d’extrusion d’Aspose.3D, qui transforme des profils 2‑D en maillages 3‑D complets.

## Pourquoi utiliser Aspose.3D for Java ?

- **API de haut niveau** – Pas besoin d’écrire des calculs de maillage bas‑niveau.  
- **Support multi‑format** – Exportation vers OBJ, FBX, STL, et plus encore.  
- **Performance optimisée** – Gère efficacement les scènes volumineuses.  
- **Documentation riche** – Inclut des exemples comme celui ci‑dessous.

## Prérequis

Avant de commencer, assurez‑vous d’avoir :

1. **Environnement de développement Java** – JDK 8 ou version supérieure installé.  
2. **Aspose.3D for Java** – Téléchargez la bibliothèque et la documentation [ici](https://reference.aspose.com/3d/java/).  
3. **Répertoire de documents** – Créez un dossier sur votre machine pour stocker les fichiers générés ; nous l’appellerons **« Your Document Directory »**.

## Importer les packages

Dans votre IDE Java, importez les classes Aspose.3D dont vous aurez besoin. Cela donne au compilateur l’accès aux fonctionnalités d’extrusion et de construction de scène.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Guide étape par étape

### Étape 1 : Configurer le profil de base

Tout d’abord, créez la forme 2‑D qui sera extrudée. Ici nous utilisons un rectangle et **définissons le rayon d’arrondi** à 0,3, ce qui adoucit les coins.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Étape 2 : Créer une scène 3D

Un objet `Scene` agit comme conteneur pour tous les nœuds 3‑D, lumières et caméras.

```java
Scene scene = new Scene();
```

### Étape 3 : Ajouter les nœuds gauche et droit

Nous placerons deux nœuds séparés côte à côte afin que vous puissiez comparer l’extrusion avec et sans centrage.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Étape 4 : Extrusion linéaire – Sans centre (nœud gauche)

Créez l’extrusion sur le nœud gauche, désactivez le centrage, et limitez le maillage à trois tranches pour un aperçu low‑poly.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Étape 5 : Ajouter un plancher de référence (nœud gauche)

Une boîte fine sert de sol visuel, vous aidant à voir l’orientation de l’extrusion.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Étape 6 : Extrusion linéaire – Centré (nœud droit)

Répétez maintenant l’extrusion, cette fois en activant `center`. La géométrie sera symétrique autour de l’origine du profil.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Étape 7 : Ajouter un plancher de référence (nœud droit)

Même plancher pour le côté droit, afin de rendre la comparaison claire.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Étape 8 : Enregistrer la scène 3D

Enfin, exportez la scène complète au format Wavefront OBJ – un format immédiatement utilisable dans la plupart des éditeurs 3‑D.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problèmes courants et solutions

| Problème | Pourquoi cela se produit | Solution |
|----------|--------------------------|----------|
| **L’extrusion apparaît décalée** | `setCenter(false)` laisse le profil ancré à son coin. | Utilisez `setCenter(true)` pour des résultats symétriques. |
| **Le fichier OBJ est vide** | Le chemin du répertoire de sortie est incorrect ou les permissions d’écriture manquent. | Vérifiez que `MyDir` pointe vers un dossier existant et que l’application possède les droits d’écriture. |
| **Les coins arrondis semblent nets** | Le rayon d’arrondi est trop petit par rapport à la taille du rectangle. | Augmentez la valeur du rayon (par ex., `setRoundingRadius(0.5)`). |

## FAQ

### Q1 : Puis‑je utiliser Aspose.3D for Java dans des projets commerciaux ?

R1 : Oui, Aspose.3D for Java est disponible pour une utilisation commerciale. Pour les détails de licence, consultez [ici](https://purchase.aspose.com/buy).

### Q2 : Existe‑t‑il une version d’essai gratuite ?

R2 : Oui, vous pouvez explorer une version d’essai gratuite d’Aspose.3D for Java [ici](https://releases.aspose.com/).

### Q3 : Où puis‑je obtenir du support pour Aspose.3D for Java ?

R3 : Le forum communautaire Aspose.3D est un excellent endroit pour demander de l’aide et partager vos expériences. Visitez le forum [ici](https://forum.aspose.com/c/3d/18).

### Q4 : Ai‑je besoin d’une licence temporaire pour les tests ?

R4 : Oui, si vous avez besoin d’une licence temporaire pour les tests, vous pouvez en obtenir une [ici](https://purchase.aspose.com/temporary-license/).

### Q5 : Où puis‑je trouver la documentation ?

R5 : La documentation d’Aspose.3D for Java est disponible [ici](https://reference.aspose.com/3d/java/).

## Conclusion

En terminant ce **java 3d graphics tutorial**, vous savez maintenant comment contrôler le centre d’une extrusion linéaire, ajuster le rayon d’arrondi, et **enregistrer le fichier OBJ java** à l’aide d’Aspose.3D. Ces techniques vous offrent un contrôle fin de la symétrie des maillages, essentiel pour les actifs de jeu, les prototypes CAD et les visualisations scientifiques. N’hésitez pas à expérimenter avec différents profils, nombres de tranches et formats d’exportation pour enrichir votre boîte à outils 3‑D.

---

**Dernière mise à jour :** 2026-02-20  
**Testé avec :** Aspose.3D for Java 24.11  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}