---
date: 2026-03-28
description: Μάθετε πώς να καταγράψετε τις ιδιότητες του υλικού, να αλλάζετε το διάχυτο
  χρώμα και να τροποποιείτε τα χαρακτηριστικά του 3D υλικού χρησιμοποιώντας το Aspose.3D
  για .NET. Περιλαμβάνονται παραδείγματα κώδικα βήμα‑βήμα.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Λίστα ιδιοτήτων υλικού σε 3Δ σκηνές με το Aspose.3D
url: /el/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Λίστα Ιδιοτήτων Υλικού σε 3D Σκηνές με Aspose.3D

## Εισαγωγή

Αν χρειάζεστε να **list material properties** ενός 3D μοντέλου και στη συνέχεια να ρυθμίσετε στοιχεία όπως το διάχυτο χρώμα, βρίσκεστε στο σωστό μέρος. Το Aspose.3D for .NET σας παρέχει ένα καθαρό, αντικειμενοστραφές API που σας επιτρέπει να ελέγχετε, να ανακτάτε και να τροποποιείτε τις ιδιότητες του υλικού χωρίς να αφήσετε τον κώδικα C#. Σε αυτό το tutorial θα δούμε πώς να φορτώσουμε μια σκηνή, να απαριθμήσουμε τις ιδιότητες του υλικού της και να αλλάξουμε τιμές όπως το διάχυτο συστατικό — ώστε να δώσετε στα μοντέλα σας την ακριβή εμφάνιση που θέλετε.

## Γρήγορες Απαντήσεις
- **Ποιος είναι ο κύριος στόχος;** List material properties and modify them (π.χ., diffuse color).  
- **Ποια βιβλιοθήκη απαιτείται;** Aspose.3D for .NET.  
- **Χρειάζομαι άδεια;** A temporary or full license is required for production use.  
- **Υποστηριζόμενες μορφές αρχείων;** FBX, OBJ, STL, STL‑ASCII, 3MF, and more.  
- **Τυπικός χρόνος υλοποίησης;** About 10‑15 minutes for a basic property‑listing script.

## Τι είναι **list material properties**;
Η καταγραφή των ιδιοτήτων υλικού σημαίνει την επανάληψη πάνω στο `PropertyCollection` ενός υλικού για την ανάγνωση του ονόματος κάθε ιδιότητας και της τρέχουσας τιμής της. Αυτό είναι χρήσιμο για εντοπισμό σφαλμάτων, οπτική επιθεώρηση ή δημιουργία ελέγχων UI που επιτρέπουν στους χρήστες να ρυθμίζουν τις ρυθμίσεις του υλικού σε χρόνο εκτέλεσης.

## Γιατί να χρησιμοποιήσετε Aspose.3D για **access material properties**;
- **No external converters** – εργασία απευθείας με εγγενή αντικείμενα .NET.  
- **Rich property model** – υποστηρίζει προσαρμοσμένα χαρακτηριστικά FBX εκτός από τις τυπικές τιμές PBR.  
- **Cross‑platform** – λειτουργεί σε .NET Framework, .NET Core και .NET 5/6+.  

## Προαπαιτούμενα

