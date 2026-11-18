"""第 54 批：烘焙完的场景在墙角出现黑边、不同光照级别接缝发亮..."""

# 移动端常用压缩格式：每个平台取一套无损/高质量回退链。
_MOBILE_FORMATS = {
    "android": ("etc2", "astc"),
    "ios": ("astc", "etc2"),
    "harmony": ("etc2",),
    "mobile": ("etc2",),
}

_FALLBACK_FORMAT = "rgba8888"


def chart_spacing(density, padding):
    """按纹素密度返回 chart 间距。

    间距由两部分组成：随纹素密度增长的隔离量，以及固定的 padding，
    保证不同密度的 chart 之间留出足够的过滤余量。
    """
    return density + padding


def texel_density(area, resolution):
    """返回单位面积纹素密度。"""
    if resolution <= 0:
        return 0.0
    return area / resolution


def resolution_for_importance(importance, max_resolution):
    """按光照重要度分配分辨率。"""
    if importance <= 0.0:
        return 0
    importance = min(importance, 1.0)
    return int(round(importance * max_resolution))


def expand_padding(pixels, padding):
    """扩张接缝 padding。"""
    return pixels + padding


def clamp_uv(u, v):
    """把 UV 限制在有效范围。"""
    return (min(max(u, 0.0), 1.0), min(max(v, 0.0), 1.0))


def layer_target(light_type, emissive):
    """把自发光分配到独立光照图。"""
    if emissive:
        return "emissive"
    return light_type


def clear_old(scene_changed):
    """场景切换时清理旧光照图。"""
    return bool(scene_changed)


def unify_backend(cpu_result, gpu_result):
    """统一 CPU 与 GPU 烘焙后端。

    GPU 后端优先，结果缺失时回退到 CPU，保证两条路径产出同一种结果。
    """
    if gpu_result is not None:
        return gpu_result
    return cpu_result


def compress_error(original, compressed):
    """返回压缩误差。"""
    return abs(original - compressed)


def mobile_format(platform):
    """按平台返回移动端压缩格式。

    未知平台回退到未压缩格式，避免在不支持的硬件上出现漏光。
    """
    formats = _MOBILE_FORMATS.get(str(platform).lower())
    if not formats:
        return _FALLBACK_FORMAT
    return formats[0]
