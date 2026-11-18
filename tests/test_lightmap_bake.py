import pytest
from render import lightmap_bake as mod

CASES = [
    ("spacing_sum", "m.chart_spacing(2.0, 3.0) == approx(5.0)"),
    ("spacing_zero", "m.chart_spacing(0.0, 3.0) == approx(3.0)"),
    ("density_calc", "m.texel_density(4.0, 2) == approx(2.0)"),
    ("density_zero", "m.texel_density(0.0, 2) == approx(0.0)"),
    ("res_half", "m.resolution_for_importance(0.5, 1024) == 512"),
    ("res_full", "m.resolution_for_importance(1.0, 1024) == 1024"),
    ("padding_grow", "m.expand_padding(2, 4) == 6"),
    ("padding_zero", "m.expand_padding(0, 4) == 4"),
    ("clamp_high", "m.clamp_uv(1.5, 0.5) == (1.0, 0.5)"),
    ("clamp_low", "m.clamp_uv(-0.5, 0.5) == (0.0, 0.5)"),
    ("layer_direct", "m.layer_target('direct', False) == 'direct'"),
    ("layer_emissive", "m.layer_target('direct', True) == 'emissive'"),
    ("clear_true", "m.clear_old(True) is True"),
    ("unify_gpu", "m.unify_backend('cpu', 'gpu') == 'gpu'"),
    ("error_abs", "m.compress_error(1.0, 0.9) == approx(0.1)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
