---
title: Tạo cảnh với kết cấu nhúng
linktitle: Tạo cảnh với kết cấu nhúng
second_title: API Aspose.3D .NET
description: Tạo cảnh 3D đầy mê hoặc với họa tiết được nhúng bằng Aspose.3D cho .NET. Hãy làm theo hướng dẫn từng bước của chúng tôi để có kết quả tuyệt vời.
type: docs
weight: 10
url: /vi/net/materials/create-scene-embedded-texture/
---
## Giới thiệu
Chào mừng bạn đến với thế giới đồ họa 3D thú vị với Aspose.3D cho .NET! Trong hướng dẫn toàn diện này, chúng tôi sẽ hướng dẫn bạn quy trình tạo cảnh 3D tuyệt đẹp với các họa tiết được nhúng bằng Aspose.3D, một thư viện mạnh mẽ và linh hoạt dành cho các nhà phát triển .NET.
## Điều kiện tiên quyết
Trước khi đi sâu vào hướng dẫn, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:
- Hiểu biết cơ bản về lập trình C# và .NET.
- Visual Studio được cài đặt trên máy của bạn.
- Thư viện Aspose.3D cho .NET mà bạn có thể tải xuống[đây](https://releases.aspose.com/3d/net/).
- Làm quen với các khái niệm về đồ họa 3D và tạo cảnh.
## Nhập không gian tên
Bắt đầu bằng cách nhập các không gian tên cần thiết vào dự án của bạn. Các không gian tên này sẽ cung cấp cho bạn các công cụ và chức năng cần thiết để thao tác đồ họa 3D.
```csharp
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
```
## Bước 1: Tạo cảnh
Bắt đầu bằng cách tạo cảnh 3D mới bằng Aspose.3D cho .NET. Điều này sẽ đóng vai trò là bức vẽ cho kiệt tác 3D của bạn.
```csharp
// Tạo tệp FBX có kết cấu được nhúng
Scene scene = new Scene();
```
## Bước 2: Tạo một kết cấu nhúng
Bây giờ, hãy thêm một số điểm nhấn trực quan vào cảnh của bạn bằng cách nhúng một họa tiết. Chúng tôi sẽ tạo một kết cấu có nội dung tùy chỉnh và gán cho nó một tên tệp.
```csharp
// Tạo một kết cấu nhúng
Texture tex = new Texture()
{
    Content = CreateTextureContent(),
    //Tên tệp là bắt buộc nếu sử dụng kết cấu nhúng.
    FileName = "test.png"
};
tex.SetProperty("TexProp", "value");
```
## Bước 3: Tạo vật liệu
Tiếp theo, tạo vật liệu cho các đối tượng 3D của bạn, kết hợp các thuộc tính tùy chỉnh và kết cấu đã tạo trước đó.
```csharp
// Tạo một vật liệu với thuộc tính tùy chỉnh
LambertMaterial mat = new LambertMaterial("my-mat");
mat.SetTexture(Material.MapDiffuse, tex);
mat.SetProperty("MyProp", 1.0);
```
## Bước 4: Tạo đối tượng 3D
Bây giờ, hãy làm cho cảnh của bạn trở nên sống động bằng cách thêm đối tượng 3D. Trong ví dụ này, chúng tôi sẽ sử dụng hình xuyến và áp dụng vật liệu bạn vừa tạo.
```csharp
// Tạo một hình xuyến với vật liệu đã tạo trước đó được áp dụng
scene.RootNode.CreateChildNode(new Torus()).Material = mat;
```
## Bước 5: Lưu cảnh
Cuối cùng, lưu kiệt tác của bạn vào một tập tin. Trong ví dụ này, chúng tôi sẽ lưu nó ở định dạng FBX.
```csharp
// Lưu cảnh vào một tập tin
scene.Save(RunExamples.GetOutputFilePath(@"test.fbx"), FileFormat.FBX7500ASCII);
```
Chúc mừng! Bạn đã tạo thành công cảnh 3D có họa tiết được nhúng bằng Aspose.3D cho .NET.
## Mã nguồn nội dung CreateTexture
```csharp
        private static byte[] CreateTextureContent()
        {
            using (var bitmap = new Bitmap(256, 256))
            {
                using (var g = Graphics.FromImage(bitmap))
                {
                    g.Clear(Color.White);
                    LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, 128, 128), Color.Moccasin,
                        Color.ForestGreen, 45);
                    using (var font = new Font(FontFamily.GenericSerif, 40))
                    {
                        g.DrawString("Aspose.3D", font, brush, Point.Empty);
                    }
                }
                using (var ms = new MemoryStream())
                {
                    bitmap.Save(ms, ImageFormat.Png);
                    return ms.ToArray();
                }
            }
        }
```
## Phần kết luận
Trong hướng dẫn này, chúng ta đã khám phá những kiến thức cơ bản về cách tạo cảnh 3D trực quan ấn tượng với các kết cấu được nhúng bằng Aspose.3D cho .NET. Được trang bị kiến thức này, bạn có thể thỏa sức sáng tạo và xây dựng các ứng dụng 3D hấp dẫn.

## Các câu hỏi thường gặp

### Câu hỏi: Tôi có thể sử dụng Aspose.3D cho .NET với các ngôn ngữ lập trình khác không?
Trả lời: Aspose.3D được thiết kế chủ yếu cho .NET, nhưng cũng có những thư viện tương tự dành cho các ngôn ngữ khác.
### Câu hỏi: Làm cách nào tôi có thể áp dụng hoạt ảnh cho cảnh 3D của mình?
Đáp: Aspose.3D cung cấp khả năng hoạt hình; tham khảo tài liệu để được hướng dẫn chi tiết.
### Câu hỏi: Có phiên bản dùng thử cho Aspose.3D cho .NET không?
 A: Có, bạn có thể tải xuống phiên bản dùng thử[đây](https://releases.aspose.com/).
### Hỏi: Tôi có thể tìm thêm nguồn hỗ trợ và nguồn lực ở đâu?
 Đáp: Hãy ghé thăm[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để được cộng đồng hỗ trợ và thảo luận.
### Câu hỏi: Tôi có thể sử dụng Aspose.3D cho các dự án thương mại không?
 Đ: Có, bạn có thể mua giấy phép[đây](https://purchase.aspose.com/buy).