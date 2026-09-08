---
date: 2026-09-08
description: Μάθετε πώς να ορίσετε units και να εξάγετε ένα scene σε FBX με Java χρησιμοποιώντας
  Aspose.3D. Αυτός ο οδηγός βήμα‑βήμα δείχνει πώς να ρυθμίσετε το application name,
  τα measurement units και να ανακτήσετε 3D scene information.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Πώς να αποθηκεύσετε FBX και να ανακτήσετε 3D Scene Info με Java
og_description: Μάθετε πώς να ορίσετε units και να εξάγετε ένα scene σε FBX με Java
  χρησιμοποιώντας Aspose.3D. Ο οδηγός καλύπτει τη ρύθμιση του application name, των
  measurement units, και την ανάκτηση 3D scene info σε λίγα βήματα.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Πώς να ορίσετε units και να εξάγετε scene σε FBX με Java
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Πώς να ορίσετε units και να εξάγετε scene σε FBX με Java
url: /el/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Πώς να ορίσετε μονάδες και να εξάγετε τη σκηνή σε FBX με Java

## Εισαγωγή

Αν ψάχνετε για έναν σαφή, πρακτικό οδηγό σχετικά με **πώς να ορίσετε μονάδες** και **να εξάγετε μια σκηνή σε FBX** ενώ εξάγετε χρήσιμα μεταδεδομένα από τις 3D σκηνές σας, βρίσκεστε στο σωστό μέρος. Σε αυτό το tutorial θα περάσουμε βήμα‑βήμα χρησιμοποιώντας τη βιβλιοθήκη **Aspose.3D for Java**: από τη δημιουργία μιας σκηνής, **ορισμό του ονόματος της εφαρμογής**, **ορισμό μονάδων μέτρησης**, μέχρι τελικά **την εξαγωγή της σκηνής σε FBX**. Στο τέλος θα έχετε ένα έτοιμο αρχείο FBX που μεταφέρει τις πληροφορίες του περιουσιακού στοιχείου που χρειάζεστε για τις επόμενες διαδικασίες.

## Γρήγορες απαντήσεις
- **Ποιος είναι ο κύριος στόχος;** Εξαγωγή μιας σκηνής σε FBX που περιέχει προσαρμοσμένες πληροφορίες περιουσιακού στοιχείου.  
- **Ποια βιβλιοθήκη χρησιμοποιείται;** Aspose.3D for Java.  
- **Χρειάζομαι άδεια;** Μια δωρεάν δοκιμή λειτουργεί για ανάπτυξη· απαιτείται εμπορική άδεια για παραγωγή.  
- **Μπορώ να αλλάξω τις μονάδες μέτρησης;** Ναι – χρησιμοποιήστε `setUnitName` και `setUnitScaleFactor`.  
- **Πού αποθηκεύεται το αποτέλεσμα;** Στο μονοπάτι που καθορίζετε στο `scene.save(...)`.  

## Προαπαιτούμενα

Πριν ξεκινήσουμε, βεβαιωθείτε ότι έχετε:

- Καλή κατανόηση της βασικής σύνταξης της Java.  
- **Aspose.3D for Java** κατεβασμένο και προστιθέμενο στο έργο σας (μπορείτε να το αποκτήσετε από την επίσημη) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Το αγαπημένο σας IDE για Java (IntelliJ IDEA, Eclipse, NetBeans κ.λπ.) σωστά ρυθμισμένο.

## Εισαγωγή πακέτων

Στο αρχείο πηγαίου κώδικα Java, εισάγετε τις κλάσεις Aspose.3D που παρέχουν υποστήριξη διαχείρισης σκηνής και μορφής αρχείου.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Συμβουλή:** Κρατήστε τη λίστα εισαγωγών ελάχιστη για να αποφύγετε περιττές εξαρτήσεις και να βελτιώσετε τους χρόνους μεταγλώττισης.

## Ποια είναι η διαδικασία αποθήκευσης ενός αρχείου FBX;

Για να αποθηκεύσετε μια σκηνή ως αρχείο FBX, δημιουργείτε ένα `Scene`, ορίζετε τυχόν επιθυμητά μεταδεδομένα περιουσιακού στοιχείου, ορίζετε τη μονάδα μέτρησης και, στη συνέχεια, καλείτε `scene.save(path, FileFormat.FBX7500ASCII)`. Αυτή η ακολουθία γράφει τη γεωμετρία, τα υλικά και τα μεταδεδομένα σε ένα ASCII FBX που μπορεί να ελεγχθεί ή να εισαχθεί από επόμενα εργαλεία.

