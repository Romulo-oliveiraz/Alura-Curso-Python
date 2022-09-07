

import PySimpleGUI as sg
def janela1():


    base_num = {'size':(6,2), 'font':('Impact', 14), 'button_color':('white', '#000000')}
    base_op = {'size':(6,2), 'font':('Impact', 14), 'button_color':('white', '#013445')}


    layout = [         
        [sg.Text('', size=(20, 1), font=('Impact', 21), text_color=('white'), background_color='#737373', key='input')],
        [sg.ReadFormButton('%',**base_op), sg.ReadFormButton('CE', **base_op), sg.ReadFormButton('C', **base_op), sg.ReadFormButton('<<',**base_op)],
        [sg.ReadFormButton('7',**base_num), sg.ReadFormButton('8', **base_num), sg.ReadFormButton('9', **base_num), sg.ReadFormButton('/', **base_op)],
        [sg.ReadFormButton('4',**base_num), sg.ReadFormButton('5',**base_num), sg.ReadFormButton('6',**base_num), sg.ReadFormButton('x',**base_op)],
        [sg.ReadFormButton('1',**base_num), sg.ReadFormButton('2',**base_num), sg.ReadFormButton('3',**base_num), sg.ReadFormButton('-',**base_op)],
        [sg.ReadFormButton('.',**base_op), sg.ReadFormButton('0',**base_num), sg.ReadFormButton('=',**base_op), sg.ReadFormButton('+',**base_op)],    
    ]
    
    return layout
        # Janela
form = sg.FlexForm('Calculadora', default_element_size=(40, 1), background_color='#29000d', auto_size_buttons=False, grab_anywhere=False)
form.Layout(janela1())

equal = ''
res = ''
list_op = ['+', '-', 'x', '/', '=']
while True:
    button, value = form.read()
    if button == sg.WIN_CLOSED:
        break
    if button == 'C':
        equal = ''
        res = ''
        form.find_element('input').Update(equal)
        form.find_element('input').Update(res)
    elif button == 'CE':
        equal = ''
        form.find_element('input').Update(equal)
    elif button == '<<':
        equal = equal[:-1]
        form.find_element('input').Update(equal)
    elif str(button) in '0123456789.+-x/':
        equal += str(button)
        form.find_element('input').Update(equal)
    #ERROR
    if equal != "":
        if '-' in equal[0]:
            equal = ""
            form.find_element('input').Update(equal)
            sg.Popup('Não é possível fazer operações com números negativos')
        elif '/' in equal[0]:
            equal = ""
            form.find_element('input').Update(equal)
            sg.Popup('Não é possível fazer operações com números negativos')
        elif '+' in equal[0]:
            equal = ""
            form.find_element('input').Update(equal)
            sg.Popup('Não é possível fazer operações com números negativos')
        elif 'x' in equal[0]:
            equal = ""
            form.find_element('input').Update(equal)
            sg.Popup('Não é possível fazer operações com números negativos')
        elif '.' in equal[0]:
            equal = "0."
            form.find_element('input').Update(equal)
        

