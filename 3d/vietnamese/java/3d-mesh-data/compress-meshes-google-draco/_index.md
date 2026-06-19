---
date: 2026-04-29
description: Tìm hiểu cách giảm kích thước mô hình 3D bằng cách tạo lưới hình cầu
  trong Java và nén nó bằng Google Draco sử dụng Aspose.3D – cần thiết cho việc xuất
  Aspose 3D.
keywords:
- reduce 3d model size
- aspose 3d export
- compress 3d mesh java
linktitle: Cách tạo lưới hình cầu trong Java – Nén lưới 3D bằng Google Draco
second_title: Aspose.3D Java API
title: 'Giảm kích thước mô hình 3D: Tạo lưới hình cầu trong Java bằng Draco'
url: /vi/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Giảm Kích Thước Mô Hình 3D: Tạo Lưới Hình Cầu trong Java với Draco

## Giới thiệu

Nếu bạn đang tìm kiếm một cách nhanh chóng để **giảm kích thước mô hình 3D** đồng thời vẫn cung cấp hình học chất lượng cao, bạn đã đến đúng nơi. Trong hướng dẫn này, chúng ta sẽ tạo một lưới hình cầu bằng **Aspose.3D for Java** và sau đó nén lưới đó bằng **Google Draco**. Khi hoàn thành, bạn sẽ có một tệp `.drc` sẵn sàng sử dụng, kích thước giảm đáng kể so với bản gốc, phù hợp cho các trình xem trên web, trò chơi di động hoặc bất kỳ ứng dụng Java nào bị giới hạn băng thông.

## Câu trả lời nhanh
- **Bài hướng dẫn này đề cập đến gì?** Tạo lưới hình cầu trong Java và nén nó bằng Google Draco thông qua Aspose.3D.  
- **Thư viện chính?** Aspose.3D for Java (được sử dụng cho cả việc tạo lưới và xuất Draco).  
- **Thời gian thực hiện điển hình?** Khoảng 10‑15 phút cho một hình cầu cơ bản.  
- **Điều kiện tiên quyết chính?** Môi trường phát triển Java với các JAR của Aspose.3D đã được thêm vào classpath.  
- **Kết quả?** Một tệp `.drc` **giảm kích thước mô hình 3D** lên tới 90 % so với lưới chưa nén.

## “Giảm kích thước mô hình 3D” trong bối cảnh phát triển 3D là gì?

Giảm kích thước mô hình 3D có nghĩa là thu hẹp lượng dữ liệu hình học cần truyền hoặc lưu trữ, mà không làm giảm đáng kể chất lượng hình ảnh. Draco đạt được điều này bằng cách mã hoá vị trí đỉnh, pháp tuyến và các thuộc tính khác trong một định dạng nhị phân cực kỳ nén. Khi kết hợp với Aspose.3D, toàn bộ quy trình vẫn nằm trong Java, vì vậy bạn không cần phải xử lý các thư viện nhị phân gốc.

## Tại sao nên sử dụng nén lưới Google Draco với Aspose.3D?

- **Giảm kích thước đáng kể:** Draco có thể cắt giảm dữ liệu lưới tới 90 % so với các định dạng như OBJ hoặc STL.  
- **Giải mã nhanh tại thời gian chạy:** Các engine như Unity, Unreal và three.js giải mã Draco một cách nguyên bản, giúp thời gian tải nhanh hơn.  
- **Tích hợp liền mạch với Java:** Aspose.3D trừu tượng hoá thư viện Draco gốc, cho phép bạn ở lại trong hệ sinh thái Java.  
- **Xuất khẩu Aspose 3D toàn diện:** API bạn dùng để tạo hình học cũng xử lý việc xuất, đơn giản hoá quy trình.

## Yêu cầu trước

