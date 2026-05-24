---
date: 2026-05-24
description: Μάθετε πώς να ορίσετε την άδεια aspose 3d σε Java, να εφαρμόσετε ένα
  αρχείο άδειας, να το μεταφέρετε μέσω ροής, ή να χρησιμοποιήσετε metered licensing
  με public and private keys.
keywords:
- set aspose 3d license
- aspose 3d java licensing
- metered licensing java
linktitle: Πώς να ορίσετε την άδεια Aspose σε Aspose.3D για Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to set aspose 3d license in Java, apply a license file, stream
    it, or use metered licensing with public and private keys.
  headline: How to Set Aspose 3D License in Java (set aspose 3d license)
  type: TechArticle
- description: Learn how to set aspose 3d license in Java, apply a license file, stream
    it, or use metered licensing with public and private keys.
  name: How to Set Aspose 3D License in Java (set aspose 3d license)
  steps:
  - name: Create a `License` object
    text: Instantiate the `License` class; this prepares the runtime to accept a license
      file.
  - name: Apply the license file
    text: Provide the absolute or relative path to your `.lic` file and call `setLicense`.
      The method returns `void`, and the license is cached after the first successful
      call, so subsequent calls are inexpensive.
  - name: Create a `License` object
    text: As before, start by creating an instance of the `License` class.
  - name: Load the license via `FileInputStream`
    text: Open a `FileInputStream` pointing to your `.lic` file (or any `InputStream`)
      and pass it to `setLicense`. The stream is read once and then closed automatically.
  - name: Initialize a `Metered` license object
    text: The `Metered` class represents a cloud‑based license that validates usage
      against Aspose’s metering server.
  - name: Set public and private keys
    text: Call `setMeteredKey(publicKey, privateKey)` with the keys you received when
      you purchased a metered license. The library contacts the server once to verify
      the keys and then caches the result.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports Java 6 through Java 21, covering more than 15
      major releases.
    question: Is Aspose.3D compatible with all Java versions?
  - answer: You can refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find additional documentation?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Can I try Aspose.3D before purchasing?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for support.
    question: How can I get support for Aspose.3D?
  - answer: Yes, obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).
    question: Do I need a temporary license for testing?
  type: FAQPage
second_title: Aspose.3D Java API
title: Πώς να ορίσετε την άδεια Aspose 3D σε Java (set aspose 3d license)
url: /el/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Πώς να ορίσετε την άδεια Aspose 3D σε Java (set aspose 3d license)

## Εισαγωγή

Σε αυτό το ολοκληρωμένο tutorial θα ανακαλύψετε **πώς να ορίσετε την άδεια aspose 3d** για το Aspose.3D σε περιβάλλον Java. Είτε προτιμάτε τη φόρτωση ενός αρχείου άδειας, τη ροή του, είτε τη χρήση μετρημένης άδειας με δημόσια και ιδιωτικά κλειδιά, θα περάσουμε βήμα‑βήμα από κάθε προσέγγιση ώστε να μπορείτε να ξεκλειδώσετε πλήρως το σύνολο λειτουργιών του Aspose.3D γρήγορα και με σιγουριά. Η σωστή ρύθμιση της άδειας αφαιρεί τα υδατογράμματα αξιολόγησης, ενεργοποιεί premium 3D μορφές και εξασφαλίζει πλήρη συμμόρφωση με το μοντέλο αδειοδότησης της Aspose.

## Γρήγορες Απαντήσεις
- **Ποιος είναι ο κύριος τρόπος για να ορίσετε μια άδεια Aspose.3D;** Χρησιμοποιήστε την κλάση `License` και καλέστε `setLicense` με διαδρομή αρχείου ή ροή.  
- **Μπορώ να φορτώσω την άδεια από ροή;** Ναι – τυλίξτε το αρχείο `.lic` σε ένα `FileInputStream` και περάστε το στο `setLicense`.  
- **Τι γίνεται αν χρειάζομαι μετρημένη άδεια;** Αρχικοποιήστε ένα αντικείμενο `Metered` και καλέστε `setMeteredKey` με τα δημόσια και ιδιωτικά κλειδιά σας.  
- **Χρειάζομαι άδεια για εκδόσεις ανάπτυξης;** Απαιτείται δοκιμαστική ή προσωρινή άδεια για οποιοδήποτε σενάριο εκτός αξιολόγησης.  
- **Ποιες εκδόσεις Java υποστηρίζονται;** Το Aspose.3D λειτουργεί με Java 6 έως Java 21, καλύπτοντας πάνω από 15 κύριες κυκλοφορίες.

