from cx_Freeze import setup, Executable

includes = [
    '_pytest.assertion.newinterpret',
    '_pytest.assertion.oldinterpret',
    '_pytest.assertion.reinterpret',
    '_pytest.assertion.rewrite',
    '_pytest.assertion.util',

    '_pytest._argcomplete',
    '_pytest.doctest',
    '_pytest.pdb',
    '_pytest.unittest',
    '_pytest.capture',
    '_pytest.config',
    '_pytest.core',
    '_pytest.genscript',
    '_pytest.helpconfig',
    '_pytest.hookspec',
    '_pytest.junitxml',
    '_pytest.main',
    '_pytest.mark',
    '_pytest.monkeypatch',
    '_pytest.nose',
    '_pytest.pastebin',
    '_pytest.pytester',
    '_pytest.python',
    '_pytest.recwarn',
    '_pytest.resultlog',
    '_pytest.runner',
    '_pytest.skipping',
    '_pytest.standalonetemplate',
    '_pytest.terminal',
    '_pytest.tmpdir',

    'py._builtin',
    'py._path.local',
    'py._io.capture',
    'py._io.saferepr',
    'py._iniconfig',
    'py._io.terminalwriter',
    'py._xmlgen',
    'py._error',
    'py._std',

    # builtin files imported by pytest using py.std implicit mechanism
    'argparse',
    'shlex',
    'warnings',
    'types',
]

setup(
    name="runtests",
    version="0.1",
    description="exemple of how embedding py.test into an executable using cx_freeze",
    executables=[Executable("runtests.py")],
    options={"build_exe": {'includes': includes}},
)