- Aspose.3D for .NET εγκατεστημένο στο έργο σας. Κατεβάστε το [εδώ](https://releases.aspose.com/3d/net/).
- Ένας φάκελος στο δίσκο για να αποθηκεύσετε τα 3‑D αρχεία πηγής σας (π.χ., ένα αρχείο FBX με ενσωματωμένες υφές).

Τώρα που έχετε τα βασικά τακτοποιημένα, ας βουτήξουμε στον κώδικα.

## Εισαγωγή Namespaces

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

## Βήμα 1: Φόρτωση 3D Σκηνής

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Βήμα 2: **Access material properties** του πρώτου κόμβου

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Βήμα 3: **List material properties** – δείτε κάθε ζεύγος όνομα/τιμή

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

## Βήμα 4: **How to change diffuse** – τροποποιήστε την ιδιότητα Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Βήμα 5: **Retrieve property by name** – λάβετε μια ισχυρά τυποποιημένη παρουσία

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Βήμα 6: Διαπέραση των ιδιοτήτων μιας ιδιότητας (προχωρημένο)

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

## Πώς να **change 3d material color** πέρα από το diffuse
Αν χρειάζεται να επηρεάσετε τα χρώματα specular, ambient ή emissive, απλώς αντικαταστήστε το `"Diffuse"` με το `"Specular"` ή το `"Ambient"` στην ανάθεση `props["..."]` παραπάνω. Οι ίδιες δομές `Vector3` ή `Vector4` ισχύουν.

## Πώς να **update material color in C#**
Η αλλαγή της οπτικής εμφάνισης ενός υλικού περιορίζεται στην ενημέρωση της κατάλληλης ιδιότητας στο `PropertyCollection`. Είτε θέλετε να τροποποιήσετε το diffuse, specular ή οποιοδήποτε προσαρμοσμένο χρώμα, το μοτίβο παραμένει το ίδιο:

1. Ανακτήστε την ιδιότητα με το ακριβές της όνομα (διάκριση πεζών‑κεφαλαίων).  
2. Αναθέστε μια νέα τιμή `Vector3` (RGB) ή `Vector4` (RGBA).  

Επειδή το API λειτουργεί απευθείας με αντικείμενα C#, μπορείτε να **update material color C#** κώδικα χωρίς ενδιάμεσα αρχεία ή μετατροπείς. Αυτό το καθιστά ιδανικό για επεξεργαστές σε πραγματικό χρόνο ή δίκτυα επεξεργασίας παρτίδων.

## Συνηθισμένα Προβλήματα & Συμβουλές
- **Property name case‑sensitivity** – τα κλειδιά ιδιοτήτων του Aspose.3D είναι διάκρισης πεζών‑κεφαλαίων· χρησιμοποιήστε το ακριβές όνομα που εμφανίζεται στην έξοδο της λίστας.  
- **Missing property** – Δεν εκθέτουν όλα τα υλικά κάθε PBR χαρακτηριστικό. Ελέγξτε `props.ContainsKey("Specular")` πριν την πρόσβαση.  
- **Saving changes** – Μετά την τροποποίηση των ιδιοτήτων, καλέστε `scene.Save("output.fbx");` για να αποθηκεύσετε τις αλλαγές.

## Συμπέρασμα

Τώρα έχετε μάθει πώς να **list material properties**, **retrieve a property by name**, και **change the diffuse color** (ή οποιοδήποτε άλλο χαρακτηριστικό υλικού) χρησιμοποιώντας το Aspose.3D for .NET. Πειραματιστείτε με διαφορετικούς τύπους ιδιοτήτων για να βελτιώσετε την εμφάνιση των 3‑D πόρων σας, και θυμηθείτε ότι μπορείτε να **update material color C#** με μόνο μία γραμμή κώδικα.

## Συχνές Ερωτήσεις

### Q1: Μπορώ να χρησιμοποιήσω Aspose.3D for .NET με άλλες μορφές αρχείων 3D;
A1: Ναι, το Aspose.3D υποστηρίζει διάφορες μορφές αρχείων 3D, συμπεριλαμβανομένων των FBX, STL και πολλών άλλων.

### Q2: Πώς μπορώ να αποκτήσω προσωρινή άδεια για το Aspose.3D for .NET;
A2: Επισκεφθείτε [εδώ](https://purchase.aspose.com/temporary-license/) για να αποκτήσετε προσωρινή άδεια.

### Q3: Υπάρχει φόρουμ κοινότητας για χρήστες του Aspose.3D;
A3: Ναι, μπορείτε να βρείτε υποστήριξη και συζητήσεις στο [Aspose.3D forum](https://forum.aspose.com/c/3d/18).

### Q4: Πού μπορώ να βρω λεπτομερή τεκμηρίωση για το Aspose.3D for .NET;
A4: Ανατρέξτε στην [documentation](https://reference.aspose.com/3d/net/) για ολοκληρωμένη καθοδήγηση.

### Q5: Μπορώ να δοκιμάσω το Aspose.3D for .NET δωρεάν πριν την αγορά;
A5: Φυσικά! Κατεβάστε την [free trial version](https://releases.aspose.com/) για να εξερευνήσετε τις δυνατότητές του.

## Συχνές Ερωτήσεις

**Q: Τι αντιπροσωπεύει το `Vector3(1, 0, 1)`;**  
A: Ορίζει το διάχυτο χρώμα σε ματζέντα (κόκκινο = 1, πράσινο = 0, μπλε = 1) σε γραμμικό χώρο χρώματος.

**Q: Πρέπει να καλέσω `scene.Save` μετά την αλλαγή των ιδιοτήτων;**  
A: Ναι, η αποθήκευση της σκηνής γράφει τις τροποποιήσεις σας στο δίσκο· διαφορετικά οι αλλαγές παραμένουν μόνο στη μνήμη.

**Q: Μπορώ να απαριθμήσω προσαρμοσμένα χαρακτηριστικά FBX;**  
A: Απόλυτα. Το `PropertyCollection` θα περιλαμβάνει τυχόν προσαρμοσμένα χαρακτηριστικά, τα οποία μπορείτε να προσπελάσετε μέσω `GetProperty("customName")`.

**Q: Υπάρχει τρόπος μαζικής ενημέρωσης πολλαπλών υλικών;**  
A: Επανάληψη μέσω `scene.RootNode.ChildNodes` και επανάληψη των βημάτων τροποποίησης ιδιοτήτων για κάθε υλικό.

**Q: Υποστηρίζει το Aspose.3D το .NET 6;**  
A: Ναι, η βιβλιοθήκη είναι πλήρως συμβατή με .NET 6 και νεότερες εκδόσεις.

**Τελευταία ενημέρωση:** 2026-03-28  
**Δοκιμή με:** Aspose.3D 24.11 for .NET  
**Συγγραφέας:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}