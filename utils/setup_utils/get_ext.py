from pathlib import Path

from setuptools import Extension


def get_ext_modules_n_cmdclass():

    root_path = Path('.')

    try:
        from Cython.Distutils import build_ext
    except ImportError:
        use_cython = False
    else:
        use_cython = True

    cmdclass = {}
    ext_modules = []
    if use_cython:
        # get all .pyx files
        pyx_paths = sorted(root_path.rglob("*.pyx"))
        for pyx_path in pyx_paths:
            path_str = str(pyx_path)
            header = pyx_path.read_text().split('\n')[0]
            if ('cpp' in header) or ('c++' in header):
                language = 'c++'
            else:
                language = 'c'

            extension = Extension(
                path_str[:-4].replace('/', '.'),
                [path_str],
                language=language,
            )

            # Have Cython embed function call signature information in docstrings,
            # so that Sphinx can extract and use those signatures.
            extension.cython_directives = {"embedsignature": True}
            ext_modules.append(extension)
        cmdclass.update({'build_ext': build_ext})

    else:
        # .c files
        c_paths = sorted(root_path.rglob("*.c"))
        for c_path in c_paths:
            path_str = str(c_path)
            ext_modules.append(
                Extension(
                    path_str[:-2].replace('/', '.'),
                    [path_str],
                ),
            )

        # .cpp files
        cpp_paths = sorted(root_path.rglob("*.cpp"))
        for cpp_path in cpp_paths:
            path_str = str(cpp_path)
            ext_modules.append(
                Extension(
                    path_str[:-4].replace('/', '.'),
                    [path_str],
                ),
            )

    return ext_modules, cmdclass
