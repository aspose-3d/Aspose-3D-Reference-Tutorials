---
date: 2026-09-08
description: Tìm hiểu cách định nghĩa đơn vị và xuất một cảnh sang FBX trong Java
  bằng Aspose.3D. Hướng dẫn từng bước này cho thấy cách đặt tên ứng dụng, đơn vị đo
  lường và truy xuất thông tin cảnh 3D.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Cách lưu FBX và truy xuất thông tin cảnh 3D trong Java
og_description: Tìm hiểu cách định nghĩa đơn vị và xuất một cảnh sang FBX trong Java
  với Aspose.3D. Hướng dẫn bao gồm việc đặt tên ứng dụng, đơn vị đo lường và truy
  xuất thông tin cảnh 3D trong một vài bước.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Cách định nghĩa đơn vị và xuất cảnh sang FBX trong Java
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
title: Cách định nghĩa đơn vị và xuất cảnh sang FBX trong Java
url: /vi/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cách định nghĩa đơn vị và xuất cảnh sang FBX trong Java

## Giới thiệu

Nếu bạn đang tìm kiếm một hướng dẫn **cách định nghĩa đơn vị** và **xuất một cảnh sang FBX** một cách rõ ràng, thực hành, đồng thời trích xuất siêu dữ liệu hữu ích từ các cảnh 3D của mình, bạn đã đến đúng nơi. Trong tutorial này, chúng ta sẽ đi qua từng bước sử dụng thư viện **Aspose.3D for Java**: từ tạo một cảnh, **đặt tên ứng dụng**, **định nghĩa đơn vị đo**, cho đến cuối cùng **xuất cảnh sang FBX**. Khi hoàn thành, bạn sẽ có một tệp FBX sẵn sàng sử dụng, chứa thông tin tài sản mà bạn cần cho các pipeline downstream.

## Câu trả lời nhanh
- **Mục tiêu chính là gì?** Xuất một cảnh sang FBX có chứa thông tin tài sản tùy chỉnh.  
- **Thư viện nào được sử dụng?** Aspose.3D for Java.  
- **Tôi có cần giấy phép không?** Bản dùng thử miễn phí đủ cho phát triển; giấy phép thương mại cần thiết cho môi trường sản xuất.  
- **Tôi có thể thay đổi đơn vị đo không?** Có – sử dụng `setUnitName` và `setUnitScaleFactor`.  
- **Đầu ra được lưu ở đâu?** Vào đường dẫn bạn chỉ định trong `scene.save(...)`.  

## Yêu cầu trước

Trước khi bắt đầu, hãy chắc chắn rằng bạn có:

- Hiểu vững về cú pháp Java cơ bản.  
- **Aspose.3D for Java** đã tải xuống và thêm vào dự án của bạn (bạn có thể lấy nó từ trang chính) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- IDE Java yêu thích của bạn (IntelliJ IDEA, Eclipse, NetBeans, v.v.) được cấu hình đúng.

## Nhập gói

Trong tệp nguồn Java của bạn, nhập các lớp Aspose.3D cung cấp khả năng xử lý cảnh và hỗ trợ định dạng tệp.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tip:** Giữ danh sách import tối thiểu để tránh các phụ thuộc không cần thiết và cải thiện thời gian biên dịch.

## Quy trình lưu tệp FBX là gì?

Để lưu một cảnh dưới dạng tệp FBX, bạn tạo một `Scene`, đặt bất kỳ siêu dữ liệu tài sản nào mong muốn, định nghĩa đơn vị đo, và sau đó gọi `scene.save(path, FileFormat.FBX7500ASCII)`. Trình tự này ghi geometry, materials và metadata vào một tệp ASCII FBX có thể được kiểm tra hoặc nhập bởi các công cụ downstream.

### Bước 1: khởi tạo một cảnh 3D

Lớp `Scene` là container cấp cao nhất của Aspose.3D, đại diện cho toàn bộ cảnh 3D, bao gồm geometry, lights, cameras và metadata. Đầu tiên, tạo một đối tượng `Scene` rỗng. Đây sẽ là container cho tất cả geometry, lights, cameras và metadata tài sản.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Cách đặt tên ứng dụng trong Java

Đối tượng `AssetInfo` lưu trữ metadata như tên ứng dụng, nhà cung cấp và phiên bản cho cảnh. Thêm metadata tùy chỉnh giúp các công cụ downstream xác định nguồn gốc của tệp. Sử dụng đối tượng `AssetInfo` để **đặt tên ứng dụng** (và nhà cung cấp) trước khi lưu tệp.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Why this matters:** Nhiều pipeline lọc hoặc gắn thẻ tài sản dựa trên ứng dụng gốc, khiến bước này trở nên thiết yếu cho các dự án lớn.

### Bước 3: định nghĩa đơn vị đo

Hệ thống đơn vị xác định tỉ lệ thực tế của cảnh; Aspose.3D cho phép bạn chỉ định tên đơn vị và hệ số tỉ lệ so với mét. Trong ví dụ này, chúng ta sử dụng một đơn vị Ai Cập cổ gọi là “pole” với hệ số tỉ lệ tùy chỉnh.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Điều chỉnh `unitScaleFactor` để phù hợp với kích thước thực tế của mô hình; 1.0 đại diện cho tỉ lệ 1‑to‑1 với đơn vị đã chọn.

### Bước 4: xuất cảnh sang FBX

Bây giờ khi thông tin tài sản đã được đính kèm, chúng ta lưu cảnh dưới dạng tệp FBX. Tùy chọn `FileFormat.FBX7500ASCII` tạo ra một tệp ASCII FBX có thể đọc được bởi con người, rất tiện cho việc gỡ lỗi.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Remember:** Thay thế `"Your Document Directory"` bằng một đường dẫn tuyệt đối hoặc một đường dẫn tương đối so với thư mục làm việc của dự án.

## Tại sao xuất cảnh sang FBX với Aspose.3D?

Aspose.3D hỗ trợ **hơn 50 định dạng nhập và xuất** và có thể xử lý các cảnh hàng trăm trang mà không cần tải toàn bộ tệp vào bộ nhớ, cho phép bạn kiểm soát đầy đủ tệp xuất — metadata, đơn vị, và geometry — mà không cần một ứng dụng tạo 3D nặng. Điều này làm cho việc tạo tài sản tự động, xử lý batch và chuyển đổi phía server nhanh chóng và đáng tin cậy.

## Các trường hợp sử dụng phổ biến

- **Quy trình tài sản trò chơi** – nhúng thông tin người tạo trực tiếp trong tệp FBX để theo dõi phiên bản.  
- **Trực quan kiến trúc** – lưu trữ đơn vị riêng của dự án để tránh lỗi tỷ lệ khi nhập vào các engine render.  
- **Báo cáo tự động** – tạo tệp FBX ngay lập tức với siêu dữ liệu mà các công cụ phân tích downstream có thể đọc.  
- **Dịch vụ 3D dựa trên đám mây** – tạo và xuất cảnh một cách lập trình mà không cần GUI, hoàn hảo cho nền tảng SaaS.

## Khắc phục sự cố & mẹo

| Vấn đề | Giải pháp |
|-------|----------|
| **Không tìm thấy tệp sau khi lưu** | Xác minh rằng `MyDir` trỏ tới một thư mục tồn tại và ứng dụng của bạn có quyền ghi. |
| **Đơn vị xuất hiện không đúng trong trình xem bên ngoài** | Kiểm tra lại `unitScaleFactor`; một số trình xem mong đợi mét làm đơn vị cơ sở. |
| **Metadata tài sản bị thiếu** | Đảm bảo bạn gọi `scene.getAssetInfo()` **trước** khi lưu; các thay đổi sau `save()` sẽ không được lưu. |
| **Nút thắt hiệu năng trên các cảnh lớn** | Sử dụng `scene.optimize()` trước khi lưu để giảm sử dụng bộ nhớ. |
| **ASCII FBX quá lớn** | Chuyển sang FBX nhị phân bằng cách dùng `FileFormat.FBX7500` (xem FAQ). |

## Câu hỏi thường gặp

**Q: Làm thế nào để thay đổi định dạng đầu ra sang FBX nhị phân?**  
A: Thay thế `FileFormat.FBX7500ASCII` bằng `FileFormat.FBX7500` khi gọi `scene.save(...)`.

**Q: Tôi có thể thêm metadata do người dùng định nghĩa tùy chỉnh ngoài các trường tài sản tích hợp không?**  
A: Có, sử dụng `scene.getUserData().add("Key", "Value")` để nhúng các cặp key‑value bổ sung.

**Q: Aspose.3D có hỗ trợ các định dạng xuất khác như OBJ hoặc GLTF không?**  
A: Có. Chỉ cần thay đổi enum `FileFormat` thành `OBJ` hoặc `GLTF2` tùy nhu cầu.

**Q: Yêu cầu phiên bản Java nào?**  
A: Aspose.3D for Java hỗ trợ Java 8 trở lên.

**Q: Có thể tải một FBX hiện có, sửa thông tin asset và lưu lại không?**  
A: Chắc chắn. Tải tệp bằng `new Scene("input.fbx")`, sửa `scene.getAssetInfo()`, sau đó lưu.

---

**Last Updated:** 2026-09-08  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose

## Hướng dẫn liên quan

- [Giảm kích thước tệp 3D – Nén cảnh với Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Cách đặt màu vector3 java: Thay đổi màu Diffuse và quản lý thuộc tính 3D trong cảnh Java bằng Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}