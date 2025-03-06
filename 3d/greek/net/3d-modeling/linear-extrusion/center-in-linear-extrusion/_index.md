---
title: Κέντρο στη Γραμμική Εξώθηση
linktitle: Κέντρο στη Γραμμική Εξώθηση
second_title: Aspose.3D .NET API
description: Εξερευνήστε τον κόσμο της τρισδιάστατης μοντελοποίησης με το Aspose.3D για .NET. Επικεντρώστε τις τεχνικές γραμμικής εξώθησης, δημιουργήστε εντυπωσιακά σχέδια και απελευθερώστε τη δημιουργικότητά σας.
weight: 10
url: /el/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Κέντρο στη Γραμμική Εξώθηση

## Εισαγωγή

Καλώς ήλθατε σε αυτόν τον περιεκτικό οδηγό για τον έλεγχο της γραμμικής εξώθησης χρησιμοποιώντας το Aspose.3D για .NET. Αν θέλετε να βελτιώσετε τις δεξιότητές σας στην τρισδιάστατη μοντελοποίηση και να δημιουργήσετε εκπληκτικές εξωθήσεις, βρίσκεστε στο σωστό μέρος. Σε αυτό το σεμινάριο, θα εμβαθύνουμε στην τεχνική της γραμμικής εξώθησης, εστιάζοντας συγκεκριμένα στην πτυχή κεντραρίσματος για να φέρουμε τα σχέδιά σας σε ένα εντελώς νέο επίπεδο.

## Προαπαιτούμενα

Πριν ξεκινήσουμε αυτό το συναρπαστικό ταξίδι, βεβαιωθείτε ότι έχετε τις ακόλουθες προϋποθέσεις:

- Βασική κατανόηση της γλώσσας προγραμματισμού C#.
- Το Visual Studio είναι εγκατεστημένο στον υπολογιστή σας.
-  Aspose.3D για τη βιβλιοθήκη .NET, την οποία μπορείτε να κατεβάσετε από το[Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).
-  Βεβαιωθείτε ότι έχετε πρόσβαση στο[Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) για αναφορά σε όλο το σεμινάριο.

## Εισαγωγή χώρων ονομάτων

Για να ξεκινήσουμε τα πράγματα, ας εισαγάγουμε τους απαραίτητους χώρους ονομάτων. Αυτά θα θέσουν τα θεμέλια για το αριστούργημα τρισδιάστατης μοντελοποίησης.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Βήμα 1: Αρχικοποιήστε το Βασικό Προφίλ

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Βήμα 2: Δημιουργήστε μια τρισδιάστατη σκηνή

```csharp
Scene scene = new Scene();
```

## Βήμα 3: Δημιουργήστε αριστερούς και δεξιούς κόμβους

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Βήμα 4: Εκτελέστε Γραμμική Εξώθηση στον Αριστερό Κόμβο

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Βήμα 5: Ορίστε το επίπεδο εδάφους για αναφορά

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Βήμα 6: Εκτελέστε Γραμμική Εξώθηση στον Δεξιό Κόμβο

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Βήμα 7: Ορισμός επιπέδου γείωσης για αναφορά (δεξιός κόμβος)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Βήμα 8: Αποθήκευση 3D σκηνής

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## συμπέρασμα

Συγχαρητήρια! Έχετε κατακτήσει με επιτυχία την τέχνη της γραμμικής εξώθησης με κεντράρισμα χρησιμοποιώντας το Aspose.3D για .NET. Μη διστάσετε να πειραματιστείτε με διαφορετικές παραμέτρους και να εξερευνήσετε τις τεράστιες δυνατότητες που προσφέρει αυτή η τεχνική.

## Συχνές ερωτήσεις

### Ε1: Μπορώ να χρησιμοποιήσω το Aspose.3D για .NET με άλλες γλώσσες προγραμματισμού;

A1: Το Aspose.3D υποστηρίζει κυρίως γλώσσες .NET όπως C# και VB.NET.

### Ε2: Πού μπορώ να βρω υποστήριξη για ερωτήματα που σχετίζονται με το Aspose.3D;

 A2: Επισκεφθείτε το[Aspose.3D Forum](https://forum.aspose.com/c/3d/18) για αφοσιωμένη υποστήριξη και συζητήσεις.

### Ε3: Υπάρχει διαθέσιμη δωρεάν δοκιμή για το Aspose.3D για .NET;

 A3: Ναι, μπορείτε να έχετε πρόσβαση στη δωρεάν δοκιμή[εδώ](https://releases.aspose.com/).

### Ε4: Πώς μπορώ να αποκτήσω μια προσωρινή άδεια χρήσης για το Aspose.3D για .NET;

 A4: Μπορείτε να αποκτήσετε μια προσωρινή άδεια[εδώ](https://purchase.aspose.com/temporary-license/).

### Ε5: Πού μπορώ να αγοράσω την άδεια χρήσης Aspose.3D για .NET;

 A5: Αγοράστε την άδειά σας[εδώ](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
