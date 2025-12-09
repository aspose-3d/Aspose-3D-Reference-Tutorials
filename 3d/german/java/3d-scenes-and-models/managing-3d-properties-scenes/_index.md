---
date: 2025-12-01
description: Erfahren Sie, wie Sie die Texturfarbe ändern, Materialeigenschaften zugreifen,
  Vector3‑Werte setzen und Eigenschaften nach Namen in Java‑Szenen mit Aspose.3D abrufen
  – ein vollständiges Aspose 3D‑Tutorial.
linktitle: Change texture color and manage 3D properties in Java scenes using Aspose.3D
second_title: Aspose.3D Java API
title: Texturfarbe ändern und 3D‑Eigenschaften in Java‑Szenen mit Aspose.3D verwalten
url: /de/java/3d-scenes-and-models/managing-3d-properties-scenes/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Ändern der Texturfarbe und Verwalten von 3D-Eigenschaften in Java‑Szenen mit Aspose.3D

## Einführung

In diesem **Aspose 3D‑Tutorial** erfahren Sie, wie Sie **die Texturfarbe ändern** und mit 3D‑Eigenschaften sowie benutzerdefinierten Daten in Java‑Szenen arbeiten können. Egal, ob Sie ein Spiel, einen Produktvisualisierer oder einen wissenschaftlichen Viewer erstellen, die Möglichkeit, Materialattribute zur Laufzeit zu ändern, gibt Ihnen volle künstlerische Kontrolle. Lassen Sie uns den Prozess Schritt für Schritt durchgehen, vom Laden einer Szene bis zum Anpassen der *Diffuse*-Farbe mit einem `Vector3`‑Wert.

## Schnelle Antworten
- **Was kann ich ändern?** Sie können die Texturfarbe, Deckkraft, Glanz und jede benutzerdefinierte Eigenschaft, die an ein Material angehängt ist, ändern.  
- **Welche Klasse enthält die Daten?** `Material` und seine `PropertyCollection`.  
- **Wie setze ich eine neue Farbe?** Verwenden Sie `props.set("Diffuse", new Vector3(r, g, b))`.  
- **Brauche ich eine Lizenz?** Eine temporäre Lizenz funktioniert für die Evaluierung; für die Produktion ist eine Voll‑Lizenz erforderlich.  
- **Unterstützte Formate?** FBX, OBJ, STL, GLTF und viele weitere.

## Voraussetzungen

