from copy import deepcopy
from time import perf_counter
from DPG_Windows.optimalSolutionWindow import optimalSolutionWindow
from transportTask import transportTask
import dearpygui.dearpygui as dpg

def firstSolutionWindow(sender,val,user_data):
    name,func,task=user_data
    start = perf_counter()
    new_data=transportTask(func,task)
    stop = perf_counter()
    n, m, vect_A, vect_B, matr_C, matr_X, txt = new_data
    with dpg.window(label=name,tag=name,on_close=lambda: dpg.delete_item(name)):
        with dpg.group(horizontal=False):
            dpg.add_text('Time collapsed: '+str(stop - start))
            dpg.add_text(txt)
            with dpg.table(user_data=new_data[:-1], width=m*50+100,borders_innerH=True,borders_innerV=True):
                dpg.add_table_column(label='')
                for j in range(m):
                    dpg.add_table_column(label=f'B{j}')
                dpg.add_table_column(label='Senders')
                for i in range(n):
                    with dpg.table_row():
                        dpg.add_text(f'A{i}')
                        for j in range(m):
                            with dpg.group(horizontal=False):
                                dpg.add_text(str(matr_C[i][j]), color=(255, 255, 255, 255))
                                dpg.add_text(str(matr_X[i][j]) if matr_X[i][j] != -1 else '',
                                             color=(255, 160, 122, 255))
                        dpg.add_text(str(vect_A[i]))
                with dpg.table_row():
                    dpg.add_text('Receivers')
                    for j in range(m):
                        dpg.add_text(str(vect_B[j]))
            dpg.add_button(label='Create Optimal Solution',user_data=new_data[:-1],callback=optimalSolutionWindow)



