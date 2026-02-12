---
date: 2026-02-12
description: Apprenez à exporter une scène au format FBX et à récupérer les informations
  d’une scène 3D à l’aide d’Aspose.3D pour Java. Ce guide étape par étape couvre la
  définition du nom de l’application, la spécification des unités de mesure et l’exportation
  de la scène au format FBX.
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: Comment exporter une scène au format FBX et récupérer les informations de la
  scène 3D en Java
url: /fr/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

 maybe "FAQ". Keep apostrophe? We'll translate to "FAQ". Keep headings.

Also translate "Last Updated", "Tested With", "Author". Keep as French.

Make sure to keep markdown formatting.

Let's produce final content.

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Comment exporter une scène au format FBX et récupérer les informations de scène 3D en Java

## Introduction

Si vous recherchez un guide clair et pratique sur **comment exporter une scène au format FBX** tout en extrayant des métadonnées utiles de vos scènes 3D, vous êtes au bon endroit. Dans ce tutoriel, nous parcourrons chaque étape en utilisant la bibliothèque **Aspose.3D Java** : de la création d’une scène, **définition du nom de l’application**, **spécification des unités de mesure**, jusqu’à **l’exportation de la scène au format FBX**. À la fin, vous disposerez d’un fichier FBX prêt à l’emploi contenant les informations d’actif dont vous avez besoin pour les pipelines en aval.

## Réponses rapides
- **Quel est l’objectif principal ?** Exporter une scène au format FBX contenant des informations d’actif personnalisées.  
- **Quelle bibliothèque est utilisée ?** Aspose.3D pour Java.  
- **Ai‑je besoin d’une licence ?** Une version d’essai gratuite suffit pour le développement ; une licence commerciale est requise pour la production.  
- **Puis‑je changer les unités de mesure ?** Oui – utilisez `setUnitName` et `setUnitScaleFactor`.  
- **Où le fichier de sortie est‑il enregistré ?** Dans le chemin que vous spécifiez dans `scene.save(...)`.

## Prérequis

Avant de commencer, assurez‑vous d’avoir :

- Une bonne maîtrise de la syntaxe de base de Java.  
- **Aspose.3D pour Java** téléchargé et ajouté à votre projet (vous pouvez le récupérer sur la page officielle) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Votre IDE Java préféré (IntelliJ IDEA, Eclipse, NetBeans, etc.) correctement configuré.

## Importer les packages

Dans votre fichier source Java, importez les classes Aspose.3D qui gèrent les scènes et la prise en charge des formats de fichiers.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Astuce :** Gardez la liste d’importations minimale pour éviter les dépendances inutiles et améliorer les temps de compilation.

## Quel est le processus pour enregistrer un fichier FBX ?

Voici un guide concis, étape par étape, qui montre **comment ajouter des informations d’actif** à une scène puis **exporter la scène au format FBX**.

### Étape 1 : Initialiser une scène 3D

Tout d’abord, créez un objet `Scene` vide. Ce sera le conteneur de toute la géométrie, les lumières, les caméras et les métadonnées d’actif.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Étape 2 : Définir les informations d’application et de fournisseur

Ajouter des métadonnées personnalisées aide les outils en aval à identifier la source du fichier. Ici, nous **définissons le nom de l’application** et le fournisseur à l’aide de l’objet `AssetInfo`.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Pourquoi c’est important :** De nombreux pipelines filtrent ou étiquettent les actifs en fonction de l’application d’origine, ce qui rend cette étape essentielle pour les grands projets.

### Étape 3 : Définir les unités de mesure

Aspose.3D vous permet de spécifier le système d’unités utilisé par votre scène. Dans cet exemple, nous utilisons une unité égyptienne ancienne appelée « pole » avec un facteur d’échelle personnalisé.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Conseil :** Ajustez `unitScaleFactor` pour correspondre à la taille réelle de vos modèles ; 1,0 représente un mappage 1 : 1 avec l’unité choisie.

### Étape 4 : Exporter la scène au format FBX

Maintenant que les informations d’actif sont attachées, nous enregistrons la scène sous forme de fichier FBX. L’option `FileFormat.FBX7500ASCII` produit un FBX ASCII lisible par l’homme, pratique pour le débogage.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Rappel :** Remplacez `"Your Document Directory"` par un chemin absolu ou un chemin relatif au répertoire de travail de votre projet.

### Étape 5 : Afficher le message de succès

Une simple sortie console confirme que l’opération a réussi et indique où le fichier a été écrit.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Pourquoi exporter une scène au format FBX avec Aspose.3D ?

