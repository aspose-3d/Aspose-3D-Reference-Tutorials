---
date: 2025-12-12
description: Tanulja meg, hogyan állíthat be anyagszínt, miközben megosztja a hálógeometriai
  adatokat, és FBX formátumban menti a jelenetet Java 3D-ben az Aspose.3D segítségével.
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: Anyag szín beállítása és háló geometriai adatainak megosztása Java 3D‑ben az
  Aspose.3D‑vel
url: /hu/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Anyag szín beállítása és hálógeometria adat megosztása Java 3D‑ben az Aspose.3D‑val

## Bevezetés

Az Aspose.3D‑val való Java 3D felfedezése rengeteg lehetőséget nyit meg lenyűgöző vizualizációk és magával ragadó élmények létrehozásához. Ebben az útmutatóban bemutatjuk, **hogyan lehet megosztani a háló** geometriai adatokat Java 3D‑ben az Aspose.3D segítségével, és megmutatjuk, **hogyan állítható be az anyag színe** minden egyes háló példányhoz. Kövesse figyelmesen a lépéseket, és a végére zökkenőmentesen tud majd háló adatokat cserélni több csomópont között, miközben a színeket szabályozza és FBX‑be exportálja.

## Gyors válaszok
- **Mi a fő cél?** Anyag szín beállítása minden csomópontnál és a háló geometriai adat megosztása.  
- **Melyik könyvtár szükséges?** Aspose.3D for Java.  
- **Hogyan exportálom az eredményt?** Mentse a jelenetet FBX fájlként (FBX7400ASCII).  
- **Szükség van licencre?** Ideiglenes vagy teljes licenc szükséges a termelési használathoz.  
- **Melyik Java verzió működik?** Bármely Java 8+ környezet.

## Előfeltételek

Mielőtt belemerülne az útmutatóba, győződjön meg róla, hogy az alábbi előfeltételek teljesülnek:

- Java fejlesztői környezet: Biztosítsa, hogy a rendszerén legyen beállítva egy Java fejlesztői környezet.  
- Aspose.3D könyvtár: Töltse le és telepítse az Aspose.3D könyvtárat. A könyvtárat megtalálja [itt](https://releases.aspose.com/3d/java/).

## Csomagok importálása

Kezdje el a szükséges csomagok importálásával a Java projektjébe. Ez a lépés elengedhetetlen az Aspose.3D könyvtár által nyújtott funkciók eléréséhez.

```java
import com.aspose.threed.*;
```

## 1. lépés: Jelenet objektum inicializálása (initialize scene java)

Indítsa el a folyamatot egy jelenet objektum inicializálásával. Ez lesz a vászon, ahol a 3D‑es varázslat kibontakozik.

```java
// Initialize scene object
Scene scene = new Scene();
```

## 2. lépés: Színvektorok definiálása

Ebben a lépésben egy színvektor tömböt definiálunk, amelyet a 3D‑es jelenet különböző elemeihez alkalmazunk.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## 3. lépés 3D háló létrehozása Java‑ban a Polygon Builder segítségével (create 3d mesh java)

Használja a Common osztályt egy háló létrehozásához a polygon builder módszerrel. Ez a háló lesz az alapja a 3D elemeinknek.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Hogyan állítható be az anyag színe minden csomópontnál?

Iteráljon a színvektorokon, hozzon létre kocka csomópontokat, és állítson be attribútumokat, mint például anyag, **set material color**, és transzláció. Ez a lépés a vizuális megjelenés vezérlésének központja minden egyes háló példánynál.

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

## 5. lépés: 3D jelenet mentése (save scene fbx, convert mesh to fbx)

Adja meg a könyvtárat és a fájlnevet a 3D jelenet mentéséhez a támogatott fájlformátumban, jelen esetben FBX7400ASCII. Ez a lépés bemutatja a **convert mesh to FBX** folyamatot is.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Összegzés

Gratulálunk! Sikeresen **beállította az anyag színét**, megosztotta a háló geometriai adatokat több csomópont között, és az eredményt FBX fájlként exportálta az Aspose.3D for Java segítségével. Ez végtelen lehetőségeket nyit meg vizuálisan lenyűgöző és interaktív 3D alkalmazások létrehozásához.

## Gyakran Ismételt Kérdések

### Q1: Használhatom az Aspose.3D‑t más Java keretrendszerekkel?

A1: Igen, az Aspose.3D úgy lett tervezve, hogy zökkenőmentesen működjön különböző Java keretrendszerekkel.

### Q2: Vannak licencelési lehetőségek az Aspose.3D‑hez?

A2: Igen, a licencelési lehetőségeket megtalálja [itt](https://purchase.aspose.com/buy).

### Q3: Hogyan kaphatok támogatást az Aspose.3D‑hez?

A3: Látogassa meg az Aspose.3D [fórumot](https://forum.aspose.com/c/3d/18) támogatás és megbeszélések céljából.

### Q4: Van ingyenes próbaidőszak?

A4: Igen, egy ingyenes próbaverziót letölthet [itt](https://releases.aspose.com/).

### Q5: Hogyan szerezhetek ideiglenes licencet az Aspose.3D‑hez?

A5: Ideiglenes licencet kaphat [itt](https://purchase.aspose.com/temporary-license/).

## További Gyakran Ismételt Kérdések

**K: Exportálhatom a jelenetet más formátumokba is, mint az FBX?**  
V: Igen, az Aspose.3D támogatja az OBJ, STL, 3MF és további formátumokat. Egyszerűen módosítsa a `FileFormat` enum értékét a `save` hívásban.

**K: Mi a teendő, ha a jelenet létrehozása után szeretném megváltoztatni az anyagot?**  
V: Szerezze meg a csomópontot, módosítsa a `LambertMaterial`‑et (pl. `setDiffuseColor`), majd mentse újra a jelenetet.

**K: Kezelni tudja a könyvtár a nagy hálókat hatékonyan?**  
V: Az Aspose.3D optimalizált adatstruktúrákat használ; azonban nagyon nagy hálók esetén érdemes streaminget vagy a jelenet felosztását alkalmazni.

**K: Van mód a színváltozás animálására?**  
V: Igen, animálhatja az anyag tulajdonságait az `AnimationController` API‑val.

---

**Utoljára frissítve:** 2025-12-12  
**Tesztelt verzió:** Aspose.3D 24.11 for Java  
**Szerző:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}