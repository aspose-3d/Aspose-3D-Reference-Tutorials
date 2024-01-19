---
title: Trung tâm đùn tuyến tính
linktitle: Trung tâm đùn tuyến tính
second_title: API Aspose.3D .NET
description: Khám phá thế giới mô hình 3D với Aspose.3D cho .NET. Kỹ thuật ép đùn tuyến tính tập trung, tạo ra các thiết kế tuyệt đẹp và thỏa sức sáng tạo của bạn.
type: docs
weight: 10
url: /vi/net/linear-extrusion/center-in-linear-extrusion/
---
## Giới thiệu

Chào mừng bạn đến với hướng dẫn toàn diện này về cách làm chủ quá trình ép đùn tuyến tính bằng Aspose.3D cho .NET. Nếu bạn đang tìm cách nâng cao kỹ năng lập mô hình 3D của mình và tạo ra các sản phẩm ép đùn tuyệt đẹp thì bạn đã đến đúng nơi. Trong hướng dẫn này, chúng ta sẽ đi sâu vào kỹ thuật ép đùn tuyến tính, đặc biệt tập trung vào khía cạnh định tâm để đưa thiết kế của bạn lên một tầm cao hoàn toàn mới.

## Điều kiện tiên quyết

Trước khi chúng ta bắt đầu cuộc hành trình thú vị này, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:

- Hiểu biết cơ bản về ngôn ngữ lập trình C#.
- Visual Studio được cài đặt trên máy của bạn.
-  Thư viện Aspose.3D cho .NET mà bạn có thể tải xuống từ[Tài liệu Aspose.3D .NET](https://reference.aspose.com/3d/net/).
-  Đảm bảo bạn có quyền truy cập vào[Tài liệu Aspose.3D .NET](https://reference.aspose.com/3d/net/) để tham khảo trong suốt hướng dẫn.

## Nhập không gian tên

Để bắt đầu, hãy nhập các không gian tên cần thiết. Những điều này sẽ đặt nền móng cho kiệt tác mô hình 3D của chúng tôi.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Bước 1: Khởi tạo hồ sơ cơ sở

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Bước 2: Tạo cảnh 3D

```csharp
Scene scene = new Scene();
```

## Bước 3: Tạo nút trái và phải

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Bước 4: Thực hiện đùn tuyến tính trên nút bên trái

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Bước 5: Đặt mặt phẳng đất để tham khảo

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Bước 6: Thực hiện đùn tuyến tính trên nút bên phải

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Bước 7: Đặt mặt phẳng đất để tham chiếu (Nút bên phải)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Bước 8: Lưu cảnh 3D

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Phần kết luận

Chúc mừng! Bạn đã thành thạo thành công nghệ thuật đùn tuyến tính với tính năng định tâm bằng Aspose.3D cho .NET. Hãy thoải mái thử nghiệm các thông số khác nhau và khám phá những khả năng to lớn mà kỹ thuật này mang lại.

## Câu hỏi thường gặp

### Câu hỏi 1: Tôi có thể sử dụng Aspose.3D cho .NET với các ngôn ngữ lập trình khác không?

Trả lời 1: Aspose.3D chủ yếu hỗ trợ các ngôn ngữ .NET như C# và VB.NET.

### Câu hỏi 2: Tôi có thể tìm hỗ trợ cho các truy vấn liên quan đến Aspose.3D ở đâu?

 A2: Tham quan[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để được hỗ trợ và thảo luận tận tình.

### Câu hỏi 3: Có bản dùng thử miễn phí dành cho Aspose.3D cho .NET không?

 Câu trả lời 3: Có, bạn có thể truy cập bản dùng thử miễn phí[đây](https://releases.aspose.com/).

### Câu hỏi 4: Làm cách nào tôi có thể nhận được giấy phép tạm thời cho Aspose.3D cho .NET?

 A4: Bạn có thể có được giấy phép tạm thời[đây](https://purchase.aspose.com/temporary-license/).

### Câu hỏi 5: Tôi có thể mua giấy phép Aspose.3D cho .NET ở đâu?

 A5: Mua giấy phép của bạn[đây](https://purchase.aspose.com/buy).
