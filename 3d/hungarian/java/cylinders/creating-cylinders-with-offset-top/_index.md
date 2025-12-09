---
date: 2025-12-05
description: Tanulja meg, hogyan hozhat létre eltolódó tetejű henger modelleket az
  Aspose.3D for Java-ban, hogyan adjon hozzá gyermekcsomópont Java lépéseket, és hogyan
  exportálja egyszerűen a 3D modell OBJ fájljait.
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Hogyan készítsünk eltolásos tetejű hengert az Aspose.3D for Java-ban
url: /hu/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hogyan hozzunk létre hengeres alakzatot eltolással a tetején az Aspose.3D for Java-ban

## Bevezetés

Ha **hogyan hozzunk létre hengert** objektumokat egy egyedi eltolással a tetején egy Java‑alapú 3D jelenetben, az Aspose.3D egyszerűvé teszi a folyamatot. Ebben az útmutatóban lépésről lépésre végigvezetünk – a jelenet beállításától a végső modell OBJ fájlként történő exportálásáig – hogy magabiztosan integrálhassa az eltolásos tetejű hengereket alkalmazásaiba.

## Gyors válaszok
- **Melyik könyvtárat használják?** Aspose.3D for Java  
- **Eltolhatom a henger tetejét?** Igen, a `setOffsetTop` használatával  
- **Hogyan adhatok hozzá gyermek csomópontot Java-ban?** Hívja a `createChildNode`-t a gyökér csomóponton  
- **Milyen formátumba exportálhatok?** Wavefront OBJ (`export 3d model obj`)  
- **Szükségem van licencre a teszteléshez?** Ideiglenes licenc elérhető értékeléshez  

## Mi az a “hogyan hozzunk létre hengert” eltolással a tetején?

Egy eltolással a tetején rendelkező henger létrehozása azt jelenti, hogy a felső kör alakú felület eltolódik az alaphoz képest, lehetővé téve a kúpos vagy aszimmetrikus formák modellezését manuális csúcspont‑módosítás nélkül. Az Aspose.3D egy dedikált konstruktorral és egy `OffsetTop` tulajdonsággal biztosítja ezt néhány kódsorral.

## Miért használjuk az Aspose.3D for Java-t?

- **Magas szintű API:** Nem szükséges alacsony szintű háló adatokat kezelni.  
- **Keresztplatformos:** Bármely JVM‑kompatibilis környezetben működik.  
- **Beépített exportálók:** Közvetlenül menthet OBJ, STL, FBX és további formátumokba.  
- **Bővíthető:** Könnyen hozzáadhat gyermek csomópontokat, alkalmazhat transzformációkat, és integrálhat más Java könyvtárakkal.  

## Előfeltételek

Mielőtt belemerülnénk, győződjön meg róla, hogy rendelkezik:

- **Java Development Kit (JDK)** – egy kompatibilis verzió telepítve.  
- **Aspose.3D for Java könyvtár** – töltse le a legújabb JAR-t a hivatalos oldalról [itt](https://releases.aspose.com/3d/java/).  
- A választott IDE (Eclipse, IntelliJ IDEA, NetBeans, stb.).

## Csomagok importálása

Először importálja a szükséges osztályokat. Helyezze ezeket a nyilatkozatokat a Java fájlja tetejére:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Lépésről‑lépésre útmutató

### 1. lépés: Jelenet létrehozása

A jelenet a konténerként szolgál az összes 3D objektum számára.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### 2. lépés: Henger inicializálása eltolással a tetején

Itt válaszolunk arra, hogy **hogyan hozzunk létre hengert** egy egyedi eltolással. A konstruktor meghatározza a sugár, magasság, szeletek, rétegek számát, valamint hogy a henger zárt‑e. Ezután a `setOffsetTop` segítségével eltoljuk a tetejét.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### 3. lépés: Hogyan **adjunk hozzá gyermek csomópontot Java** – Az első henger csatolása

Létrehozunk egy gyermek csomópontot a jelenet gyökér csomópontja alatt, és a hengert a kívánt helyre helyezzük.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### 4. lépés: Második henger inicializálása (eltolás nélkül)

Összehasonlításként hozzáadunk egy szabályos hengert eltolás nélkül.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### 5. lépés: Hogyan **adjunk hozzá gyermek csomópontot Java** – A második henger csatolása

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### 6. lépés: Hogyan **exportáljunk 3d modellt OBJ‑ként** – Jelenet mentése

Végül exportáljuk az egész jelenetet (mindkét hengert) Wavefront OBJ fájlként, amelyet széles körben támogatnak a 3D eszközök.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

A program futtatásakor megtalálja a `CustomizedOffsetTopCylinder.obj` fájlt a megadott könyvtárban, készen állva a Blender, Maya vagy bármely más OBJ‑kompatibilis megjelenítőben való megnyitásra.

## Gyakori problémák és megoldások

| Probléma | Ok | Megoldás |
|----------|----|----------|
| **OBJ fájl üres** | A jelenet nincs megfelelően mentve vagy az útvonal hibás. | Ellenőrizze, hogy a kimeneti könyvtár létezik, és van írási jogosultsága. |
| **Az eltolás nem került alkalmazásra** | Régebbi Aspose.3D verzió használata. | Frissítsen a legújabb könyvtárra, ahol a `setOffsetTop` támogatott. |
| **A gyermek csomópont nem látható** | A transzformáció nem lett alkalmazva. | Győződjön meg róla, hogy a gyermek csomópont létrehozása után meghívja a `getTransform().setTranslation`‑t. |

## Gyakran Ismételt Kérdések

**Q: Az Aspose.3D kompatibilis különböző Java IDE‑kkel?**  
A: Igen, zökkenőmentesen működik az Eclipse, IntelliJ IDEA, NetBeans és más IDE‑kkel.

**Q: Alkalmazhatok textúrákat a létrehozott 3D objektumokra?**  
A: Természetesen! Használja a `Material` osztályt a textúrák és felületi tulajdonságok hozzárendeléséhez.

**Q: Vannak licencelési lehetőségek az Aspose.3D‑hez?**  
A: Különböző licencmodellek érhetők el; megtekintheti őket [itt](https://purchase.aspose.com/buy).

**Q: Hogyan kaphatok segítséget vagy oszthatom meg tapasztalataimat?**  
A: Csatlakozzon az Aspose.3D közösségi fórumhoz [itt](https://forum.aspose.com/c/3d/18) támogatás és beszélgetés céljából.

**Q: Elérhető-e ideiglenes licenc teszteléshez?**  
A: Igen, ideiglenes licenc kérhető értékeléshez [itt](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---
**Utoljára frissítve:** 2025-12-05  
3D for Java 24.12 (latest)  
**Szerző:** Aspose