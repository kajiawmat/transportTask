import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

from DPG_Windows.createTaskWindow import createTaskWindow

if __name__ == '__main__':
    dpg.create_context()
    createTaskWindow()
    dpg.create_viewport(title='Transport Task Solver', width=960, height=1080, x_pos=0, y_pos=0)
    demo.show_demo()
    dpg.show_item_registry()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
