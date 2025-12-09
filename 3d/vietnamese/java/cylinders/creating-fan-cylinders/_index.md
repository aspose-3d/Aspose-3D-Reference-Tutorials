---
date: 2025-12-09
description: Học cách thêm nút con, định vị các đối tượng 3D và lưu cảnh dưới dạng
  OBJ trong khi tạo các hình trụ quạt tùy chỉnh bằng Aspose.3D cho Java.
language: vi
linktitle: Adding Child Node for Fan Cylinders with Aspose.3D Java
second_title: Aspose.3D Java API
title: Thêm nút con để xây dựng các hình trụ dạng quạt với Aspose.3D cho Java
url: /java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Thêm Nút Con để Tạo Trụ Quạt với Aspose.3D cho Java

## Giới thiệu

Sẵn sàng **add child node** vào một cảnh 3‑D và tạo các trụ quạt bắt mắt? Trong hướng dẫn này, chúng tôi sẽ đi qua từng bước — từ thiết lập cảnh, định vị các đối tượng 3D đến cuối cùng **save scene as OBJ** — bằng cách sử dụng Aspose.3D cho Java. Dù bạn đang tinh chỉnh tài sản cho trò chơi hay xây dựng một nguyên mẫu nhanh, các khái niệm ở đây sẽ giúp bạn kiểm soát vững chắc các mô hình 3‑D của mình.

## Câu trả lời nhanh
- **What does “add child node” do?** Nó chèn một đối tượng mới vào đồ thị cảnh, kế thừa các biến đổi từ nút cha.  
- **How can I position a 3D object?** Bằng cách áp dụng một phép dịch (hoặc quay/thu phóng) lên transform của nút.  
- **Which file format is used for export?** Ví dụ lưu mô hình dưới dạng tệp Wavefront OBJ.  
- **Do I need a license to run the code?** Bản dùng thử miễn phí đủ cho việc đánh giá; cần có giấy phép cho môi trường sản xuất.  
- **What IDE works best?** Bất kỳ IDE Java nào (IntelliJ IDEA, Eclipse, VS Code) hỗ trợ JDK 8+.

## add child node là gì trong Aspose.3D?
Thêm một nút con có nghĩa là tạo một nút mới dưới một nút cha hiện có trong cấu trúc cảnh. Nút con kế thừa hệ tọa độ của nút cha, giúp dễ dàng **position 3d object** các thể hiện tương đối với nhau.

## Tại sao cần thêm nút con khi tạo trụ quạt?
- **Modular design:** Mỗi trụ (quạt hoặc không quạt) tồn tại trong nút riêng của nó, giúp đơn giản hoá việc chỉnh sửa sau này.  
- **Transform inheritance:** Di chuyển, quay hoặc thu phóng nút cha và tất cả các nút con sẽ tự động theo.  
- **Cleaner scene graph:** Cải thiện khả năng đọc và gỡ lỗi của các mô hình phức tạp.

## Yêu cầu trước

- **Java Development Kit (JDK)** – tải xuống từ [official site](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – lấy thư viện mới nhất từ [download link](https://releases.aspose.com/3d/java/).

## Nhập các gói

Bắt đầu bằng cách nhập các gói cần thiết vào dự án Java của bạn. Bước này rất quan trọng để truy cập các chức năng do Aspose.3D cung cấp.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Bước 1: Tạo một Scene

Đầu tiên, chúng ta tạo một cảnh 3‑D trống sẽ chứa tất cả các đối tượng của chúng ta.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Bước 2: Tạo một Trụ Quạt

Tiếp theo, chúng ta xây dựng một trụ sẽ được hiển thị như một quạt (phạm vi quay một phần).

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

## Bước 3: Thêm Nút Con & Định Vị Đối Tượng 3D

Bây giờ chúng ta **add child node** vào cảnh và **position the 3d object** bằng cách đặt phép dịch cho nó. Đây là nơi trụ quạt trở thành một phần của đồ thị cảnh.

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Bước 4: Tạo một Trụ Không Quạt

Để minh họa tính linh hoạt của Aspose.3D, chúng ta cũng tạo một trụ thông thường không có quạt và thêm nó như một nút con khác.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Bước 5: Lưu Scene dưới dạng OBJ

Cuối cùng, chúng ta **save scene as OBJ** để bạn có thể xem kết quả trong bất kỳ trình xem 3‑D tiêu chuẩn nào.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Chúc mừng! Bạn đã **added child node** thành công, định vị các đối tượng của mình, và xuất mô hình.

## Các vấn đề thường gặp & Mẹo

| Vấn đề | Giải pháp |
|-------|----------|
| **File not found** khi lưu | Đảm bảo thư mục đích tồn tại và bạn có quyền ghi. |
| **Cylinder appears flat** | Kiểm tra lại giá trị bán kính và chiều cao; Aspose.3D yêu cầu các đơn vị cùng tỉ lệ. |
| **Fan slice looks incomplete** | Điều chỉnh `ThetaLength` (đơn vị radian) để bao phủ góc mong muốn. |
| **Scene not visible in viewer** | Xác nhận tệp OBJ đã được lưu kèm theo tệp `.mtl` (vật liệu) nếu cần. |

## Câu hỏi thường gặp

**Q:** *Aspose.3D có tương thích với các thư viện Java khác cho mô hình 3D không?*  
**A:** Có, Aspose.3D hoạt động cùng với các thư viện Java 3‑D khác, cho phép bạn kết hợp các tính năng khi cần.

**Q:** *Tôi có thể tùy chỉnh thêm giao diện của các trụ quạt đã tạo không?*  
**A:** Chắc chắn. Bạn có thể áp dụng vật liệu, kết cấu và ánh sáng bằng các lớp `Material` và `Light`.

**Q:** *Tôi có thể tìm hỗ trợ hoặc trợ giúp bổ sung cho Aspose.3D ở đâu?*  
**A:** Truy cập [Aspose.3D forum](https://forum.aspose.com/c/3d/18) để nhận sự giúp đỡ từ cộng đồng và phản hồi chính thức.

**Q:** *Có bản dùng thử miễn phí cho Aspose.3D không?*  
**A:** Có, bạn có thể khám phá Aspose.3D bằng một [free trial](https://releases.aspose.com/) trước khi mua.

**Q:** *Làm sao tôi có thể nhận giấy phép tạm thời cho Aspose.3D?*  
**A:** Lấy giấy phép tạm thời [tại đây](https://purchase.aspose.com/temporary-license/) để thử nghiệm và phát triển.

## Kết luận

Trong hướng dẫn này, chúng tôi đã trình bày cách **add child node**, **position 3d object**, và **save scene as OBJ** trong khi tạo các trụ quạt tùy chỉnh bằng Aspose.3D cho Java. Những khối xây dựng này cung cấp cho bạn tính linh hoạt để xây dựng các cấu trúc 3‑D phức tạp và xuất chúng cho bất kỳ quy trình downstream nào.

---

**Cập nhật lần cuối:** 2025-12-09  
**Kiểm tra với:** Aspose.3D 24.12 for Java  
**Tác giả:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}