## Τι είναι η κλάση `License`;
Η κλάση `License` είναι το κεντρικό αντικείμενο αδειοδότησης του Aspose.3D που φορτώνει ένα αρχείο `.lic` στη μνήμη, επικυρώνει τις πληροφορίες της άδειας και, μόλις δημιουργηθεί, εφαρμόζει την άδεια παγκοσμίως για τη διαδικασία JVM, διασφαλίζοντας ότι όλες οι επόμενες λειτουργίες του Aspose.3D εκτελούνται σε λειτουργία αδειοδοτημένη χωρίς περιορισμούς αξιολόγησης.

## Γιατί να ορίσετε την άδεια Aspose 3D;
Η εφαρμογή έγκυρης άδειας ενεργοποιεί **πάνω από 50 premium 3D μορφές αρχείων** (συμπεριλαμβανομένων των FBX, OBJ, STL και GLTF) και αφαιρεί το υδατογράφημα “Evaluation” από τις αποδομένες εικόνες. Επίσης, αφαιρεί περιορισμούς στο μέγεθος σκηνής, επιτρέποντας την επεξεργασία μοντέλων με **έως 1 εκατομμύριο κορυφές** χωρίς μείωση απόδοσης.

## Προαπαιτούμενα

Πριν ξεκινήσουμε, βεβαιωθείτε ότι έχετε τα παρακάτω προαπαιτούμενα:

