from firstSolution import northWestAngle, minCast, FogelApproximation
from DPG_Windows.firstSolutionWindow import firstSolutionWindow
import dearpygui.dearpygui as dpg
def cell_a_callback(sender,val,user_data):
    data=dpg.get_item_user_data('transport_task')[2]
    i=user_data
    data[i]=val

def cell_b_callback(sender,val,user_data):
    data=dpg.get_item_user_data('transport_task')[3]
    j=user_data
    data[j]=val

def cell_c_callback(sender,val,user_data):
    data=dpg.get_item_user_data('transport_task')[4]
    i,j=user_data
    data[i][j]=val

def fill_data(file_path):
    if file_path==None:
        n = dpg.get_value('input_n')
        m = dpg.get_value('input_m')
        matr_C = [[0] * m for i in range(n)]
        vect_A = [0] * n
        vect_B = [0] * m
    else:
        with open(file_path,'r') as f:
            n,m=map(int,f.readline().split())
            vect_A=[]
            vect_B=[]
            matr_C=[]
            for i in range(n):
                list_temp=list(map(int,f.readline().split()))
                vect_A.append(list_temp.pop())
                matr_C.append(list_temp.copy())
            vect_B=list(map(int,f.readline().split()))


    return (n,m,vect_A,vect_B,matr_C)
def fillTaskWindow(sender,val,user_data):
    if not dpg.does_item_exist('task_fill'):
        with dpg.window(label='Fill task',tag='fillTaskWindow',on_close=lambda: dpg.delete_item('fillTaskWindow')):
            new_data=fill_data(user_data)
            n, m, vect_A, vect_B, matr_C=new_data
            with dpg.table(tag='transport_task',header_row=True,user_data=new_data,width=m*150+150,borders_innerH=True,borders_innerV=True):
                dpg.add_table_column(label='')
                for j in range(m):
                    dpg.add_table_column(label=f'B{j}')
                dpg.add_table_column(label='Senders')
                for i in range(n):
                    with dpg.table_row():
                        dpg.add_text(f'A{i}')
                        for j in range(m):
                            dpg.add_input_int(default_value=matr_C[i][j],max_value=10000,min_value=0,min_clamped=True,max_clamped=True,user_data=(i,j),callback=cell_c_callback)
                        dpg.add_input_int(default_value=vect_A[i],max_value=10000,min_value=0,min_clamped=True,max_clamped=True,user_data=i,callback=cell_a_callback)
                with dpg.table_row():
                    dpg.add_text('Receivers')
                    for j in range(m):
                        dpg.add_input_int(default_value=vect_B[j],max_value=10000,min_value=0,min_clamped=True,max_clamped=True,user_data=j,callback=cell_b_callback)
            with dpg.group(horizontal=False):
                dpg.add_button(
                    label='northWestAngle',
                    user_data=('northWestAngle',northWestAngle,dpg.get_item_user_data('transport_task')),
                    callback=firstSolutionWindow
                )
                dpg.add_button(
                    label='minCast',
                    user_data=('minCast',minCast,dpg.get_item_user_data('transport_task')),
                    callback=firstSolutionWindow
                )
                dpg.add_button(
                    label='FogelApproximation',
                    user_data=('FogelApproximation', FogelApproximation, dpg.get_item_user_data('transport_task')),
                    callback=firstSolutionWindow
                )