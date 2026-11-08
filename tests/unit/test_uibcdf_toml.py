"""Exercise the public TOML APIs used by this compatibility branch."""

import pyKVFinder
import tomlkit


def test_characterization_toml_round_trip(tmp_path):
    path = tmp_path / 'results.toml'
    pyKVFinder.write_results(
        str(path),
        input='input.pdb',
        ligand=None,
        output='cavity.pdb',
        volume={'KAA': 8.125},
        area={'KAA': 12.5},
        residues={'KAA': [['10', 'A', 'GLY']]},
        max_depth={'KAA': 1.5},
        avg_depth={'KAA': 0.75},
        step=0.5,
    )
    with path.open() as handle:
        actual = tomlkit.load(handle)
    # The fork retains upstream's Python 3.10 range. Use the independent stdlib
    # reader where available without adding a runtime backport for this test.
    try:
        import tomllib
    except ModuleNotFoundError:
        tomllib = None
    if tomllib is not None:
        assert actual == tomllib.loads(path.read_text())
    assert actual['RESULTS']['VOLUME'] == {'KAA': 8.125}
    assert actual['RESULTS']['AREA'] == {'KAA': 12.5}
    assert actual['RESULTS']['RESIDUES'] == {'KAA': [['10', 'A', 'GLY']]}
    assert actual['PARAMETERS']['STEP'] == 0.5
