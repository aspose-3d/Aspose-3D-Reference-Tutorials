---
date: 2026-01-17
description: Μάθετε πώς να καταγράφετε τις ιδιότητες του υλικού, να αλλάζετε το χρώμα
  διάχυσης και να τροποποιείτε τις 3D ιδιότητες του υλικού χρησιμοποιώντας το Aspose.3D
  για .NET. Περιλαμβάνονται παραδείγματα κώδικα βήμα προς βήμα.
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

Αν χρειάζεστε **list material properties** ενός 3D μοντέλου και μετά θέλετε να ρυθμίσετε στοιχεία όπως το diffuse χρώμα, βρίσκεστε στο σωστό μέρος. Το Aspose.3D for .NET σας παρέχει ένα καθαρό, αντικειμενοστραφές API που σας επιτρέπει να ελέγχετε, να ανακτάτε και να τροποποιείτε ιδιότητες υλικού χωρίς να αφήσετε τον κώδικα C#. Σε αυτό το tutorial θα δούμε πώς να φορτώσουμε μια σκηνή, να απαριθμήσουμε τις ιδιότητες υλικού της και να αλλάξουμε τιμές όπως το diffuse component—ώστε να δώσετε στα μοντέλα σας την ακριβή εμφάνιση που θέλετε.

## Γρήγορες Απαντήσεις
- **Ποιος είναι ο κύριος στόχος;** Λίστα ιδιοτήτων υλικού και τροποποίηση (π.χ., χρώμα diffuse).  
- **Ποια βιβλιοθήκη απαιτείται;** Aspose.3D for .NET.  
- **Χρειάζομαι άδεια;** Απαιτείται προσωρινή ή πλήρης άδεια για παραγωγική χρήση.  
- **Υποστηριζόμενες μορφές αρχείων;** FBX, OBJ, STL, STL‑ASCII, 3MF, κ.ά.  
- **Τυπικός χρόνος υλοποίησης;** Περίπου 10‑15 λεπτά για ένα βασικό script λίστας ιδιοτήτων.

## Τι είναι η **list material properties**;
Η λίστα ιδιοτήτων υλικού σημαίνει επανάληψη πάνω στο `PropertyCollection` ενός υλικού για την ανάγνωση κάθε ονόματος ιδιότητας και της τρέχουσας τιμής της. Αυτό είναι χρήσιμο για εντοπισμό σφαλμάτων, οπτική επιθεώρηση ή δημιουργία UI ελέγχων που επιτρέπουν στους χρήστες να ρυθμίζουν τις ρυθμίσεις υλικού σε πραγματικό χρόνο.

## Γιατί να χρησιμοποιήσετε Aspose.3D για **access material properties**;
- **Χωρίς εξωτερικούς μετατροπείς** – εργασία απευθείας με εγγενή αντικείμενα .NET.  
- **Πλούσιο μοντέλο ιδιοτήτων** – υποστηρίζει προσαρμοσμένα χαρακτηριστικά FBX εκτός των τυπικών τιμών PBR.  
- **Δια‑πλατφόρμα** – λειτουργεί σε .NET Framework, .NET Core, και .NET 5/6+.  

## Προαπαιτούμενα

