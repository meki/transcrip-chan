import sys
import dearpygui.dearpygui


class Fonts:
    def __init__(self, dpg: dearpygui.dearpygui):
        self.dpg: dearpygui.dearpygui = dpg
        self.fonts_dir = f"{sys.path[0]}/../assets/fonts/"
        self.regular_font_path = self.fonts_dir + "NotoSansJP-Regular.ttf"
        self.bold_font_path = self.fonts_dir + "NotoSansJP-Bold.ttf"

        with dpg.font_registry():
            with dpg.font(self.regular_font_path, 40) as self.default_font:
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)
                dpg.add_font_range(0x3100, 0x3ff0)

            dpg.bind_font(self.default_font)

            with dpg.font(self.bold_font_path, 50) as self.h1_font:
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)
                dpg.add_font_range(0x3100, 0x3ff0)

    def show_font_manager(self):
        self.dpg.show_font_manager()

    def bind_item_font_h1(self, item):
        self.dpg.bind_item_font(item, self.h1_font)
