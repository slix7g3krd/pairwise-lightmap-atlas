"""第 54 批：烘焙完的场景在墙角出现黑边、不同光照级别接缝发亮..."""

def chart_spacing(density, padding):
    """按纹素密度返回 chart 间距。"""
    raise NotImplementedError("TODO: chart_spacing")

def texel_density(area, resolution):
    """返回单位面积纹素密度。"""
    raise NotImplementedError("TODO: texel_density")

def resolution_for_importance(importance, max_resolution):
    """按光照重要度分配分辨率。"""
    raise NotImplementedError("TODO: resolution_for_importance")

def expand_padding(pixels, padding):
    """扩张接缝 padding。"""
    raise NotImplementedError("TODO: expand_padding")

def clamp_uv(u, v):
    """把 UV 限制在有效范围。"""
    raise NotImplementedError("TODO: clamp_uv")

def layer_target(light_type, emissive):
    """把自发光分配到独立光照图。"""
    raise NotImplementedError("TODO: layer_target")

def clear_old(scene_changed):
    """场景切换时清理旧光照图。"""
    raise NotImplementedError("TODO: clear_old")

def unify_backend(cpu_result, gpu_result):
    """统一 CPU 与 GPU 烘焙后端。"""
    raise NotImplementedError("TODO: unify_backend")

def compress_error(original, compressed):
    """返回压缩误差。"""
    raise NotImplementedError("TODO: compress_error")

def mobile_format(platform):
    """按平台返回移动端压缩格式。"""
    raise NotImplementedError("TODO: mobile_format")
