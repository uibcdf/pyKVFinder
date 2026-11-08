# UIBCDF compatibility branch

This GPL-3.0-or-later branch starts at upstream pyKVFinder 0.9.6,
commit `20add3537319ffd11e5e660a9181dd986651e928` from
https://github.com/LBC-LNBio/pyKVFinder. It retains the original scientific
implementation, API, citations and licence. It is a third-party compatibility
fork, not an independent detector or a newly admitted MolSysSuite component.

The local version `0.9.6+uibcdf.2` identifies our packaging changes separately
from the original PyPI distribution. Do not describe this branch as upstream
0.9.6 when reporting a comparison; record the full source commit, local version,
compiled-extension checksum, NumPy/compiler versions and actual execution route.

## Changes

- Admit NumPy 2.5 in the dependency range. Compatibility requires the recorded
  native-build, upstream scientific-test and direct-original-output evidence;
  widening metadata alone is not that evidence.
- Keep NumPy and tomlkit as runtime requirements. Matplotlib and Plotly belong
  to the `plotting` extra; upstream already imports them inside plotting calls.
  Use `python -m pip install '.[plotting]'` when requesting those functions.
- Remove unused Cython from build requirements. The original extension is
  generated with SWIG and compiled from C; setuptools, wheel, NumPy and SWIG
  remain build requirements. No scientific kernel or compiler optimization
  setting changes are made by this branch.
- Keep `tomlkit>=0.14.0` without an upper cap. Only the public load/dump API
  is used. The metadata guard admits 0.16 as a future version; this is not a
  runtime compatibility claim for an unreleased version. The installed and
  latest released version observed on 2026-11-07 is 0.15.2.

## Development and evidence

Build against the intended NumPy and compiler in a controlled Python 3.14
environment, with one build worker initially. Preserve the upstream main checkout
for consultation. TopoMT can select this built source explicitly with
`upstream_root` and can select an isolated worker interpreter with `python_cmd`;
the normal original-provider route is not silently replaced by this fork.

Run the upstream tests appropriate to detection, spatial characterization,
constitutional membership and exports, then compare a small direct workflow
with the TopoMT adapter and engine-independent recovery. Report the executed
selection, resource limits and any deferred tests. No full platform/interpreter
or upstream NumPy-range qualification is implied by a local source pilot.

Changes suitable for upstream should be proposed separately under its normal
contribution rules. Keep the compatibility patch small and review it when
upstream dependency policy changes.

## Initial source checkpoint — 2026-11-07

The packaging-only test `tests/unit/test_uibcdf_metadata.py` passes on the
TopoMT Python 3.14.10 workspace. Native compilation and upstream scientific
tests remain pending installation of SWIG and tomlkit. No runtime compatibility
or scientific equivalence is claimed by this initial branch. Consumer tracking:
https://github.com/uibcdf/topomt/issues/136.

After the maintainer installed SWIG 4.5.1 and tomlkit 0.15.2, the first native
build succeeded against NumPy 2.5.4 on Python 3.14.10. The initial 23 upstream
grid/TOML/radius controls passed. Broader native characterization and original
workflow checks are recorded in the continuation checkpoint before acceptance.

The two upstream unit modules plus the metadata/TOML controls passed all 266
tests with NumPy 2.5.4 and tomlkit 0.15.2, using one CPU, one OpenMP thread,
a 4 GiB address-space cap and 120 CPU seconds. Maximum observed RSS was about
161 MiB. This covers detection, grids, spatial/depth/constitutional/hydropathy
characterization and exports; it is not the full interpreter/platform matrix.
An original-workflow TopoMT source pilot produced 12 cavities on the retained
1AKD input with 1 Å grid spacing and recovered the saved output without an
engine rerun. Version 0.9.6+uibcdf.2 changes only the dependency/version/test
metadata relative to the first compiled compatibility source; scientific files
and compiler optimization flags remain unchanged.
