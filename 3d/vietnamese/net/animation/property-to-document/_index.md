---
title: Thuộc tính hoạt hình cho tài liệu trong cảnh 3D
linktitle: Thuộc tính hoạt hình cho tài liệu trong cảnh 3D
second_title: API Aspose.3D .NET
description: Tìm hiểu cách tạo hiệu ứng động cho các thuộc tính 3D bằng Aspose.3D cho .NET. Hướng dẫn từng bước để tạo cảnh động.
weight: 10
url: /vi/net/animation/property-to-document/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Thuộc tính hoạt hình cho tài liệu trong cảnh 3D

## Giới thiệu

Nếu bạn đang đi sâu vào lĩnh vực tạo cảnh và hoạt hình 3D trong .NET, Aspose.3D là bộ công cụ bạn nên sử dụng. Trong hướng dẫn từng bước này, chúng ta sẽ khám phá quy trình tạo hoạt ảnh cho các thuộc tính trong cảnh 3D bằng Aspose.3D cho .NET. Cuối cùng, bạn sẽ được trang bị kiến thức để thổi sức sống vào các dự án 3D của mình.

## Điều kiện tiên quyết

Trước khi chúng ta bắt đầu cuộc hành trình thú vị này, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:

-  Aspose.3D for .NET: Đảm bảo bạn đã cài đặt thư viện. Bạn có thể tải nó xuống từ[Trang web Aspose.3D](https://releases.aspose.com/3d/net/).

- Kiến thức về C#: Làm quen với ngôn ngữ lập trình C# là điều cần thiết để hiểu và triển khai các ví dụ.

- Môi trường phát triển tích hợp (IDE): Sử dụng IDE ưa thích của bạn, chẳng hạn như Visual Studio, để viết mã cùng với các ví dụ.

- Các khái niệm cảnh 3D cơ bản: Việc nắm bắt các khái niệm cảnh 3D cơ bản sẽ giúp quá trình học tập của bạn suôn sẻ hơn.

## Nhập không gian tên

Trong mã C# của bạn, hãy đảm bảo bạn nhập các vùng tên cần thiết cho Aspose.3D. Đây là một ví dụ:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## Bước 1: Khởi tạo đối tượng cảnh

```csharp
Scene scene = new Scene();
```

## Bước 2: Tạo lưới bằng Polygon Builder

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Bước 3: Tạo nút khối

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## Bước 4: Tìm thuộc tính dịch

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## Bước 5: Tạo điểm liên kết

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## Bước 6: Liên kết đường cong hoạt hình trên thành phần X

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## Bước 7: Liên kết đường cong hoạt hình trên thành phần Z

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## Bước 8: Lưu cảnh 3D

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## Bước 9: Hiển thị thông báo thành công

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## Phần kết luận

Chúc mừng! Bạn vừa nắm vững nghệ thuật tạo hoạt ảnh cho các thuộc tính trong cảnh 3D bằng cách sử dụng Aspose.3D cho .NET. Bây giờ, hãy để khả năng sáng tạo của bạn tuôn trào khi bạn truyền sức sống vào các tác phẩm 3D của mình.

## Các câu hỏi thường gặp

### Câu hỏi 1: Tôi có thể tìm tài liệu Aspose.3D ở đâu?

 A1: Tài liệu có sẵn[đây](https://reference.aspose.com/3d/net/).

### Câu hỏi 2: Làm cách nào để tải xuống Aspose.3D cho .NET?

 A2: Bạn có thể tải xuống từ[trang phát hành](https://releases.aspose.com/3d/net/).

### Câu 3: Có bản dùng thử miễn phí không?

 A3: Có, bạn có thể dùng thử miễn phí[đây](https://releases.aspose.com/).

### Câu hỏi 4: Tôi có thể nhận hỗ trợ cho Aspose.3D ở đâu?

 A4: Tham quan[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để hỗ trợ.

### Câu hỏi 5: Tôi có thể xin giấy phép tạm thời không?

 A5: Có, bạn có thể nhận được giấy phép tạm thời[đây](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
