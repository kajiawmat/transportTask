from time import perf_counter

import dearpygui.dearpygui as dpg

from optimalSolution import optimalSolution


def optimalSolutionWindow(sender, val, user_data):
    start = perf_counter()
    new_data = optimalSolution(user_data)
    stop = perf_counter()
    n, m, vect_A, vect_B, matr_C, matr_X, txt, iter = new_data
    with dpg.window(label='Optimal Solution', tag='optimalSolution',
                    on_close=lambda: dpg.delete_item('optimalSolution')):
        with dpg.group(horizontal=False):
            dpg.add_text('Iterations: ' + str(iter))
            dpg.add_text('Time collapsed: ' + str(stop - start))
            dpg.add_text(txt)
            with dpg.table(user_data=new_data[:-1], width=m * 50 + 100, borders_innerH=True, borders_innerV=True):
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
