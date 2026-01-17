---
date: 2026-01-17
description: Erfahren Sie, wie Sie Materialeigenschaften auflisten, die Diffusfarbe
  ändern und 3D‑Materialattribute mit Aspose.3D für .NET bearbeiten. Schritt‑für‑Schritt‑Codebeispiele
  enthalten.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Auflisten von Materialeigenschaften in 3D‑Szenen mit Aspose.3D
url: /de/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Materialeigenschaften in 3D‑Szenen mit Aspose.3D auflisten

## Introduction

Wenn Sie **Materialeigenschaften** eines 3D‑Modells auflisten und anschließend Dinge wie die Diffusfarbe anpassen möchten, sind Sie hier genau richtig. Aspose.3D für .NET bietet Ihnen eine saubere, objektorientierte API, mit der Sie Materialattribute inspizieren, abrufen und ändern können, ohne Ihren C#‑Code zu verlassen. In diesem Tutorial führen wir Sie durch das Laden einer Szene, das Auflisten ihrer Materialeigenschaften und das Ändern von Werten wie der Diffuskomponente – damit Sie Ihren Modellen das gewünschte Aussehen verleihen können.

## Quick Answers
- **Was ist das Hauptziel?** Materialeigenschaften auflisten und ändern (z. B. Diffusfarbe).  
- **Welche Bibliothek wird benötigt?** Aspose.3D für .NET.  
- **Benötige ich eine Lizenz?** Für den Produktionseinsatz ist eine temporäre oder vollständige Lizenz erforderlich.  
- **Unterstützte Dateiformate?** FBX, OBJ, STL, STL‑ASCII, 3MF und weitere.  
- **Typische Implementierungsdauer?** Etwa 10‑15 Minuten für ein einfaches Skript zum Auflisten von Eigenschaften.

## What is **list material properties**?

Das Auflisten von Materialeigenschaften bedeutet, über die `PropertyCollection` eines Materials zu iterieren, um jeden Eigenschaftsnamen und dessen aktuellen Wert zu lesen. Dies ist nützlich für Debugging, visuelle Inspektion oder zum Erstellen von UI‑Steuerelementen, die es Benutzern ermöglichen, Materialeinstellungen zur Laufzeit anzupassen.

## Why use Aspose.3D to **access material properties**?
- **Keine externen Konverter** – arbeiten Sie direkt mit nativen .NET‑Objekten.  
- **Umfangreiches Eigenschaftsmodell** – unterstützt benutzerdefinierte FBX‑spezifische Attribute zusätzlich zu den Standard‑PBR‑Werten.  
- **Plattformübergreifend** – funktioniert auf .NET Framework, .NET Core und .NET 5/6+.

## Prerequisites

- Aspose.3D für .NET in Ihrem Projekt installiert. Laden Sie es [hier](https://releases.aspose.com/3d/net/) herunter.  
- Ein Ordner auf dem Datenträger, um Ihre 3‑D‑Quelldateien zu speichern (z. B. eine FBX‑Datei mit eingebetteten Texturen).

Jetzt, da Sie die Grundlagen geklärt haben, tauchen wir in den Code ein.

## Import Namespaces

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Step 1: Load 3D Scene

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Step 2: **Access material properties** of the first node

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Step 3: **List material properties** – see every name/value pair

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## Step 4: **How to change diffuse** – modify the Diffuse property

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Step 5: **Retrieve property by name** – get a strongly‑typed instance

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Step 6: Traverse a property's own properties (advanced)

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## How to **change 3d material color** beyond diffuse
Wenn Sie spekulare, ambientale oder emittierende Farben beeinflussen müssen, ersetzen Sie einfach `"Diffuse"` durch `"Specular"` oder `"Ambient"` in der oben genannten `props["..."]`‑Zuweisung. Die gleichen `Vector3`‑ oder `Vector4`‑Strukturen gelten.

## Common Pitfalls & Tips
- **Groß‑/Kleinschreibung von Eigenschaftsnamen** – Aspose.3D‑Eigenschaftsschlüssel sind case‑sensitive; verwenden Sie den genauen Namen, der in der Auflistung ausgegeben wird.  
- **Fehlende Eigenschaft** – Nicht alle Materialien stellen jedes PBR‑Attribut bereit. Prüfen Sie `props.ContainsKey("Specular")`, bevor Sie darauf zugreifen.  
- **Änderungen speichern** – Nach dem Ändern von Eigenschaften rufen Sie `scene.Save("output.fbx");` auf, um die Änderungen zu speichern.

## Conclusion

Sie haben nun gelernt, wie man **Materialeigenschaften auflistet**, **eine Eigenschaft nach Namen abruft** und **die Diffusfarbe** (oder ein anderes Materialattribut) mit Aspose.3D für .NET ändert. Experimentieren Sie mit verschiedenen Eigenschaftstypen, um das Aussehen Ihrer 3‑D‑Assets fein abzustimmen.

## FAQ's

### Q1: Kann ich Aspose.3D für .NET mit anderen 3D‑Dateiformaten verwenden?

A1: Ja, Aspose.3D unterstützt verschiedene 3D‑Dateiformate, einschließlich FBX, STL und viele weitere.

### Q2: Wie kann ich eine temporäre Lizenz für Aspose.3D für .NET erhalten?

A2: Besuchen Sie [hier](https://purchase.aspose.com/temporary-license/), um eine temporäre Lizenz zu erhalten.

### Q3: Gibt es ein Community‑Forum für Aspose.3D‑Benutzer?

A3: Ja, Sie finden Support und Diskussionen im [Aspose.3D‑Forum](https://forum.aspose.com/c/3d/18).

### Q4: Wo finde ich detaillierte Dokumentation für Aspose.3D für .NET?

A4: Siehe die [Dokumentation](https://reference.aspose.com/3d/net/) für umfassende Anleitungen.

### Q5: Kann ich Aspose.3D für .NET kostenlos testen, bevor ich kaufe?

A5: Natürlich! Laden Sie die [kostenlose Testversion](https://releases.aspose.com/) herunter, um die Funktionen zu erkunden.

## Frequently Asked Questions

**Q: Was stellt `Vector3(1, 0, 1)` dar?**  
A: Es setzt die Diffusfarbe auf Magenta (rot = 1, grün = 0, blau = 1) im linearen Farbraum.

**Q: Muss ich `scene.Save` nach dem Ändern von Eigenschaften aufrufen?**  
A: Ja, das Speichern der Szene schreibt Ihre Änderungen auf die Festplatte; andernfalls bleiben die Änderungen nur im Speicher.

**Q: Kann ich benutzerdefinierte FBX‑Attribute aufzählen?**  
A: Absolut. Die `PropertyCollection` enthält alle benutzerdefinierten Attribute, auf die Sie über `GetProperty("customName")` zugreifen können.

**Q: Gibt es eine Möglichkeit, mehrere Materialien stapelweise zu aktualisieren?**  
A: Durchlaufen Sie `scene.RootNode.ChildNodes` und wiederholen Sie die Schritte zur Eigenschaftsänderung für jedes Material.

**Q: Unterstützt Aspose.3D .NET 6?**  
A: Ja, die Bibliothek ist vollständig kompatibel mit .NET 6 und neueren Versionen.

---

**Last Updated:** 2026-01-17  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}