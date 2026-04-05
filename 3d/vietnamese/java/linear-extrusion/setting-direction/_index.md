---
date: 2026-02-22
description: Học cách đặt hướng trong quá trình ép tuyến tính và xuất mô hình 3D định
  dạng OBJ bằng Aspose.3D cho Java. Thực hiện theo hướng dẫn từng bước của chúng tôi.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Cách đặt hướng trong Extrusion tuyến tính bằng Aspose.3D cho Java
url: /vi/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cách Đặt Hướng trong Linear Extrusion với Aspose.3D cho Java

## Giới thiệu

Trong hướng dẫn toàn diện này, bạn sẽ khám phá **cách đặt hướng** khi thực hiện linear extrusion với Aspose.3D cho Java. Cho dù bạn đang xây dựng một công cụ kiểu CAD hay tạo geometry cho một engine game, việc kiểm soát hướng extrusion cho phép bạn tạo ra hình dạng chính xác mà bạn cần. Chúng tôi sẽ hướng dẫn từng bước, từ khởi tạo profile đến lưu kết quả dưới dạng file OBJ, để bạn cũng có thể **xuất file mô hình 3d obj** trực tiếp từ Java.

## Câu trả lời nhanh
- **Lớp chính cho linear extrusion là gì?** `LinearExtrusion`
- **Phương thức nào định nghĩa hướng extrusion?** `setDirection(Vector3 direction)`
- **Tôi có thể xuất kết quả dưới dạng OBJ không?** Có, sử dụng `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Tôi có cần giấy phép để phát triển không?** Có bản dùng thử miễn phí; giấy phép cần thiết cho môi trường sản xuất.
- **IDE Java nào hoạt động tốt nhất?** IntelliJ IDEA hoặc Eclipse đều được hỗ trợ đầy đủ.

## Linear Extrusion là gì?

Linear extrusion lấy một profile 2‑D (như hình chữ nhật hoặc hình tròn) và kéo dài nó dọc theo một đường thẳng để tạo thành một khối 3‑D. Mặc định, extrusion theo trục Z dương, nhưng Aspose.3D cho phép bạn thay đổi đường đi này bằng thuộc tính `setDirection`.

## Tại sao cần đặt hướng trong Linear Extrusion?

Việc đặt hướng tùy chỉnh hữu ích khi:
- Căn chỉnh geometry với các đối tượng đã có trong scene.
- Tạo các bộ phận nghiêng hoặc có góc mà không cần bước biến đổi bổ sung.
- Xuất mô hình phải khớp với hệ tọa độ cụ thể (ví dụ: cho in 3‑D hoặc engine game).

## Yêu cầu trước

Trước khi bắt đầu, hãy chắc chắn rằng bạn có:

- Kiến thức cơ bản về Java.
- Thư viện Aspose.3D đã được cài đặt. Bạn có thể tải xuống từ [here](https://releases.aspose.com/3d/java/).
- Một IDE như Eclipse hoặc IntelliJ IDEA.

## Nhập các gói

Đầu tiên, nhập các namespace cung cấp các lớp 3‑D cốt lõi và các kiểu tiện ích.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Bước 1: Khởi tạo Profile Cơ bản

Tạo hình dạng sẽ được extrusion. Trong ví dụ này, chúng ta sử dụng `RectangleShape` với bán kính bo tròn nhỏ để các cạnh trông mượt hơn.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Bước 2: Tạo Scene

Đối tượng `Scene` hoạt động như một container cho tất cả các node 3‑D, ánh sáng, camera và vật liệu.

```java
Scene scene = new Scene();
```

## Bước 3: Tạo Nodes

Thêm hai node con vào gốc scene — một cho extrusion bên trái và một cho extrusion bên phải. Node bên phải được dịch chuyển để hai đối tượng không chồng lên nhau.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Bước 4: Thực hiện Linear Extrusion trên Node Trái

Extrude profile trên node trái bằng hướng trục Z mặc định. Chúng ta cũng thêm một vòng quay 360° đầy đủ và tăng số slice để lưới mịn hơn.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Bước 5: Thực hiện Linear Extrusion trên Node Phải với Hướng

Đây là nơi chúng ta **đặt hướng**. Bằng cách truyền một `Vector3` tùy chỉnh vào `setDirection`, extrusion sẽ theo vector (0.3, 0.2, 1), tạo ra một hình dạng nghiêng.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Bước 6: Lưu Scene 3D

Cuối cùng, xuất scene sang định dạng Wavefront OBJ. Bước này minh họa cách **save obj file java** và giúp bạn dễ dàng xem kết quả trong bất kỳ trình xem 3‑D nào.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Các vấn đề thường gặp và giải pháp

| Vấn đề | Nguyên nhân | Cách khắc phục |
|-------|-------------|----------------|
| File OBJ xuất ra rỗng | Profile chưa được thêm vào node | Đảm bảo `createChildNode` được gọi trên một node hợp lệ |
| Hướng không thay đổi | `setDirection` được gọi sau khi extrusion đã được tạo | Đặt hướng trong khởi tạo `LinearExtrusion` như trong ví dụ |
| Lưới có độ phân giải thấp | Giá trị `setSlices` quá thấp | Tăng số slice (ví dụ: 100 hoặc hơn) |

## Kết luận

Bạn đã biết **cách đặt hướng** trong linear extrusion, cách điều chỉnh twist và slice, và cách **xuất file mô hình 3d obj** bằng Aspose.3D cho Java. Những kỹ thuật này cho phép bạn kiểm soát chi tiết quá trình tạo geometry và dễ dàng tích hợp tài sản 3‑D vào các pipeline lớn hơn.

## Câu hỏi thường gặp

### Q1: Tôi có thể dùng Aspose.3D với các ngôn ngữ lập trình khác không?

A1: Aspose.3D hỗ trợ nhiều ngôn ngữ lập trình, bao gồm .NET và Java.

### Q2. Có bản dùng thử miễn phí cho Aspose.3D không?

A2: Có, bạn có thể khám phá các tính năng của Aspose.3D với bản dùng thử miễn phí [here](https://releases.aspose.com/).

### Q3: Tôi có thể tìm tài liệu chi tiết cho Aspose.3D cho Java ở đâu?

A3: Tài liệu đầy đủ có sẵn [here](https://reference.aspose.com/3d/java/).

### Q4: Làm sao để nhận hỗ trợ cho Aspose.3D?

A4: Truy cập [Aspose.3D forum](https://forum.aspose.com/c/3d/18) để được trợ giúp hoặc đặt câu hỏi.

### Q5: Có giấy phép tạm thời cho Aspose.3D không?

A5: Có, bạn có thể nhận giấy phép tạm thời [here](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-02-22  
**Tested With:** Aspose.3D for Java (latest release)  
**Author:** Aspose