- Aspose.3D for .NET εγκατεστημένο στο έργο σας. Κατεβάστε το [εδώ](https://releases.aspose.com/3d/net/).  
- Ένας φάκελος στο δίσκο για να αποθηκεύσετε τα 3‑D αρχεία πηγής σας (π.χ., ένα αρχείο FBX με ενσωματωμένες υφές).

Τώρα που έχετε τα βασικά, ας βουτήξουμε στον κώδικα.

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

## Βήμα 4: **How to change diffuse** – τροποποίηση της ιδιότητας Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Βήμα 5: **Retrieve property by name** – λήψη μιας έντονα τυποποιημένης εμφάνισης

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Βήμα 6: Διέλευση των ιδιοτήτων μιας ιδιότητας (προχωρημένο)

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
Αν χρειάζεστε να επηρεάσετε τα χρώματα specular, ambient ή emissive, απλώς αντικαταστήστε το `"Diffuse"` με `"Specular"` ή `"Ambient"` στην εντολή `props["..."]` παραπάνω. Οι δομές `Vector3` ή `Vector4` παραμένουν ίδιες.

## Συνηθισμένα Πιθανά Σφάλματα & Συμβουλές
- **Διάκριση πεζών/κεφαλαίων στα ονόματα ιδιοτήτων** – τα κλειδιά ιδιοτήτων του Aspose.3D είναι case‑sensitive· χρησιμοποιήστε ακριβώς το όνομα που εμφανίζεται στην έξοδο.  
- **Απουσία ιδιότητας** – δεν εκθέτουν όλα τα υλικά κάθε χαρακτηριστικό PBR. Ελέγξτε `props.ContainsKey("Specular")` πριν την πρόσβαση.  
- **Αποθήκευση αλλαγών** – μετά την τροποποίηση, καλέστε `scene.Save("output.fbx");` για να διατηρήσετε τις αλλαγές.

## Συμπέρασμα

Μάθατε πώς να **list material properties**, να **retrieve a property by name** και να **change the diffuse color** (ή οποιαδήποτε άλλη ιδιότητα υλικού) χρησιμοποιώντας το Aspose.3D for .NET. Πειραματιστείτε με διαφορετικούς τύπους ιδιοτήτων για να βελτιώσετε την εμφάνιση των 3‑D περιουσιακών σας στοιχείων.

## Συχνές Ερωτήσεις

### Q1: Μπορώ να χρησιμοποιήσω Aspose.3D for .NET με άλλες μορφές 3D αρχείων;

A1: Ναι, το Aspose.3D υποστηρίζει διάφορες μορφές 3D αρχείων, συμπεριλαμβανομένων των FBX, STL και πολλών άλλων.

### Q2: Πώς μπορώ να αποκτήσω προσωρινή άδεια για το Aspose.3D for .NET;

A2: Επισκεφθείτε [εδώ](https://purchase.aspose.com/temporary-license/) για να αποκτήσετε μια προσωρινή άδεια.

### Q3: Υπάρχει φόρουμ κοινότητας για χρήστες του Aspose.3D;

A3: Ναι, μπορείτε να βρείτε υποστήριξη και συζητήσεις στο [Aspose.3D forum](https://forum.aspose.com/c/3d/18).

### Q4: Πού μπορώ να βρω λεπτομερή τεκμηρίωση για το Aspose.3D for .NET;

A4: Ανατρέξτε στην [documentation](https://reference.aspose.com/3d/net/) για ολοκληρωμένη καθοδήγηση.

### Q5: Μπορώ να δοκιμάσω το Aspose.3D for .NET δωρεάν πριν την αγορά;

A5: Φυσικά! Κατεβάστε την [free trial version](https://releases.aspose.com/) για να εξερευνήσετε τις δυνατότητές του.

## Συχνές Ερωτήσεις

**Q: Τι αντιπροσωπεύει το `Vector3(1, 0, 1)`;**  
A: Ορίζει το diffuse χρώμα σε ματζέντα (κόκκινο = 1, πράσινο = 0, μπλε = 1) σε γραμμικό χρωματικό χώρο.

**Q: Πρέπει να καλέσω `scene.Save` μετά την αλλαγή ιδιοτήτων;**  
A: Ναι, η αποθήκευση της σκηνής γράφει τις τροποποιήσεις στο δίσκο· διαφορετικά οι αλλαγές παραμένουν μόνο στη μνήμη.

**Q: Μπορώ να απαριθμήσω προσαρμοσμένα χαρακτηριστικά FBX;**  
A: Απόλυτα. Το `PropertyCollection` περιλαμβάνει τυχόν προσαρμοσμένα χαρακτηριστικά, στα οποία μπορείτε να έχετε πρόσβαση μέσω `GetProperty("customName")`.

**Q: Υπάρχει τρόπος να ενημερώσω μαζικά πολλαπλά υλικά;**  
A: Κάντε βρόχο μέσω `scene.RootNode.ChildNodes` και επαναλάβετε τα βήματα τροποποίησης ιδιοτήτων για κάθε υλικό.

**Q: Υποστηρίζει το Aspose.3D το .NET 6;**  
A: Ναι, η βιβλιοθήκη είναι πλήρως συμβατή με .NET 6 και νεότερες εκδόσεις.

---

**Τελευταία Ενημέρωση:** 2026-01-17  
**Δοκιμή με:** Aspose.3D 24.11 for .NET  
**Συγγραφέας:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}