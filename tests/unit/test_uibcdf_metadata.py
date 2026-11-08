"""Packaging checks only; native/scientific compatibility needs its own tests."""

import tomlkit
from pathlib import Path

from packaging.requirements import Requirement


def test_uibcdf_metadata_admits_numpy_25_and_keeps_plotting_optional():
    root = Path(__file__).resolve().parents[2]
    data = tomlkit.loads((root / 'pyproject.toml').read_text())
    required = {
        item.name.lower(): item
        for item in map(Requirement, data['project']['dependencies'])
    }
    assert required['numpy'].specifier.contains('2.5.4')
    assert 'tomlkit' in required
    assert required['tomlkit'].specifier.contains('0.16.0')
    assert 'matplotlib' not in required and 'plotly' not in required
    plotting = {
        Requirement(item).name.lower()
        for item in data['project']['optional-dependencies']['plotting']
    }
    assert plotting == {'matplotlib', 'plotly'}
    builds = {
        Requirement(item).name.lower() for item in data['build-system']['requires']
    }
    assert 'swig' in builds and 'cython' not in builds
