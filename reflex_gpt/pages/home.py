"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from reflex_gpt import ui

def home_page() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        rx.vstack(
            rx.heading("Hello, My Name is Perfilev Dmitrii", size="10"),
            rx.text(
                "This site is my personal blog",
                size="10",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
