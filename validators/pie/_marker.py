import _plotly_utils.basevalidators


class MarkerValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="marker", parent_name="pie", **kwargs):
        super(MarkerValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Marker"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            colors
                Sets the color of each sector. If not
                specified, the default trace color set is used
                to pick the sector colors.
            colorssrc
                Sets the source reference on Chart Studio Cloud
                for  colors .
            line
                :class:`new_plotly.graph_objects.pie.marker.Line`
                instance or dict with compatible properties
""",
            ),
            **kwargs
        )
