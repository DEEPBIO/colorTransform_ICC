from PIL import Image, ImageCms
import tifffile
from tifffile import TiffFile

def getColorTransform(wsipath, intent=None):
    try:
        assert intent in (0, 1, 2, 3, None)
        with TiffFile(wsipath) as tif:
            iccs = [page.tags['InterColorProfile'].value for page in tif.pages
                        if 'InterColorProfile' in page.tags]
        if len(iccs) == 0:
            return None
        p_source = ImageCms.ImageCmsProfile(BytesIO(iccs[0]))
        p_target = ImageCms.createProfile('sRGB')
        intent = p_source.profile.rendering_intent if intent is None else intent
        return ImageCms.buildTransform(p_source, p_target, 'RGB', 'RGB', renderingIntent=intent)
    except Exception as e:
        return None
    return None
    


''' 사용예시

_transform = getColorTransform(slide_path)

def _read_patch(slide, left_top: Tuple[int, int], level: int, model_patch_size: Union[int, int], real_patch_size: Union[int, int], _transform) -> np.ndarray:
    patch = slide.read_region(left_top,
                              level,
                              real_patch_size).convert('RGB')

    patch = ImageCms.applyTransform(patch, _transform).convert('RGB') # 이렇게 적용하면 됩니다

    if real_patch_size != (model_patch_size, model_patch_size):
        patch = patch.resize((model_patch_size, model_patch_size))

    patch = np.array(patch)[..., :3]
    patch = patch.astype(np.float32)
    patch = np.divide(patch, 255)
    patch = np.transpose(patch, [2, 0, 1])
    patch = np.ascontiguousarray(patch, dtype=np.float32)
    return patch
    
'''
