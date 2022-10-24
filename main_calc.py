from tkinter import *
import locale

def printInput():
    Lb1.delete(0,5)
    try:
        valor_bi = float(input_valor.get(1.0, "end-1c").replace('.', '').replace(',', '.'))
        valor_relatorio = float(input_valor2.get(1.0, "end-1c").replace('.', '').replace(',', '.'))
        valor_dif = ''
        if valor_bi > valor_relatorio:
            valor_dif = valor_bi - valor_relatorio
            porcentagem_dif = f'{((valor_bi - valor_relatorio)/valor_relatorio)*100:.4f}% - (B.I acima)'
        elif valor_bi < valor_relatorio:
            valor_dif = valor_relatorio - valor_bi
            porcentagem_dif = f'-{((valor_relatorio - valor_bi)/valor_bi)*100:.4f}% - (B.I abaixo)'
        else:
            valor_confere = f'Valores conferem!'

        #valor_bi = f'{valor_bi:.2f}'.replace('.', ',')
        #valor_relatorio = f'{valor_relatorio:.2f}'.replace('.', ',')

        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        valor_bi = locale.currency(valor_bi, grouping=True, symbol=None)
        valor_relatorio = locale.currency(valor_relatorio, grouping=True, symbol=None)
        #operaçõs tkinter:
        if valor_dif != '':
            #valor_dif = f'{valor_dif:.2f}'.replace('.', ',')
            valor_dif = locale.currency(valor_dif, grouping=True, symbol=None)
            Lb1.insert(1, f'Valor painel B.I: R$ {valor_bi}')
            Lb1.insert(2, f'Valor do relatório: R$ {valor_relatorio}')
            Lb1.insert(3, f'Valor da diferença: R$ {valor_dif}')
            Lb1.insert(4, f'Porcentagem da diferença: {porcentagem_dif}') 
        else:
            Lb1.insert(1, f'Valor painel B.I: {valor_bi}')
            Lb1.insert(2, f'Valor do relatório: {valor_relatorio}')
            Lb1.insert(3, valor_confere)
    except ValueError:
        Lb1.insert(1, f'Digite Valores validos!!!')
    
def listbox_copy():
    janela.clipboard_clear()
    selected = f'{Lb1.get(0)}\n{Lb1.get(1)}\n{Lb1.get(2)}\n{Lb1.get(3)}\n{Lb1.get(4)}\n'
    selected = selected.strip()
    janela.clipboard_append(selected)
    
janela = Tk() #começa janela
janela.title('Calculadora de divergência') #Titulo do programa
#Tamanho da Janela
largura = 300
altura = 400
#resolução do monitor
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
#posição da janela
posx = int(largura_tela/2 - largura/2)
posy = int(altura_tela/2 - altura/2)
janela.geometry(f'{largura}x{altura}+{posx}+{posy}') #altera tamanho e posição inicial da janela 'larguraxaltura+posição1+posição2
janela.resizable(False, False) #habilita se a altura e largura da janela pode ser redimencionada


#back ground
janela['bg'] = 'DarkSlateBlue' 

#Um texto na janela
texto_cabecalho = Label(janela, 
              text='Calculadora de divergência',
              bg='DarkSlateBlue',
              fg='white',
              font='Times') 
#texto_cabecalho.pack()
texto_cabecalho.place(x = 40, y = 0)
texto_valor1 = Label(janela, 
              text='Valor B.I:          R$',
              bg='DarkSlateBlue',
              fg='white',
              font='Times 12'
              ) 
texto_valor1.place(x = 10, y = 50)
    
input_valor = Text(janela,
                   height = 1,
                   width = 15)
input_valor.place(x = 135, y = 50)

texto_valor2 = Label(janela, 
              text='Valor Relatório: R$',
              bg='DarkSlateBlue',
              fg='white',
              font='Times 12'
              ) 
texto_valor2.place(x = 10, y = 80)
    
input_valor2 = Text(janela,
                   height = 1,
                   width = 15)
input_valor2.place(x = 135, y = 80)

botao = Button(janela, text='Calcular', command=lambda:printInput(), font='Times 10',bd = 8,fg='black',width=25) #passar a função no command sem os '()', assim ela será executada  somente quando clicar no botão
botao.place(x=52, y=120)

Lb1 = Listbox(janela, width=46)
Lb1.place(x=10,y=170)

botao_copy = Button(janela, text='Copiar', command=lambda:listbox_copy(), font='Times 10',bd = 8,fg='black',width=25)
botao_copy.place(x=50,y=340)



janela.mainloop()#mainloop é para que a janela se mantenha aberta, sempre será minha ultima linha de código