- **Java Development Kit (JDK)** – phiên bản 8 trở lên.  
- **Aspose.3D for Java** – tải xuống các JAR mới nhất từ trang chính thức [tại đây](https://releases.aspose.com/3d/java/).  
- **Kiến thức cơ bản về Google Draco** – bạn sẽ sử dụng lớp bao của Aspose.3D, vì vậy không cần cài đặt Draco gốc.

## Nhập các gói

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

### Bước 1: Thiết lập dự án

Tạo một dự án Java mới (bất kỳ IDE nào cũng được) và thêm tất cả các JAR của Aspose.3D vào classpath. Giữ các tệp nguồn trong một package như `com.example.draco` để dễ quản lý.

### Bước 2: Cách tạo lưới hình cầu trong Java

```java
// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();
```

> **Mẹo:** Lớp `Sphere` tạo ra một lưới tam giác với bán kính mặc định là 1.0. Bạn có thể truyền bán kính tùy chỉnh, mức chia lưới hoặc tham số vật liệu nếu cần mức chi tiết khác trước khi nén.

### Bước 3: Cách nén lưới bằng Google Draco

```java
// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
```

Đặt mức nén thành `OPTIMAL` sẽ mang lại mức giảm kích thước lớn nhất trong khi vẫn giữ được độ trung thực hình ảnh, trực tiếp giúp bạn **giảm kích thước mô hình 3D**.

### Bước 4: Lưu lưới đã nén

```java
// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

Tệp `SphereMeshtoDRC_Out.drc` tạo ra có thể được truyền tới khách hàng, lưu trong CDN, hoặc tải trực tiếp bởi bất kỳ engine nào hỗ trợ Draco.

## Các trường hợp sử dụng phổ biến

| Kịch bản | Tại sao giảm kích thước mô hình? | Cách hướng dẫn này hỗ trợ |
|----------|----------------------------------|----------------------------|
| Cấu hình sản phẩm trên web | Tải trang nhanh hơn trên kết nối chậm | Các tệp `.drc` đã nén bằng Draco tải trong vài giây |
| Ứng dụng AR/VR trên di động | Giảm dung lượng bộ nhớ trên thiết bị | Lưới nhỏ hơn giúp ứng dụng phản hồi nhanh |
| Cảnh render trên đám mây | Giảm chi phí băng thông | Xuất một cú nhấp chuột từ Aspose.3D sang Draco |

## Các vấn đề thường gặp và giải pháp

| Vấn đề | Nguyên nhân | Giải pháp |
|-------|-------------|----------|
| **`NoClassDefFoundError` for Draco classes** | Các JAR của Aspose.3D không có trong classpath | Kiểm tra rằng *tất cả* các tệp JAR của Aspose.3D đã được bao gồm và phiên bản phù hợp với tài liệu. |
| **Output file is empty** | `MyDir` trỏ tới thư mục không tồn tại | Tạo thư mục bằng chương trình (`Files.createDirectories(Paths.get(MyDir))`) trước khi ghi tệp. |
| **Compressed mesh looks distorted** | Sử dụng mức nén thấp hoặc độ chia lưới không đủ | Chuyển sang `DracoCompressionLevel.OPTIMAL` và tăng độ chia lưới của hình cầu (ví dụ, `new Sphere(1.0, 64, 64)`). |

## Câu hỏi thường gặp

**H: Aspose.3D có tương thích với các định dạng tệp 3D khác nhau không?**  
Đ: Có, Aspose.3D hỗ trợ OBJ, FBX, STL, GLTF và nhiều định dạng khác, làm cho nó trở thành lựa chọn đa năng cho các pipeline **xuất khẩu Aspose 3D**.

**H: Tôi có thể sử dụng Google Draco để nén trong các ngôn ngữ lập trình khác không?**  
Đ: Chắc chắn. Draco cung cấp các thư viện gốc cho C++, Python và JavaScript. Bài hướng dẫn này tập trung vào Java, nhưng các khái niệm áp dụng cho mọi ngôn ngữ.

**H: Tôi có thể tìm tài liệu Aspose.3D bổ sung ở đâu?**  
Đ: Tham khảo [tài liệu Aspose.3D Java](https://reference.aspose.com/3d/java/) để có đầy đủ tham chiếu API và nhiều ví dụ hơn.

**H: Làm sao để tôi có được giấy phép tạm thời cho Aspose.3D?**  
Đ: Khám phá các tùy chọn cấp phép tạm thời [tại đây](https://purchase.aspose.com/temporary-license/).

**H: Có diễn đàn cộng đồng nào hỗ trợ Aspose.3D không?**  
Đ: Có, tham gia thảo luận tại [Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18).

## Kết luận

Trong hướng dẫn này, chúng ta đã chứng minh cách **giảm kích thước mô hình 3D** bằng cách tạo một lưới hình cầu trong Java và sau đó nén nó bằng Google Draco thông qua Aspose.3D. Bằng cách thực hiện các bước ngắn gọn này, bạn có thể thu nhỏ đáng kể các tệp lưới, cải thiện thời gian tải và giữ cho các ứng dụng 3D dựa trên Java của bạn phản hồi nhanh và tiết kiệm băng thông.

---

**Cập nhật lần cuối:** 2026-04-29  
**Đã kiểm tra với:** Aspose.3D for Java 24.12 (mới nhất)  
**Tác giả:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}