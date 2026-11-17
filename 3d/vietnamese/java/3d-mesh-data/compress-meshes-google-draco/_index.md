---
date: 2026-11-17
description: Cách giảm kích thước mô hình 3D bằng cách tạo lưới hình cầu trong Java
  và nén nó bằng Google Draco thông qua Aspose.3D. Học quy trình đầy đủ trong vài
  phút.
images:
- /java/3d-mesh-data/compress-meshes-google-draco/og-image.png
keywords:
- create sphere mesh
- how to compress 3d
- reduce 3d model size
- aspose 3d java
- compress 3d mesh
lastmod: 2026-11-17
linktitle: Cách giảm kích thước mô hình 3D – Tạo lưới hình cầu trong Java bằng Google
  Draco
og_description: Tạo lưới hình cầu và nén mô hình 3D bằng Java sử dụng Aspose.3D và
  Google Draco. Hướng dẫn này chỉ ra cách tạo một hình cầu, xuất ra .drc và đạt giảm
  kích thước lên tới 95% trong vài phút.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Tạo lưới hình cầu và nén mô hình 3D bằng Java và Draco
schemas:
- author: Aspose
  dateModified: '2026-11-17'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: Cách giảm kích thước mô hình 3D bằng lưới hình cầu Java và Draco
url: /vi/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cách giảm kích thước mô hình 3d bằng lưới cầu Java và Draco

## Giới thiệu

Aspose.3D for Java là một thư viện cho phép tạo, thao tác và chuyển đổi các mô hình 3‑D trực tiếp từ mã Java. Nếu bạn đang tìm kiếm cách nhanh chóng để **giảm kích thước mô hình 3d** đồng thời vẫn cung cấp hình học chất lượng cao, bạn đã đến đúng nơi. Trong hướng dẫn này, chúng tôi sẽ hướng dẫn cách tạo lưới cầu bằng **Aspose.3D for Java** và sau đó nén lưới đó bằng **Google Draco**. Khi hoàn thành, bạn sẽ có một tệp `.drc` sẵn sàng sử dụng, có kích thước nhỏ hơn đáng kể so với bản gốc, phù hợp cho các trình xem trên web, trò chơi di động, hoặc bất kỳ ứng dụng Java nào có hạn chế về băng thông.

## Câu trả lời nhanh
- **Câu hỏi này hướng dẫn gì?** Tạo lưới cầu trong Java và nén nó bằng Google Draco thông qua Aspose.3D.  
- **Thư viện chính?** Aspose.3D for Java (được sử dụng cho cả việc tạo lưới và xuất Draco).  
- **Thời gian thực hiện điển hình?** Khoảng 10‑15 phút cho một cầu cơ bản.  
- **Yêu cầu chính?** Môi trường phát triển Java với các JAR Aspose.3D có trong classpath.  
- **Kết quả?** Một tệp `.drc` mà **giảm kích thước mô hình 3d** lên tới 95 % so với lưới chưa nén.

## Cách giảm kích thước mô hình 3d?

Tải cầu của bạn và nén nó trong hai bước đơn giản. Đầu tiên, bạn **tạo lưới cầu** bằng `new Sphere(1.0, 32, 32)`. Sau đó, bạn xuất cảnh trực tiếp sang Draco bằng `scene.save("sphere.drc", SaveFormat.Draco)`. Aspose.3D tự động xử lý lượng tử hoá hình học và loại bỏ đỉnh trùng lặp, tạo ra các tệp thường nhỏ hơn 80‑95 % trong khi vẫn giữ được độ trung thực hình ảnh.

Lớp `Sphere` là trình tạo hình học tích hợp sẵn của Aspose.3D, tạo ra một lưới cầu được tam giác hoá. Nó nhận các tham số bán kính và tessellation, cho phép bạn kiểm soát mức độ chi tiết trước khi nén.

## “Giảm kích thước mô hình 3d” là gì trong bối cảnh phát triển 3d?

