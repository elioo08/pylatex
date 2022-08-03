# Importando as bibliotecas
import PySimpleGUI as sg 
from pylatex.base_classes import Environment
from pylatex.package import Package
from pylatex import Document, Section
from pylatex.utils import NoEscape
from pylatex import Itemize, Enumerate, Description, \
Command, NoEscape
from pylatex import Table, Tabular, UnsafeCommand
from pylatex.base_classes import CommandBase, Arguments
      
sg.theme('BluePurple') # Tema da interface 
   
    # Interface
layout = [[sg.Text('          Python e Latex'), 
           sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Text('Titulo'), sg.Input(size=(30,1), key='-titulo-')], 
          [sg.Text('Seu nome: '), sg.Input(size=(12,1), key='-nome-')], 
          [sg.Text('Marque uma das alternativas')],
          [sg.Radio('Alternativa 1', "radio1", default=True, key='a1')],
          [sg.Radio('Alternativa 2', "radio1", default=False, key='a2')],
          [sg.Radio('Alternativa 3', "radio1", default=False, key='a3')],
          [sg.Text('Faça sua itemize')],
          [sg.Text('1. '), sg.Input(size=(12,1), key='-i1-')], 
          [sg.Text('2. '), sg.Input(size=(12,1), key='-i2-')],
          [sg.Text('3. '), sg.Input(size=(12,1), key='-i3-')],
           [sg.Text('Faça sua tabela')],
          [sg.Input(size=(12,1), key='-t11-'), sg.Input(size=(12,1), key='-t12-')],
          [sg.Input(size=(12,1), key='-t21-'), sg.Input(size=(12,1), key='-t22-')],
          [sg.Input(size=(12,1), key='-t31-'), sg.Input(size=(12,1), key='-t32-')],
          [sg.Input(size=(12,1), key='-t41-'), sg.Input(size=(12,1), key='-t42-')],
          [sg.Button('Criar TEX'), sg.Button('Sair')]],
          
  
window = sg.Window('Introduction', layout) 
  
while True: 
    event, values = window.read() 
    print(event, values) 
      
    if event in  (None, 'Sair'): 
        break

    name = values['-nome-']  # Pega os valores do input na interface
    
    if event == 'Criar TEX': 
        class AllTT(Environment):
            """A class to wrap LaTeX's alltt environment."""

        class ExampleEnvironment(Environment):
            """
             A class representing a custom LaTeX environment.

            This class represents a custom LaTeX environment named
            ``exampleEnvironment``.
            """

            _latex_name = 'exampleEnvironment'
            packages = [Package('mdframed')]
            packages = [Package('alltt')]
            escape = False
            content_separator = "\n"

        
        # Create a new document
        doc = Document()
        doc.packages.append(Package('mdframed'))

        vtitulo = values['-titulo-']
        # Define a style for our box
        mdf_style_definition = UnsafeCommand('mdfdefinestyle',
                                         arguments=['my_style',
                                                    ('linecolor=#1,'
                                                     'linewidth=#2,'
                                                     'fontsize=#20'
                                                     'leftmargin=1cm,'
                                                     'leftmargin=1cm')])

        # Define the new environment using the style definition above
        new_env = UnsafeCommand('newenvironment', 'exampleEnvironment', options=2,
                            extra_arguments=[
                                mdf_style_definition.dumps() +
                                r'\begin{mdframed}[style=my_style]',
                                r'\end{mdframed}'])
        doc.append(new_env)

        with doc.create(
                ExampleEnvironment(arguments=Arguments('red', 3))) as environment:
            environment.append('This is the actual content')

        with doc.create(Section(f'Nome: {name}')):
            doc.append(NoEscape(
            r"""
            The following is a demonstration of a custom \LaTeX{}
            command with a couple of parameters.
        """))
        # Radios
        if values["a1"] == True: 
                valueradio = "1"    
        elif values["a2"] == True:
                valueradio = "2"  
        elif values["a3"] == True:
                valueradio = "3"  

        with doc.create(Section(f'Alternativa: {valueradio}')):
            doc.append(NoEscape(
            r"""
            
        """))

        
        with doc.create(Section('Itemize')):
            with doc.create(Itemize()) as itemize:
                itemize.add_item(values["-i1-"])
                itemize.add_item(values["-i2-"])
                itemize.add_item(values["-i3-"])

             # Variaveis da Tabela
        ta11 = values['-t11-']  
        ta12 = values['-t12-']
        ta21 = values['-t21-']
        ta22 = values['-t22-']
        ta31 = values['-t31-']
        ta32 = values['-t32-']
        ta41 = values['-t41-']
        ta42 = values['-t42-']
        with doc.create(Section('Tabela')):
            with doc.create(Table(position='h!')) as table:
                with doc.create(Tabular('|c|c|')) as tabular:
                    tabular.add_hline()
                    tabular.add_row((ta11, ta12))
                    tabular.add_hline()
                    tabular.add_hline()
                    tabular.add_row((ta21, ta22))
                    tabular.add_hline()
                    tabular.add_row((ta31, ta32))
                    tabular.add_hline()
                    tabular.add_row((ta41, ta42))
                    tabular.add_hline()
                table.add_caption('My Table Caption')

        # Gerar TEX
        doc.generate_pdf('introduction', clean_tex=False)
        
  
window.close() 