import dearpygui.dearpygui as dpg

dpg.setup_viewport()
dpg.set_viewport_title(title='Custom Title')
dpg.set_viewport_width(500)
dpg.set_viewport_height(200)

with dpg.window() as mainwindow:
    dpg.add_text("Hello, world")
    dpg.add_input_text(label='Viewport Title', hint="yoyo", callback=lambda sender: dpg.set_viewport_title(title=dpg.get_value(sender)))

dpg.set_primary_window(mainwindow, True)

dpg.start_dearpygui()