**Giảm kích thước mô hình 3d** có nghĩa là thu nhỏ lượng dữ liệu hình học cần truyền hoặc lưu trữ, mà không làm giảm đáng kể chất lượng hình ảnh. Draco đạt được điều này bằng cách mã hoá vị trí đỉnh, pháp tuyến và các thuộc tính khác trong một định dạng nhị phân cực kỳ gọn. Khi kết hợp với Aspose.3D, toàn bộ quy trình vẫn nằm trong Java, vì vậy bạn không cần phải xử lý các binary gốc.

## Tại sao sử dụng nén lưới Google Draco với Aspose.3D?

Google Draco kết hợp với Aspose.3D cung cấp một quy trình hiệu quả, giảm đáng kể kích thước tệp lưới đồng thời vẫn dễ dàng tích hợp vào các dự án Java. Thư viện xử lý mọi việc mã hoá cấp thấp, cho phép các nhà phát triển tập trung vào việc tạo hình học mà không phải làm việc với các binary Draco gốc, dẫn đến phát triển nhanh hơn và tài sản nhỏ hơn cho web và di động.

- **Giảm kích thước mạnh mẽ:** Draco có thể cắt dữ liệu lưới tới 95 % cho các mô hình điển hình, biến tệp OBJ 5 MB thành `.drc` 0.3 MB.  
- **Giải mã nhanh tại thời gian chạy:** Các engine như Unity, Unreal và three.js giải mã Draco một cách nguyên bản, giúp thời gian tải nhanh hơn.  
- **Tích hợp Java liền mạch:** Aspose.3D trừu tượng hoá thư viện Draco gốc, cho phép bạn ở trong hệ sinh thái Java.  
- **Xuất Aspose 3D một chỗ:** API bạn dùng để tạo hình học cũng xử lý việc xuất, đơn giản hoá quy trình.  

Aspose.3D hỗ trợ **hơn 50 định dạng đầu vào và đầu ra** — bao gồm OBJ, FBX, STL, GLTF và nhiều định dạng khác — và có thể xử lý các mô hình hàng trăm trang mà không cần tải toàn bộ tệp vào bộ nhớ.

## Yêu cầu trước

