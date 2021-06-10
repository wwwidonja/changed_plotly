import warnings

warnings.filterwarnings(
    "default", r"new_plotly\.graph_objs\.\w+ is deprecated", DeprecationWarning
)


class Data(list):
    """
    new_plotly.graph_objs.Data is deprecated.
Please replace it with a list or tuple of instances of the following types
  - new_plotly.graph_objs.Scatter
  - new_plotly.graph_objs.Bar
  - new_plotly.graph_objs.Area
  - new_plotly.graph_objs.Histogram
  - etc.

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Data is deprecated.
Please replace it with a list or tuple of instances of the following types
  - new_plotly.graph_objs.Scatter
  - new_plotly.graph_objs.Bar
  - new_plotly.graph_objs.Area
  - new_plotly.graph_objs.Histogram
  - etc.

        """
        warnings.warn(
            """new_plotly.graph_objs.Data is deprecated.
Please replace it with a list or tuple of instances of the following types
  - new_plotly.graph_objs.Scatter
  - new_plotly.graph_objs.Bar
  - new_plotly.graph_objs.Area
  - new_plotly.graph_objs.Histogram
  - etc.
""",
            DeprecationWarning,
        )
        super(Data, self).__init__(*args, **kwargs)


class Annotations(list):
    """
    new_plotly.graph_objs.Annotations is deprecated.
Please replace it with a list or tuple of instances of the following types
  - new_plotly.graph_objs.layout.Annotation
  - new_plotly.graph_objs.layout.scene.Annotation

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Annotations is deprecated.
Please replace it with a list or tuple of instances of the following types
  - new_plotly.graph_objs.layout.Annotation
  - new_plotly.graph_objs.layout.scene.Annotation

        """
        warnings.warn(
            """new_plotly.graph_objs.Annotations is deprecated.
Please replace it with a list or tuple of instances of the following types
  - new_plotly.graph_objs.layout.Annotation
  - new_plotly.graph_objs.layout.scene.Annotation
""",
            DeprecationWarning,
        )
        super(Annotations, self).__init__(*args, **kwargs)


class Frames(list):
    """
    new_plotly.graph_objs.Frames is deprecated.
Please replace it with a list or tuple of instances of the following types
  - new_plotly.graph_objs.Frame

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Frames is deprecated.
Please replace it with a list or tuple of instances of the following types
  - new_plotly.graph_objs.Frame

        """
        warnings.warn(
            """new_plotly.graph_objs.Frames is deprecated.
Please replace it with a list or tuple of instances of the following types
  - new_plotly.graph_objs.Frame
""",
            DeprecationWarning,
        )
        super(Frames, self).__init__(*args, **kwargs)


class AngularAxis(dict):
    """
    new_plotly.graph_objs.AngularAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.AngularAxis
  - new_plotly.graph_objs.layout.polar.AngularAxis

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.AngularAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.AngularAxis
  - new_plotly.graph_objs.layout.polar.AngularAxis

        """
        warnings.warn(
            """new_plotly.graph_objs.AngularAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.AngularAxis
  - new_plotly.graph_objs.layout.polar.AngularAxis
""",
            DeprecationWarning,
        )
        super(AngularAxis, self).__init__(*args, **kwargs)


class Annotation(dict):
    """
    new_plotly.graph_objs.Annotation is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Annotation
  - new_plotly.graph_objs.layout.scene.Annotation

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Annotation is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Annotation
  - new_plotly.graph_objs.layout.scene.Annotation

        """
        warnings.warn(
            """new_plotly.graph_objs.Annotation is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Annotation
  - new_plotly.graph_objs.layout.scene.Annotation
""",
            DeprecationWarning,
        )
        super(Annotation, self).__init__(*args, **kwargs)


class ColorBar(dict):
    """
    new_plotly.graph_objs.ColorBar is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.marker.ColorBar
  - new_plotly.graph_objs.surface.ColorBar
  - etc.

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.ColorBar is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.marker.ColorBar
  - new_plotly.graph_objs.surface.ColorBar
  - etc.

        """
        warnings.warn(
            """new_plotly.graph_objs.ColorBar is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.marker.ColorBar
  - new_plotly.graph_objs.surface.ColorBar
  - etc.
""",
            DeprecationWarning,
        )
        super(ColorBar, self).__init__(*args, **kwargs)


