# UIBCDF compatibility branch

This GPL-3.0-or-later branch starts at upstream pyKVFinder 0.9.6,
commit `20add3537319ffd11e5e660a9181dd986651e928` from
https://github.com/LBC-LNBio/pyKVFinder. It retains the original scientific
implementation, API, citations and licence. It is a third-party compatibility
fork, not an independent detector or a newly admitted MolSysSuite component.

The local version `0.9.6+uibcdf.1` identifies our packaging changes separately
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
