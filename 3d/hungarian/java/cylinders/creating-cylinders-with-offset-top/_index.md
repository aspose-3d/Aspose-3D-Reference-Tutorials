---
date: 2026-04-08
description: Tanulja meg, hogyan hozhat létre eltolással felső részt tartalmazó hengert
  az Aspose.3D for Java-ban, adjon hozzá gyermekcsomópontot Java-ban, állítsa be a
  felső eltolást, generáljon 3D modellt, és exportálja OBJ formátumba egy Aspose ideiglenes
  licenc segítségével.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Aspose ideiglenes licenc – Henger létrehozása eltolással a tetején (Java)
second_title: Aspose.3D Java API
title: Aspose ideiglenes licenc – Henger létrehozása eltolással a tetején (Java)
url: /hu/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose ideiglenes licenc – Henger létrehozása eltolással a tetején (Java)

## Bevezetés

Ha **henger létrehozása** objektumokat szeretne egy egyedi eltolással a tetején egy Java‑alapú 3D jelenetben, az Aspose.3D egyszerűvé teszi a folyamatot. Ebben az útmutatóban lépésről lépésre végigvezetjük – a jelenet beállításától a végső modell OBJ fájlként való exportálásáig –, hogy magabiztosan integrálhassa az eltolással a tetején rendelkező hengereket alkalmazásaiba. A útmutató végére megérti, hogyan teszi lehetővé egy **aspose ideiglenes licenc** ezen funkciók kiértékelését teljes vásárlás nélkül.

## Gyors válaszok
- **Melyik könyvtárat használják?** Aspose.3D for Java  
- **Eltolhatom a henger tetejét?** Yes, using `setOffsetTop`  
- **Hogyan adhatok hozzá gyermek csomópontot Java‑ban?** Call `createChildNode` on the root node  
- **Melyik formátumba exportálhatok?** Wavefront OBJ (`java export obj`)  
- **Szükségem van licencre a teszteléshez?** An **aspose temporary license** is available for evaluation  

## Mi az Aspose ideiglenes licenc?

Az **aspose ideiglenes licenc** egy rövid távú, ingyenes kiértékelő kulcs, amely feloldja az Aspose.3D for Java teljes funkciókészletét a fejlesztés és tesztelés során. Eltávolítja a kiértékelési vízjeleket, és lehetővé teszi, hogy 3D modell fájlokat, például OBJ, STL vagy FBX, ugyanúgy generáljon, mint egy fizetett licenc.

## Miért használjuk az Aspose.3D for Java‑t?

- **High‑level API:** Nem kell alacsony szintű háló adatokat kezelni.  
- **Cross‑platform:** Bármely JVM‑kompatibilis környezetben működik.  
- **Built‑in exporters:** Közvetlenül ment OBJ, STL, FBX és további formátumokba.  
- **Extensible:** Könnyen hozzáadhat gyermek csomópontokat, alkalmazhat transzformációkat, és integrálhat más Java könyvtárakkal.  

## Előfeltételek

- **Java Development Kit (JDK)** – egy kompatibilis verzió telepítve.  
- **Aspose.3D for Java library** – töltse le a legújabb JAR‑t a hivatalos oldalról [here](https://releases.aspose.com/3d/java/).  
- A kedvenc IDE-je (Eclipse, IntelliJ IDEA, NetBeans, stb.).  

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

### 1. lépés: Java 3D jelenet létrehozása

A **java 3d scene** a konténerként szolgál az összes 3D objektum számára.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### 2. lépés: Henger inicializálása eltolással a tetején

Itt válaszolunk arra, **hogyan hozhatunk létre hengert** egy egyedi eltolással. A konstruktor meghatározza a sugár, magasság, szeletek, rétegek számát, és hogy a henger zárt‑e. Ezután a `setOffsetTop`‑mal eltoljuk a tetejét.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### 3. lépés: Gyermek csomópont hozzáadása Java – Az első henger csatolása

Létrehozunk egy gyermek csomópontot a jelenet gyökér csomópontja alatt, és a hengert a kívánt helyre mozgatjuk.

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

### 5. lépés: Gyermek csomópont hozzáadása Java – A második henger csatolása

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### 6. lépés: Java Export OBJ – Jelenet mentése OBJ‑ként

Végül **java export obj**-val elmentjük az egész jelenetet (mindkét hengert) Wavefront OBJ fájlként, amelyet széles körben támogatnak a 3D eszközök.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

A program futtatásakor megtalálja a `CustomizedOffsetTopCylinder.obj` fájlt a megadott könyvtárban, készen állva a Blender, Maya vagy bármely más OBJ‑kompatibilis megjelenítőben való megnyitásra.

## Hogyan generáljunk 3D modellt és exportáljunk OBJ‑t Java‑ban

A `Scene.save(..., FileFormat.WAVEFRONTOBJ)` és az **aspose ideiglenes licenc** kombinációja lehetővé teszi, hogy gyorsan **3d modell** fájlokat **generáljunk**, anélkül, hogy külső konverterekre lenne szükség. Ez különösen hasznos prototípus készítésekor vagy amikor tervezőkkel oszt meg eszközöket.

## Valós példák

- **Architectural visualisation:** Az eltolással a tetején rendelkező hengerek oszlopokat modelleznek, amelyek a mennyezet felé keskenyebbé válnak.  
- **Mechanical parts:** Dugattyúk vagy fogaskerék házak létrehozása, ahol a felső felület szándékosan el van tolva.  
- **Game assets:** Változatos oszlopformák előállítása menet közben, csökkentve a kézzel készített hálók szükségességét.  

## Gyakori problémák és megoldások

| Probléma | Ok | Megoldás |
|----------|----|----------|
| **OBJ fájl üres** | A jelenet nincs megfelelően mentve vagy az útvonal hibás. | Ellenőrizze, hogy a kimeneti könyvtár létezik, és van írási jogosultsága. |
| **Az eltolás nem került alkalmazásra** | Régebbi Aspose.3D verzió használata. | Frissítsen a legújabb könyvtárra, ahol a `setOffsetTop` támogatott. |
| **Gyermek csomópont nem látható** | A transzformáció nem lett alkalmazva. | Győződjön meg róla, hogy a gyermek csomópont létrehozása után meghívja a `getTransform().setTranslation`‑t. |

## Gyakran ismételt kérdések

**Q: Az Aspose.3D kompatibilis különböző Java IDE‑kkel?**  
A: Igen, zökkenőmentesen működik az Eclipse, IntelliJ IDEA, NetBeans és más IDE‑kkel.

**Q: Alkalmazhatok textúrákat a létrehozott 3D objektumokra?**  
A: Természetesen! Használja a `Material` osztályt a textúrák és felületi tulajdonságok hozzárendeléséhez.

**Q: Vannak licencelési lehetőségek az Aspose.3D‑hez?**  
A: Különböző licencmodellek érhetők el; megtekintheti őket [here](https://purchase.aspose.com/buy).

**Q: Hogyan kaphatok segítséget vagy oszthatok meg tapasztalatokat?**  
A: Csatlakozzon az Aspose.3D közösségi fórumhoz [here](https://forum.aspose.com/c/3d/18) támogatás és beszélgetés céljából.

**Q: Elérhető-e ideiglenes licenc teszteléshez?**  
A: Igen, egy **aspose ideiglenes licenc** beszerezhető kiértékeléshez [here](https://purchase.aspose.com/temporary-license/).

---

**Utoljára frissítve:** 2026-04-08  
**Tesztelve:** Aspose.3D for Java 24.12 (latest)  
**Szerző:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}