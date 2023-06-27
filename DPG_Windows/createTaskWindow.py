import os

import dearpygui.dearpygui as dpg

from DPG_Windows.fillTaskWindow import fillTaskWindow


def setFilePath():
    file = dpg.get_value('list_of_files')
    dpg.set_item_user_data('btn_file', file)


def closeAllWindows():
    if dpg.does_item_exist('fillTaskWindow'):
        dpg.delete_item('fillTaskWindow')
    if dpg.does_item_exist('northWestAngle'):
        dpg.delete_item('northWestAngle')
    if dpg.does_item_exist('minCast'):
        dpg.delete_item('minCast')
    if dpg.does_item_exist('FogelApproximation'):
        dpg.delete_item('FogelApproximation')
    if dpg.does_item_exist('optimalSolution'):
        dpg.delete_item('optimalSolution')


def createTaskWindow():
    list_of_files = []
    for file in os.listdir(os.getcwd()):
        if file.endswith('.txt'):
            list_of_files.append(file)
    with dpg.window(label='Transport Task Create', tag='createTaskWindow', width=400, height=200):
        with dpg.group(horizontal=True):
            with dpg.group(horizontal=False):
                with dpg.group(horizontal=True):
                    dpg.add_text('n:')
                    dpg.add_input_int(default_value=1, min_value=1, max_value=100, min_clamped=True, max_clamped=True,
                                      tag='input_n', width=100)
                with dpg.group(horizontal=True):
                    dpg.add_text('m:')
                    dpg.add_input_int(default_value=1, min_value=1, max_value=100, min_clamped=True, max_clamped=True,
                                      tag='input_m', width=100)
                dpg.add_button(label='Create Transport Task', user_data=None, callback=fillTaskWindow)
            with dpg.group(horizontal=False):
                dpg.add_text('Choose file with task:')
                dpg.add_combo(list_of_files, tag='list_of_files', callback=setFilePath)
                dpg.add_button(label='Solve task from file', tag='btn_file', user_data=None, callback=fillTaskWindow)
        dpg.add_button(label='Close all windows', callback=closeAllWindows)
