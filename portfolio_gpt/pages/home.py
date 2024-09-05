"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from portfolio_gpt import ui

def home_page() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        rx.vstack(
            rx.heading("您好，我叫杜铭。这是 PERFILEV DMITRII GPT!", size="9"),
            rx.text(
                "software engineer, data scientist, machine learning engineer ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