- **Java Development Kit (JDK)** – phiên bản 8 hoặc mới hơn.  
- **Aspose.3D for Java** – tải xuống các JAR mới nhất từ **[trang phát hành Aspose 3D Java](https://releases.aspose.com/3d/java/)**.  
- **Kiến thức cơ bản về Google Draco** – bạn sẽ sử dụng wrapper của Aspose.3D, vì vậy không cần cài đặt Draco gốc.

## Nhập gói

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Hướng dẫn từng bước

### Bước 1: thiết lập dự án

Tạo một dự án Java mới (bất kỳ IDE nào cũng được) và thêm tất cả các JAR Aspose.3D vào classpath. Giữ các tệp nguồn của bạn trong một package như `com.example.draco` để rõ ràng.

### Bước 2: cách tạo lưới cầu trong Java

Lớp `Sphere` là trình tạo hình học tích hợp của Aspose.3D, tạo ra một lưới cầu được tam giác hoá.  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **Mẹo:** Lớp `Sphere` tạo ra một lưới tam giác với bán kính mặc định là 1.0. Bạn có thể truyền bán kính tùy chỉnh, tessellation, hoặc các tham số vật liệu nếu cần mức độ chi tiết khác trước khi nén.

### Bước 3: xuất lưới sang định dạng Draco

`Scene` là lớp đại diện cho một cảnh 3‑D hoàn chỉnh có thể chứa lưới, ánh sáng và camera. Lớp `DracoCompressionOptions` cho phép bạn tùy chỉnh các thiết lập nén Draco như lượng tử hoá và mức nén. Sau khi cầu được thêm vào đối tượng `Scene`, gọi `scene.save("sphere.drc", SaveFormat.Draco)`. Aspose.3D tự động chọn các thiết lập nén tối ưu, nhưng bạn có thể tinh chỉnh chúng bằng cách điều chỉnh `DracoCompressionOptions` nếu cần tệp nhỏ nhất có thể. `DracoCompressionOptions` cho phép bạn

### Bước 4: xác minh đầu ra

`DRACOLoader` là tiện ích của three.js để tải các tệp `.drc` đã nén bằng Draco và chuyển chúng thành hình học tương thích WebGL. Mở tệp `.drc` đã tạo bằng một trình xem Draco (ví dụ, three.js `DRACOLoader`) để đảm bảo hình học được hiển thị đúng. Bạn sẽ nhận thấy sự giảm kích thước tệp đáng kể — thường giảm tới mười lần hoặc hơn.

## Các trường hợp sử dụng phổ biến

| Kịch bản | Tại sao giảm kích thước mô hình? | Cách hướng dẫn này hỗ trợ |
|----------|----------------------------------|----------------------------|
| Cấu hình sản phẩm dựa trên web | Tải trang nhanh hơn trên kết nối chậm | Các tệp `.drc` nén bằng Draco tải trong vài giây |
| Ứng dụng AR/VR di động | Giảm dung lượng bộ nhớ trên thiết bị | Lưới nhỏ hơn giúp ứng dụng phản hồi nhanh |
| Cảnh render trên đám mây | Giảm chi phí băng thông | Xuất một cú nhấp từ Aspose.3D sang Draco |

## Các vấn đề thường gặp và giải pháp

| Vấn đề | Nguyên nhân | Giải pháp |
|--------|-------------|-----------|
| **`NoClassDefFoundError` for Draco classes** | Các JAR Aspose.3D không có trong classpath | Xác minh rằng *tất cả* các tệp JAR Aspose.3D đã được bao gồm và phiên bản khớp với tài liệu. |
| **Output file is empty** | `MyDir` trỏ tới thư mục không tồn tại | Tạo thư mục bằng chương trình (`Files.createDirectories(Paths.get(MyDir))`) trước khi ghi tệp. |
| **Compressed mesh looks distorted** | Sử dụng mức nén thấp hoặc tessellation không đủ | Chuyển sang `DracoCompressionLevel.OPTIMAL` và tăng tessellation của cầu (ví dụ, `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` chọn chất lượng nén cao nhất cho đầu ra Draco. |

## Câu hỏi thường gặp

**Q: Aspose.3D có tương thích với các định dạng tệp 3d khác nhau không?**  
A: Có, Aspose.3D hỗ trợ OBJ, FBX, STL, GLTF và nhiều định dạng khác, làm cho nó trở thành lựa chọn đa năng cho các quy trình **xuất Aspose 3d**.

**Q: Tôi có thể sử dụng Google Draco để nén trong các ngôn ngữ lập trình khác không?**  
A: Chắc chắn. Draco cung cấp các thư viện gốc cho C++, Python và JavaScript. Hướng dẫn này tập trung vào Java, nhưng các khái niệm áp dụng cho mọi ngôn ngữ.

**Q: Tôi có thể tìm tài liệu Aspose.3D bổ sung ở đâu?**  
A: Truy cập **[tài liệu Aspose.3D Java](https://reference.aspose.com/3d/java/)** để xem toàn bộ tham chiếu API và nhiều ví dụ hơn.

**Q: Làm thế nào để tôi có được giấy phép tạm thời cho Aspose.3D?**  
A: Khám phá các tùy chọn giấy phép tạm thời trên **[trang giấy phép tạm thời của Aspose](https://purchase.aspose.com/temporary-license/)**.

**Q: Có diễn đàn cộng đồng hỗ trợ Aspose.3D không?**  
A: Có, tham gia thảo luận tại **[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18)**.

## Kết luận

Trong hướng dẫn này, chúng tôi đã trình bày cách **giảm kích thước mô hình 3d** bằng cách tạo lưới cầu trong Java và sau đó nén nó bằng Google Draco thông qua Aspose.3D. Bằng cách thực hiện các bước ngắn gọn này, bạn có thể thu nhỏ tệp lưới đáng kể, cải thiện thời gian tải và giữ cho các ứng dụng 3d dựa trên Java của bạn phản hồi nhanh và thân thiện với băng thông.

---

**Cập nhật lần cuối:** 2026-11-17  
**Kiểm tra với:** Aspose.3D for Java 24.12 (latest)  
**Tác giả:** Aspose

## Các hướng dẫn liên quan

- [Giảm kích thước tệp 3D – Nén cảnh với Aspose.3D cho Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Tạo đám mây điểm Draco từ các cầu bằng Aspose.3D cho Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Học cách tam giác hoá lưới để tối ưu hoá việc render trong Java bằng Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}