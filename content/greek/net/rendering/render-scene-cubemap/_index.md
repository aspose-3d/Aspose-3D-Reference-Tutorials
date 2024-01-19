---
title: Απόδοση σκηνής σε χάρτη κύβων με έξι πρόσωπα
linktitle: Απόδοση σκηνής σε χάρτη κύβων με έξι πρόσωπα
second_title: Aspose.3D .NET API
description: Δημιουργήστε εντυπωσιακούς χάρτες κυβισμού με το Aspose.3D για .NET. Ακολουθήστε τον βήμα προς βήμα οδηγό μας για την απόδοση τρισδιάστατων σκηνών σε συναρπαστικούς κυβοχάρτες έξι όψεων.
type: docs
weight: 14
url: /el/net/rendering/render-scene-cubemap/
---
## Εισαγωγή
Καλώς ήρθατε σε αυτόν τον οδηγό βήμα προς βήμα για την απόδοση μιας σκηνής σε χάρτη κυβισμού με έξι πρόσωπα χρησιμοποιώντας το Aspose.3D για .NET. Σε αυτό το σεμινάριο, θα σας καθοδηγήσουμε στη διαδικασία δημιουργίας ενός εντυπωσιακού cubemap αποδίδοντας μια τρισδιάστατη σκηνή. Το Aspose.3D είναι ένα ισχυρό API .NET που απλοποιεί τον χειρισμό τρισδιάστατων γραφικών και με αυτόν τον οδηγό, θα αξιοποιήσετε τις δυνατότητές του για να δημιουργήσετε συναρπαστικούς χάρτες κυβισμού.
## Προαπαιτούμενα
Πριν ξεκινήσουμε το σεμινάριο, βεβαιωθείτε ότι έχετε τις ακόλουθες προϋποθέσεις:
- Γνώση εργασίας για ανάπτυξη C# και .NET.
-  Εγκαταστάθηκε το Aspose.3D για .NET. Μπορείτε να το κατεβάσετε[εδώ](https://releases.aspose.com/3d/net/).
- Ένα αρχείο σκηνής 3D σε μορφή GLB (π.χ. "VirtualCity.glb") για απόδοση.
## Εισαγωγή χώρων ονομάτων
Ξεκινήστε εισάγοντας τους απαραίτητους χώρους ονομάτων για το Aspose.3D στον κώδικα C#:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## Βήμα 1: Φορτώστε τη σκηνή
Φορτώστε το αρχείο τρισδιάστατης σκηνής χρησιμοποιώντας τον ακόλουθο κώδικα:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Βήμα 2: Δημιουργήστε κάμερα και φώτα
Δημιουργήστε μια κάμερα και δύο φώτα για να φωτίσετε τη σκηνή:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## Βήμα 3: Δημιουργήστε Renderer και Render Target
Δημιουργήστε ένα renderer και έναν κύβο στόχο απόδοσης χάρτη με υφή βάθους:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Βήμα 4: Αποθήκευση προσώπων Cubemap
Αποθηκεύστε κάθε όψη του cubemap στο δίσκο με καθορισμένα ονόματα αρχείων:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## συμπέρασμα
Συγχαρητήρια! Έχετε αποδώσει με επιτυχία μια τρισδιάστατη σκηνή σε χάρτη κυβισμού χρησιμοποιώντας το Aspose.3D για .NET. Εξερευνήστε περαιτέρω επιλογές προσαρμογής και βελτιώστε τα τρισδιάστατα έργα γραφικών σας με αυτό το ισχυρό API.
## Συχνές Ερωτήσεις
### Ε: Μπορώ να χρησιμοποιήσω το Aspose.3D για .NET με άλλες μορφές αρχείων 3D;
Ναι, το Aspose.3D υποστηρίζει διάφορες μορφές αρχείων 3D, παρέχοντας ευελιξία στα έργα σας.
### Ε: Πώς μπορώ να λάβω υποστήριξη για το Aspose.3D;
 Επισκέψου το[Aspose.3D φόρουμ](https://forum.aspose.com/c/3d/18) για κοινοτική υποστήριξη και συζητήσεις.
### Ε: Υπάρχει δωρεάν δοκιμή διαθέσιμη;
 Ναι, μπορείτε να έχετε πρόσβαση στη δωρεάν δοκιμή[εδώ](https://releases.aspose.com/).
### Ε: Μπορώ να αποδώσω σκηνές με κινούμενα σχέδια χρησιμοποιώντας το Aspose.3D;
Απολύτως! Το Aspose.3D υποστηρίζει την απόδοση κινούμενων σκηνών 3D.
### Ε: Πού μπορώ να βρω λεπτομερή τεκμηρίωση;
 Αναφέρομαι στο[Aspose.3D τεκμηρίωση](https://reference.aspose.com/3d/net/) για εις βάθος πληροφορίες.