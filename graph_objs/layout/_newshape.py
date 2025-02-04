from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Newshape(_BaseLayoutHierarchyType):

    # class properties
    # --------------------
    _parent_path_str = "layout"
    _path_str = "layout.newshape"
    _valid_props = {
        "drawdirection",
        "fillcolor",
        "fillrule",
        "layer",
        "line",
        "opacity",
    }

    # drawdirection
    # -------------
    @property
    def drawdirection(self):
        """
        When `dragmode` is set to "drawrect", "drawline" or
        "drawcircle" this limits the drag to be horizontal, vertical or
        diagonal. Using "diagonal" there is no limit e.g. in drawing
        lines in any direction. "ortho" limits the draw to be either
        horizontal or vertical. "horizontal" allows horizontal extend.
        "vertical" allows vertical extend.
    
        The 'drawdirection' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['ortho', 'horizontal', 'vertical', 'diagonal']

        Returns
        -------
        Any
        """
        return self["drawdirection"]

    @drawdirection.setter
    def drawdirection(self, val):
        self["drawdirection"] = val

    # fillcolor
    # ---------
    @property
    def fillcolor(self):
        """
        Sets the color filling new shapes' interior. Please note that
        if using a fillcolor with alpha greater than half, drag inside
        the active shape starts moving the shape underneath, otherwise
        a new shape could be started over.
    
        The 'fillcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        return self["fillcolor"]

    @fillcolor.setter
    def fillcolor(self, val):
        self["fillcolor"] = val

    # fillrule
    # --------
    @property
    def fillrule(self):
        """
        Determines the path's interior. For more info please visit
        https://developer.mozilla.org/en-
        US/docs/Web/SVG/Attribute/fill-rule
    
        The 'fillrule' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['evenodd', 'nonzero']

        Returns
        -------
        Any
        """
        return self["fillrule"]

    @fillrule.setter
    def fillrule(self, val):
        self["fillrule"] = val

    # layer
    # -----
    @property
    def layer(self):
        """
        Specifies whether new shapes are drawn below or above traces.
    
        The 'layer' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['below', 'above']

        Returns
        -------
        Any
        """
        return self["layer"]

    @layer.setter
    def layer(self, val):
        self["layer"] = val

    # line
    # ----
    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`new_plotly.graph_objs.layout.newshape.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor
    
            Supported dict properties:
                
                color
                    Sets the line color. By default uses either
                    dark grey or white to increase contrast with
                    background color.
                dash
                    Sets the dash style of lines. Set to a dash
                    type string ("solid", "dot", "dash",
                    "longdash", "dashdot", or "longdashdot") or a
                    dash length list in px (eg "5px,10px,2px,2px").
                width
                    Sets the line width (in px).

        Returns
        -------
        new_plotly.graph_objs.layout.newshape.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of new shapes.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        drawdirection
            When `dragmode` is set to "drawrect", "drawline" or
            "drawcircle" this limits the drag to be horizontal,
            vertical or diagonal. Using "diagonal" there is no
            limit e.g. in drawing lines in any direction. "ortho"
            limits the draw to be either horizontal or vertical.
            "horizontal" allows horizontal extend. "vertical"
            allows vertical extend.
        fillcolor
            Sets the color filling new shapes' interior. Please
            note that if using a fillcolor with alpha greater than
            half, drag inside the active shape starts moving the
            shape underneath, otherwise a new shape could be
            started over.
        fillrule
            Determines the path's interior. For more info please
            visit https://developer.mozilla.org/en-
            US/docs/Web/SVG/Attribute/fill-rule
        layer
            Specifies whether new shapes are drawn below or above
            traces.
        line
            :class:`new_plotly.graph_objects.layout.newshape.Line`
            instance or dict with compatible properties
        opacity
            Sets the opacity of new shapes.
        """

    def __init__(
        self,
        arg=None,
        drawdirection=None,
        fillcolor=None,
        fillrule=None,
        layer=None,
        line=None,
        opacity=None,
        **kwargs
    ):
        """
        Construct a new Newshape object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`new_plotly.graph_objs.layout.Newshape`
        drawdirection
            When `dragmode` is set to "drawrect", "drawline" or
            "drawcircle" this limits the drag to be horizontal,
            vertical or diagonal. Using "diagonal" there is no
            limit e.g. in drawing lines in any direction. "ortho"
            limits the draw to be either horizontal or vertical.
            "horizontal" allows horizontal extend. "vertical"
            allows vertical extend.
        fillcolor
            Sets the color filling new shapes' interior. Please
            note that if using a fillcolor with alpha greater than
            half, drag inside the active shape starts moving the
            shape underneath, otherwise a new shape could be
            started over.
        fillrule
            Determines the path's interior. For more info please
            visit https://developer.mozilla.org/en-
            US/docs/Web/SVG/Attribute/fill-rule
        layer
            Specifies whether new shapes are drawn below or above
            traces.
        line
            :class:`new_plotly.graph_objects.layout.newshape.Line`
            instance or dict with compatible properties
        opacity
            Sets the opacity of new shapes.

        Returns
        -------
        Newshape
        """
        super(Newshape, self).__init__("newshape")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the new_plotly.graph_objs.layout.Newshape 
constructor must be a dict or 
an instance of :class:`new_plotly.graph_objs.layout.Newshape`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("drawdirection", None)
        _v = drawdirection if drawdirection is not None else _v
        if _v is not None:
            self["drawdirection"] = _v
        _v = arg.pop("fillcolor", None)
        _v = fillcolor if fillcolor is not None else _v
        if _v is not None:
            self["fillcolor"] = _v
        _v = arg.pop("fillrule", None)
        _v = fillrule if fillrule is not None else _v
        if _v is not None:
            self["fillrule"] = _v
        _v = arg.pop("layer", None)
        _v = layer if layer is not None else _v
        if _v is not None:
            self["layer"] = _v
        _v = arg.pop("line", None)
        _v = line if line is not None else _v
        if _v is not None:
            self["line"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
