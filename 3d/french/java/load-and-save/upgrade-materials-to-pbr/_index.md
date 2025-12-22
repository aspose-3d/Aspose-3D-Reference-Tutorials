---
date: 2025-12-22
description: Apprenez à exporter une scène au format glTF en Java avec Aspose.3D tout
  en passant les matériaux 3D au PBR pour un réalisme amélioré.
linktitle: Export Scene to glTF in Java with Aspose.3D
second_title: Upgrade 3D Materials to PBR
title: Exporter la scène au format glTF en Java avec Aspose.3D
url: /fr/java/load-and-save/upgrade-materials-to-pbr/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Exporter une scène en glTF avec Java et Aspose.3D – Mettre à jour les matériaux en PBR

## Introduction

Dans ce tutoriel, vous apprendrez comment **exporter une scène en glTF** avec Java et Aspose.3D tout en mettant à jour vos matériaux 3D vers le rendu physiquement basé (PBR). Passer au PBR donne à vos modèles un aspect beaucoup plus réaliste, et l’exportation au format largement supporté glTF 2.0 vous permet de partager ces actifs de haute qualité entre moteurs, navigateurs et plateformes AR/VR. Nous passerons en revue les prérequis, importerons les packages nécessaires, et détaillerons chaque exemple pas à pas afin que vous puissiez appliquer la technique dans vos propres projets.

## Réponses rapides
- **Que signifie « exporter une scène en glTF » ?** Cela convertit une scène Aspose.3D au format de fichier glTF 2.0, en conservant la géométrie, les matériaux et la hiérarchie.  
- **Pourquoi mettre à jour les matériaux en PBR d’abord ?** Les matériaux PBR correspondent directement au workflow metallic‑roughness de glTF, offrant un éclairage réaliste sans étapes de conversion supplémentaires.  
- **Ai‑je besoin d’une licence pour exécuter le code ?** Un essai gratuit suffit pour le développement ; une licence commerciale est requise pour la production.  
- **Quels IDE Java sont supportés ?** Tout IDE capable de compiler du Java (Eclipse, IntelliJ IDEA, VS Code, etc.).  
- **Puis‑je exporter de grandes scènes ?** Oui, Aspose.3D diffuse les données efficacement ; assurez‑vous simplement d’avoir suffisamment de mémoire heap pour les modèles très volumineux.

## Qu’est‑ce que « exporter une scène en glTF » ?
Exporter une scène en glTF signifie sérialiser l’ensemble de la scène 3D — maillages, nœuds, caméras, lumières et matériaux — dans le GL Transmission Format (glTF). glTF est un format ouvert optimisé pour le rendu en temps réel, ce qui le rend idéal pour le web, le mobile et les moteurs de jeu.

## Pourquoi mettre à jour les matériaux en PBR avant l’exportation ?
Les matériaux PBR (Physically‑Based Rendering) décrivent comment la lumière interagit avec les surfaces à l’aide de paramètres tels que l’albédo, le métal et la rugosité. glTF 2.0 prend en charge nativement le PBR, de sorte que convertir des matériaux Phong ou personnalisés en PBR garantit que les couleurs, les réflexions et l’ombrage restent corrects lorsqu’ils sont chargés dans n’importe quel visualiseur compatible glTF.

## Prérequis

Avant de commencer, assurez‑vous d’avoir :

