import com.aspose.threed.*;
public class TempVerify {
// ExStart:SetupUVOnCube
// UVs
com.aspose.threed.FVector4[] uvs = new com.aspose.threed.FVector4[]
{
    new com.aspose.threed.FVector4(0.0f, 1.0f, 0.0f, 1.0f),
    new com.aspose.threed.FVector4(1.0f, 0.0f, 0.0f, 1.0f),
    new com.aspose.threed.FVector4(0.0f, 0.0f, 0.0f, 1.0f),
    new com.aspose.threed.FVector4(1.0f, 1.0f, 0.0f, 1.0f)
};

// Indices of the uvs per each polygon
int[] uvsId = new int[]
{
    0,1,3,2,2,3,5,4,4,5,7,6,6,7,9,8,1,10,11,3,12,0,2,13
};
// ExEnd:SetupUVOnCube
}