L’exportation vers FBX est une exigence courante car le FBX est largement supporté par les moteurs de jeu, les outils DCC et les pipelines AR/VR. Aspose.3D vous donne un contrôle total sur le fichier exporté — métadonnées, unités et géométrie — sans nécessiter d’application d’auteur 3D lourde. Cela rend la génération automatisée d’actifs, le traitement par lots et les conversions côté serveur rapides et fiables.

## Cas d’utilisation courants

- **Pipelines d’actifs de jeu** – intégrer les informations du créateur directement dans les fichiers FBX pour le suivi de version.  
- **Visualisation architecturale** – stocker les unités spécifiques au projet afin d’éviter les erreurs d’échelle lors de l’importation dans les moteurs de rendu.  
- **Rapports automatisés** – générer des fichiers FBX à la volée avec des métadonnées lisibles par les outils d’analyse en aval.  
- **Services 3D basés sur le cloud** – créer et exporter des scènes programmatiquement sans interface graphique, idéal pour les plateformes SaaS.

## Dépannage et astuces

| Problème | Solution |
|----------|----------|
| **Fichier introuvable après l’enregistrement** | Vérifiez que `MyDir` pointe vers un dossier existant et que votre application possède les droits d’écriture. |
| **Les unités apparaissent incorrectes dans le visualiseur externe** | Revérifiez `unitScaleFactor` ; certains visualiseurs attendent les mètres comme unité de base. |
| **Métadonnées d’actif manquantes** | Assurez‑vous d’appeler `scene.getAssetInfo()` **avant** l’enregistrement ; les modifications effectuées après `save()` ne seront pas persistées. |
| **Goulot d’étranglement de performance sur de grandes scènes** | Utilisez `scene.optimize()` avant l’enregistrement pour réduire l’utilisation de la mémoire. |
| **Le FBX ASCII est trop volumineux** | Passez au FBX binaire en utilisant `FileFormat.FBX7500` (voir FAQ). |

## FAQ

### Q1 : Aspose.3D est‑il compatible avec tous les IDE Java ?

R1 : Oui, Aspose.3D est conçu pour fonctionner sans problème avec tous les principaux IDE Java.

### Q2 : Puis‑je utiliser Aspose.3D pour des projets commerciaux ?

R2 : Absolument. Aspose.3D propose des licences commerciales pour les développeurs, vous assurant de respecter les exigences de licence.

### Q3 : Où puis‑je trouver un support supplémentaire pour Aspose.3D ?

R3 : Pour toute question ou assistance, visitez le [forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4 : Existe‑t‑il une version d’essai gratuite d’Aspose.3D ?

R4 : Oui, vous pouvez explorer les fonctionnalités avec une version d’essai gratuite disponible [ici](https://releases.aspose.com/).

### Q5 : Comment obtenir une licence temporaire pour Aspose.3D ?

R5 : Obtenez une licence temporaire à des fins de test [ici](https://purchase.aspose.com/temporary-license/).

## Questions fréquemment posées

**Q : Comment changer le format de sortie en FBX binaire ?**  
R : Remplacez `FileFormat.FBX7500ASCII` par `FileFormat.FBX7500` lors de l’appel à `scene.save(...)`.

**Q : Puis‑je ajouter des métadonnées définies par l’utilisateur au‑delà des champs d’actif intégrés ?**  
R : Oui, utilisez `scene.getUserData().add("Key", "Value")` pour intégrer des paires clé‑valeur supplémentaires.

**Q : Aspose.3D prend‑il en charge d’autres formats d’exportation comme OBJ ou GLTF ?**  
R : Oui. Changez simplement l’énumération `FileFormat` en `OBJ` ou `GLTF2` selon vos besoins.

**Q : Quelle version de Java est requise ?**  
R : Aspose.3D pour Java prend en charge Java 8 et versions ultérieures.

**Q : Est‑il possible de charger un FBX existant, modifier ses informations d’actif et le réenregistrer ?**  
R : Tout à fait. Chargez le fichier avec `new Scene("input.fbx")`, modifiez `scene.getAssetInfo()`, puis enregistrez.

## Conclusion

Vous disposez maintenant d’un flux de travail complet et prêt pour la production permettant **d’exporter une scène au format FBX** tout en intégrant des informations d’actif précieuses telles que le nom de l’application, le fournisseur et des unités de mesure personnalisées. Cette approche rationalise la gestion des actifs, réduit la saisie manuelle et garantit que les outils en aval reçoivent tout le contexte nécessaire. N’hésitez pas à explorer d’autres formats d’exportation, à ajouter des données utilisateur personnalisées ou à intégrer ce code dans des pipelines d’automatisation plus vastes.

---

**Dernière mise à jour :** 2026-02-12  
**Testé avec :** Aspose.3D pour Java 24.11  
**Auteur :** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}