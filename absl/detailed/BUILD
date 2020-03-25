py_library(
    name = "a_class",
    srcs = ["a.py"],
    visibility = ["//visibility:public"],
)

py_library(
    name = "b_class",
    srcs = ["b.py"],
    visibility = ["//visibility:public"],
    deps = [":a_class"],
)

py_library(
    name = "c_class",
    srcs = ["c.py"],
    visibility = ["//visibility:public"],
    deps = [":b_class"],
)

py_test(
    name = "a_test",
    srcs = ["tests/a_test.py"],
    visibility = ["//visibility:public"],
    deps = [":a_class"],
)

py_test(
    name = "b_test",
    srcs = ["tests/b_test.py"],
    visibility = ["//visibility:public"],
    deps = [":b_class"],
)

py_test(
    name = "c_test",
    srcs = ["tests/c_test.py"],
    visibility = ["//visibility:public"],
    deps = [":c_class"],
)