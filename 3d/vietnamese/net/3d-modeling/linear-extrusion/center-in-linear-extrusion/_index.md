---
date: 2026-01-07
description: Học cách thêm mặt phẳng nền khi thực hiện extrude tuyến tính với Aspose.3D
  cho .NET và xuất tệp Wavefront OBJ. Nắm vững kỹ thuật căn giữa và đặt nền trong
  mô hình 3‑D.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: Thêm Mặt Phẳng Nền và Trung Tâm trong Đùn Tuyến Tính
url: /vi/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Thêm Mặt Phẳng Đất và Trung Tâm trong Đùn Đường Thẳng

## Giới thiệu

Chào mừng bạn đến với hướng dẫn toàn diện này về việc làm chủ kỹ thuật đùn đường thẳng bằng Aspose.3D cho .NET. Nếu bạn muốn **thêm mặt phẳng đất** vào mô hình và **xuất tệp Wavefront OBJ** trong khi giữ cho đùn được căn giữa, bạn đã đến đúng nơi. Trong tutorial này, chúng ta sẽ khám phá kỹ thuật đùn đường thẳng, đặc biệt tập trung vào khía cạnh căn giữa và cách một mặt phẳng đất giúp bạn hình dung kết quả rõ ràng hơn.

## Câu trả lời nhanh
- **“add ground plane” mang lại gì?** Nó cung cấp một tham chiếu trực quan giúp dễ dàng nhìn thấy vị trí của đùn trên mặt phẳng X‑Z.  
- **Định dạng nào được sử dụng để xuất mô hình?** Cảnh được lưu dưới dạng tệp Wavefront OBJ (`FileFormat.WavefrontOBJ`).  
- **Tôi có cần giấy phép để chạy mã không?** Bản dùng thử miễn phí đủ cho phát triển; giấy phép vĩnh viễn cần thiết cho môi trường sản xuất.  
- **Tôi có thể thay đổi độ dài đùn không?** Có – chỉnh sửa tham số thứ hai của `LinearExtrusion`.  
- **Căn giữa có phải là tùy chọn không?** Đặt `Center = true` sẽ căn giữa đùn quanh profile; `false` sẽ căn nó về một phía.

## Yêu cầu trước

Trước khi chúng ta bắt đầu hành trình thú vị này, hãy chắc chắn rằng bạn đã chuẩn bị đầy đủ các yêu cầu sau:

- Kiến thức cơ bản về ngôn ngữ lập trình C#.
- Visual Studio đã được cài đặt trên máy của bạn.
- Thư viện Aspose.3D cho .NET, bạn có thể tải xuống từ [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).
- Đảm bảo bạn có quyền truy cập vào [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) để tham khảo trong suốt tutorial.

## Nhập các không gian tên

Để bắt đầu, chúng ta hãy nhập các không gian tên cần thiết. Chúng sẽ tạo nền tảng cho kiệt tác mô hình 3D của chúng ta.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Bước 1: Khởi tạo Profile Cơ bản

Chúng ta bắt đầu bằng việc định nghĩa một profile hình chữ nhật sẽ được đùn. `RoundingRadius` thêm một vòng bo nhẹ vào các góc.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Bước 2: Tạo một Scene 3D

Đối tượng `Scene` hoạt động như một container cho tất cả hình học, ánh sáng và camera.

```csharp
Scene scene = new Scene();
```

## Bước 3: Tạo các Node Trái và Phải

Hai node anh em được tạo dưới node gốc. Một sẽ minh họa việc đùn **không** căn giữa, còn một khác **có** căn giữa. Chúng tôi cũng dịch chuyển node trái để hai ví dụ không chồng lên nhau.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Bước 4: Thực hiện Linear Extrusion trên Node Trái (Không Căn Giữa)

Ở đây chúng ta đùn profile mà không căn giữa. Lưu ý cờ `Center = false`.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Bước 5: Thêm Mặt Phẳng Đất để Tham Chiếu (Node Trái)

Thêm một hộp mỏng hoạt động như một **mặt phẳng đất** để bạn có thể nhìn rõ cách đùn đặt trên nền.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Bước 6: Thực hiện Linear Extrusion trên Node Phải (Có Căn Giữa)

Bây giờ chúng ta đùn cùng một profile nhưng bật tính năng căn giữa. Hình học sẽ được đặt đối xứng quanh gốc của profile.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Bước 7: Thêm Mặt Phẳng Đất để Tham Chiếu (Node Phải)

Một mặt phẳng đất thứ hai được thêm vào node phải để duy trì so sánh trực quan nhất quán.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Bước 8: Xuất Tệp Wavefront OBJ

Cuối cùng, chúng ta **xuất Wavefront OBJ** để kết quả có thể được mở trong bất kỳ trình xem 3‑D tiêu chuẩn nào.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Tại sao cần thêm Mặt Phẳng Đất?

Thêm một mặt phẳng đất cung cấp cho bạn một gợi ý trực quan ngay lập tức về chiều cao và vị trí căn chỉnh của đùn. Điều này đặc biệt hữu ích khi bạn cần so sánh kết quả có căn giữa và không căn giữa, như đã trình bày trong tutorial này.

## Vấn đề thường gặp & Mẹo

- **Mặt phẳng đất không hiển thị:** Đảm bảo độ dày của mặt phẳng (`0.01` trong hàm khởi tạo `Box`) đủ nhỏ để không che khuất đùn nhưng đủ lớn để được render.  
- **Xuất thất bại:** Kiểm tra thư mục đầu ra tồn tại và bạn có quyền ghi.  
- **Đùn được căn giữa xuất hiện lệch:** Kiểm tra lại thuộc tính `Center`; `true` căn giữa profile, `false` căn nó về một phía.

## Câu hỏi thường gặp

### Hỏi 1: Tôi có thể sử dụng Aspose.3D cho .NET với các ngôn ngữ lập trình khác không?

A1: Aspose.3D chủ yếu hỗ trợ các ngôn ngữ .NET như C# và VB.NET.

### Hỏi 2: Tôi có thể tìm hỗ trợ cho các câu hỏi liên quan đến Aspose.3D ở đâu?

A2: Truy cập [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) để nhận hỗ trợ và thảo luận chuyên biệt.

### Hỏi 3: Có bản dùng thử miễn phí cho Aspose.3D cho .NET không?

A3: Có, bạn có thể truy cập bản dùng thử miễn phí [tại đây](https://releases.aspose.com/).

### Hỏi 4: Làm thế nào để tôi có được giấy phép tạm thời cho Aspose.3D cho .NET?

A4: Bạn có thể lấy giấy phép tạm thời [tại đây](https://purchase.aspose.com/temporary-license/).

### Hỏi 5: Tôi có thể mua giấy phép Aspose.3D cho .NET ở đâu?

A5: Mua giấy phép của bạn [tại đây](https://purchase.aspose.com/buy).

### Hỏi 6: Tôi có thể xuất scene sang các định dạng khác ngoài OBJ không?

A6: Có, Aspose.3D hỗ trợ nhiều định dạng như STL, FBX và GLTF. Chỉ cần thay đổi giá trị enum `FileFormat` trong phương thức `Save`.

### Hỏi 7: Làm sao để thay đổi số lượng lát (slices) của đùn?

A7: Điều chỉnh thuộc tính `Slices` trong hàm khởi tạo `LinearExtrusion` để kiểm soát mật độ lưới.

---

**Cập nhật lần cuối:** 2026-01-07  
**Kiểm tra với:** Aspose.3D cho .NET phiên bản mới nhất  
**Tác giả:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}