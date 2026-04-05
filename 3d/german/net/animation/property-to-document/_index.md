---
date: 2026-03-28
description: Erfahren Sie, wie Sie einen Würfel in 3D‑Szenen mit Aspose.3D für .NET
  animieren und die animierte Szene als FBX exportieren. Dieses Handbuch zeigt, wie
  man eine Animationskurve erstellt, Keyframes bindet und 3D‑Eigenschaften animiert.
linktitle: Animating Properties to Document in 3D Scenes
second_title: Aspose.3D .NET API
title: Wie man einen Würfel in 3D‑Szenen mit Aspose.3D für .NET animiert
url: /de/net/animation/property-to-document/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Wie man einen Würfel in 3D‑Szenen mit Aspose.3D für .NET animiert

## Einführung

Wenn Sie in die Welt der 3D‑Szenenerstellung und -animation in .NET eintauchen, ist Aspose.3D Ihr bevorzugtes Toolkit. In diesem Schritt‑für‑Schritt‑Leitfaden werden wir **wie man einen Würfel animiert** untersuchen, indem wir seine Eigenschaften animieren, Animationskurven erstellen und Keyframes binden. Am Ende haben Sie einen vollständig animierten Würfel, den Sie in gängige 3D‑Formate exportieren können.

## Schnelle Antworten
- **Welche Bibliothek wird verwendet?** Aspose.3D für .NET  
- **Welche Hauptaufgabe deckt dieses Tutorial ab?** Wie man einen Würfel in einer 3D‑Szene animiert  
- **Wichtige Schritte?** Namespaces importieren, eine Szene erstellen, Keyframes binden, die Datei speichern  
- **Brauche ich eine Lizenz?** Eine kostenlose Testversion reicht zum Lernen; für die Produktion ist eine kommerzielle Lizenz erforderlich  
- **Unterstütztes Ausgabeformat?** FBX (ASCII 7500) und weitere, die von Aspose.3D unterstützt werden  

## Was bedeutet „wie man einen Würfel animiert“ in Aspose.3D?

Einen Würfel zu animieren bedeutet, seine Transformations‑Eigenschaften (wie Translation, Rotation oder Skalierung) über die Zeit hinweg mithilfe von Keyframe‑Daten zu verändern. Aspose.3D bietet eine klare API, um **Animationskurven** zu erstellen, **Keyframes zu binden** und **3D‑Eigenschaften** direkt an Szenenknoten zu animieren.

## Warum einen Würfel mit Aspose.3D animieren?
- **Vollständige .NET‑Integration** – funktioniert mit .NET Framework, .NET Core und .NET 5/6.  
- **Keine externen Abhängigkeiten** – keine Notwendigkeit für Unity oder andere Engines für einfache Animationen.  
- **Export‑Flexibilität** – animierte Szenen können als FBX, OBJ, GLTF usw. gespeichert werden, für nachgelagerte Pipelines.  

## Voraussetzungen

Bevor wir diese spannende Reise beginnen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllt haben:

