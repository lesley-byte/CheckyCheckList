import PySimpleGUI as sg
sg.ChangeLookAndFeel('GreenTan')
layout = [
    [sg.Text('It is a Checklist, Baby!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Things I cant forget to do:')],
    [sg.Text('Did I remember to do this(check for yes):')],
    [sg.Checkbox('ask one simple question:', size=(30,1))],
    [sg.Checkbox('ask 2nd question:', size=(30,1))],
    [sg.Checkbox('ask 3rd question:', size=(30,1))],
    [sg.Checkbox('ask 4rth question:', size=(30,1))],
    [sg.Checkbox('ask 5th question:', size=(30,1))],
    [sg.Checkbox('ask 6th question:', size=(30,1))],
    [sg.Checkbox('ask 7th question:', size=(30,1))],
    [sg.Checkbox('ask 8th question:', size=(30,1))],
    [sg.Checkbox('ask 9th question:', size=(30,1))],
    [sg.Checkbox('ask 10th simple question:', size=(30,1)),  sg.Checkbox('ask question in another column:')]]
window = sg.Window('Lesley Checklist!!', layout, default_element_size=(40, 1), grab_anywhere=False)
event, values = window.read()
window.close()
