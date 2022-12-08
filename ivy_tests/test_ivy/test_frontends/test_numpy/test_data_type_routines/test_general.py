# global
from hypothesis import strategies as st, settings

# local
import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers.testing_helpers import handle_frontend_test


# can_cast
@handle_frontend_test(
    fn_tree="numpy.can_cast",
    from_=helpers.get_dtypes("valid", full=False),
    to=helpers.get_dtypes("valid", full=False),
    casting=st.sampled_from(["no", "equiv", "safe", "same_kind", "unsafe"]),
)
@settings(max_examples=200)
def test_numpy_can_cast(
    *,
    from_,
    to,
    casting,
    as_variable,
    native_array,
    on_device,
    fn_tree,
    frontend,
):
    helpers.test_frontend_function(
        input_dtypes=[],
        as_variable_flags=as_variable,
        with_out=False,
        num_positional_args=3,
        native_array_flags=native_array,
        frontend=frontend,
        fn_tree=fn_tree,
        on_device=on_device,
        from_=from_[0],
        to=to[0],
        casting=casting,
    )