1. **Aspose.3D pour Java** – téléchargez‑le depuis la [page de version](https://releases.aspose.com/3d/java/).  
2. **Environnement de développement Java** – JDK 8 ou supérieur et l’IDE de votre choix.  
3. **Répertoire de documents** – un dossier sur votre machine où vous lirez/écrirez les fichiers 3D.

## Importer les packages

Ajoutez l’espace de noms principal d’Aspose.3D à votre projet :

```java
import com.aspose.threed.*;
```

Cette unique importation vous donne accès à `Scene`, `Box`, `PhongMaterial`, `PbrMaterial`, `GltfSaveOptions` et à l’API de conversion de matériaux.

## Étape 1 : Initialiser une nouvelle scène 3D

Créez une scène vierge qui contiendra votre géométrie et vos matériaux :

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene s = new Scene();
// ExEnd:InitializeScene
```

> **Astuce :** Conservez `MyDir` comme chemin absolu pendant le développement afin d’éviter les erreurs « file‑not‑found ».

## Étape 2 : Créer une boîte avec un PhongMaterial

Nous commencerons avec une boîte simple utilisant un matériau Phong classique. Celui‑ci sera ensuite converti en matériau PBR lors de l’exportation :

```java
// ExStart:CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd:CreateBoxWithMaterial
```

> **Pourquoi Phong ?** `PhongMaterial` est facile à configurer et montre comment fonctionne la logique de conversion.

## Étape 3 : Enregistrer au format GLTF 2.0 (Exporter la scène en glTF)

Configurez les options d’enregistrement GLTF pour convertir automatiquement tout `PhongMaterial` en `PbrMaterial`. C’est le cœur de **l’exportation de scène en glTF** :

```java
// ExStart:SaveInGLTF
GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
opt.setMaterialConverter(new MaterialConverter() {
    @Override
    public Material call(Material material) {
        PhongMaterial m = (PhongMaterial) material;
        PbrMaterial ret = new PbrMaterial();
        ret.setAlbedo(m.getDiffuseColor());
        return ret;
    }
});
s.save(MyDir + "Non_PBRtoPBRMaterial_Out.gltf", opt);
// ExEnd:SaveInGLTF
```

Lorsque ce code s’exécute, la scène est écrite dans `Non_PBRtoPBRMaterial_Out.gltf`. Le `MaterialConverter` personnalisé assure que le matériau Phong est transformé en matériau PBR, de sorte que le fichier glTF résultant s’affiche avec un ombrage réaliste dans n’importe quel visualiseur glTF.

## Problèmes courants & Solutions

| Problème | Solution |
|----------|----------|
| **FileNotFoundException** lors de l’enregistrement | Vérifiez que `MyDir` pointe vers un dossier existant et que l’application dispose des permissions d’écriture. |
| **ClassCastException** dans le convertisseur | Assurez‑vous que le matériau passé au convertisseur est bien un `PhongMaterial`. Ajoutez une vérification `instanceof` si vous mélangez différents types de matériaux. |
| **Textures manquantes** après l’exportation | glTF attend que les textures soient fournies séparément ; ajoutez la gestion des textures au convertisseur si nécessaire. |

## Questions fréquentes

**Q : Aspose.3D est‑il compatible avec des environnements de développement Java autres qu’Eclipse ?**  
R : Oui, Aspose.3D fonctionne avec n’importe quel IDE Java, y compris IntelliJ IDEA, NetBeans et VS Code.

**Q : Puis‑je utiliser Aspose.3D pour des projets commerciaux ?**  
R : Oui, vous pouvez utiliser Aspose.3D tant pour des projets personnels que commerciaux. Consultez la [page d’achat](https://purchase.aspose.com/buy) pour les détails de licence.

**Q : Existe‑t‑il un essai gratuit ?**  
R : Oui, vous pouvez accéder à un essai gratuit [ici](https://releases.aspose.com/).

**Q : Où puis‑je trouver du support pour Aspose.3D ?**  
R : Explorez le [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pour obtenir de l’aide communautaire.

**Q : Comment obtenir une licence temporaire pour Aspose.3D ?**  
R : Visitez [ce lien](https://purchase.aspose.com/temporary-license/) pour les informations sur les licences temporaires.

## Conclusion

En suivant les étapes ci‑dessus, vous savez maintenant comment **exporter une scène en glTF** avec Java en utilisant Aspose.3D tout en mettant automatiquement à jour les matériaux Phong vers le PBR. Ce flux de travail vous permet de créer des actifs de haute qualité, physiquement basés, prêts pour les pipelines de rendu modernes, les visualiseurs web et les expériences AR/VR. Expérimentez avec des géométries, textures et éclairages plus complexes pour exploiter pleinement la puissance du PBR et du glTF.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Dernière mise à jour :** 2025-12-22  
**Testé avec :** Aspose.3D 24.12 pour Java  
**Auteur :** Aspose  

---