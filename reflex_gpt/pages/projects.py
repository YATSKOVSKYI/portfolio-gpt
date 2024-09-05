"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from reflex_gpt import ui

def projects_page() -> rx.Component:
    # About us Page
    return ui.base_layout(
        rx.vstack(
            rx.heading("Welcome to projects!", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )