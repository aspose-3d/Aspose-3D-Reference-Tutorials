---
date: 2025-12-19
description: Tìm hiểu cách tạo cảnh 3D và xuất tệp OBJ 3D bằng Twist Offset trong
  Linear Extrusion với Aspose.3D cho Java.
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: Tạo cảnh 3D với Twist Offset – Aspose.3D Java
url: /vi/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tạo cảnh 3d với Twist Offset – Aspose.3D cho Java

## Giới thiệu

Trong thế giới động của đồ họa 3D, việc học cách **create 3d scene** với extrude tuyến tính là một bước đột phá. Với Aspose.3D cho Java, bạn có thể nâng cao kỹ năng mô hình 3D của mình bằng cách tích hợp tính năng Twist Offset vào quá trình extrude tuyến tính. Hướng dẫn này sẽ chỉ cho bạn các bước sử dụng Twist Offset trong Linear Extrusion bằng Aspose.3D cho Java, cung cấp cho bạn công cụ để tạo ra các cảnh 3D ấn tượng.

## Câu trả lời nhanh
- **What does Twist Offset do?** Nó dịch chuyển điểm bắt đầu của twist dọc theo đường extrude, cho bạn kiểm soát tốt hơn hình học.  
- **Which file format is used for export?** Ví dụ lưu mô hình dưới dạng Wavefront OBJ (`.obj`).  
- **Do I need a license for development?** Bản dùng thử miễn phí đủ cho việc thử nghiệm; cần giấy phép thương mại cho môi trường sản xuất.  
- **What Java version is required?** Java 8 hoặc mới hơn.  
- **Can I change the number of slices?** Có – phương thức `setSlices` xác định độ mượt của twist.

## Yêu cầu trước

Trước khi bắt đầu hướng dẫn, hãy chắc chắn rằng bạn đã chuẩn bị các yêu cầu sau:

- Java Environment: Đảm bảo bạn đã cài đặt môi trường phát triển Java trên hệ thống.  
- Aspose.3D for Java: Tải xuống và cài đặt thư viện Aspose.3D từ [download link](https://releases.aspose.com/3d/java/).  
- Documentation: Làm quen với [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  

## Nhập các gói

Trong dự án Java của bạn, nhập các gói cần thiết để bắt đầu sử dụng Aspose.3D cho Java. Đảm bảo bạn đã bao gồm các thư viện cần thiết để tích hợp mượt mà.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Bước 1: Thiết lập môi trường

Bắt đầu bằng việc thiết lập môi trường phát triển Java và đảm bảo Aspose.3D cho Java đã được cài đặt đúng cách.

## Bước 2: Khởi tạo hồ sơ cơ bản

Tạo một hồ sơ cơ bản cho việc extrude, trong trường hợp này là `RectangleShape` với bán kính bo tròn là 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Bước 3: Tạo một cảnh 3D

Xây dựng một cảnh 3D để chứa các đối tượng đã được extrude.

```java
// Create a scene
Scene scene = new Scene();
```

## Bước 4: Tạo các Node

Tạo các node trong cảnh để đại diện cho các thực thể khác nhau.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Bước 5: Thực hiện Linear Extrusion

Sử dụng linear extrusion trên cả node trái và phải với các thuộc tính khác nhau.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Bước 6: Lưu cảnh 3D

Lưu cảnh 3D mới tạo của bạn với định dạng tệp đã chỉ định.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Cách lưu mô hình 3d và xuất 3d obj

Lệnh `scene.save` trong bước trước **saves the 3d model** dưới dạng tệp OBJ, một định dạng **export 3d obj** được hỗ trợ rộng rãi. Bạn có thể thay đổi tên tệp hoặc chọn định dạng hỗ trợ khác (ví dụ: STL, FBX) bằng cách điều chỉnh enum `FileFormat`.

## Kết luận

Chúc mừng! Bạn đã triển khai thành công Twist Offset trong Linear Extrusion bằng Aspose.3D cho Java. Tính năng mạnh mẽ này mở ra một thế giới khả năng cho công việc mô hình 3D của bạn, cho phép bạn **create 3d scene** với các vòng xoắn và offset tinh vi, và sau đó **save 3d model** ở định dạng sẵn sàng cho các pipeline tiếp theo.

## Câu hỏi thường gặp

### Q1: Can I use Aspose.3D for Java in non-commercial projects?

A1: Có, Aspose.3D cho Java có thể được sử dụng trong cả dự án thương mại và phi thương mại. Kiểm tra [licensing options](https://purchase.aspose.com/buy) để biết thêm chi tiết.

### Q2: Where can I find support for Aspose.3D for Java?

A2: Truy cập [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18) để nhận hỗ trợ và kết nối với cộng đồng.

### Q3: Is there a free trial available for Aspose.3D for Java?

A3: Có, bạn có thể khám phá phiên bản dùng thử miễn phí từ [releases page](https://releases.aspose.com/).

### Q4: How do I obtain a temporary license for Aspose.3D for Java?

A4: Nhận giấy phép tạm thời cho dự án của bạn bằng cách truy cập [this link](https://purchase.aspose.com/temporary-license/).

### Q5: Are there additional examples and tutorials available?

A5: Có, tham khảo [documentation](https://reference.aspose.com/3d/java/) để có thêm ví dụ và hướng dẫn chi tiết.

## Các câu hỏi thường gặp

**Q: Is this tutorial part of an Aspose 3d tutorial series?**  
A: Có – đây là một **aspose 3d tutorial** chính thức minh họa một tính năng cụ thể của thư viện.

**Q: Can I use a different shape instead of a rectangle?**  
A: Chắc chắn. Bất kỳ triển khai `IProfile` nào (ví dụ: `CircleShape`, `PolygonShape` tùy chỉnh) đều có thể được extrude.

**Q: What happens if I omit `setTwistOffset`?**  
A: Quá trình extrude sẽ bắt đầu xoắn từ gốc của profile, tạo ra một vòng xoắn đối xứng.

**Q: How do I increase the smoothness of the twist?**  
A: Tăng giá trị truyền vào `setSlices`; số lượng slice cao hơn tạo ra hình học mượt hơn.

**Q: Which other file formats can I export besides OBJ?**  
A: Aspose.3D hỗ trợ STL, FBX, GLTF, 3MF và một số định dạng khác thông qua enum `FileFormat`.

---

**Cập nhật lần cuối:** 2025-12-19  
**Kiểm tra với:** Aspose.3D 24.11 cho Java  
**Tác giả:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}