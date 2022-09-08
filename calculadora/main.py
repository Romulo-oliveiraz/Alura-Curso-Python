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


form = sg.FlexForm('Calculadora', default_element_size=(40, 1), background_color='#29000d', auto_size_buttons=False, grab_anywhere=False)
form.Layout(janela1())

equal = ''
list_op = ['+', '-', 'x', '/', '*']

while True:
    button, value = form.read()

    if button == sg.WIN_CLOSED:
        break
    #clean the numbers in te screen and in the operation
    if button == 'C':
        equal = ''
        form.find_element('input').Update(equal)

    elif button == 'CE':
        equal = ''
        form.find_element('input').Update(equal)

    #erase the last character
    elif button == '<<':
        equal = equal[:-1]
        form.find_element('input').Update(equal)

    #puts what was clicked on the screen and in the operation

    elif str(button) in '0123456789.+-/x':
        
        if equal == '' and button in list_op:
            pass
        elif equal == '' and button == '.':
            pass
        else:
            equal += str(button)

        form.find_element('input').Update(equal)

    #ERROR
    if equal != "":

        if len(equal) > 1:    
            if equal[-1] in list_op and equal[-2] in list_op:
                equal = equal[:-1] 
                form.find_element('input').Update(equal)
            elif equal[-1] == '.' and equal[-2] in list_op:
                equal = equal[:-1] 
                form.find_element('input').Update(equal)

    #result
    if button == '=' and equal != '':

        try:
            for i in equal:
                if i in list_op and i in equal[0]:
                    equal = ""
                    form.find_element('input').Update(equal)
            #x sintaxe error 
            if 'x' in equal:
                equal = equal.replace('x', '*')
            #last caracter operator symble error resolution
            if equal[-1] not in list_op:
                resolução = eval(equal)
                form.find_element('input').Update(resolução)
                equal = str(resolução)
            else:
                equal = equal[:-1] 
                form.find_element('input').Update(equal)
        except ZeroDivisionError:
            sg.popup('Não é possivel dividir por 0!')