- Βασική κατανόηση του προγραμματισμού Java.  
- Η βιβλιοθήκη Aspose.3D είναι εγκατεστημένη. Μπορείτε να τη κατεβάσετε από τη [σελίδα κυκλοφορίας](https://releases.aspose.com/3d/java/).  

## Εισαγωγή Πακέτων

Για να ξεκινήσετε, εισάγετε τα απαραίτητα πακέτα στο έργο Java σας. Βεβαιωθείτε ότι το Aspose.3D έχει προστεθεί στο classpath. Ακολουθεί ένα παράδειγμα:

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

Η κλάση `License` είναι υπεύθυνη για τη φόρτωση ενός αρχείου `.lic` και την παγκόσμια εφαρμογή του, ενώ η κλάση `Metered` ενεργοποιεί τη μετρημένη άδεια μέσω cloud, επικυρώνοντας τα δημόσια και ιδιωτικά κλειδιά έναντι του διακομιστή αδειοδότησης της Aspose.

## Πώς να εφαρμόσετε άδεια από αρχείο;

Φορτώστε την άδεια απευθείας από ένα αρχείο `.lic` στο δίσκο. Αυτή η μέθοδος είναι η πιο απλή για εφαρμογές desktop ή on‑premises, και εξασφαλίζει ότι η άδεια διαβάζεται μία φορά κατά την εκκίνηση και αποθηκεύεται στην κρυφή μνήμη για όλη τη διάρκεια του JVM, εξαλείφοντας τυχόν επιπλέον φόρτο χρόνου εκτέλεσης μετά τη αρχική φόρτωση.

### Βήμα 1: Δημιουργήστε ένα αντικείμενο `License`
Δημιουργήστε μια παρουσία της κλάσης `License`; αυτό προετοιμάζει το runtime να δεχτεί ένα αρχείο άδειας.

### Βήμα 2: Εφαρμόστε το αρχείο άδειας
Δώστε την απόλυτη ή σχετική διαδρομή προς το αρχείο `.lic` σας και καλέστε `setLicense`. Η μέθοδος δεν επιστρέφει τιμή, και η άδεια αποθηκεύεται στην κρυφή μνήμη μετά την πρώτη επιτυχημένη κλήση, ώστε οι επόμενες κλήσεις να είναι φθηνές.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Πώς να εφαρμόσετε άδεια από ροή;

Η ροή μιας άδειας είναι χρήσιμη όταν το αρχείο είναι ενσωματωμένο ως πόρος, αποθηκευμένο σε ασφαλή θέση ή ανακτάται από απομακρυσμένη υπηρεσία κατά το runtime. Χρησιμοποιώντας ένα `InputStream`, αποφεύγετε την αποκάλυψη της φυσικής διαδρομής του αρχείου και μπορείτε να διατηρήσετε τα δεδομένα της άδειας κρυπτογραφημένα ή πακεταρισμένα μέσα στο JAR, ενισχύοντας την ασφάλεια ενώ επιτρέπετε στη βιβλιοθήκη να διαβάσει τα byte της άδειας.

### Βήμα 1: Δημιουργήστε ένα αντικείμενο `License`
Όπως και πριν, ξεκινήστε δημιουργώντας μια παρουσία της κλάσης `License`.

### Βήμα 2: Φορτώστε την άδεια μέσω `FileInputStream`
Ανοίξτε ένα `FileInputStream` που δείχνει στο αρχείο `.lic` σας (ή σε οποιοδήποτε `InputStream`) και περάστε το στο `setLicense`. Η ροή διαβάζεται μία φορά και κλείνει αυτόματα.

```java
License license = new License();
```

## Πώς να χρησιμοποιήσετε δημόσια και ιδιωτικά κλειδιά για μετρημένη άδεια;

Η μετρημένη άδεια σας επιτρέπει να ενεργοποιήσετε το Aspose.3D χωρίς φυσικό αρχείο `.lic`, χρησιμοποιώντας κλειδιά που εκδίδονται από την υπηρεσία cloud της Aspose. Αυτή η προσέγγιση είναι ιδανική για SaaS ή cloud‑βάσιμες υλοποιήσεις όπου η διαχείριση αρχείων άδειας σε κάθε instance είναι μη πρακτική· η βιβλιοθήκη επικοινωνεί με τον διακομιστή μετρημένων αδειών της Aspose μία φορά για την επικύρωση των κλειδιών και στη συνέχεια αποθηκεύει το αποτέλεσμα για τη διάρκεια της συνεδρίας.

### Βήμα 1: Αρχικοποιήστε ένα αντικείμενο άδειας `Metered`
Η κλάση `Metered` αντιπροσωπεύει μια cloud‑βάσιμη άδεια που επικυρώνει τη χρήση έναντι του διακομιστή μετρημένων αδειών της Aspose.

### Βήμα 2: Ορίστε τα δημόσια και ιδιωτικά κλειδιά
Καλέστε `setMeteredKey(publicKey, privateKey)` με τα κλειδιά που λάβατε όταν αγοράσατε μια μετρημένη άδεια. Η βιβλιοθήκη επικοινωνεί με τον διακομιστή μία φορά για την επαλήθευση των κλειδιών και στη συνέχεια αποθηκεύει το αποτέλεσμα.

```java
license.setLicense("Aspose._3D.lic");
```

## Συχνά Προβλήματα & Συμβουλές

- **Αρχείο δεν βρέθηκε** – Επαληθεύστε ότι η διαδρομή του αρχείου `.lic` είναι σωστή σε σχέση με τον τρέχοντα φάκελο ή χρησιμοποιήστε απόλυτη διαδρομή.  
- **Η ροή κλείνει πρόωρα** – Όταν χρησιμοποιείτε ροή, διατηρήστε το αντικείμενο `License` ενεργό για όλη τη διάρκεια της εφαρμογής· η άδεια αποθηκεύεται στην κρυφή μνήμη μετά την πρώτη επιτυχημένη κλήση.  
- **Ασυμφωνία κλειδιού μετρημένης άδειας** – Ελέγξτε ξανά ότι τα δημόσια και ιδιωτικά κλειδιά αντιστοιχούν στην ίδια μετρημένη άδεια· ένα τυπογραφικό λάθος θα προκαλέσει εξαίρεση χρόνου εκτέλεσης.  
- **Συμβουλή:** Αποθηκεύστε το αρχείο άδειας σε ασφαλή τοποθεσία εκτός του δέντρου πηγαίου κώδικα και φορτώστε το μέσω μεταβλητής περιβάλλοντος για να αποφύγετε την καταχώρηση στο σύστημα ελέγχου εκδόσεων.

## Συμπέρασμα

Συγχαρητήρια! Έχετε μάθει με επιτυχία **πώς να ορίσετε την άδεια aspose 3d** σε Java χρησιμοποιώντας τρεις αξιόπιστες μεθόδους: εφαρμογή άδειας από αρχείο, ροή της και διαμόρφωση μετρημένης άδειας με δημόσια και ιδιωτικά κλειδιά. Με την άδεια σε θέση, μπορείτε τώρα να ενσωματώσετε το Aspose.3D αβίαστα στις εφαρμογές Java, να ξεκλειδώσετε όλες τις premium λειτουργίες επεξεργασίας 3D και να συμμορφωθείτε με τις απαιτήσεις αδειοδότησης της Aspose.

## Συχνές Ερωτήσεις

**Ε: Είναι το Aspose.3D συμβατό με όλες τις εκδόσεις Java;**  
Α: Ναι, το Aspose.3D υποστηρίζει Java 6 έως Java 21, καλύπτοντας περισσότερες από 15 κύριες κυκλοφορίες.

**Ε: Πού μπορώ να βρω πρόσθετη τεκμηρίωση;**  
Α: Μπορείτε να ανατρέξετε στην τεκμηρίωση [εδώ](https://reference.aspose.com/3d/java/).

**Ε: Μπορώ να δοκιμάσω το Aspose.3D πριν το αγοράσω;**  
Α: Ναι, μπορείτε να εξερευνήσετε μια δωρεάν δοκιμή [εδώ](https://releases.aspose.com/).

**Ε: Πώς μπορώ να λάβω υποστήριξη για το Aspose.3D;**  
Α: Επισκεφθείτε το [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) για υποστήριξη.

**Ε: Χρειάζομαι προσωρινή άδεια για δοκιμές;**  
Α: Ναι, αποκτήστε μια προσωρινή άδεια [εδώ](https://purchase.aspose.com/temporary-license/).

**Ε: Ποια είναι η διαφορά μεταξύ άδειας αρχείου και μετρημένης άδειας;**  
Α: Η άδεια αρχείου είναι ένα στατικό αρχείο `.lic` συνδεδεμένο με συγκεκριμένη έκδοση προϊόντος, ενώ η μετρημένη άδεια επικυρώνει τη χρήση έναντι της cloud‑βασισμένης υπηρεσίας μετρημένων αδειών της Aspose χρησιμοποιώντας δημόσια/ιδιωτικά κλειδιά.

**Ε: Μπορώ να ενσωματώσω τον κώδικα φόρτωσης άδειας σε static initializer;**  
Α: Απόλυτα – η τοποθέτηση της αρχικοποίησης `License` σε static block διασφαλίζει ότι η άδεια εφαρμόζεται μία φορά όταν η κλάση φορτώνεται για πρώτη φορά.

```java
License license = new License();
```
```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```
```java
Metered metered = new Metered();
```
```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

{{< blocks/products/products-backtop-button >}}

## Σχετικά Μαθήματα

- [Οδηγός Άδειας βήμα-βήμα για Aspose.3D Java](/3d/java/licensing/)
- [Δημιουργία 3D Σκηνής Java με Aspose 3D Java](/3d/java/3d-scenes-and-models/)
- [Δημιουργία 3D Κύβου, Εφαρμογή Υλικών PBR σε Java με Aspose.3D](/3d/java/geometry/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}