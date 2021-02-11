# Minimal example of KDDockWidgets with Qt6 and Conan.

The *kddockwidgets_conan\conanfile.py* conan package definition for KDDockWidgets has been adjusted to set the `KDDockWidgets_QT6` flag to `True` by default, and also use qt/6.0.1 by default.

It was then created and inserted into the conan cache using the command below:

``` bash
conan create -s build_type=Release -o kddockwidgets:build_tests=True -pr ..\pr_vs2019_release . kdab/stable
```

The above command builds correctly and the generated test executables work with Qt6.