class Contours(dict):
    """
    new_plotly.graph_objs.Contours is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.contour.Contours
  - new_plotly.graph_objs.surface.Contours
  - etc.

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Contours is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.contour.Contours
  - new_plotly.graph_objs.surface.Contours
  - etc.

        """
        warnings.warn(
            """new_plotly.graph_objs.Contours is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.contour.Contours
  - new_plotly.graph_objs.surface.Contours
  - etc.
""",
            DeprecationWarning,
        )
        super(Contours, self).__init__(*args, **kwargs)


class ErrorX(dict):
    """
    new_plotly.graph_objs.ErrorX is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.ErrorX
  - new_plotly.graph_objs.histogram.ErrorX
  - etc.

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.ErrorX is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.ErrorX
  - new_plotly.graph_objs.histogram.ErrorX
  - etc.

        """
        warnings.warn(
            """new_plotly.graph_objs.ErrorX is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.ErrorX
  - new_plotly.graph_objs.histogram.ErrorX
  - etc.
""",
            DeprecationWarning,
        )
        super(ErrorX, self).__init__(*args, **kwargs)


class ErrorY(dict):
    """
    new_plotly.graph_objs.ErrorY is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.ErrorY
  - new_plotly.graph_objs.histogram.ErrorY
  - etc.

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.ErrorY is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.ErrorY
  - new_plotly.graph_objs.histogram.ErrorY
  - etc.

        """
        warnings.warn(
            """new_plotly.graph_objs.ErrorY is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.ErrorY
  - new_plotly.graph_objs.histogram.ErrorY
  - etc.
""",
            DeprecationWarning,
        )
        super(ErrorY, self).__init__(*args, **kwargs)


class ErrorZ(dict):
    """
    new_plotly.graph_objs.ErrorZ is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter3d.ErrorZ

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.ErrorZ is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter3d.ErrorZ

        """
        warnings.warn(
            """new_plotly.graph_objs.ErrorZ is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter3d.ErrorZ
""",
            DeprecationWarning,
        )
        super(ErrorZ, self).__init__(*args, **kwargs)


class Font(dict):
    """
    new_plotly.graph_objs.Font is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Font
  - new_plotly.graph_objs.layout.hoverlabel.Font
  - etc.

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Font is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Font
  - new_plotly.graph_objs.layout.hoverlabel.Font
  - etc.

        """
        warnings.warn(
            """new_plotly.graph_objs.Font is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Font
  - new_plotly.graph_objs.layout.hoverlabel.Font
  - etc.
""",
            DeprecationWarning,
        )
        super(Font, self).__init__(*args, **kwargs)


class Legend(dict):
    """
    new_plotly.graph_objs.Legend is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Legend

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Legend is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Legend

        """
        warnings.warn(
            """new_plotly.graph_objs.Legend is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Legend
""",
            DeprecationWarning,
        )
        super(Legend, self).__init__(*args, **kwargs)


class Line(dict):
    """
    new_plotly.graph_objs.Line is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.Line
  - new_plotly.graph_objs.layout.shape.Line
  - etc.

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Line is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.Line
  - new_plotly.graph_objs.layout.shape.Line
  - etc.

        """
        warnings.warn(
            """new_plotly.graph_objs.Line is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.Line
  - new_plotly.graph_objs.layout.shape.Line
  - etc.
""",
            DeprecationWarning,
        )
        super(Line, self).__init__(*args, **kwargs)


class Margin(dict):
    """
    new_plotly.graph_objs.Margin is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Margin

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Margin is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Margin

        """
        warnings.warn(
            """new_plotly.graph_objs.Margin is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Margin
""",
            DeprecationWarning,
        )
        super(Margin, self).__init__(*args, **kwargs)


class Marker(dict):
    """
    new_plotly.graph_objs.Marker is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.Marker
  - new_plotly.graph_objs.histogram.selected.Marker
  - etc.

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Marker is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.Marker
  - new_plotly.graph_objs.histogram.selected.Marker
  - etc.

        """
        warnings.warn(
            """new_plotly.graph_objs.Marker is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.Marker
  - new_plotly.graph_objs.histogram.selected.Marker
  - etc.
""",
            DeprecationWarning,
        )
        super(Marker, self).__init__(*args, **kwargs)


class RadialAxis(dict):
    """
    new_plotly.graph_objs.RadialAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.RadialAxis
  - new_plotly.graph_objs.layout.polar.RadialAxis

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.RadialAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.RadialAxis
  - new_plotly.graph_objs.layout.polar.RadialAxis

        """
        warnings.warn(
            """new_plotly.graph_objs.RadialAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.RadialAxis
  - new_plotly.graph_objs.layout.polar.RadialAxis
""",
            DeprecationWarning,
        )
        super(RadialAxis, self).__init__(*args, **kwargs)


