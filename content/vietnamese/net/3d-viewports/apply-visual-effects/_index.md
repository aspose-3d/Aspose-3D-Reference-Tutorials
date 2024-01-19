---
title: Áp dụng hiệu ứng hình ảnh trong chế độ xem 3D
linktitle: Áp dụng hiệu ứng hình ảnh trong chế độ xem 3D
second_title: API Aspose.3D .NET
description: Khám phá thế giới trực quan 3D với Aspose.3D cho .NET. Tìm hiểu cách áp dụng các hiệu ứng hình ảnh hấp dẫn cho cảnh của bạn bằng cách sử dụng hướng dẫn từng bước. Nâng cao dự án của bạn với các hiệu ứng pixel, thang độ xám, phát hiện cạnh và làm mờ.
type: docs
weight: 10
url: /vi/net/3d-viewports/apply-visual-effects/
---
## Giới thiệu

Nâng cao sức hấp dẫn trực quan của cảnh 3D là một khía cạnh quan trọng trong việc tạo ra trải nghiệm sống động. Aspose.3D for .NET cung cấp một bộ công cụ mạnh mẽ để áp dụng hiệu ứng hình ảnh cho chế độ xem 3D. Trong hướng dẫn này, chúng ta sẽ tìm hiểu quy trình áp dụng các hiệu ứng khác nhau cho cảnh 3D, bao gồm tạo pixel, thang độ xám, phát hiện cạnh và làm mờ.

## Điều kiện tiên quyết

Trước khi đi sâu vào hướng dẫn, hãy đảm bảo bạn có những điều sau:

- Kiến thức làm việc về phát triển C# và .NET.
- Đã cài đặt thư viện Aspose.3D cho .NET. Bạn có thể tải nó xuống từ[đây](https://releases.aspose.com/3d/net/).
- Tệp cảnh 3D (ví dụ: "scene.obj") để thử nghiệm.

## Nhập không gian tên

Để bắt đầu, hãy nhập các không gian tên cần thiết cho Aspose.3D và các phần phụ thuộc khác. Thêm các dòng sau vào mã của bạn:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## Bước 1: Tải cảnh 3D hiện có

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 Tải cảnh 3D của bạn bằng cách sử dụng`Scene` lớp học.

## Bước 2: Tạo máy ảnh

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

Tạo một phiên bản camera và đặt vị trí cũng như mục tiêu của nó.

## Bước 3: Thêm ánh sáng vào cảnh

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

Giới thiệu ánh sáng để nâng cao hiệu ứng hình ảnh.

## Bước 4: Tạo Trình kết xuất và Mục tiêu kết xuất

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // Định cấu hình cài đặt trình kết xuất
    renderer.EnableShadows = false;

    // Tạo mục tiêu kết xuất
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // Định cấu hình chế độ xem
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // Kết xuất cảnh thành kết cấu
        renderer.Render(rt);

        // Lưu kết cấu được hiển thị vào một tệp
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // Tiếp tục với các hiệu ứng xử lý hậu kỳ...
    }
}
```

Tạo trình kết xuất và mục tiêu kết xuất để chụp cảnh.

## Bước 5: Áp dụng hiệu ứng xử lý hậu kỳ

### Bước 5.1 Hiệu ứng pixel

```csharp
//Tạo hiệu ứng pixel
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

Áp dụng hiệu ứng pixel và lưu kết quả.

### Bước 5.2 Hiệu ứng thang độ xám

```csharp
// Tạo hiệu ứng thang độ xám
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

Áp dụng hiệu ứng thang độ xám và lưu kết quả.

### Bước 5.3 Kết hợp các hiệu ứng

```csharp
// Kết hợp các hiệu ứng thang độ xám và pixel
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

Kết hợp nhiều hiệu ứng để có kết quả độc đáo.

### Bước 5.4 Hiệu ứng phát hiện cạnh

```csharp
// Tạo hiệu ứng phát hiện cạnh
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

Áp dụng hiệu ứng phát hiện cạnh và lưu kết quả.

### Bước 5.5 Hiệu ứng làm mờ

```csharp
// Tạo hiệu ứng mờ
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

Áp dụng hiệu ứng làm mờ và lưu kết quả.

## Phần kết luận

Thử nghiệm các hiệu ứng hình ảnh trong khung nhìn 3D sẽ tăng thêm chiều sâu và tính sáng tạo cho cảnh của bạn. Aspose.3D for .NET đơn giản hóa quy trình này, cung cấp một loạt hiệu ứng xử lý hậu kỳ để nâng cao dự án của bạn.

## Câu hỏi thường gặp

### Q1: Tôi có thể áp dụng nhiều hiệu ứng cùng lúc không?

Câu trả lời 1: Có, bạn có thể kết hợp các hiệu ứng xử lý hậu kỳ khác nhau để có kết quả độc đáo và phức tạp.

### Câu hỏi 2: Làm cách nào để điều chỉnh cường độ hiệu ứng hình ảnh?

Câu trả lời 2: Mỗi hiệu ứng có thể có các thông số mà bạn có thể điều chỉnh để kiểm soát cường độ của nó. Tham khảo tài liệu để biết chi tiết cụ thể.

### Câu 3: Aspose.3D có phù hợp để phát triển trò chơi không?

Câu trả lời 3: Mặc dù Aspose.3D được thiết kế chủ yếu để tạo mô hình và kết xuất 3D, nhưng nó có thể được sử dụng trong một số khía cạnh nhất định của quá trình phát triển trò chơi.

### Câu hỏi 4: Có các hiệu ứng xử lý hậu kỳ bổ sung không?

Câu trả lời 4: Aspose.3D cung cấp nhiều hiệu ứng xử lý hậu kỳ tích hợp sẵn và bạn có thể tạo các hiệu ứng tùy chỉnh bằng thư viện.

### Câu hỏi 5: Tôi có thể sử dụng Aspose.3D cho các dự án thương mại không?

 Câu trả lời 5: Có, bạn có thể sử dụng Aspose.3D cho mục đích thương mại. Tham khảo đến[trang mua hàng](https://purchase.aspose.com/buy) để biết chi tiết cấp phép.