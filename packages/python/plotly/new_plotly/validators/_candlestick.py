import _plotly_utils.basevalidators


class CandlestickValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="candlestick", parent_name="", **kwargs):
        super(CandlestickValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Candlestick"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            close
                Sets the close values.
            closesrc
                Sets the source reference on Chart Studio Cloud
                for  close .
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on Chart Studio Cloud
                for  customdata .
            decreasing
                :class:`new_plotly.graph_objects.candlestick.Decrea
                sing` instance or dict with compatible
                properties
            high
                Sets the high values.
            highsrc
                Sets the source reference on Chart Studio Cloud
                for  high .
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on Chart Studio Cloud
                for  hoverinfo .
            hoverlabel
                :class:`new_plotly.graph_objects.candlestick.Hoverl
                abel` instance or dict with compatible
                properties
            hovertext
                Same as `text`.
            hovertextsrc
                Sets the source reference on Chart Studio Cloud
                for  hovertext .
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on Chart Studio Cloud
                for  ids .
            increasing
                :class:`new_plotly.graph_objects.candlestick.Increa
                sing` instance or dict with compatible
                properties
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            line
                :class:`new_plotly.graph_objects.candlestick.Line`
                instance or dict with compatible properties
            low
                Sets the low values.
            lowsrc
                Sets the source reference on Chart Studio Cloud
                for  low .
            meta
                Assigns extra meta information associated with
                this trace that can be used in various text
                attributes. Attributes such as trace `name`,
                graph, axis and colorbar `title.text`,
                annotation `text` `rangeselector`,
                `updatemenues` and `sliders` `label` text all
                support `meta`. To access the trace `meta`
                values in an attribute in the same trace,
                simply use `%{meta[i]}` where `i` is the index
                or key of the `meta` item in question. To
                access trace `meta` in layout attributes, use
                `%{data[n[.meta[i]}` where `i` is the index or
                key of the `meta` and `n` is the trace index.
            metasrc
                Sets the source reference on Chart Studio Cloud
                for  meta .
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            open
                Sets the open values.
            opensrc
                Sets the source reference on Chart Studio Cloud
                for  open .
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            stream
                :class:`new_plotly.graph_objects.candlestick.Stream
                ` instance or dict with compatible properties
            text
                Sets hover text elements associated with each
                sample point. If a single string, the same
                string appears over all the data points. If an
                array of string, the items are mapped in order
                to this trace's sample points.
            textsrc
                Sets the source reference on Chart Studio Cloud
                for  text .
            uid
                Assign an id to this trace, Use this to provide
                object constancy between traces during
                animations and transitions.
            uirevision
                Controls persistence of some user-driven
                changes to the trace: `constraintrange` in
                `parcoords` traces, as well as some `editable:
                true` modifications such as `name` and
                `colorbar.title`. Defaults to
                `layout.uirevision`. Note that other user-
                driven trace attribute changes are controlled
                by `layout` attributes: `trace.visible` is
                controlled by `layout.legend.uirevision`,
                `selectedpoints` is controlled by
                `layout.selectionrevision`, and
                `colorbar.(x|y)` (accessible with `config:
                {editable: true}`) is controlled by
                `layout.editrevision`. Trace changes are
                tracked by `uid`, which only falls back on
                trace index if no `uid` is provided. So if your
                app can add/remove traces before the end of the
                `data` array, such that the same trace has a
                different index, you can still preserve user-
                driven changes if you give each trace a `uid`
                that stays with it as it moves.
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            whiskerwidth
                Sets the width of the whiskers relative to the
                box' width. For example, with 1, the whiskers
                are as wide as the box(es).
            x
                Sets the x coordinates. If absent, linear
                coordinate will be generated.
            xaxis
                Sets a reference between this trace's x
                coordinates and a 2D cartesian x axis. If "x"
                (the default value), the x coordinates refer to
                `layout.xaxis`. If "x2", the x coordinates
                refer to `layout.xaxis2`, and so on.
            xcalendar
                Sets the calendar system to use with `x` date
                data.
            xhoverformat
                Sets the hover text formatting rule for `x`
                using d3 formatting mini-languages which are
                very similar to those in Python. See:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                And for dates see:
                https://github.com/d3/d3-time-
                format#locale_format By default the values are
                formatted using `xaxis.hoverformat`.
            xperiod
                Only relevant when the axis `type` is "date".
                Sets the period positioning in milliseconds or
                "M<n>" on the x axis. Special values in the
                form of "M<n>" could be used to declare the
                number of months. In this case `n` must be a
                positive integer.
            xperiod0
                Only relevant when the axis `type` is "date".
                Sets the base for period positioning in
                milliseconds or date string on the x0 axis.
                When `x0period` is round number of weeks, the
                `x0period0` by default would be on a Sunday
                i.e. 2000-01-02, otherwise it would be at
                2000-01-01.
            xperiodalignment
                Only relevant when the axis `type` is "date".
                Sets the alignment of data points on the x
                axis.
            xsrc
                Sets the source reference on Chart Studio Cloud
                for  x .
            yaxis
                Sets a reference between this trace's y
                coordinates and a 2D cartesian y axis. If "y"
                (the default value), the y coordinates refer to
                `layout.yaxis`. If "y2", the y coordinates
                refer to `layout.yaxis2`, and so on.
            yhoverformat
                Sets the hover text formatting rule for `y`
                using d3 formatting mini-languages which are
                very similar to those in Python. See:
                https://github.com/d3/d3-3.x-api-
                reference/blob/master/Formatting.md#d3_format
                And for dates see:
                https://github.com/d3/d3-time-
                format#locale_format By default the values are
                formatted using `yaxis.hoverformat`.
""",
            ),
            **kwargs
        )
