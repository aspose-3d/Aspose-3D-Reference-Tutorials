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

## Introduction

Nếu bạn cần **tạo các đối tượng đùn 3d** trông mượt mà và chính xác, việc kiểm soát số lượng các lát là chìa khóa. Trong hướng dẫn này chúng ta sẽ đi qua cách chỉ định các lát khi thực hiện một đùn tuyến tính với Aspose.3D cho Java. Bạn sẽ thấy tại sao số lượng lát quan trọng, cách đặt bán kính làm tròn, và cách xuất kết quả dưới dạng tệp OBJ có thể dùng trong bất kỳ quy trình 3D nào.

## Quick Answers
- **“slices” kiểm soát gì?** Số lượng các mặt cắt trung gian được dùng để xấp xỉ bề mặt đùn.  
- **Phương thức nào đặt số lượng lát?** `LinearExtrusion.setSlices(int)`  
- **Tôi có thể thay đổi bán kính làm tròn của hình dạng không?** Có, thông qua `RectangleShape.setRoundingRadius(double)`  
- **Định dạng tệp nào được sử dụng trong ví dụ này?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Tôi có cần giấy phép để chạy mã không?** Bản dùng thử miễn phí đủ cho việc đánh giá; giấy phép thương mại cần thiết cho môi trường sản xuất.

## What is a linear extrusion with slices?

Đùn tuyến tính lấy một hình dạng 2‑D (như hình chữ nhật) và kéo dài nó dọc theo một đường thẳng để tạo thành một khối 3‑D. Bằng cách chỉ định **slices**, bạn cho Aspose.3D biết cần tạo bao nhiêu bước trung gian, điều này ảnh hưởng trực tiếp đến độ mượt của các cạnh cong như hình chữ nhật có góc bo tròn.

## Why use Aspose.3D for Java to create 3d extrusion?

* **Kiểm soát đầy đủ** – Bạn có thể điều chỉnh số lượng lát, bán kính làm tròn và định dạng xuất một cách lập trình.  
* **Đa nền tảng** – Hoạt động trên bất kỳ môi trường hỗ trợ Java nào mà không cần phụ thuộc gốc.  
* **Linh hoạt trong xuất** – Lưu trực tiếp sang OBJ, FBX, STL và nhiều định dạng khác.

## Prerequisites

1. **Bộ công cụ phát triển Java** – JDK 8 trở lên đã được cài đặt.  
2. **Aspose.3D cho Java** – Tải thư viện từ trang chính thức [here](https://releases.aspose.com/3d/java/).  
3. Một IDE hoặc trình soạn thảo văn bản mà bạn lựa chọn.

## Import Packages

Thêm không gian tên Aspose.3D vào dự án của bạn để có thể truy cập các lớp mô hình 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Step‑by‑Step Guide

### Step 1: Set up the scene and define the profile

Đầu tiên chúng ta tạo một `RectangleShape` và đặt **bán kính làm tròn** để các góc trở nên mượt. Sau đó chúng ta khởi tạo một `Scene` mới sẽ chứa toàn bộ hình học.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Step 2: **Create child node** objects for each extrusion

Mỗi phần hình học đều nằm dưới một `Node`. Ở đây chúng ta tạo hai nút anh em – một cho đùn ít lát và một cho đùn nhiều lát – và di chuyển nút bên trái một chút sang phía để kết quả dễ so sánh.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Step 3: Perform linear extrusion and **set slices**

Bây giờ chúng ta thực sự **tạo các đối tượng đùn 3d**. Hàm tạo `LinearExtrusion` nhận hình dạng và độ sâu đùn. Sử dụng một **lớp nội bộ ẩn danh** chúng ta gọi `setSlices` để điều khiển độ mượt. Nút bên trái chỉ có 2 lát (thô), trong khi nút bên phải có 10 lát (mượt).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Step 4: **Export OBJ** – save the scene

Cuối cùng chúng ta ghi cảnh vào tệp Wavefront OBJ, một định dạng được hỗ trợ rộng rãi bởi các trình chỉnh sửa 3‑D và engine game. Điều này minh họa khả năng **export obj java** của Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Common Issues and Solutions

| Vấn đề | Nguyên nhân | Giải pháp |
|-------|-------------|-----------|
| **Đùn xuất hiện phẳng** | Số lượng lát được đặt thành 1 hoặc 0 | Đảm bảo `setSlices` được gọi với giá trị ≥ 2. |
| **Các góc bo tròn trông răng cưa** | Bán kính làm tròn quá nhỏ so với số lượng lát | Tăng bán kính hoặc số lượng lát để có đường cong mượt hơn. |
| **Không tìm thấy tệp khi lưu** | `MyDir` trỏ tới thư mục không tồn tại | Tạo thư mục trước hoặc sử dụng đường dẫn tuyệt đối. |

## Frequently Asked Questions

**Q: Làm thế nào tôi có thể tải Aspose.3D cho Java?**  
A: Bạn có thể tải thư viện [here](https://releases.aspose.com/3d/java/).

**Q: Tôi có thể tìm tài liệu cho Aspose.3D ở đâu?**  
A: Tham khảo tài liệu [here](https://reference.aspose.com/3d/java/).

**Q: Có bản dùng thử miễn phí không?**  
A: Có, bạn có thể khám phá bản dùng thử miễn phí [here](https://releases.aspose.com/).

**Q: Làm sao tôi có thể nhận hỗ trợ cho Aspose.3D?**  
A: Truy cập diễn đàn hỗ trợ [here](https://forum.aspose.com/c/3d/18).

**Q: Tôi có thể mua giấy phép tạm thời không?**  
A: Có, giấy phép tạm thời có thể được mua [here](https://purchase.aspose.com/temporary-license/).

---

**Cập nhật lần cuối:** 2026-02-22  
**Kiểm tra với:** Aspose.3D for Java 24.11 (phiên bản mới nhất tại thời điểm viết)  
**Tác giả:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}