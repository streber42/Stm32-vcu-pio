from os.path import join, isfile

Import("env")

FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-libopencm3")
patchflag_path = join(FRAMEWORK_DIR, ".patching-done")

# patch file only if we didn't do it before
if not isfile(join(FRAMEWORK_DIR, ".patching-done")):
    patched_file = join("patches", "libopencm3.diff")

    assert  isfile(patched_file)

    env.Execute("python -m patch -d %s %s " % (FRAMEWORK_DIR, patched_file))
    # env.Execute("touch " + patchflag_path)


    def _touch(path):
        with open(path, "w") as fp:
            fp.write("")

    env.Execute(lambda *args, **kwargs: _touch(patchflag_path))