- Aspose.3D für .NET: Stellen Sie sicher, dass die Bibliothek installiert ist. Sie können sie von der [Aspose.3D‑Website](https://releases.aspose.com/3d/net/) herunterladen.  
- Kenntnisse in C#: Vertrautheit mit der Programmiersprache C# ist für das Verständnis und die Umsetzung der Beispiele unerlässlich.  
- Integrierte Entwicklungsumgebung (IDE): Verwenden Sie Ihre bevorzugte IDE, z. B. Visual Studio, zum Codieren mit den Beispielen.  
- Grundlegende 3D‑Szenenkonzepte: Ein Verständnis grundlegender 3D‑Szenenkonzepte erleichtert Ihren Lernweg.  

## Namespaces importieren

Stellen Sie in Ihrem C#‑Code sicher, dass Sie die erforderlichen Namespaces für Aspose.3D importieren. Hier ist das benötigte Set:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## Schritt 1: Das Szenen‑Objekt initialisieren

Erstellen Sie eine leere Szene, die alle unsere Knoten und Animationen enthält.

```csharp
Scene scene = new Scene();
```

## Schritt 2: Mesh mit Polygon Builder erstellen

Wir erzeugen ein einfaches Würfel‑Mesh mithilfe der Hilfsmethode `Common.CreateMeshUsingPolygonBuilder()`.

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Schritt 3: Würfel‑Knoten erstellen

Fügen Sie das Würfel‑Mesh der Szene als Kindknoten des Root‑Knotens hinzu. Der Knotenname **cube1** wird später verwendet, wenn wir Keyframes binden.

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Schritt 4: Übersetzungs‑Eigenschaft finden

Um die Position des Würfels zu animieren, müssen wir seine **Translation**‑Eigenschaft im Transform des Knotens finden.

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Schritt 5: Einen Bind‑Punkt erstellen

Ein `BindPoint` verknüpft eine Szenen‑Eigenschaft mit einer Animationskurve. Hier binden wir die Übersetzungs‑Eigenschaft.

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Schritt 6: Animationskurve für die X‑Komponente binden

Jetzt erstellen wir eine Animationskurve für die **X**‑Achse. Dies demonstriert den Schritt **Animationskurve erstellen** und zeigt, wie man **Keyframes bindet**.

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Schritt 7: Animationskurve für die Z‑Komponente binden

Ähnlich animieren wir die **Z**‑Achse, um dem Würfel einen dynamischeren Bewegungsweg zu geben.

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Schritt 8: 3D‑Szene speichern

Exportieren Sie die animierte Szene in eine FBX‑Datei. Das Format `FBX7500ASCII` wird von vielen 3D‑Tools unterstützt.

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Schritt 9: Erfolgsnachricht anzeigen

Geben Sie dem Benutzer Rückmeldung, dass die Animation erfolgreich hinzugefügt wurde.

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Animierte Szene nach FBX exportieren

Eine der häufigsten Aufgaben nach der Animation eines Würfels ist das **Exportieren der animierten Szene als FBX**, damit andere 3D‑Anwendungen sie nutzen können. Der obige Code speichert die Szene bereits im FBX7500ASCII‑Format, das die Keyframe‑Daten bewahrt und nahtlos mit Tools wie Autodesk Maya, Blender und Unity funktioniert. Wenn Sie die resultierende `.fbx`‑Datei öffnen, sollten Sie den Würfel sehen, der sich entlang der X‑ und Z‑Achsen exakt wie durch die Keyframe‑Sequenzen definiert bewegt.

## Häufige Probleme und Lösungen

| Problem | Grund | Lösung |
|-------|--------|-----|
| Keine Bewegung beobachtet | Keyframe‑Zeiten stimmen nicht mit dem Wiedergabebereich überein | Stellen Sie sicher, dass die Animations‑Zeitleiste der Szene die Keyframe‑Zeiten abdeckt (0‑5 Sekunden in diesem Beispiel). |
| Falscher Dateipfad | `output` verweist auf ein nicht existierendes Verzeichnis | Erstellen Sie das Verzeichnis zuerst oder verwenden Sie einen absoluten Pfad. |
| Lizenz‑Ausnahme | Ausführung ohne gültige Lizenz in der Produktion | Wenden Sie Ihre Aspose.3D‑Lizenz an, bevor Sie das `Scene`‑Objekt erstellen. |

## Häufig gestellte Fragen

### Q1: Wo finde ich die Aspose.3D‑Dokumentation?
A1: Die Dokumentation ist [hier](https://reference.aspose.com/3d/net/) verfügbar.

### Q2: Wie lade ich Aspose.3D für .NET herunter?
A2: Sie können es von der [Release‑Seite](https://releases.aspose.com/3d/net/) herunterladen.

### Q3: Gibt es eine kostenlose Testversion?
A3: Ja, Sie können eine kostenlose Testversion [hier](https://releases.aspose.com/) erhalten.

### Q4: Wo bekomme ich Support für Aspose.3D?
A4: Besuchen Sie das [Aspose.3D‑Forum](https://forum.aspose.com/c/3d/18) für Support.

### Q5: Kann ich eine temporäre Lizenz erhalten?
A5: Ja, Sie können eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/) erhalten.

## Zusätzliche FAQ (KI‑optimiert)

**Q: Kann ich andere Eigenschaften wie Rotation oder Skalierung animieren?**  
A: Absolut. Verwenden Sie `cube1.Transform.FindProperty("Rotation")` oder `"Scale"` und binden Sie Keyframe‑Sequenzen auf dieselbe Weise.

**Q: Unterstützt Aspose.3D Interpolations‑Typen für Keyframes außer Bezier und Linear?**  
A: Ja, es unterstützt auch `Interpolation.Step` und `Interpolation.Cubic` für mehr Kontrolle.

**Q: Wie kann ich die Animation vor dem Exportieren ansehen?**  
A: Aspose.3D bietet einen einfachen Viewer in seiner API; alternativ können Sie das exportierte FBX in einem 3D‑Viewer wie Autodesk FBX Review laden.

**Q: Ist es möglich, mehrere Würfel gleichzeitig zu animieren?**  
A: Erstellen Sie separate Knoten für jeden Würfel, rufen Sie deren jeweiligen Eigenschaften ab und binden Sie unabhängige Keyframe‑Sequenzen.

## Fazit

Herzlichen Glückwunsch! Sie haben gerade **wie man einen Würfel animiert** in einer 3D‑Szene mit Aspose.3D für .NET gemeistert. Sie wissen jetzt, wie man **Animationskurven erstellt**, **Keyframes bindet** und **animierte Szene als FBX exportiert**, um statische Geometrie zum Leben zu erwecken. Experimentieren Sie gern mit Rotationen, Skalierungen oder sogar Morph‑Targets, um Ihr Animations‑Werkzeugset zu erweitern.

---

**Zuletzt aktualisiert:** 2026-03-28  
**Getestet mit:** Aspose.3D 24.11 für .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}