class Scene(dict):
    """
    new_plotly.graph_objs.Scene is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Scene

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Scene is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Scene

        """
        warnings.warn(
            """new_plotly.graph_objs.Scene is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.Scene
""",
            DeprecationWarning,
        )
        super(Scene, self).__init__(*args, **kwargs)


class Stream(dict):
    """
    new_plotly.graph_objs.Stream is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.Stream
  - new_plotly.graph_objs.area.Stream

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Stream is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.Stream
  - new_plotly.graph_objs.area.Stream

        """
        warnings.warn(
            """new_plotly.graph_objs.Stream is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.scatter.Stream
  - new_plotly.graph_objs.area.Stream
""",
            DeprecationWarning,
        )
        super(Stream, self).__init__(*args, **kwargs)


class XAxis(dict):
    """
    new_plotly.graph_objs.XAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.XAxis
  - new_plotly.graph_objs.layout.scene.XAxis

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.XAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.XAxis
  - new_plotly.graph_objs.layout.scene.XAxis

        """
        warnings.warn(
            """new_plotly.graph_objs.XAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.XAxis
  - new_plotly.graph_objs.layout.scene.XAxis
""",
            DeprecationWarning,
        )
        super(XAxis, self).__init__(*args, **kwargs)


class YAxis(dict):
    """
    new_plotly.graph_objs.YAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.YAxis
  - new_plotly.graph_objs.layout.scene.YAxis

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.YAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.YAxis
  - new_plotly.graph_objs.layout.scene.YAxis

        """
        warnings.warn(
            """new_plotly.graph_objs.YAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.YAxis
  - new_plotly.graph_objs.layout.scene.YAxis
""",
            DeprecationWarning,
        )
        super(YAxis, self).__init__(*args, **kwargs)


class ZAxis(dict):
    """
    new_plotly.graph_objs.ZAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.scene.ZAxis

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.ZAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.scene.ZAxis

        """
        warnings.warn(
            """new_plotly.graph_objs.ZAxis is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.layout.scene.ZAxis
""",
            DeprecationWarning,
        )
        super(ZAxis, self).__init__(*args, **kwargs)


class XBins(dict):
    """
    new_plotly.graph_objs.XBins is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.histogram.XBins
  - new_plotly.graph_objs.histogram2d.XBins

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.XBins is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.histogram.XBins
  - new_plotly.graph_objs.histogram2d.XBins

        """
        warnings.warn(
            """new_plotly.graph_objs.XBins is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.histogram.XBins
  - new_plotly.graph_objs.histogram2d.XBins
""",
            DeprecationWarning,
        )
        super(XBins, self).__init__(*args, **kwargs)


class YBins(dict):
    """
    new_plotly.graph_objs.YBins is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.histogram.YBins
  - new_plotly.graph_objs.histogram2d.YBins

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.YBins is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.histogram.YBins
  - new_plotly.graph_objs.histogram2d.YBins

        """
        warnings.warn(
            """new_plotly.graph_objs.YBins is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.histogram.YBins
  - new_plotly.graph_objs.histogram2d.YBins
""",
            DeprecationWarning,
        )
        super(YBins, self).__init__(*args, **kwargs)


class Trace(dict):
    """
    new_plotly.graph_objs.Trace is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.Scatter
  - new_plotly.graph_objs.Bar
  - new_plotly.graph_objs.Area
  - new_plotly.graph_objs.Histogram
  - etc.

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Trace is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.Scatter
  - new_plotly.graph_objs.Bar
  - new_plotly.graph_objs.Area
  - new_plotly.graph_objs.Histogram
  - etc.

        """
        warnings.warn(
            """new_plotly.graph_objs.Trace is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.Scatter
  - new_plotly.graph_objs.Bar
  - new_plotly.graph_objs.Area
  - new_plotly.graph_objs.Histogram
  - etc.
""",
            DeprecationWarning,
        )
        super(Trace, self).__init__(*args, **kwargs)


class Histogram2dcontour(dict):
    """
    new_plotly.graph_objs.Histogram2dcontour is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.Histogram2dContour

    """

    def __init__(self, *args, **kwargs):
        """
        new_plotly.graph_objs.Histogram2dcontour is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.Histogram2dContour

        """
        warnings.warn(
            """new_plotly.graph_objs.Histogram2dcontour is deprecated.
Please replace it with one of the following more specific types
  - new_plotly.graph_objs.Histogram2dContour
""",
            DeprecationWarning,
        )
        super(Histogram2dcontour, self).__init__(*args, **kwargs)
