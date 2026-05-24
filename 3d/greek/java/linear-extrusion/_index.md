---
date: 2026-05-24
description: Μάθετε πώς να εξωθήσετε σχήμα χρησιμοποιώντας το Aspose.3D for Java.
  Αυτό το java 3d modeling tutorial καλύπτει linear extrusion, center control, direction,
  slices, twist και πολλά άλλα!
keywords:
- how to extrude shape
- java 3d geometry
- create 3d model java
- create solid from 2d
linktitle: Δημιουργία 3D Μοντέλων με Linear Extrusion σε Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  headline: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  type: TechArticle
- description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  name: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  steps:
  - name: Define the 2‑D profile
    text: Create a `Polygon` or `Polyline` that represents the shape you want to extrude.
      *A `Polygon` represents a closed shape defined by vertices, while a `Polyline`
      is an open series of line segments.* Ready to get started? [Perform Linear Extrusion
      Now](./performing-linear-extrusion/) For a detailed tuto
  - name: Configure extrusion options
    text: 'Set the center, direction, slices, twist, and twist offset on an `Extrusion`
      object. *The `Extrusion` class encapsulates all parameters needed to generate
      a 3‑D mesh from a 2‑D profile.* Get hands‑on with center control: [Control Center
      in Linear Extrusion](./controlling-center/) Read more about cen'
  - name: Add the extrusion to the scene
    text: 'Instantiate a `Scene`, attach the extrusion mesh, and export to your desired
      format. *`Scene` is the container that holds all 3‑D objects and handles exporting
      to various file formats.* Ready to set the direction? [Explore Now](./setting-direction/)
      Learn more about direction: [Setting Direction in '
  - name: Export or render
    text: 'Use `Scene.save()` to write the model to OBJ, STL, or any supported format.
      *`Scene.save()` writes the entire scene to the specified file format, applying
      any necessary post‑processing.* Start specifying slices: [Learn More](./specifying-slices/)
      Detailed guide: [Specifying Slices in Linear Extrusio'
  type: HowTo
- questions:
  - answer: Yes, a valid Aspose license is required for production use, but a free
      trial is available for evaluation.
    question: Can I use Aspose.3D for Java in a commercial project?
  - answer: The library works with Java 8 and newer runtimes, including Java 11, 17,
      and 21.
    question: Which Java versions are supported?
  - answer: Aspose.3D handles mesh generation efficiently, but you can call `scene.dispose()`
      when you’re done with large scenes to free native resources.
    question: Do I need to manage memory for large extrusions?
  - answer: Absolutely – you can create several extrusion objects, position them independently,
      and add them to the same scene.
    question: Can I combine multiple extrusion operations in one model?
  - answer: Yes, the “Applying Twist” and “Using Twist Offset” tutorials demonstrate
      how to set both properties on the same extrusion object.
    question: Is there sample code for applying twist and twist offset together?
  type: FAQPage
second_title: Aspose.3D Java API
title: Πώς να Εξωθήσετε Σχήμα - Δημιουργία 3D Μοντέλων με Linear Extrusion σε Java
url: /el/java/linear-extrusion/
weight: 23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Πώς να Εξωθήσετε Σχήμα – Δημιουργία 3D Μοντέλων με Γραμμική Εξώθηση σε Java

Αν ποτέ αναρωτηθήκατε **πώς να εξωθήσετε σχήμα** σε μια εφαρμογή Java, βρίσκεστε στο σωστό μέρος. Σε αυτό το tutorial θα περάσουμε από τις δυνατότητες γραμμικής εξώθησης του Aspose.3D for Java, δείχνοντάς σας πώς να μετατρέψετε απλά 2‑D προφίλ σε πλήρη 3‑D μοντέλα. Είτε χτίζετε έναν προβολέα τύπου CAD, μια αλυσίδα δημιουργίας περιουσιακών στοιχείων για παιχνίδια, ή απλώς πειραματίζεστε με γεωμετρία, η κατανόηση της γραμμικής εξώθησης θα σας δώσει την αυτοπεποίθηση να δημιουργήσετε σύνθετα σχήματα με λίγες μόνο γραμμές κώδικα.

## Σύντομες Απαντήσεις
- **Τι είναι η γραμμική εξώθηση;** Μετατρέπει ένα 2‑D σκίτσο σε ένα 3‑D στερεό επεκτείνοντάς το κατά μια κατεύθυνση.  
- **Ποια βιβλιοθήκη σας βοηθά;** Το Aspose.3D for Java παρέχει ένα ευέλικτο API για εργασίες εξώθησης.  
- **Χρειάζομαι άδεια;** Μια δωρεάν δοκιμή λειτουργεί για εκμάθηση· απαιτείται εμπορική άδεια για παραγωγή.  
- **Ποια έκδοση Java απαιτείται;** Java 8 ή νεότερη.  
- **Μπορώ να εφαρμόσω στρίψιμο ή μετατοπίσεις;** Ναι – το API υποστηρίζει γωνία στρίψιμου και offset στρίψιμου έτοιμα προς χρήση.  

## Τι είναι το “πώς να εξωθήσετε σχήμα” σε Java;
Η λειτουργία `Extrusion` είναι το κεντρικό χαρακτηριστικό του Aspose.3D που μετατρέπει ένα επίπεδο περίγραμμα σε ένα όγκο πλέγμα. Με απλά λόγια, παρέχετε ένα 2‑D προφίλ (π.χ. ένα ορθογώνιο ή ένα προσαρμοσμένο πολύγωνο), λέτε στη μηχανή πόσο μακριά να το τραβήξει, και η βιβλιοθήκη δημιουργεί τη 3‑D γεωμετρία για εσάς.

## Γιατί να χρησιμοποιήσετε Aspose.3D for Java;
Το Aspose.3D υποστηρίζει **50+ μορφές εισόδου και εξόδου** – συμπεριλαμβανομένων των OBJ, STL, FBX και GLTF – και μπορεί να δημιουργήσει πλέγματα με έως και **10 000 κορυφές ανά εξώθηση** χωρίς να φορτώνει ολόκληρη τη σκηνή στη μνήμη. Η πλατφόρμα του λειτουργεί σε Windows, Linux και macOS, παρέχοντας συνεπή αποτελέσματα είτε εργάζεστε σε επιτραπέζιο σταθμό εργασίας είτε σε headless CI server.

## Προαπαιτούμενα
- Java 8 ή νεότερη εγκατεστημένη στο μηχάνημά σας.  
- Maven ή Gradle για διαχείριση εξαρτήσεων.  
- Αρχείο άδειας Aspose.3D for Java (προαιρετικό για δοκιμή).  

## Πώς λειτουργεί η γραμμική εξώθηση;
Η γραμμική εξώθηση δημιουργεί ένα 3‑D στερεό σκάνοντας ένα 2‑D προφίλ κατά μια ευθεία γραμμή. Η μηχανή πρώτα τριγωνοποιεί το προφίλ, στη συνέχεια το αντιγράφει σε κάθε τομή κατά τον άξονα εξώθησης, και τέλος ενώνει τις τομές για να σχηματίσει ένα αδιάβροχο πλέγμα. Αυτή η διαδικασία υπολογίζει αυτόματα τις κανονικές και τις συντεταγμένες UV, ώστε να μπορείτε να αποδώσετε το αποτέλεσμα χωρίς πρόσθετη επεξεργασία γεωμετρίας.

## Ποιοι είναι οι βασικοί παράμετροι για μια γραμμική εξώθηση;
Η γραμμική εξώθηση μπορεί να προσαρμοστεί με αρκετές παραμέτρους. Το **center** ορίζει το σημείο περιστροφής του προφίλ πριν την εξώθηση. Το διανύσμα **direction** καθορίζει τον άξονα εξώθησης, προεπιλεγμένο στον θετικό άξονα Z. Τα **slices** ελέγχουν πόσες ενδιάμεσες διατομές θα δημιουργηθούν, επηρεάζοντας την ομαλότητα για στριμμένες ή στενές μορφές. Η **twist angle** περιστρέφει το προφίλ προοδευτικά από την αρχή μέχρι το τέλος, ενώ το **twist offset** προσθέτει μια γραμμική μετατόπιση κατά τον άξονα, επιτρέποντας σπειροειδείς μορφές.

- **Center** – Το σημείο περιστροφής γύρω από το οποίο το προφίλ τοποθετείται πριν την εξώθηση.  
- **Direction** – Ένα διανύσμα που ορίζει τον άξονα εξώθησης· η προεπιλογή είναι ο θετικός άξονας Z.  
- **Slices** – Ο αριθμός των ενδιάμεσων διατομών· περισσότερες τομές προσφέρουν πιο ομαλές μεταβάσεις για στριμμένες ή στενές εξώθησεις.  
- **Twist Angle** – Η συνολική περιστροφή που εφαρμόζεται στο προφίλ από την αρχή μέχρι το τέλος, εκφρασμένη σε μοίρες.  
- **Twist Offset** – Μια γραμμική μετατόπιση που μετακινεί το προφίλ κατά τον άξονα εξώθησης ενώ στριφογυρίζει, επιτρέποντας σπειροειδείς μορφές.

## Εκτέλεση Γραμμικής Εξώθησης σε Aspose.3D for Java

Φορτώστε το προφίλ σας, διαμορφώστε τις παραμέτρους και αφήστε το API να δημιουργήσει το πλέγμα. Τα παρακάτω βήματα περιγράφουν τη συνήθη ροή εργασίας.

### Βήμα 1: Ορισμός του 2‑D προφίλ
Δημιουργήστε ένα `Polygon` ή `Polyline` που αντιπροσωπεύει το σχήμα που θέλετε να εξωθήσετε.  
*Ένα `Polygon` αντιπροσωπεύει ένα κλειστό σχήμα ορισμένο από κορυφές, ενώ ένα `Polyline` είναι μια ανοιχτή σειρά τμημάτων γραμμής.*  
Ready to get started? [Εκτελέστε τη Γραμμική Εξώθηση Τώρα](./performing-linear-extrusion/)  
Για λεπτομερή tutorial, δείτε [Performing Linear Extrusion in Aspose.3D for Java](./performing-linear-extrusion/).

### Βήμα 2: Διαμόρφωση επιλογών εξώθησης
Ορίστε το center, direction, slices, twist και twist offset σε ένα αντικείμενο `Extrusion`.  
*Η κλάση `Extrusion` περιλαμβάνει όλες τις παραμέτρους που απαιτούνται για τη δημιουργία ενός 3‑D πλέγματος από ένα 2‑D προφίλ.*  
Get hands‑on with center control: [Control Center in Linear Extrusion](./controlling-center/)  
Read more about center control: [Controlling Center in Linear Extrusion with Aspose.3D for Java](./controlling-center/)

### Βήμα 3: Προσθήκη της εξώθησης στη σκηνή
Δημιουργήστε ένα `Scene`, προσθέστε το πλέγμα εξώθησης και εξάγετε στο επιθυμητό φορμάτ.  
*Το `Scene` είναι το κοντέινερ που κρατά όλα τα 3‑D αντικείμενα και διαχειρίζεται την εξαγωγή σε διάφορα φορμάτ αρχείων.*  
Ready to set the direction? [Explore Now](./setting-direction/)  
Learn more about direction: [Setting Direction in Linear Extrusion with Aspose.3D for Java](./setting-direction/)

### Βήμα 4: Εξαγωγή ή απόδοση
Χρησιμοποιήστε `Scene.save()` για να γράψετε το μοντέλο σε OBJ, STL ή οποιοδήποτε υποστηριζόμενο φορμάτ.  
*Το `Scene.save()` γράφει ολόκληρη τη σκηνή στο καθορισμένο φορμάτ αρχείου, εφαρμόζοντας τυχόν απαραίτητες μετα-επεξεργασίες.*  
Start specifying slices: [Learn More](./specifying-slices/)  
Detailed guide: [Specifying Slices in Linear Extrusion with Aspose.3D for Java](./specifying-slices/)

## Πώς να εφαρμόσετε στρίψιμο σε μια εξώθηση;
Εφαρμόστε στρίψιμο ορίζοντας την ιδιότητα `twistAngle` στις επιλογές εξώθησης. Η μηχανή περιστρέφει κάθε τομή αναλογικά, δημιουργώντας ένα ελικοειδές εφέ. Ρυθμίζοντας τη γωνία μπορείτε να παράγετε από ήπια στρέψη μέχρι πλήρεις σπείρες 360°, χρήσιμες για διακοσμητικά στοιχεία ή λειτουργικές ελατήρια.  
Ready to twist it up? [Apply Twist Now](./applying-twist/)  
Full example: [Applying Twist in Linear Extrusion with Aspose.3D for Java](./applying-twist/)

## Πώς να χρησιμοποιήσετε offset στρίψης για σπειροειδείς μορφές;
Το offset στρίψης μετακινεί κάθε τομή κατά τον άξονα εξώθησης ενώ περιστρέφεται, σχηματίζοντας μια σπειροειδή σκάλα ή γεωμετρία τύπου καρού. Συνδυάζοντας γωνία στρίψιμου με θετικό offset δημιουργείται μια ομαλή ελικοειδής κλίμακα, ενώ αρνητικό offset μπορεί να δημιουργήσει κατιούσες σπείρες. Αυτή η τεχνική είναι ιδανική για μοντελοποίηση σπειρών, ελατηρίων ή καλλιτεχνικών κορδονιών.  
Enhance your skills: [Learn Twist Offset](./using-twist-offset/)  
Comprehensive guide: [Using Twist Offset in Linear Extrusion with Aspose.3D for Java](./using-twist-offset/)

## Συνηθισμένες Περιπτώσεις Χρήσης για Γραμμική Εξώθηση
- **Mechanical parts** – Γρήγορη δημιουργία βιδών, αξόνων και στηριγμάτων από απλά σκίτσα.  
- **Architectural elements** – Εξώθηση σχεδίων δαπέδων σε τοίχους ή κολώνες για πρωτότυπα BIM.  
- **Game assets** – Δημιουργία low‑poly αντικειμένων όπως φράχτες, σωλήνες ή διακοσμητικές ράγες απευθείας από 2‑D τέχνη.  
- **Educational tools** – Οπτικοποίηση μαθηματικών επιφανειών εξωθώντας παραμετρικές καμπύλες.

## Επίλυση Συνηθισμένων Προβλημάτων
- **Missing faces** – Βεβαιωθείτε ότι το προφίλ είναι κλειστό βρόχο· ανοιχτά περιγράμματα δημιουργούν κενά.  
- **Excessive memory usage** – Μειώστε τον αριθμό `slices` ή ενεργοποιήστε `scene.setMemoryOptimization(true)`.  
- **Incorrect twist direction** – Θετικές γωνίες περιστρέφουν δεξιόστροφα όταν κοιτάζετε κατά μήκος της κατεύθυνσης εξώθησης· χρησιμοποιήστε αρνητικές τιμές για αντίστροφη περιστροφή.  

## Συχνές Ερωτήσεις

**Q: Μπορώ να χρησιμοποιήσω Aspose.3D for Java σε εμπορικό έργο;**  
A: Ναι, απαιτείται έγκυρη άδεια Aspose για παραγωγική χρήση, αλλά υπάρχει δωρεάν δοκιμή για αξιολόγηση.

**Q: Ποιες εκδόσεις Java υποστηρίζονται;**  
A: Η βιβλιοθήκη λειτουργεί με Java 8 και νεότερα, συμπεριλαμβανομένων των Java 11, 17 και 21.

**Q: Πρέπει να διαχειριστώ τη μνήμη για μεγάλες εξώθησεις;**  
A: Το Aspose.3D διαχειρίζεται αποδοτικά τη δημιουργία πλέγματος, αλλά μπορείτε να καλέσετε `scene.dispose()` όταν τελειώσετε με μεγάλες σκηνές για να ελευθερώσετε φυσικούς πόρους.

**Q: Μπορώ να συνδυάσω πολλαπλές εξώθησεις σε ένα μοντέλο;**  
A: Απόλυτα – μπορείτε να δημιουργήσετε πολλά αντικείμενα εξώθησης, να τα τοποθετήσετε ανεξάρτητα και να τα προσθέσετε στην ίδια σκηνή.

**Q: Υπάρχει δείγμα κώδικα για εφαρμογή στρίψιμου και offset στρίψιμου μαζί;**  
A: Ναι, τα tutorials “Applying Twist” και “Using Twist Offset” δείχνουν πώς να ορίσετε και τις δύο ιδιότητες στο ίδιο αντικείμενο εξώθησης.

**Τελευταία Ενημέρωση:** 2026-05-24  
**Δοκιμάστηκε Με:** Aspose.3D for Java 24.11  
**Συγγραφέας:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Σχετικά Μαθήματα

- [Java 3D Graphics Tutorial – Center in Linear Extrusion](/3d/java/linear-extrusion/controlling-center/)
- [How to Set Direction in Linear Extrusion with Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [Create 3D Extrusion with Slices – Aspose.3D for Java](/3d/java/linear-extrusion/specifying-slices/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}