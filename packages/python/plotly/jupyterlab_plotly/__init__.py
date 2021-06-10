def _jupyter_labextension_paths():
    return [{"src": "labextension", "dest": "jupyterlab-new_plotly"}]


def _jupyter_nbextension_paths():
    return [
        {
            "section": "notebook",
            "src": "nbextension",
            "dest": "jupyterlab-new_plotly",
            "require": "jupyterlab-new_plotly/extension",
        }
    ]
