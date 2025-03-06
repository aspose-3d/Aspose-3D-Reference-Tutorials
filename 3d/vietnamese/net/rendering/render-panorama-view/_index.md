---
title: Dễ dàng kết xuất ảnh toàn cảnh 3D với Aspose.3D cho .NET
linktitle: Hiển thị Chế độ xem Toàn cảnh của Cảnh 3D
second_title: API Aspose.3D .NET
description: Tìm hiểu cách tạo chế độ xem toàn cảnh 3D tuyệt đẹp bằng Aspose.3D cho .NET. Hãy làm theo hướng dẫn từng bước của chúng tôi để hiển thị cảnh sống động.
weight: 13
url: /vi/net/rendering/render-panorama-view/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Dễ dàng kết xuất ảnh toàn cảnh 3D với Aspose.3D cho .NET

## Giới thiệu
Tạo cảnh 3D quyến rũ và hiển thị chúng thành chế độ xem toàn cảnh đã trở thành một khía cạnh thiết yếu của các ứng dụng hiện đại. Aspose.3D for .NET cung cấp một giải pháp mạnh mẽ cho các nhà phát triển muốn tích hợp liền mạch khả năng kết xuất 3D vào dự án của họ. Trong hướng dẫn này, chúng ta sẽ khám phá quá trình hiển thị chế độ xem toàn cảnh của cảnh 3D bằng Aspose.3D cho .NET.
## Điều kiện tiên quyết
Trước khi đi sâu vào hướng dẫn, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:
-  Aspose.3D for .NET: Tải xuống và cài đặt thư viện Aspose.3D. Bạn có thể tìm thấy thư viện và tài liệu[đây](https://releases.aspose.com/3d/net/).
- Môi trường phát triển .NET: Đảm bảo bạn đã cài đặt môi trường phát triển .NET đang hoạt động trên máy của mình.
- Cảnh 3D mẫu: Tải xuống tệp cảnh 3D mẫu, ví dụ: "VirtualCity.glb" mà chúng tôi sẽ sử dụng để hiển thị chế độ xem toàn cảnh.
## Nhập không gian tên
Trong dự án .NET của bạn, hãy nhập các vùng tên cần thiết để làm việc với Aspose.3D:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## Bước 1: Tải cảnh 3D
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
Tải cảnh 3D bằng Aspose.3D. Thay thế "VirtualCity.glb" bằng đường dẫn đến tệp cảnh 3D mà bạn mong muốn.
## Bước 2: Thiết lập camera và đèn
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
Thiết lập camera và đèn để chụp cảnh 3D phù hợp.
## Bước 3: Tạo mục tiêu kết xuất và kết xuất
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024 * 3, 1024);
```
Tạo trình kết xuất và xác định mục tiêu kết xuất cho bản đồ khối và hình ảnh toàn cảnh cuối cùng.
## Bước 4: Định cấu hình Viewport và Render
```csharp
rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
renderer.Render(rt);
```
Định cấu hình chế độ xem bằng camera và hiển thị bản đồ khối.
## Bước 5: Áp dụng xử lý hậu kỳ cho chế độ xem toàn cảnh
```csharp
PostProcessing equirectangular = renderer.GetPostProcessing("equirectangular");
equirectangular.Input = rt.Targets[0];
renderer.Execute(equirectangular, final);
```
Áp dụng xử lý hậu kỳ hình chiếu tương đương để tạo ra chế độ xem toàn cảnh.
## Bước 6: Lưu ảnh toàn cảnh được hiển thị
```csharp
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "panorama.png", ImageFormat.Png);
```
Lưu hình ảnh toàn cảnh được hiển thị vào một thư mục đầu ra được chỉ định.
## Phần kết luận
Với Aspose.3D cho .NET, việc hiển thị chế độ xem toàn cảnh của cảnh 3D trở thành một quá trình đơn giản. Nâng cao ứng dụng của bạn bằng cách kết hợp liền mạch các hình ảnh 3D sống động.
## Các câu hỏi thường gặp
### Câu hỏi: Tôi có thể sử dụng cảnh 3D tùy chỉnh của mình để hiển thị ảnh toàn cảnh không?
Có, chỉ cần thay thế đường dẫn tệp cảnh mẫu bằng đường dẫn đến cảnh 3D tùy chỉnh của bạn.
### Câu hỏi: Có các hiệu ứng xử lý hậu kỳ bổ sung không?
Aspose.3D for .NET cung cấp nhiều hiệu ứng xử lý hậu kỳ khác nhau để nâng cao hình ảnh được hiển thị của bạn.
### Câu hỏi: Làm cách nào tôi có thể tối ưu hóa hiệu suất kết xuất?
Điều chỉnh các tham số kết xuất và kích thước mục tiêu dựa trên yêu cầu của ứng dụng của bạn.
### Câu hỏi: Tôi có thể tích hợp hướng dẫn này vào một ứng dụng web không?
Có, bằng cách kết hợp Aspose.3D cho .NET vào dự án web .NET của bạn.
### Câu hỏi: Có diễn đàn cộng đồng nào hỗ trợ Aspose.3D không?
 Vâng, hãy ghé thăm[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để hỗ trợ cộng đồng.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