### Βήμα 1: αρχικοποίηση 3D σκηνής

Η κλάση `Scene` είναι το κορυφαίο κοντέινερ της Aspose.3D που αντιπροσωπεύει ολόκληρη μια 3D σκηνή, συμπεριλαμβανομένης της γεωμετρίας, των φωτισμών, των καμερών και των μεταδεδομένων. Πρώτα, δημιουργήστε ένα κενό αντικείμενο `Scene`. Αυτό θα είναι το κοντέινερ για όλη τη γεωμετρία, τα φώτα, τις κάμερες και τα μεταδεδομένα περιουσιακού στοιχείου.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Πώς να ορίσετε το όνομα της εφαρμογής σε Java

Το αντικείμενο `AssetInfo` αποθηκεύει μεταδεδομένα όπως το όνομα της εφαρμογής, ο προμηθευτής και η έκδοση για τη σκηνή. Η προσθήκη προσαρμοσμένων μεταδεδομένων βοηθά τα επόμενα εργαλεία να αναγνωρίσουν την πηγή του αρχείου. Χρησιμοποιήστε το αντικείμενο `AssetInfo` για να **ορίσετε το όνομα της εφαρμογής** (και του προμηθευτή) πριν αποθηκεύσετε το αρχείο.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Γιατί είναι σημαντικό:** Πολλές αλυσίδες επεξεργασίας φιλτράρουν ή ετικετοποιούν περιουσιακά στοιχεία βάσει της εφαρμογής προέλευσης, καθιστώντας αυτό το βήμα απαραίτητο για μεγάλα έργα.

### Βήμα 3: ορισμός μονάδων μέτρησης

Το σύστημα μονάδων καθορίζει την πραγματική κλίμακα της σκηνής· η Aspose.3D σας επιτρέπει να καθορίσετε ένα όνομα μονάδας και έναν συντελεστή κλίμακας σε σχέση με τα μέτρα. Σε αυτό το παράδειγμα χρησιμοποιούμε μια αρχαία αιγυπτιακή μονάδα που ονομάζεται «pole» με προσαρμοσμένο συντελεστή κλίμακας.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Συμβουλή:** Ρυθμίστε το `unitScaleFactor` ώστε να ταιριάζει με το πραγματικό μέγεθος των μοντέλων σας· 1.0 αντιπροσωπεύει αντιστοίχιση 1‑προς‑1 με την επιλεγμένη μονάδα.

### Βήμα 4: εξαγωγή σκηνής σε FBX

Τώρα που τα στοιχεία του περιουσιακού στοιχείου έχουν προσαρτηθεί, αποθηκεύουμε τη σκηνή ως αρχείο FBX. Η επιλογή `FileFormat.FBX7500ASCII` παράγει ένα ανθρώπινα αναγνώσιμο ASCII FBX, χρήσιμο για εντοπισμό σφαλμάτων.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Θυμηθείτε:** Αντικαταστήστε το `"Your Document Directory"` με απόλυτο μονοπάτι ή με μονοπάτι σχετικό με τον φάκελο εργασίας του έργου σας.

## Γιατί να εξάγετε σκηνή σε FBX με Aspose.3D;

Η Aspose.3D υποστηρίζει **πάνω από 50 μορφές εισόδου και εξόδου** και μπορεί να επεξεργαστεί σκηνές πολλαπλών εκατοντάδων σελίδων χωρίς να φορτώνει ολόκληρο το αρχείο στη μνήμη, παρέχοντάς σας πλήρη έλεγχο του εξαγόμενου αρχείου — μεταδεδομένα, μονάδες και γεωμετρία — χωρίς την ανάγκη βαριάς εφαρμογής 3D δημιουργίας. Αυτό καθιστά την αυτόματη δημιουργία περιουσιακών στοιχείων, την επεξεργασία σε παρτίδες και τις μετατροπές στο διακομιστή γρήγορες και αξιόπιστες.

## Κοινές περιπτώσεις χρήσης

