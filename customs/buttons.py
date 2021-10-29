#! /usr/bin/env python3

from discord_components import Button, ButtonStyle

Buttons = [
    [
        Button(style=ButtonStyle.grey, label='1'),
        Button(style=ButtonStyle.grey, label='2'),
        Button(style=ButtonStyle.grey, label='3'),
        Button(style=ButtonStyle.blue, label='x'),
        Button(style=ButtonStyle.red, label='Quit')
    ],
    [
        Button(style=ButtonStyle.grey, label='4'),
        Button(style=ButtonStyle.grey, label='5'),
        Button(style=ButtonStyle.grey, label='6'),
        Button(style=ButtonStyle.blue, label='÷'),
        Button(style=ButtonStyle.red, label='⟵')
    ],
    [
        Button(style=ButtonStyle.grey, label='7'),
        Button(style=ButtonStyle.grey, label='8'),
        Button(style=ButtonStyle.grey, label='9'),
        Button(style=ButtonStyle.blue, label='+'),
        Button(style=ButtonStyle.red, label='Clear')
    ],
    [
        Button(style=ButtonStyle.grey, label='00'),
        Button(style=ButtonStyle.grey, label='0'),
        Button(style=ButtonStyle.blue, label='.'),
        Button(style=ButtonStyle.blue, label='-'),
        Button(style=ButtonStyle.red, label='Answ')
    ],
]

KillButtons = [
    [
        Button(style=ButtonStyle.grey, label='1', disabled=True),
        Button(style=ButtonStyle.grey, label='2', disabled=True),
        Button(style=ButtonStyle.grey, label='3', disabled=True),
        Button(style=ButtonStyle.blue, label='X', disabled=True),
        Button(style=ButtonStyle.red, label='Quit', disabled=True)
    ],
    [
        Button(style=ButtonStyle.grey, label='4', disabled=True),
        Button(style=ButtonStyle.grey, label='5', disabled=True),
        Button(style=ButtonStyle.grey, label='6', disabled=True),
        Button(style=ButtonStyle.blue, label='÷', disabled=True),
        Button(style=ButtonStyle.red, label='⟵', disabled=True)
    ],
    [
        Button(style=ButtonStyle.grey, label='7', disabled=True),
        Button(style=ButtonStyle.grey, label='8', disabled=True),
        Button(style=ButtonStyle.grey, label='9', disabled=True),
        Button(style=ButtonStyle.blue, label='+', disabled=True),
        Button(style=ButtonStyle.red, label='Clear', disabled=True)
    ],
    [
        Button(style=ButtonStyle.grey, label='00', disabled=True),
        Button(style=ButtonStyle.grey, label='0', disabled=True),
        Button(style=ButtonStyle.blue, label='.', disabled=True),
        Button(style=ButtonStyle.blue, label='-', disabled=True),
        Button(style=ButtonStyle.red, label='Answ', disabled=True)
    ],
]
