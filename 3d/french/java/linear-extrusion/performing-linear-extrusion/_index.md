---
date: 2025-12-18
description: Apprenez à extruder des formes en Java avec Aspose.3D, créez une scène
  3D et exportez facilement des fichiers Wavefront OBJ.
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: Comment extruder une forme en Java avec Aspose.3D extrusion linéaire
url: /fr/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Réalisation d'une extrusion linéaire avec Aspose.3D pour Java

## Introduction

Bienvenue dans ce tutoriel complet sur **how to extrude shape** avec Aspose.3D pour Java ! Si vous souhaitez améliorer vos compétences en modélisation 3D avec Java, vous êtes au bon endroit. Nous vous guiderons à travers la création d’une scène 3D, l’exécution d’une extrusion linéaire et l’exportation du résultat sous forme de fichier Wavefront OBJ — le tout avec des exemples de code clairs, étape par étape.

## Quick Answers
- **What is linear extrusion?** Extension d’un profil 2D le long d’un chemin droit pour créer un solide 3D.  
- **Which library handles this in Java?** Aspose.3D for Java.  
- **Can I export to OBJ?** Oui, en utilisant la fonction d’export Wavefront OBJ.  
- **Do I need a license for development?** Un essai gratuit suffit pour les tests ; une licence est requise pour la production.  
- **What Java version is required?** Java 1.6 ou version ultérieure.

## What is “how to extrude shape”?
L’extrusion linéaire est une technique fondamentale en **3d modeling java** qui transforme un profil plat — comme un rectangle — en un objet volumétrique en le tirant sur une distance définie. Cette méthode est largement utilisée pour créer des pièces mécaniques, des éléments architecturaux et des modèles décoratifs.

## Why use Aspose.3D for linear extrusion?
- **Full control** sur la géométrie (tranches, torsion, décalage).  
- **Seamless integration** avec les projets Java — aucune dépendance native.  
- **Built‑in exporters** pour les formats populaires, y compris Wavefront OBJ, facilitant la **generate 3d model** des fichiers pour les pipelines en aval.

## Prerequisites

Avant de plonger dans le tutoriel, assurez-vous d’avoir les prérequis suivants :

1. **Java Development Environment** – un JDK (1.6 ou plus récent) et votre IDE préféré.  
2. **Aspose.3D Library** – téléchargez et installez la bibliothèque depuis le site officiel **[here](https://releases.aspose.com/3d/java/)**.

## Import Packages

Une fois votre environnement de développement configuré et la bibliothèque Aspose.3D installée, importez le package nécessaire :

```java
import com.aspose.threed.*;
```

### Step 1: Set Document Directory

Définissez le dossier où les fichiers générés seront enregistrés :

```java
String MyDir = "Your Document Directory";
```

> Cela garantit que l’opération **generate 3d model** écrit le fichier OBJ à un emplacement connu.

### Step 2: Initialize Base Shape

Créez un rectangle qui servira de profil d’extrusion :

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Vous pouvez ajuster le rayon d’arrondi pour obtenir des coins arrondis ou le régler à `0` pour un rectangle parfait.

### Step 3: Perform Linear Extrusion

Nous extrudons maintenant le rectangle le long de l’axe Z, ajoutons des tranches, activons le centrage et appliquons une torsion avec un décalage :

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Extrusion length** – `10` unités.  
- **Slices** – `100` pour une géométrie lisse.  
- **Twist** – `360°` crée une rotation complète.  
- **Twist offset** – déplace l’origine de la torsion à `(10, 0, 0)`.

### Step 4: Create 3D Scene

Créez un conteneur de scène et ajoutez l’extrusion en tant que nœud enfant. Cette étape **creates 3d scene** qui peut contenir plusieurs objets :

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### Step 5: Save 3D Scene

Exportez la scène vers un fichier Wavefront OBJ. Cela montre les capacités de **wavefront obj export** et **save 3d obj** :

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Après l’exécution du code, vous trouverez `LinearExtrusion.obj` dans le répertoire que vous avez spécifié, prêt à être ouvert dans n’importe quel visualiseur 3D ou à être traité davantage.

## Common Issues and Solutions

| Issue | Reason | Fix |
|-------|--------|-----|
| Le fichier OBJ est vide | Le chemin du répertoire de sortie est incorrect ou non inscriptible | Vérifiez que `MyDir` pointe vers un dossier existant avec des permissions d’écriture. |
| La torsion n’est pas appliquée | `setCenter(true)` omis | Assurez‑vous que le centrage est activé ou ajustez les valeurs de `setTwistOffset`. |
| Erreur de compilation sur `LinearExtrusion` | Utilisation d’une version plus ancienne d’Aspose.3D | Mettez à jour vers la dernière version d’Aspose.3D. |

## Frequently Asked Questions

**Q : Aspose.3D est‑il compatible avec toutes les versions de Java ?**  
R : Aspose.3D fonctionne avec Java 1.6 et versions ultérieures.

**Q : Puis‑je utiliser Aspose.3D pour des projets commerciaux ?**  
R : Oui, l’utilisation commerciale est autorisée avec une licence valide. Vous pouvez en obtenir une **[here](https://purchase.aspose.com/buy)**.

**Q : Où puis‑je obtenir de l’aide cas de problème ?**  
R : Consultez le **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** pour l’aide de la communauté ou achetez une **[temporary license](https://purchase.aspose.com/temporary-license/)** pour un support premium.

**Q : Quelles autres fonctionnalités de modélisation 3D Aspose.3D propose‑t‑il ?**  
R : La bibliothèque inclut la manipulation de maillages, les opérations booléennes, le mapping de textures, et bien plus. Voir la liste complète **[here](https://reference.aspose.com/3d/java/)**.

**Q : Existe‑t‑il une version d’essai gratuite ?**  
R : Oui, vous pouvez télécharger une version d’essai **[here](https://releases.aspose.com/)**.

## Conclusion

Vous avez maintenant appris **how to extrude shape** avec Aspose.3D pour Java, créé une scène 3D et exporté le résultat sous forme de fichier Wavefront OBJ. Cette technique ouvre la porte à une large gamme de projets **3d modeling java** — des pièces simples aux assemblages complexes. Explorez des fonctionnalités supplémentaires comme les opérations booléennes ou le mapping de textures pour enrichir davantage vos modèles.

---

**Last Updated:** 2025-12-18  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## TARGET KEYWORDS:

**Primary Keyword (HIGHEST PRIORITY):**
how to extrude shape

**Secondary Keywords (SUPPORTING):**
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj