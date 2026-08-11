---
date: 2026-08-02
description: Tìm hiểu cách thay đổi hướng extrusion trong linear extrusion và xuất
  file OBJ bằng Aspose.3D cho Java. Tham khảo hướng dẫn step‑by‑step của chúng tôi.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Thay đổi hướng extrusion – Aspose.3D Java
og_description: Thay đổi hướng extrusion trong linear extrusion với Aspose.3D cho
  Java và xuất file OBJ. Hướng dẫn này trình bày mã step‑by‑step và các mẹo cho nhà
  phát triển.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Thay đổi hướng extrusion – Hướng dẫn Aspose.3D Java
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Thay đổi hướng extrusion trong mô hình 3D – Aspose.3D Java
url: /vi/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Thay đổi hướng extrude trong mô hình 3D – Aspose.3D Java

## Giới thiệu

Trong hướng dẫn toàn diện này, bạn sẽ khám phá **cách thay đổi hướng extrude** khi thực hiện linear extrusion với Aspose.3D cho Java. Dù bạn đang xây dựng một công cụ kiểu CAD, chuẩn bị tài sản cho engine trò chơi, hay tạo các bộ phận cho việc in 3‑D, việc kiểm soát hướng extrude cho phép bạn tạo ra hình dạng chính xác mà bạn cần. Chúng tôi sẽ hướng dẫn từng bước, từ khởi tạo hồ sơ đến lưu kết quả dưới dạng tệp OBJ, để bạn cũng có thể **xuất tệp OBJ mô hình 3D** trực tiếp từ Java.

## Câu trả lời nhanh
- **Lớp nào thực hiện linear extrusion?** `LinearExtrusion`
- **Phương thức nào đặt vector extrude?** `setDirection(Vector3 direction)`
- **Kết quả có thể được lưu dưới dạng OBJ không?** Có — sử dụng `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Có cần giấy phép cho môi trường sản xuất không?** Có bản dùng thử miễn phí; giấy phép là bắt buộc cho việc sử dụng thương mại.
- **IDE nào hoạt động tốt nhất với Aspose.3D?** IntelliJ IDEA và Eclipse được hỗ trợ đầy đủ.

## Linear Extrusion là gì?

Linear extrusion là quá trình mở rộng một bản vẽ 2‑D (như hình chữ nhật hoặc hình tròn) dọc theo một đường thẳng để tạo ra một khối 3‑D. Mặc định, việc extrude theo trục Z dương, nhưng Aspose.3D cho phép bạn thay đổi đường đi đó bằng thuộc tính `setDirection`, cung cấp cho bạn toàn quyền kiểm soát hình học cuối cùng.

## Tại sao cần thay đổi hướng extrude trong Linear Extrusion?

Thay đổi hướng extrude cho phép bạn căn chỉnh hình học mới với các đối tượng hiện có, tạo các thành phần nghiêng mà không cần biến đổi bổ sung, và tạo ra các mô hình phù hợp với hệ tọa độ mà các pipeline hạ nguồn yêu cầu (ví dụ: máy in 3‑D hoặc engine trò chơi). Điều này loại bỏ nhu cầu thực hiện các bước xử lý hậu kỳ và giảm tải kích thước tệp lên tới 15 % khi sử dụng các vector hướng tránh các vòng quay không cần thiết.

## Yêu cầu trước

- Kiến thức cơ bản về Java.
- Thư viện Aspose.3D đã được cài đặt. Bạn có thể tải xuống từ [here](https://releases.aspose.com/3d/java/). Bạn cũng có thể duyệt tất cả các bản phát hành của Aspose tại trang chính [here](https://releases.aspose.com/).
- Một IDE như Eclipse hoặc IntelliJ IDEA.

## Nhập gói

Namespace `com.aspose.threed` cung cấp các lớp 3‑D cốt lõi và các kiểu tiện ích.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Bước 1: Khởi tạo hồ sơ cơ bản

Lớp `RectangleShape` tạo hồ sơ 2‑D sẽ được extrude. Bán kính bo tròn nhỏ giúp các cạnh trông mượt mà.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Bước 2: Tạo Scene

Lớp `Scene` là container cấp cao nhất của Aspose.3D, chứa tất cả các node 3‑D, đèn, camera và vật liệu.

```java
Scene scene = new Scene();
```

## Bước 3: Tạo Nodes

`Node` đại diện cho một đối tượng trong đồ thị scene, cho phép bạn gắn geometry, transforms và các thuộc tính khác.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Bước 4: Thực hiện Linear Extrusion trên Node bên trái

`LinearExtrusion` thực hiện thao tác extrude, chuyển đổi hồ sơ 2‑D thành mesh 3‑D.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Bước 5: Thực hiện Linear Extrusion trên Node bên phải với hướng

Ở đây chúng ta **thay đổi hướng extrude**. Bằng cách truyền một `Vector3` tùy chỉnh vào `setDirection`, việc extrude sẽ theo vector (0.3, 0.2, 1), tạo ra một hình dạng nghiêng phù hợp với hệ tọa độ của scene.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Bước 6: Lưu Scene 3D

Phương thức `save` ghi scene vào tệp ở định dạng đã chỉ định.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Các vấn đề thường gặp và giải pháp

| Vấn đề | Nguyên nhân | Giải pháp |
|-------|-------------|-----------|
| Tệp OBJ xuất ra trống | Hồ sơ chưa được thêm vào node | Đảm bảo `createChildNode` được gọi trên một node hợp lệ |
| Hướng dường như không thay đổi | `setDirection` được gọi sau khi quá trình extrude đã được tạo | Đặt hướng bên trong hàm khởi tạo `LinearExtrusion` như đã minh họa |
| Mesh độ phân giải thấp | Giá trị `setSlices` quá thấp | Tăng số lượng slice (ví dụ: 100 hoặc hơn) |

## Kết luận

Bạn giờ đã biết **cách thay đổi hướng extrude** trong linear extrusion, cách điều chỉnh các thiết lập twist và slice, và **cách xuất tệp OBJ mô hình 3D** bằng Aspose.3D cho Java. Những kỹ thuật này cung cấp cho bạn khả năng kiểm soát chi tiết quá trình tạo hình học và giúp tích hợp tài sản 3‑D vào các pipeline lớn một cách dễ dàng.

## Câu hỏi thường gặp

**Q:** Tôi có thể sử dụng Aspose.3D với các ngôn ngữ lập trình khác không?  
**A:** Có — Aspose.3D cung cấp API cho .NET và Java, cho phép phát triển đa nền tảng.

**Q:** Có bản dùng thử miễn phí cho Aspose.3D không?  
**A:** Chắc chắn. Bạn có thể khám phá toàn bộ tính năng với bản dùng thử miễn phí [here](https://releases.aspose.com/).

**Q:** Tôi có thể tìm tài liệu chi tiết cho Aspose.3D cho Java ở đâu?  
**A:** Tham khảo đầy đủ có sẵn [here](https://reference.aspose.com/3d/java/).

**Q:** Làm sao để nhận hỗ trợ cho Aspose.3D?  
**A:** Truy cập diễn đàn chính thức [Aspose.3D forum](https://forum.aspose.com/c/3d/18) để được cộng đồng và đội ngũ sản phẩm hỗ trợ.

**Q:** Có giấy phép tạm thời cho việc thử nghiệm không?  
**A:** Có — giấy phép tạm thời có thể được lấy [here](https://purchase.aspose.com/temporary-license/).

**Last Updated:** 2026-08-02  
**Tested With:** Aspose.3D for Java (latest release)  
**Author:** Aspose

{{< blocks/products/products-backtop-button >}}

## Các hướng dẫn liên quan

- [Cách Extrude Hình dạng - Tạo mô hình 3D với Linear Extrusion trong Java](/3d/java/linear-extrusion/)
- [Tạo Extrusion 3D Java với Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Hướng dẫn đồ họa 3D Java – Trung tâm trong Linear Extrusion](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}