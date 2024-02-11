import dearpygui.dearpygui


def _code(colorcode: str) -> tuple:
    """Converts a hex color code to an RGB tuple.
    Args:
        colorcode (str): A hex color code. (e.g. "#FF0000", "#F00")
        Returns: An RGB tuple. (e.g. (255, 0, 0))"""
    colorcode = colorcode.replace("#", "")
    if len(colorcode) == 3:
        colorcode = colorcode[0] * 2 + colorcode[1] * 2 + colorcode[2] * 2
    return tuple(int(colorcode[i:i + 2], 16) for i in (0, 2, 4))


class Theme:
    def __init__(self, dpg: dearpygui.dearpygui):
        self.dpg: dearpygui.dearpygui = dpg
        with dpg.theme() as global_theme:

            with dpg.theme_component(dpg.mvAll):
                # https://dearpygui.readthedocs.io/en/latest/documentation/themes.html
                dpg.add_theme_style(
                    dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Text,
                                    _code("#eee"), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg,
                                    _code("#111"), category=dpg.mvThemeCat_Core)
                # mvThemeCol_Button
                dpg.add_theme_color(dpg.mvThemeCol_Button,
                                    _code("#43766C"), category=dpg.mvThemeCat_Core)

        dpg.bind_theme(global_theme)

    def show_theme_editor(self):
        self.dpg.show_style_editor()
