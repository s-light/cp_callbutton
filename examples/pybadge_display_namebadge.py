#!/usr/bin/env python3
"""Simple PyBadge NameBadge Example."""


from adafruit_pybadger import pybadger

pybadger.show_badge(name_string="FASW", hello_scale=1, my_name_is_scale=1, name_scale=3)

while True:
    pybadger.auto_dim_display(delay=10)
    if pybadger.button.a:
        pybadger.show_business_card(
            image_name="faswlogo.bmp", name_string="FASW", name_scale=2
        )
    elif pybadger.button.b:
        pybadger.show_qr_code(data="https://circuitpython.org")
    elif pybadger.button.start:
        pybadger.show_badge(
            name_string="Hello World",
            hello_scale=2,
            my_name_is_scale=2,
            name_scale=2,
        )
