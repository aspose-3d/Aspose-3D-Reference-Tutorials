---
title: Aplikujte materiály PBR na 3D objekty v Javě pomocí Aspose.3D
linktitle: Aplikujte materiály PBR na 3D objekty v Javě pomocí Aspose.3D
second_title: Aspose.3D Java API
description: Naučte se aplikovat realistické PBR materiály na 3D objekty v Javě pomocí Aspose.3D. Vylepšete vizuální kvalitu pomocí fyzicky založeného vykreslování.
type: docs
weight: 10
url: /cs/java/geometry/apply-pbr-materials-to-objects/
---
## Úvod

Vítejte v tomto podrobném průvodci aplikací materiálů PBR (Physical Based Rendering) na 3D objekty v Javě pomocí Aspose.3D. Aspose.3D je výkonná Java knihovna, která poskytuje komplexní funkce pro práci s 3D modely a scénami. V tomto tutoriálu se zaměříme na aplikaci materiálů PBR, které simulují skutečné osvětlení a vlastnosti povrchu, čímž zvyšují realističnost vašich 3D objektů.

## Předpoklady

Než se pustíme do výukového programu, ujistěte se, že máte splněny následující předpoklady:

1. Vývojové prostředí Java: Ujistěte se, že máte v systému nainstalovanou Javu.

2.  Knihovna Aspose.3D: Stáhněte a nainstalujte knihovnu Aspose.3D z[odkaz ke stažení](https://releases.aspose.com/3d/java/).

3.  Dokumentace: Viz[dokumentace](https://reference.aspose.com/3d/java/)pro Aspose.3D, abyste se seznámili s funkcemi knihovny.

4.  Dočasná licence (volitelné): Pokud nemáte licenci, můžete získat a[dočasná licence](https://purchase.aspose.com/temporary-license/) pro testování.

## Importujte balíčky

Do svého projektu Java zahrňte potřebné balíčky pro použití Aspose.3D. Přidejte do kódu následující příkazy pro import:

```java
import com.aspose.threed.*;
```

## Krok 1: Inicializujte scénu

Začněte vytvořením 3D scény pomocí Aspose.3D. Scéna slouží jako plátno pro vaše 3D objekty.

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

## Krok 2: Inicializujte materiál PBR

Vytvořte materiál PBR a přizpůsobte jeho vlastnosti, jako je kov a faktory drsnosti.

```java
// ExStart:InitializePBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

## Krok 3: Vytvořte 3D objekt

Vygenerujte 3D objekt (např. krabici), na který bude aplikován materiál PBR.

```java
// ExStart:Create3Dobject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3Dobject
```

## Krok 4: Uložte 3D scénu

Uložte 3D scénu, včetně použitého materiálu PBR, do specifického formátu souboru, jako je STL.

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
//ExEnd:Save3DScene
```

Opakujte tyto kroky pro složitější scény nebo různé objekty.

## Závěr

Gratulujeme! Úspěšně jste aplikovali materiály PBR na 3D objekt v Javě pomocí Aspose.3D. To zvyšuje vizuální přitažlivost vašich 3D modelů, díky čemuž jsou realističtější a vizuálně ohromující.

## FAQ

### Q1: Mohu použít Aspose.3D pro komerční projekty?

 A1: Ano, můžete. Navštivte[nákupní stránku](https://purchase.aspose.com/buy) pro podrobnosti o licencích.

### Q2: Jak získám podporu pro Aspose.3D?

 A2: Připojte se[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu a pomoc komunity.

### Q3: Je k dispozici bezplatná zkušební verze?

 A3: Ano, můžete prozkoumat a[zkušební verze zdarma](https://releases.aspose.com/) před nákupem.

### Q4: Kde najdu podrobnou dokumentaci k Aspose.3D?

 A4: Viz[dokumentace](https://reference.aspose.com/3d/java/) za komplexní návod.

### Q5: Jak získám dočasnou licenci pro testování?

 A5: Návštěva[tento odkaz](https://purchase.aspose.com/temporary-license/) získat dočasnou licenci.