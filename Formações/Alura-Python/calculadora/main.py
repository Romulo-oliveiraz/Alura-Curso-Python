import PySimpleGUI as sg
def janela1():


    base_num = {'size':(6,2), 'font':('Arial Black', 11), 'button_color':('white', '#000000')}
    base_op = {'size':(6,2), 'font':('Arial Black', 11), 'button_color':('white', '#013445')}


    layout = [         
        [sg.Text('', size=(17, 1), font=('Arial Black', 20), text_color=('white'), background_color='#737373', key='input')],
        [sg.ReadFormButton('(',**base_op), sg.ReadFormButton(')', **base_op), sg.ReadFormButton('C', **base_op), sg.ReadFormButton('<<',**base_op)],
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
list_op2 = ['x', '/', '*']

while True:
    try:
        button, value = form.read()

        if button == sg.WIN_CLOSED:
            break

        #clean the numbers in te screen and in the operation
        if button == 'C':
            equal = ''
            form.find_element('input').Update(equal)

        #erase the last character
        elif button == '<<':
            equal = equal[:-1]
            form.find_element('input').Update(equal)

        #puts what was clicked on the screen and in the operation

        elif str(button) in '0123456789.+-/x()':

            #errors pass
            if equal == '' and button in list_op2:
                pass
            elif equal == '' and button == '.':
                pass
            elif equal == '' and button == ')':
                pass
            else:
                equal += str(button)

            form.find_element('input').Update(equal)

        #ERROR
        if equal != "":
            
            if len(equal) > 1:
                #mutiple operators signals resolution
                if equal[-1] in list_op and equal[-2] in list_op:
                    equal = equal[:-1] 
                    form.find_element('input').Update(equal)

                #error when have a '.' in start of equal
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
                    elif i in ')' and equal.find('(') == -1:
                        equal = equal.replace(')', '')
                        form.find_element('input').Update(equal)
                        print(equal)
                    # elif equal.find('()'):
                    #     equal = equal.replace('()', '0')
                    #     form.find_element('input').Update(equal)
                    # if equal.find(')('):
                    #     equal = equal.replace(')(', '0')
                    #     form.find_element('input').Update(equal)

                #x sintaxe error 
                if 'x' in equal:
                    equal = equal.replace('x', '*')

                if equal.find(')(') != -1:
                    equal = equal.replace(')(', '0')
                    form.find_element('input').Update(equal)

                if equal.find('()') != -1:
                    equal = equal.replace('()', '0')
                    form.find_element('input').Update(equal)

                print('c')
                print(equal)
                #last caracter operator symble error resolution
                if equal[-1] not in list_op:
                    resolução = eval(equal)
                    history = equal+'='+str(resolução)
                    form.find_element('input').Update(resolução)
                    equal = str(resolução)

                    #make a txt file with the history of results
                    with open("history.txt", "a") as history_txt:
                        history_txt.write(str(history))
                        history_txt.write('\n')
                else:
                    equal = equal[:-1] 
                    form.find_element('input').Update(equal)

            except ZeroDivisionError:
                sg.popup('Não é possivel dividir por 0!')
            except SyntaxError:
                sg.popup('Error, Verifique os parenteses!')
            except IndexError:
                if resolução == 0:
                    equal = '0'
                    form.find_element('input').Update(equal)
    except Exception as e:
        print(e)
