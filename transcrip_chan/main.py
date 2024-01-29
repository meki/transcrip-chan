import sys
import dearpygui.dearpygui as dpg
from util.fonts import Fonts
from util.theme import Theme

this_script_dir = sys.path[0]


def button_callback():
    print("Clicked!")


if __name__ == '__main__':
    dpg.create_context()

    fonts = Fonts(dpg)
    theme = Theme(dpg)

    with dpg.window(label="Transcrip-chan", width=800, height=600, pos=(0, 0),
                    no_resize=True, no_move=True, no_close=True, no_collapse=True, no_title_bar=True):
        txt = dpg.add_text("トランスクリプちゃん")
        # txt to center
        btn = dpg.add_button(
            label="Button",  callback=button_callback, pos=[200, 120])

        fonts.bind_item_font_h1(txt)

    dpg.create_viewport(title="Transcrip-chan", width=800,
                        height=600, resizable=False)
    dpg.setup_dearpygui()

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
