---
date: 2026-02-25
description: Apprenez à créer des extrusions 3D en Java avec Aspose.3D et à exporter
  des fichiers OBJ en Java, en fournissant des modèles 3D de haute qualité dans les
  applications Java.
linktitle: Create 3D Extrusion Java with Aspose.3D
second_title: Aspose.3D Java API
title: Créer une extrusion 3D en Java avec Aspose.3D
url: /fr/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Créer une extrusion 3D Java avec Aspose.3D

## Introduction

Si vous devez **créer une extrusion 3d java** rapidement et de manière fiable, vous êtes au bon endroit. Dans les quelques minutes qui suivent, nous verrons comment générer une extrusion linéaire, personnaliser sa géométrie et **exporter un fichier obj java** à l’aide de la bibliothèque Aspose.3D. Que vous construisiez un outil de type CAD, une chaîne d’assets pour un jeu, ou tout autre flux de travail 3‑D basé sur Java, ce guide vous fournit une base solide, prête pour la production.

## Quick Answers
- **Que signifie « extrusion linéaire » ?** Elle balaye un profil 2‑D le long d’une ligne droite pour former un solide 3‑D.  
- **Quelle bibliothèque gère l’extrusion ?** Aspose.3D pour Java fournit une API de haut niveau.  
- **Puis‑je exporter le résultat au format OBJ ?** Oui – le tutoriel se termine par `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Ai‑je besoin d’une licence pour le développement ?** Une version d’essai gratuite suffit pour l’apprentissage ; une licence commerciale est requise pour la production.  
- **Quelle version de Java est prise en charge ?** Java 1.6 et ultérieures.

## Qu’est‑ce que Créer une extrusion 3D Java ?
Créer une extrusion 3D en Java consiste à prendre une forme 2‑D simple (comme un rectangle) et à l’étendre dans la troisième dimension. Le maillage résultant peut être enregistré dans des formats courants tels que OBJ, compris par de nombreux éditeurs 3‑D.

## Pourquoi utiliser Aspose.3D pour l’extrusion linéaire ?
- **API pure Java** – aucune dépendance native, idéal pour les projets multiplateformes.  
- **Contrôles géométriques riches** – arrondi, torsion, tranches et décalage sont tous exposés via des propriétés simples.  
- **Export direct** – sauvegarde en OBJ, STL, FBX, etc. sans convertisseurs supplémentaires.  
- **Support de niveau entreprise** – licences, documentation et forums communautaires disponibles.

## Prérequis

Avant de commencer, assurez‑vous d’avoir :

1. **Environnement de développement Java** – JDK 1.6+ installé et configuré.  
2. **Bibliothèque Aspose.3D** – Téléchargez le JAR le plus récent depuis le site officiel [ici](https://releases.aspose.com/3d/java/).  

## Import Packages

Ajoutez l’espace de noms principal d’Aspose.3D à votre fichier source Java :

```java
import com.aspose.threed.*;
```

## Étape 1 : Définir le répertoire du document

Spécifiez où les fichiers générés seront écrits :

```java
String MyDir = "Your Document Directory";
```

> **Astuce :** Utilisez un chemin absolu ou une propriété configurable afin que l’emplacement de sortie fonctionne sur tous les environnements.

## Étape 2 : Initialiser la forme de base

Créez un rectangle qui servira de profil d’extrusion. Le rayon d’arrondi adoucit les coins :

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Vous pouvez expérimenter avec `setRoundingRadius` pour obtenir un profil plus circulaire ou plus anguleux.

## Étape 3 : Effectuer l’extrusion linéaire

Nous transformons maintenant le rectangle 2‑D en objet 3‑D. Le constructeur prend le profil et la profondeur d’extrusion (10 unités dans cet exemple). D’autres propriétés affinent le maillage :

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Slices** – contrôle la fluidité de l’extrusion.  
- **Center** – aligne la géométrie autour de l’origine.  
- **Twist** – fait pivoter le profil le long de l’axe d’extrusion (ici un tour complet de 360°).  
- **TwistOffset** – déplace le pivot de torsion, démontrant comment créer des spirales.

## Étape 4 : Créer la scène 3D

Un `Scene` est le conteneur de tous les objets 3‑D. Ajouter l’extrusion comme nœud enfant l’intègre au graphe de scène :

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## Étape 5 : Enregistrer la scène 3D

Enfin, exportez la scène vers un fichier Wavefront OBJ – un format largement supporté par les éditeurs 3‑D, les moteurs de jeu et les pipelines d’impression :

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Après l’exécution du code, vous trouverez **LinearExtrusion.obj** dans le répertoire que vous avez indiqué, prêt à être ouvert dans Blender, Maya ou tout autre visualiseur compatible OBJ.

## Problèmes courants et solutions

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| `FileNotFoundException` lors de l’enregistrement | `MyDir` n’existe pas ou les permissions d’écriture sont insuffisantes | Créez le dossier au préalable ou utilisez un chemin absolu avec les permissions appropriées. |
| L’OBJ apparaît vide dans le visualiseur | Aucun géométrie n’a été ajoutée à la scène | Vérifiez que l’objet `LinearExtrusion` est correctement instancié et attaché au nœud racine. |
| La torsion est incorrecte | Valeurs de `TwistOffset` erronées | Ajustez les coordonnées du `Vector3` ; rappelez‑vous que le décalage est appliqué avant la rotation de torsion. |

## Foire aux questions

### Q1 : Aspose.3D est‑il compatible avec toutes les versions de Java ?
R1 : Aspose.3D est conçu pour fonctionner avec Java 1.6 et les versions ultérieures.

### Q2 : Puis‑je utiliser Aspose.3D pour des projets commerciaux ?
R2 : Oui, Aspose.3D peut être utilisé tant pour des projets personnels que commerciaux. Consultez les détails de licence [ici](https://purchase.aspose.com/buy).

### Q3 : Comment obtenir du support pour Aspose.3D ?
R3 : Visitez le [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour le support communautaire ou envisagez l’achat d’une [licence temporaire](https://purchase.aspose.com/temporary-license/) pour un support premium.

### Q4 : Existe‑t‑il d’autres fonctionnalités de modélisation 3D dans Aspose.3D ?
R4 : Absolument ! Explorez la documentation exhaustive [ici](https://reference.aspose.com/3d/java/) pour une liste complète des fonctionnalités et des exemples.

### Q5 : Une version d’essai gratuite est‑elle disponible pour Aspose.3D ?
R5 : Oui, vous pouvez accéder à une version d’essai gratuite [ici](https://releases.aspose.com/).

## Conclusion

Vous savez maintenant comment **créer une extrusion 3d java** avec Aspose.3D, personnaliser sa géométrie et **exporter un fichier obj java** pour les étapes suivantes. Expérimentez avec différents profils, torsions et formats d’exportation afin de répondre aux besoins spécifiques de votre projet. Lorsque vous serez prêt, explorez d’autres capacités d’Aspose.3D telles que la manipulation de maillages, le mapping de textures et l’animation pour enrichir davantage vos applications 3‑D basées sur Java.

---

**Dernière mise à jour :** 2026-02-25  
**Testé avec :** Aspose.3D 24.12 pour Java  
**Auteur :** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}