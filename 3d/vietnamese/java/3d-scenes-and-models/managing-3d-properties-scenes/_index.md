---
date: 2025-12-01
description: Tìm hiểu cách thay đổi màu kết cấu, truy cập các thuộc tính vật liệu,
  đặt giá trị Vector3 và lấy các thuộc tính theo tên trong các cảnh Java với Aspose.3D
  – một hướng dẫn đầy đủ về Aspose 3D.
linktitle: Change texture color and manage 3D properties in Java scenes using Aspose.3D
second_title: Aspose.3D Java API
title: Thay đổi màu kết cấu và quản lý các thuộc tính 3D trong các cảnh Java bằng
  Aspose.3D
url: /vi/java/3d-scenes-and-models/managing-3d-properties-scenes/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Thay đổi màu kết cấu và quản lý các thuộc tính 3D trong cảnh Java bằng Aspose.3D

## Giới thiệu

Trong **bài hướng dẫn Aspose 3D** này, bạn sẽ khám phá cách **thay đổi màu kết cấu** và làm việc với các thuộc tính 3D cũng như dữ liệu tùy chỉnh bên trong các cảnh Java. Dù bạn đang xây dựng một trò chơi, một công cụ hiển thị sản phẩm, hay một trình xem khoa học, khả năng chỉnh sửa các thuộc tính vật liệu tại thời gian chạy cho phép bạn kiểm soát nghệ thuật một cách toàn diện. Hãy cùng đi qua quy trình từng bước, từ việc tải một cảnh đến việc tinh chỉnh màu *Diffuse* bằng giá trị `Vector3`.

## Câu trả lời nhanh
- **Tôi có thể chỉnh sửa gì?** Bạn có thể thay đổi màu kết cấu, độ trong suốt, độ bóng, và bất kỳ thuộc tính tùy chỉnh nào gắn vào vật liệu.  
- **Lớp nào chứa dữ liệu?** `Material` và `PropertyCollection` của nó.  
- **Cách đặt màu mới?** Dùng `props.set("Diffuse", new Vector3(r, g, b))`.  
- **Cần giấy phép không?** Giấy phép tạm thời đủ cho việc đánh giá; giấy phép đầy đủ cần thiết cho môi trường sản xuất.  
- **Các định dạng được hỗ trợ?** FBX, OBJ, STL, GLTF và nhiều hơn nữa.

## Yêu cầu trước