- **Διαδρόμους περιουσιακών στοιχείων παιχνιδιών** – ενσωματώστε πληροφορίες δημιουργού απευθείας σε αρχεία FBX για παρακολούθηση εκδόσεων.  
- **Αρχιτεκτονική απεικόνιση** – αποθηκεύστε μονάδες ειδικές για το έργο ώστε να αποφύγετε σφάλματα κλιμάκωσης κατά την εισαγωγή σε μηχανές απόδοσης.  
- **Αυτοματοποιημένη αναφορά** – δημιουργήστε αρχεία FBX εν κινήσει με μεταδεδομένα που μπορούν να διαβάσουν τα επόμενα εργαλεία ανάλυσης.  
- **Υπηρεσίες 3D βασισμένες στο cloud** – δημιουργήστε και εξάγετε σκηνές προγραμματιστικά χωρίς GUI, ιδανικό για πλατφόρμες SaaS.

## Αντιμετώπιση προβλημάτων & συμβουλές

| Πρόβλημα | Λύση |
|----------|------|
| **Το αρχείο δεν βρέθηκε μετά την αποθήκευση** | Επαληθεύστε ότι το `MyDir` δείχνει σε έναν υπάρχον φάκελο και ότι η εφαρμογή σας έχει δικαιώματα εγγραφής. |
| **Οι μονάδες εμφανίζονται λανθασμένες σε εξωτερικό πρόγραμμα προβολής** | Ελέγξτε ξανά το `unitScaleFactor`; ορισμένα προγράμματα προβολής αναμένουν τα μέτρα ως βασική μονάδα. |
| **Τα μεταδεδομένα περιουσιακού στοιχείου λείπουν** | Βεβαιωθείτε ότι καλείτε το `scene.getAssetInfo()` **πριν** την αποθήκευση· οι αλλαγές μετά το `save()` δεν θα διατηρηθούν. |
| **Σ bottleneck απόδοσης σε μεγάλες σκηνές** | Χρησιμοποιήστε `scene.optimize()` πριν την αποθήκευση για μείωση της χρήσης μνήμης. |
| **Το ASCII FBX είναι πολύ μεγάλο** | Μεταβείτε σε δυαδικό FBX χρησιμοποιώντας `FileFormat.FBX7500` (δείτε τις Συχνές Ερωτήσεις). |

## Συχνές ερωτήσεις

**Ε: Πώς αλλάζω τη μορφή εξόδου σε δυαδικό FBX;**  
Α: Αντικαταστήστε το `FileFormat.FBX7500ASCII` με `FileFormat.FBX7500` όταν καλείτε `scene.save(...)`.

**Ε: Μπορώ να προσθέσω προσαρμοσμένα μεταδεδομένα ορισμένα από τον χρήστη πέρα από τα ενσωματωμένα πεδία περιουσιακού στοιχείου;**  
Α: Ναι, χρησιμοποιήστε `scene.getUserData().add("Key", "Value")` για να ενσωματώσετε επιπλέον ζεύγη κλειδί‑τιμή.

**Ε: Η Aspose.3D υποστηρίζει άλλες μορφές εξαγωγής όπως OBJ ή GLTF;**  
Α: Ναι. Απλώς αλλάξτε το enum `FileFormat` σε `OBJ` ή `GLTF2` όπως απαιτείται.

**Ε: Ποια έκδοση της Java απαιτείται;**  
Α: Η Aspose.3D for Java υποστηρίζει Java 8 και μεταγενέστερες.

**Ε: Είναι δυνατόν να φορτώσετε ένα υπάρχον FBX, να τροποποιήσετε τις πληροφορίες του περιουσιακού στοιχείου και να το αποθηκεύσετε ξανά;**  
Α: Απόλυτα. Φορτώστε το αρχείο με `new Scene("input.fbx")`, τροποποιήστε το `scene.getAssetInfo()`, και στη συνέχεια αποθηκεύστε.

---

**Τελευταία ενημέρωση:** 2026-09-08  
**Δοκιμή με:** Aspose.3D for Java 24.11  
**Συγγραφέας:** Aspose

## Σχετικά μαθήματα

- [Μείωση μεγέθους αρχείου 3D – Συμπίεση σκηνών με Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Πώς να ορίσετε χρώμα vector3 σε Java: Αλλαγή Diffuse Color και Διαχείριση 3D ιδιοτήτων σε σκηνές Java χρησιμοποιώντας Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}