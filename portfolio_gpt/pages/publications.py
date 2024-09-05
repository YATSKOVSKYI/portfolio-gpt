"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from portfolio_gpt import ui



def publications_page() -> rx.Component:
    # About us Page
    return ui.base_layout(
        rx.vstack(
            rx.heading("Welcome to publications!", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
