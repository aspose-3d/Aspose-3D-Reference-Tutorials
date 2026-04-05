---
date: 2026-02-25
description: Apprenez à inverser le système de coordonnées et à personnaliser l'importation
  3D à l'aide d'Aspose.3D LoadOptions en Java. Guide étape par étape pour 3DS, OBJ,
  STL, U3D, glTF, PLY, X et éventuellement FBX.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Inverser le système de coordonnées – Personnaliser le chargement de fichiers
  3D en Java avec Aspose.3D
url: /fr/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Système de coordonnées inversé – Personnaliser le chargement de fichiers 3D en Java avec Aspose.3D

Dans le paysage en constante évolution de la conception et du développement 3D, **inverser le système de coordonnées** lors de l’importation de modèles est une exigence courante. Que vous convertissiez des actifs d’un système droit à un système gauche ou que vous deviez aligner les modèles avec les conventions d’axes de votre moteur, Aspose.3D pour Java vous offre un contrôle granulaire. Ce tutoriel vous guide pour **personnaliser l’importation 3D** à l’aide de `LoadOptions` d’Aspose.3D, en couvrant les formats les plus populaires tels que 3DS, OBJ, STL, U3D, glTF, PLY, X et le FBX optionnel.

## Réponses rapides
- **Que fait « inverser le système de coordonnées » ?** Cela échange les axes X/Y/Z pour correspondre à la convention de coordonnées cible.  
- **Quels formats prennent en charge l’inversion ?** Tous les principaux formats (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) exposent une option `setFlipCoordinateSystem`.  
- **Ai‑je besoin de bibliothèques supplémentaires ?** Seulement le JAR Aspose.3D pour Java ; aucun convertisseur externe n’est requis.  
- **Puis‑je charger les matériaux en même temps ?** Oui — utilisez `setEnableMaterials(true)` pour les fichiers OBJ.  
- **Une licence est‑elle requise pour la production ?** Une licence Aspose.3D valide est nécessaire pour les déploiements non‑essai.

## Qu’est‑ce que « inverser le système de coordonnées » ?
Inverser le système de coordonnées modifie l’orientation des axes utilisés par le modèle importé. Cela est essentiel lorsque le fichier source utilise une main différente (droit vs. gauche) de celle de votre moteur de rendu, évitant ainsi que les modèles apparaissent en miroir ou inversés.

## Pourquoi personnaliser l’importation 3D ?
Personnaliser l’importation vous permet de :
- Conserver les transformations d’animation (`setApplyAnimationTransform`).  
- Corriger la gestion des couleurs (`setGammaCorrectedColor`).  
- Résoudre les chemins des ressources externes via `getLookupPaths()`.  
- Optimiser l’utilisation de la mémoire en ne chargeant que ce dont vous avez besoin.

## Prérequis

- Compréhension de base de la programmation Java.  
- JDK (Java Development Kit) installé.  
- Bibliothèque Aspose.3D pour Java téléchargée. Vous pouvez l’obtenir [ici](https://releases.aspose.com/3d/java/).  
- Familiarité avec les formats de fichiers 3D tels que 3DS, OBJ, STL, U3D, glTF, PLY, X et FBX.

## Importer les packages

Dans votre projet Java, assurez‑vous d’importer les packages Aspose.3D nécessaires :

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Comment personnaliser l’importation 3D avec LoadOptions

Vous trouverez ci‑dessous des extraits de code pas à pas qui démontrent comment activer l’option **inverser le système de coordonnées** pour chaque format pris en charge. Les extraits sont prêts à être copiés dans votre projet ; remplacez simplement `"Your Document Directory"` par le chemin réel de vos actifs.

### Étape 1 : Personnaliser le chargement d’un fichier 3DS

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### Étape 2 : Personnaliser le chargement d’un fichier OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Étape 3 : Personnaliser le chargement d’un fichier STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Étape 4 : Personnaliser le chargement d’un fichier U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Étape 5 : Personnaliser le chargement d’un fichier glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Étape 6 : Personnaliser le chargement d’un fichier PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Étape 7 : Personnaliser le chargement d’un fichier X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Étape 8 : Personnaliser le chargement d’un fichier FBX (Optionnel)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## Problèmes courants et solutions
- **Le modèle apparaît en miroir après le chargement** – Vérifiez que `setFlipCoordinateSystem(true)` est bien défini pour le format concerné.  
- **Les matériaux sont manquants** – Pour les fichiers OBJ, assurez‑vous que `setEnableMaterials(true)` est activé et que les fichiers de matériaux (.mtl) se trouvent dans l’un des chemins de recherche.  
- **Les coordonnées de texture sont inversées** – Pour glTF, il peut être nécessaire d’ajouter `setFlipTexCoordV(true)` en plus de l’inversion des axes.  
- **Erreurs « fichier introuvable »** – Ajoutez le répertoire contenant les ressources externes (textures, fichiers auxiliaires) à `loadOpts.getLookupPaths()`.

## Conclusion

En exploitant les `LoadOptions` d’Aspose.3D, vous pouvez **inverser le système de coordonnées** et **personnaliser l’importation 3D** pour pratiquement tous les formats majeurs. Ce niveau de contrôle élimine le besoin de scripts de post‑traitement et garantit que vos actifs sont rendus correctement du premier coup.

## Questions fréquemment posées

### Q1 : Où puis‑je trouver la documentation Aspose.3D pour Java ?
R1 : La documentation est disponible [ici](https://reference.aspose.com/3d/java/).

### Q2 : Comment télécharger Aspose.3D pour Java ?
R2 : Vous pouvez le télécharger [ici](https://releases.aspose.com/3d/java/).

### Q3 : Existe‑t‑il un essai gratuit ?
R3 : Oui, vous pouvez accéder à l’essai gratuit [ici](https://releases.aspose.com/).

### Q4 : Où obtenir du support pour Aspose.3D pour Java ?
R4 : Visitez le forum de support [ici](https://forum.aspose.com/c/3d/18).

### Q5 : Ai‑je besoin d’une licence temporaire pour les tests ?
R5 : Oui, obtenez une licence temporaire [ici](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Dernière mise à jour :** 2026-02-25  
**Testé avec :** Aspose.3D pour Java 24.11 (dernière version)  
**Auteur :** Aspose