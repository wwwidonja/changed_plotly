import _plotly_utils.basevalidators


class UnselectedValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="unselected", parent_name="scatterpolar", **kwargs):
        super(UnselectedValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Unselected"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            marker
                :class:`new_plotly.graph_objects.scatterpolar.unsel
                ected.Marker` instance or dict with compatible
                properties
            textfont
                :class:`new_plotly.graph_objects.scatterpolar.unsel
                ected.Textfont` instance or dict with
                compatible properties
""",
            ),
            **kwargs
        )
