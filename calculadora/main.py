
import PySimpleGUI as sg
def janela1():
    sg.theme('Reddit')
    layout = [  
        [sg.Txt(''  * 10)],         
        [sg.Text('', size=(15, 2), font=('Helvetica', 18), text_color='red', key='input')],
        [sg.Txt(''  * 10)],
        [sg.ReadFormButton('%', size=(5, 2)), sg.ReadFormButton('CE', size=(5, 2)), sg.ReadFormButton('C', size=(5, 2)), sg.ReadFormButton('<<', size=(5, 2))],
        [sg.ReadFormButton('7', size=(5,2)), sg.ReadFormButton('8', size=(5,2)), sg.ReadFormButton('9', size=(5,2)), sg.ReadFormButton('/', size=(5,2))],
        [sg.ReadFormButton('4', size=(5,2)), sg.ReadFormButton('5', size=(5,2)), sg.ReadFormButton('6', size=(5,2)), sg.ReadFormButton('x', size=(5,2))],
        [sg.ReadFormButton('1', size=(5,2)), sg.ReadFormButton('2', size=(5,2)), sg.ReadFormButton('3', size=(5,2)), sg.ReadFormButton('-', size=(5,2))],
        [sg.ReadFormButton('.', size=(5,2)), sg.ReadFormButton('0', size=(5,2)), sg.ReadFormButton('=', size=(5,2)), sg.ReadFormButton('+', size=(5,2))],    
    ]
    
    return layout
        # Janela
form = sg.FlexForm('Calculadora', default_element_size=(40, 1))
form.Layout(janela1())

equal = ''
list_op = ['+', '-', 'x', '/']
while True:
    button, value = form.read()
    if button == sg.WIN_CLOSED:
        break
    if button is 'C':
        equal = ''
        form.FindElement('input').Update(equal)
    elif button is '<<':
        equal = equal[:-1]
        form.FindElement('input').Update(equal)
    elif str(button) in '0123456789.+-x/':
        equal += str(button)
        form.FindElement('input').Update(equal)


