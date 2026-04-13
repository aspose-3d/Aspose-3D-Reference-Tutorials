---
date: 2026-02-22
description: Học cách tạo extrude 3D với các lát cắt bằng Aspose.3D cho Java. Hướng
  dẫn chi tiết này bao gồm extrude tuyến tính, thiết lập bán kính bo tròn và xuất
  OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Tạo Đùn 3D với Các Lát – Aspose.3D cho Java
url: /vi/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tạo Đùn 3D với Các Lát – Aspose.3D cho Java

## Giới thiệu

Nếu bạn cần **tạo các đối tượng đậm 3d** nhìn mượt mà và chính xác, hãy kiểm soát số lượng lát là chìa khóa. Trong hướng dẫn này, chúng tôi sẽ thực hiện cách chỉ định các lát khi thực hiện một tuyến tính với Aspose.3D cho Java. Bạn sẽ thấy số lượng lát quan trọng, cách đặt kính làm tròn và cách xuất kết quả dưới dạng OBJ tệp có thể sử dụng trong bất kỳ quy trình 3D nào.

## Trả lời nhanh
- **“slices” kiểm soát cái gì?** Số lượng các mặt cắt trung gian được sử dụng để tiến độ bề mặt đùn.
- **Phương thức nào đặt số lượng lát?** `LinearExtrusion.setSlices(int)`
- **Tôi có thể thay đổi dạng bán kính dạng tròn thành không?** Có, thông qua `RectangleShape.setRoundingRadius(double)`
- **Định dạng tệp nào được sử dụng trong ví dụ này?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)
- **Tôi có cần giấy phép để chạy mã không?** Bản dùng thử miễn phí đủ cho việc đánh giá; giấy phép thương mại cần thiết cho môi trường sản xuất.

## Đùn tuyến tính với các lát là gì?

Tuyến tính lấy một hình dạng 2‑D (như hình chữ cập nhật) và kéo dài nó theo chiều dọc để tạo thành một khối 3‑D. Bằng cách định nghĩa **slices**, bạn chọn Aspose.3D biết cần tạo bao nhiêu bước trung gian, điều này ảnh hưởng trực tiếp đến độ mượt của các cạnh cong như hình chữ cập nhật có góc bo tròn.

## Tại sao nên sử dụng Aspose.3D cho Java để tạo khối đùn 3d?

* **Kiểm soát đầy đủ** – Bạn có thể điều chỉnh số lượng lát, bán kính làm tròn và định dạng một trình cài đặt.
* **Da nền** – Hoạt động trên bất kỳ môi trường hỗ trợ Java nào mà không cần phụ thuộc gốc.
* **Linh hoạt trong xuất** – Lưu trực tiếp sang OBJ, FBX, STL và nhiều định dạng khác.

## Điều kiện tiên quyết

1. **Bộ công cụ phát triển Java** – JDK 8 đã được cài đặt.
2. **Aspose.3D cho Java** – Tải thư viện từ trang chính thức [tại đây](https://releases.aspose.com/3d/java/).
3. Một IDE hoặc trình soạn thảo văn bản mà bạn lựa chọn.

## Nhập gói

Thêm không gian tên Aspose.3D vào dự án của bạn để có thể truy cập các lớp mô hình 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Hướng dẫn từng bước

### Bước 1: Thiết lập khung cảnh và xác định hình dạng

Đầu tiên chúng ta tạo một `RectangleShape` và đặt **bán kính làm tròn** để các góc trở nên mượt. Sau đó chúng ta khởi tạo một `Scene` mới sẽ chứa toàn bộ hình học.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Bước 2: **Tạo các đối tượng nút con** cho mỗi phần đùn

Mỗi phần hình học đều nằm dưới một `Node`. Ở đây chúng ta tạo hai nút anh em – một cho đùn ít lát và một cho đùn nhiều lát – và di chuyển nút bên trái một chút sang phía để kết quả dễ so sánh.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Bước 3: Thực hiện đùn tuyến tính và **thiết lập các lát cắt**

Bây giờ chúng ta thực sự **tạo các đối tượng đùn 3d**. Hàm tạo `LinearExtrusion` nhận hình dạng và độ sâu đùn. Sử dụng một **lớp nội bộ ẩn danh** chúng ta gọi `setSlices` để điều khiển độ mượt. Nút bên trái chỉ có 2 lát (thô), trong khi nút bên phải có 10 lát (mượt).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Bước 4: **Xuất OBJ** – lưu khung cảnh

Cuối cùng chúng ta ghi cảnh vào tệp Wavefront OBJ, một định dạng được hỗ trợ rộng rãi bởi các trình chỉnh sửa 3‑D và engine game. Điều này minh họa khả năng **export obj java** của Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Các vấn đề thường gặp và giải pháp

| Vấn đề | Nguyên nhân | Giải pháp |
|-------|-------------|----------|
| **Dùn xuất hiện** | Số lượng được đặt thành 1 hoặc 0 | Đảm bảo `setSlices` được gọi với giá trị ≥2. |
| **Các góc bo tròn thẳng** | Bán kính làm tròn quá nhỏ nên với số lượng lát | Tăng bán kính hoặc số lượng lát để có đường cong mượt hơn. |
| **Không tìm thấy tệp khi lưu** | `MyDir` trỏ tới thư mục không tồn tại | Tạo thư mục trước hoặc sử dụng đường dẫn tuyệt đối. |

## Câu hỏi thường gặp

**Q: Làm thế nào tôi có thể tải Aspose.3D cho Java?**
A: Bạn có thể tải thư viện [tại đây](https://releases.aspose.com/3d/java/).

**Q: Tôi có thể tìm tài liệu cho Aspose.3D ở đâu?**
A: Tham khảo tài liệu [tại đây](https://reference.aspose.com/3d/java/).

**Q: Có bản dùng thử miễn phí không?**
A: Có, bạn có thể khám phá bản thử miễn phí [tại đây](https://releases.aspose.com/).

**Q: Làm sao tôi có thể nhận được hỗ trợ cho Aspose.3D?**
A: Truy cập diễn đàn được hỗ trợ [tại đây](https://forum.aspose.com/c/3d/18).

**Q: Tôi có thể mua giấy phép tạm thời không?**
A: Có, giấy phép tạm thời có thể được mua [tại đây](https://purchase.aspose.com/temporary-license/).

---

**Cập nhật lần cuối:** 2026-02-22
**Kiểm tra với:** Aspose.3D for Java 24.11 (phiên bản mới nhất tại thời điểm viết)
**Tác giả:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}