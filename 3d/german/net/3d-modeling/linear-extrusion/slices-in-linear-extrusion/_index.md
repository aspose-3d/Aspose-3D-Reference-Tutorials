---
date: 2026-01-09
description: Erfahren Sie, wie Sie eine 3D‑Szene erstellen und ein 3D‑Modell mit Aspose.3D
  für .NET speichern, einschließlich des Exports von Wavefront‑OBJ und linearen Extrusionsschnitten.
linktitle: Create 3D Scene with Linear Extrusion Slices
second_title: Aspose.3D .NET API
title: 3D‑Szene mit linearen Extrusionsscheiben erstellen
url: /de/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Erstellen einer 3D‑Szene mit linearen Extrusionsabschnitten

## Einführung

Willkommen in der Welt des 3D‑Designs mit Aspose.3D für .NET! In diesem Tutorial werden Sie **create 3d scene**‑Objekte erstellen, lineare Extrusion mit benutzerdefinierten Slice‑Anzahlen anwenden und schließlich **save 3d model** als Wavefront‑OBJ‑Datei speichern. Egal, ob Sie einen schnellen Prototypen oder eine produktionsreife Visualisierung erstellen, die nachfolgenden Schritte zeigen Ihnen **how to use Aspose**, um hochwertige Geometrie direkt aus C# zu erzeugen.

## Schnelle Antworten
- **What does “create 3d scene” mean?** Es bedeutet, ein Scene‑Objekt zu bauen, das alle 3D‑Entitäten (Meshes, Lichter, Kameras) enthält.  
- **Which format is used for export?** Das Beispiel exportiert zu **Wavefront OBJ** (`export wavefront obj`).  
- **How many slices can I set?** Sie können jede ganze Zahl setzen; die Demo zeigt 2 und 10 Slices.  
- **Do I need a license?** Eine temporäre oder vollständige Lizenz ist für den Produktionseinsatz erforderlich.  
- **Can I run this on .NET Core?** Ja, Aspose.3D unterstützt .NET Framework und .NET Core.

## Voraussetzungen

Bevor Sie in die Welt des 3D‑Designs mit Aspose.3D eintauchen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

- Aspose.3D for .NET Library: Stellen Sie sicher, dass Sie die Aspose.3D‑Bibliothek installiert haben. Sie können sie von [hier](https://releases.aspose.com/3d/net/) herunterladen.

- Integrated Development Environment (IDE): Verwenden Sie eine bevorzugte IDE, die mit .NET‑Entwicklung kompatibel ist.

- Basic Understanding of C#: Machen Sie sich mit den Grundlagen der Programmiersprache C# vertraut.

- Desire to Explore 3D Design: Eine Leidenschaft dafür, visuell beeindruckende 3D‑Modelle zu erstellen!

## Namespaces importieren

Um Ihre 3D‑Design‑Reise mit Aspose.3D zu starten, müssen Sie die erforderlichen Namespaces importieren. Dadurch kann Ihr Code auf die benötigten Klassen und Funktionen zugreifen.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Wie man eine 3d scene mit Linear Extrusion erstellt

Im Folgenden führen wir Sie Schritt für Schritt durch den Aufbau der Szene, die Anwendung der Extrusion und das **save 3d model** als OBJ‑Datei. Die Erklärungen sind in einem lockeren Ton gehalten, damit Sie leicht folgen können.

### Schritt 1: Basisprofil initialisieren

Zuerst definieren wir die 2‑D‑Form, die extrudiert werden soll. In diesem Fall ein Rechteck mit abgerundeten Ecken.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Schritt 2: Eine 3D‑Szene erstellen

Ein `Scene`‑Objekt ist der Container für alle Geometrien, Lichter und Kameras – das Kernstück des **creating a 3d scene**.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Schritt 3: Linke und rechte Knoten erstellen

Wir fügen dem Szenen‑Root zwei Kindknoten hinzu. Einer verwendet eine niedrige Slice‑Anzahl, der andere eine höhere, sodass Sie den visuellen Unterschied sehen können.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Schritt 4: Lineare Extrusion am linken Knoten durchführen

Hier extrudieren wir das Rechteck mit **2 slices**. Weniger Slices ergeben ein gröberes Aussehen.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Schritt 5: Lineare Extrusion am rechten Knoten durchführen

Jetzt extrudieren wir dasselbe Profil, jedoch mit **10 slices**, was eine glattere Oberfläche erzeugt.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Schritt 6: 3D‑Szene speichern

Abschließend exportieren wir die Szene in eine Wavefront‑OBJ‑Datei. Dies demonstriert **how to save obj** und **export wavefront obj** mit Aspose.3D.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Häufige Probleme und Lösungen

| Problem | Warum es passiert | Lösung |
|---------|-------------------|--------|
| OBJ‑Datei erscheint leer | Der Ausgabepfad ist falsch oder es fehlen Schreibrechte. | Stellen Sie sicher, dass das Verzeichnis existiert und die Anwendung Schreibzugriff hat. |
| Slices beeinflussen die Glätte nicht | Der Wert `Slices` ist für die Geometriegröße zu niedrig. | Erhöhen Sie die Slice‑Anzahl oder passen Sie die Profilabmessungen an. |
| Lizenz‑Ausnahme | Ausführung ohne gültige Lizenz in einem Nicht‑Trial‑Build. | Wenden Sie eine temporäre oder permanente Lizenz an mit `License license = new License(); license.SetLicense("Aspose.3D.lic");` |

## Häufig gestellte Fragen

**Q: Kann ich Aspose.3D für .NET mit anderen Programmiersprachen verwenden?**  
A: Aspose.3D ist primär für .NET konzipiert, Sie können jedoch Interoperabilitätsoptionen mit Sprachen wie Python über .NET‑Bindings erkunden.

**Q: Wo finde ich detaillierte Dokumentation für Aspose.3D für .NET?**  
A: Siehe die Dokumentation [hier](https://reference.aspose.com/3d/net/) für tiefgehende Informationen zu den Fähigkeiten und der Nutzung von Aspose.3D.

**Q: Gibt es eine kostenlose Testversion für Aspose.3D für .NET?**  
A: Ja, Sie können Ihre kostenlose Testversion [hier](https://releases.aspose.com/) herunterladen, um die Funktionen der Bibliothek vor einem Kauf zu erkunden.

**Q: Wie erhalte ich technischen Support für Aspose.3D für .NET?**  
A: Besuchen Sie das Aspose.3D‑Forum [hier](https://forum.aspose.com/c/3d/18), um Unterstützung zu erhalten und sich mit der Community auszutauschen.

**Q: Kann ich eine temporäre Lizenz für Aspose.3D für .NET verwenden?**  
A: Ja, erhalten Sie eine temporäre Lizenz [hier](https://purchase.aspose.com/temporary-license/) für Evaluierungszwecke.

## Fazit

Herzlichen Glückwunsch! Sie haben erfolgreich gelernt, wie man **create 3d scene** erstellt, lineare Extrusion mit benutzerdefinierten Slice‑Anzahlen anwendet und **save 3d model** als Wavefront‑OBJ‑Datei mit Aspose.3D für .NET speichert. Dies ist erst der Anfang Ihrer 3D‑Design‑Reise – experimentieren Sie gern mit verschiedenen Profilen, Slice‑Werten und Exportformaten, um das volle Potenzial von **3d modeling c#** auszuschöpfen.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Zuletzt aktualisiert:** 2026-01-09  
**Getestet mit:** Aspose.3D 24.11 für .NET  
**Autor:** Aspose