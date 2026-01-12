---
date: 2026-01-12
description: Học cách tạo trụ đáy cắt và cách xuất mô hình 3D định dạng OBJ bằng Aspose.3D
  cho .NET. Hãy làm theo hướng dẫn từng bước này để thành thạo mô hình 3D.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Cách tạo hình trụ đáy nghiêng bằng Aspose.3D cho .NET
url: /vi/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Đồ Họa Xi Lan Đáy Cắt Xén Tùy Chỉnh

## Giới thiệu
Chào mừng bạn đến với hướng dẫn chi tiết, nơi **bạn sẽ học cách tạo mô hình shear bottom cylinder** bằng Aspose.3D for .NET. Dù bạn đang xây dựng tài sản cho trò chơi, một bộ phận cơ khí, hay một bản demo trực quan, tutorial này sẽ chỉ cho bạn cách tạo hình đáy xi lan, áp dụng shear, và cuối cùng **xuất file mô hình 3D OBJ** để sử dụng trong bất kỳ quy trình downstream nào. Hãy cùng đi qua từng bước, để bạn có thể bắt đầu tạo geometry tùy chỉnh trong vài phút.

## Câu trả lời nhanh
- **Shear bottom cylinder là gì?** Một xi lan mà mặt đáy bị nghiêng (cắt xén) thay vì phẳng.  
- **Thư viện nào được sử dụng?** Aspose.3D for .NET.  
- **Làm thế nào để xuất mô hình?** Sử dụng `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Có cần giấy phép không?** Có phiên bản dùng thử; giấy phép thương mại cần thiết cho môi trường sản xuất.  
- **Các điều kiện tiên quyết là gì?** Môi trường phát triển .NET và gói NuGet Aspose.3D.

## Shear bottom cylinder là gì?
Shear bottom cylinder là một lưới xi lan tiêu chuẩn mà mặt đáy đã được biến đổi bằng thao tác shear. Điều này cho phép bạn tạo các nền nghiêng, dốc, hoặc các kết nối tùy chỉnh mà không cần chỉnh sửa các đỉnh thủ công.

## Tại sao nên dùng Aspose.3D cho nhiệm vụ này?
- **Kiểm soát đầy đủ** các tham số hình học (bán kính, chiều cao, số đoạn).  
- **Hỗ trợ cắt xén tích hợp** qua thuộc tính `ShearBottom`, giúp bạn tránh việc thao tác lưới cấp thấp.  
- **Xuất một cú nhấp** sang các định dạng phổ biến như OBJ, FBX và STL, giúp tích hợp với các công cụ khác mượt mà.

## Điều kiện tiên quyết
- Kiến thức cơ bản về C# và .NET.  
- Aspose.3D for .NET đã được cài đặt. Bạn có thể tải xuống **[tại đây](https://releases.aspose.com/3d/net/)**.  
- Một IDE tương thích .NET (Visual Studio, Rider, hoặc VS Code).

## Nhập các Namespace
Trong file C# của bạn, bắt đầu bằng việc nhập các namespace cần thiết:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Bước 1: Tạo một Scene
Đầu tiên, khởi tạo một scene 3‑D mới sẽ chứa tất cả các đối tượng của chúng ta.

```csharp
Scene scene = new Scene();
```

## Bước 2: Tạo Cylinder 1
Tạo xi lan chính mà chúng ta sẽ tùy chỉnh với đáy cắt xén.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Bước 3: Tùy chỉnh Shear Bottom cho Cylinder 1
Áp dụng shear, bật tính năng tạo fan, và điều chỉnh các thuộc tính khác để đạt được hình dạng mong muốn.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Bước 4: Thêm Cylinder 1 vào Scene
Đặt xi lan đã tùy chỉnh vào scene và di chuyển một chút sang phải để chúng ta có thể nhìn thấy cả hai đối tượng cạnh nhau.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Bước 5: Tạo Cylinder 2
Tạo một xi lan thứ hai, đơn giản, để so sánh.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Bước 6: Thêm Cylinder 2 vào Scene
Thêm xi lan thứ hai mà không có shear tùy chỉnh—điều này giúp minh họa hiệu ứng của các bước trước.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Bước 7: Lưu Scene
Cuối cùng, xuất toàn bộ scene dưới dạng file OBJ để bạn có thể mở trong Blender, Maya, hoặc bất kỳ trình xem 3‑D nào khác.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Các vấn đề thường gặp & Mẹo
- **Giá trị shear**: `Vector2` nhận các hệ số shear X và Y. Giá trị `0.83` tương đương khoảng 47,5°, nhưng bạn có thể điều chỉnh cho các góc khác.  
- **Đường dẫn xuất**: Đảm bảo thư mục bạn chỉ định tồn tại và bạn có quyền ghi; nếu không `scene.Save` sẽ ném ngoại lệ.  
- **Hiệu năng**: Đối với các xi lan có rất nhiều đoạn, hãy cân nhắc giảm số đoạn (`20` trong ví dụ) để giữ kích thước file OBJ ở mức hợp lý.

## Câu hỏi thường gặp

### Aspose.3D for .NET có phù hợp cho người mới bắt đầu không?
Chắc chắn! Aspose.3D for .NET cung cấp API thân thiện, dễ tiếp cận cho cả người mới và các nhà phát triển có kinh nghiệm.

### Tôi có thể áp dụng các góc shear khác nhau cho các xi lan không?
Có, bạn có thể tùy chỉnh `ShearBottom` cho mỗi xi lan riêng biệt, cho phép tạo ra các hiệu ứng độc đáo.

### Có phiên bản dùng thử không?
Có, bạn có thể khám phá phiên bản dùng thử miễn phí **[tại đây](https://releases.aspose.com/)**.

### Tôi có thể tìm hỗ trợ bổ sung ở đâu?
Truy cập **[diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18)** để nhận hỗ trợ cộng đồng và thảo luận.

### Làm sao để có được giấy phép tạm thời?
Nhận giấy phép tạm thời **[tại đây](https://purchase.aspose.com/temporary-license/)**.

**Additional Q&A**

**Q: Làm sao để thay đổi định dạng xuất sang FBX?**  
A: Thay `FileFormat.WavefrontOBJ` bằng `FileFormat.FBX` trong lời gọi `scene.Save`.

**Q: Tôi có thể tạo hoạt hình cho xi lan sau khi xuất không?**  
A: OBJ không hỗ trợ hoạt hình; hãy dùng FBX hoặc GLTF nếu bạn cần dữ liệu hoạt hình.

**Q: Nếu tôi cần bán kính xi lan lớn hơn thì sao?**  
A: Điều chỉnh hai tham số đầu tiên của hàm khởi tạo `Cylinder` (ví dụ, `new Cylinder(4, 4, …)`).

## Kết luận
Bạn đã nắm vững cách **tạo shear bottom cylinder** và xuất chúng dưới dạng file OBJ bằng Aspose.3D for .NET. Hãy thử nghiệm với các giá trị shear khác nhau, số đoạn khác nhau, và các định dạng xuất để đáp ứng nhu cầu dự án của bạn. Chúc bạn mô hình hoá vui vẻ!

---

**Last Updated:** 2026-01-12  
**Tested With:** Aspose.3D for .NET 24.11 (phiên bản mới nhất tại thời điểm viết)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}