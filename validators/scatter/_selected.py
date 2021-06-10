import _plotly_utils.basevalidators


class SelectedValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="selected", parent_name="scatter", **kwargs):
        super(SelectedValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Selected"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            marker
                :class:`new_plotly.graph_objects.scatter.selected.M
                arker` instance or dict with compatible
                properties
            textfont
                :class:`new_plotly.graph_objects.scatter.selected.T
                extfont` instance or dict with compatible
                properties
""",
            ),
            **kwargs
        )