- Java Development Kit (JDK) 8 hoặc mới hơn đã được cài đặt.  
- Thư viện Aspose.3D for Java (tải từ [trang web Aspose](https://releases.aspose.com/3d/java/)).  
- Kiến thức cơ bản về cú pháp Java và các khái niệm hướng đối tượng.

## Nhập gói

Trước khi viết bất kỳ logic nào, hãy nhập các lớp cho phép bạn truy cập vào thuộc tính vật liệu và thao tác vector.

```java
import java.io.IOException;

import com.aspose.threed.Material;
import com.aspose.threed.Property;
import com.aspose.threed.PropertyCollection;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;
```

### Tại sao cần nhập các lớp này?

- `Scene` tải và đại diện cho tệp 3D.  
- `Material` cung cấp định nghĩa bề mặt (kết cấu, màu sắc, v.v.).  
- `PropertyCollection` là một container kiểu từ điển cho phép bạn **truy cập các thuộc tính vật liệu** theo tên.  
- `Vector3` là kiểu dữ liệu được dùng cho màu sắc và các vector ba thành phần khác.

## Bước 1: Khởi tạo Scene

```java
String dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
```

Chúng ta tạo một đối tượng `Scene` bằng cách tải tệp FBX đã chứa sẵn kết cấu. Đây là “canvas” mà chúng ta sẽ **thay đổi màu kết cấu**.

## Bước 2: Truy cập thuộc tính vật liệu

```java
Material material = scene.getRootNode().getChildNodes().get(0).getMaterial();
PropertyCollection props = material.getProperties();
```

Ở đây chúng ta **truy cập các thuộc tính vật liệu** của lưới (mesh) đầu tiên trong cảnh. Đối tượng `Material` chứa một `PropertyCollection` lưu trữ mọi thuộc tính có thể cấu hình, như *Diffuse*, *Specular*, và dữ liệu người dùng tùy chỉnh.

## Bước 3: Liệt kê tất cả các thuộc tính

```java
for (Property prop : props) {
    System.out.println("Name" + prop.getName() + " Value = " + prop.getValue());
}
```

Duyệt qua `props` sẽ in ra tên mỗi thuộc tính và giá trị hiện tại của nó. Việc kiểm kê nhanh này giúp bạn phát hiện các khóa có thể chỉnh sửa sau này, ví dụ `"Diffuse"` cho màu cơ bản.

## Bước 4: Đặt giá trị Vector3 để thay đổi màu kết cấu

```java
props.set("Diffuse", new Vector3(1, 0, 1));
```

**Mẹo:** Hàm khởi tạo `Vector3` nhận ba số thực đại diện cho các thành phần **đỏ, xanh lá và xanh dương** (phạm vi 0‑1). Đặt `(1, 0, 1)` sẽ thay đổi màu cơ bản của kết cấu thành màu hồng tím, thực tế **thay đổi màu kết cấu** của mô hình.

## Bước 5: Lấy thuộc tính theo tên

```java
Object diffuse = (Vector3) props.get("Diffuse");
System.out.println(diffuse);
```

Điều này minh họa **lấy thuộc tính theo tên**. Chúng ta ép kiểu đối tượng trả về `Object` sang `Vector3` để làm việc với màu một cách lập trình.

## Bước 6: Truy cập thể hiện thuộc tính

```java
Property pdiffuse = props.findProperty("Diffuse");
System.out.println(pdiffuse);
```

`findProperty` trả về toàn bộ đối tượng `Property`, cho phép bạn truy cập vào siêu dữ liệu như kiểu thuộc tính, nhãn, và bất kỳ dữ liệu tùy chỉnh nào được gắn kèm.

## Bước 7: Duyệt các thuộc tính con của thuộc tính

```java
for (Property pp : pdiffuse.getProperties()) {
    System.out.println("Diffuse. " + pp.getName() + " = " + pp.getValue());
}
```

Một số thuộc tính có cấu trúc phân cấp. Duyệt `pdiffuse.getProperties()` sẽ hiển thị bất kỳ thuộc tính lồng nhau nào (ví dụ: tọa độ kết cấu, khóa animation) thuộc mục *Diffuse*.

## Các vấn đề thường gặp & Giải pháp

| Vấn đề | Nguyên nhân | Giải pháp |
|-------|-------------|-----------|
| **`NullPointerException` trên `material`** | Node có thể chưa được gán vật liệu. | Gọi `node.setMaterial(new Material())` trước khi truy cập thuộc tính. |
| **Màu không thay đổi** | Mô hình sử dụng kết cấu ghi đè màu *Diffuse*. | Tắt kết cấu hoặc chỉnh sửa trực tiếp hình ảnh kết cấu. |
| **`ClassCastException` khi lấy** | Cố gắng ép kiểu một thuộc tính không phải Vector3. | Kiểm tra kiểu thuộc tính bằng `pdiffuse.getValue().getClass()` trước khi ép. |

## Câu hỏi thường gặp

**H: Làm sao cài đặt thư viện Aspose.3D trong dự án Java?**  
Đ: Tải JAR từ [trang web Aspose](https://releases.aspose.com/3d/java/) và thêm vào classpath của dự án hoặc khai báo trong Maven/Gradle.

**H: Có tùy chọn dùng thử miễn phí cho Aspose.3D không?**  
Đ: Có, bạn có thể nhận bản dùng thử đầy đủ 30 ngày từ [trang dùng thử miễn phí của Aspose](https://releases.aspose.com/).

**H: Tài liệu chi tiết cho Aspose.3D trong Java ở đâu?**  
Đ: Tham khảo API chính thức tại [tài liệu Aspose.3D](https://reference.aspose.com/3d/java/).

**H: Có diễn đàn hỗ trợ cho Aspose.3D để đặt câu hỏi không?**  
Đ: Có—truy cập [diễn đàn hỗ trợ Aspose.3D](https://forum.aspose.com/c/3d/18) để kết nối với cộng đồng và các chuyên gia.

**H: Làm sao lấy giấy phép tạm thời cho Aspose.3D?**  
Đ: Yêu cầu qua [trang giấy phép tạm thời](https://purchase.aspose.com/temporary-license/) trên site Aspose.

**H: Tôi có thể thay đổi các thuộc tính vật liệu khác ngoài màu không?**  
Đ: Có, các thuộc tính như `Specular`, `Opacity`, và dữ liệu người dùng tùy chỉnh cũng có thể được chỉnh sửa bằng cùng mẫu `props.set`.

## Kết luận

Bạn đã học cách **thay đổi màu kết cấu**, **truy cập thuộc tính vật liệu**, **đặt giá trị Vector3**, và **lấy thuộc tính theo tên** trong một cảnh Java bằng Aspose.3D. Những kỹ thuật này cung cấp khả năng kiểm soát chi tiết đối với bất kỳ tài sản 3D nào, cho phép tạo hiệu ứng hình ảnh động và tùy chỉnh thời gian chạy trong ứng dụng của bạn.

---

**Cập nhật lần cuối:** 2025-12-01  
**Được kiểm tra với:** Aspose.3D for Java 24.11  
**Tác giả:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}