---
title: Récupérer des informations à partir de scènes 3D dans des applications Java
linktitle: Récupérer des informations à partir de scènes 3D dans des applications Java
second_title: API Java Aspose.3D
description: Explorez le monde de la manipulation de scènes 3D en Java avec Aspose.3D. Ce tutoriel vous guide pas à pas dans la récupération des informations.
type: docs
weight: 12
url: /fr/java/3d-scenes-and-models/get-scene-information/
---
## Introduction

Bienvenue dans ce guide complet sur la récupération d'informations à partir de scènes 3D dans des applications Java à l'aide d'Aspose.3D. Si vous êtes un développeur Java cherchant à améliorer les capacités de votre application grâce à la manipulation de scènes 3D, vous êtes au bon endroit. Ce didacticiel vous guidera tout au long du processus, étape par étape, en vous assurant de bien comprendre chaque concept.

## Conditions préalables

Avant de plonger dans le didacticiel, assurez-vous d'avoir les éléments suivants en place :

- Compréhension de base de la programmation Java.
-  Bibliothèque Aspose.3D installée. Sinon, téléchargez-le[ici](https://releases.aspose.com/3d/java/).
- Java IDE (Integrated Development Environment) installé et configuré.

## Importer des packages

Dans votre projet Java, importez les packages nécessaires pour exploiter les fonctionnalités Aspose.3D. Ajoutez les lignes suivantes à votre code :

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

## Étape 1 : initialiser une scène 3D

```java
// ExStart : AddAssetInformationToScene
Scene scene = new Scene();
```

 Commencez par créer une nouvelle scène 3D à l'aide d'Aspose.3D.`Scene` classe.

## Étape 2 : Définir les informations sur l'application et le fournisseur

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

Spécifiez le nom de l'application et du fournisseur associé à votre scène 3D.

## Étape 3 : Définir les unités de mesure

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

Définissez les unités de mesure de votre scène 3D. Dans cet exemple, nous utilisons des unités égyptiennes anciennes.

## Étape 4 : Enregistrer la scène dans un fichier

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd : AddAssetInformationToScene
```

Spécifiez le répertoire et le nom de fichier pour enregistrer la scène 3D. L'exemple enregistre la scène au format FBX avec encodage ASCII.

## Étape 5 : Imprimer le message de réussite

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

Affichez un message de réussite indiquant que les informations sur l'actif ont été ajoutées avec succès à la scène.

## Conclusion

Toutes nos félicitations! Vous avez appris avec succès comment récupérer des informations à partir de scènes 3D dans des applications Java à l'aide d'Aspose.3D. Cette puissante bibliothèque ouvre des possibilités infinies pour améliorer vos projets Java avec un contenu 3D immersif.

## FAQ

### Q1 : Aspose.3D est-il compatible avec tous les IDE Java ?

A1 : Oui, Aspose.3D est conçu pour fonctionner de manière transparente avec tous les principaux IDE Java.

### Q2 : Puis-je utiliser Aspose.3D pour des projets commerciaux ?

A2 : Absolument. Aspose.3D propose des licences commerciales pour les développeurs, garantissant que vous respectez les exigences de licence.

### Q3 : Où puis-je trouver une assistance supplémentaire pour Aspose.3D ?

 A3 : Pour toute question ou assistance, visitez le[Forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4 : Existe-t-il un essai gratuit disponible pour Aspose.3D ?

 A4 : Oui, vous pouvez explorer les fonctionnalités avec un essai gratuit disponible[ici](https://releases.aspose.com/).

### Q5 : Comment puis-je obtenir une licence temporaire pour Aspose.3D ?

 A5 : Obtenez une licence temporaire à des fins de test[ici](https://purchase.aspose.com/temporary-license/).