- Java Development Kit (JDK) 8 oder neuer installiert.  
- Aspose.3D für Java‑Bibliothek (Download von der [Aspose-Website](https://releases.aspose.com/3d/java/)).  
- Grundlegende Kenntnisse der Java‑Syntax und objektorientierter Konzepte.

## Pakete importieren

Bevor Sie Logik schreiben, importieren Sie die Klassen, die Ihnen Zugriff auf Materialeigenschaften und Vektormanipulation geben.

```java
import java.io.IOException;

import com.aspose.threed.Material;
import com.aspose.threed.Property;
import com.aspose.threed.PropertyCollection;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;
```

### Warum diese Klassen importieren?

- `Scene` lädt und repräsentiert die 3D‑Datei.  
- `Material` liefert die Oberflächendefinition (Texturen, Farben usw.).  
- `PropertyCollection` ist ein wörterbuchähnlicher Container, der Ihnen ermöglicht, **Materialeigenschaften** nach Namen zu **zugreifen**.  
- `Vector3` ist der Datentyp, der für Farben und andere Vektoren mit drei Komponenten verwendet wird.

## Schritt 1: Szene initialisieren

```java
String dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
```

Wir erstellen ein `Scene`‑Objekt, indem wir eine FBX‑Datei laden, die bereits eine Textur enthält. Dies ist die Leinwand, auf der wir die **Texturfarbe ändern** werden.

## Schritt 2: Materialeigenschaften zugreifen

```java
Material material = scene.getRootNode().getChildNodes().get(0).getMaterial();
PropertyCollection props = material.getProperties();
```

Hier greifen wir die **Materialeigenschaften** des ersten Meshes in der Szene **zu**. Das `Material`‑Objekt enthält eine `PropertyCollection`, die jedes konfigurierbare Attribut speichert, wie *Diffuse*, *Specular* und benutzerdefinierte Daten.

## Schritt 3: Alle Eigenschaften auflisten

```java
for (Property prop : props) {
    System.out.println("Name" + prop.getName() + " Value = " + prop.getValue());
}
```

Das Durchlaufen von `props` gibt jeden Eigenschaftsnamen und dessen aktuellen Wert aus. Dieses schnelle Inventar hilft Ihnen, herauszufinden, welche Schlüssel Sie später ändern können, z. B. `"Diffuse"` für die Grundfarbe.

## Schritt 4: Vector3‑Wert setzen, um die Texturfarbe zu ändern

```java
props.set("Diffuse", new Vector3(1, 0, 1));
```

**Pro‑Tipp:** Der `Vector3`‑Konstruktor nimmt drei Gleitkommazahlen entgegen, die die **Rot‑, Grün‑ und Blau**‑Komponenten (Bereich 0‑1) darstellen. Das Setzen von `(1, 0, 1)` ändert die Grundfarbe der Textur zu Magenta und **ändert damit die Texturfarbe** des Modells.

## Schritt 5: Eigenschaft nach Namen abrufen

```java
Object diffuse = (Vector3) props.get("Diffuse");
System.out.println(diffuse);
```

Dies demonstriert das **Abrufen einer Eigenschaft nach Namen**. Wir casten das zurückgegebene `Object` zu `Vector3`, um programmgesteuert mit der Farbe zu arbeiten.

## Schritt 6: Auf die Eigenschaftsinstanz zugreifen

```java
Property pdiffuse = props.findProperty("Diffuse");
System.out.println(pdiffuse);
```

`findProperty` gibt das vollständige `Property`‑Objekt zurück, das Ihnen Zugriff auf Metadaten wie den Typ der Eigenschaft, die Bezeichnung und alle angehängten benutzerdefinierten Daten gibt.

## Schritt 7: Untereigenschaften einer Eigenschaft durchlaufen

```java
for (Property pp : pdiffuse.getProperties()) {
    System.out.println("Diffuse. " + pp.getName() + " = " + pp.getValue());
}
```

Einige Eigenschaften sind hierarchisch. Das Durchlaufen von `pdiffuse.getProperties()` zeigt Ihnen alle verschachtelten Attribute (z. B. Texturkoordinaten, Animationsschlüssel), die zum *Diffuse*-Eintrag gehören.

## Häufige Probleme & Lösungen

| Problem | Warum es passiert | Lösung |
|---------|-------------------|--------|
| **`NullPointerException` on `material`** | Der Knoten hat möglicherweise kein zugewiesenes Material. | Rufen Sie `node.setMaterial(new Material())` auf, bevor Sie auf Eigenschaften zugreifen. |
| **Farbe ändert sich nicht** | Das Modell verwendet eine Textur, die die *Diffuse*-Farbe überschreibt. | Deaktivieren Sie die Textur oder ändern Sie das Texturbild direkt. |
| **`ClassCastException` when retrieving** | Versuch, eine Eigenschaft, die kein Vector3 ist, zu casten. | Überprüfen Sie den Eigenschaftstyp mit `pdiffuse.getValue().getClass()` bevor Sie casten. |

## Häufig gestellte Fragen

**Q:** Wie kann ich die Aspose.3D‑Bibliothek in meinem Java‑Projekt installieren?  
**A:** Laden Sie das JAR von der [Aspose-Website](https://releases.aspose.com/3d/java/) herunter und fügen Sie es dem Klassenpfad Ihres Projekts oder den Maven/Gradle‑Abhängigkeiten hinzu.

**Q:** Gibt es kostenlose Testoptionen für Aspose.3D?  
**A:** Ja, ein voll funktionsfähiger 30‑Tage‑Test kann von der [Aspose-Testseite](https://releases.aspose.com/) erhalten werden.

**Q:** Wo finde ich detaillierte Dokumentation für Aspose.3D in Java?  
**A:** Die offizielle API‑Referenz finden Sie unter [Aspose.3D-Dokumentation](https://reference.aspose.com/3d/java/).

**Q:** Gibt es ein Support‑Forum für Aspose.3D, in dem ich Fragen stellen kann?  
**A:** Ja—besuchen Sie das [Aspose.3D-Support-Forum](https://forum.aspose.com/c/3d/18), um mit der Community und Experten in Kontakt zu treten.

**Q:** Wie kann ich eine temporäre Lizenz für Aspose.3D erhalten?  
**A:** Fordern Sie eine über die [Temporäre-Lizenz-Seite](https://purchase.aspose.com/temporary-license/) auf der Aspose-Website an.

**Q:** Kann ich andere Materialattribute außer der Farbe ändern?  
**A:** Ja, Eigenschaften wie `Specular`, `Opacity` und benutzerdefinierte Daten können mit demselben `props.set`‑Muster geändert werden.

## Fazit

Sie haben nun gelernt, wie man **die Texturfarbe ändert**, **Materialeigenschaften zugreift**, **einen Vector3‑Wert setzt** und **eine Eigenschaft nach Namen abruft** in einer Java‑Szene mit Aspose.3D. Diese Techniken geben Ihnen eine feinkörnige Kontrolle über jedes 3D‑Asset und ermöglichen dynamische visuelle Effekte sowie Laufzeit‑Anpassungen in Ihren Anwendungen.

---

**Zuletzt aktualisiert:** 2025-12-01  
**Getestet mit:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}