import reflex as rx

from .state import ChatState

def chat_form() -> rx.Component:

    return rx.form(
        rx.vstack(
            rx.text_area(
                name='message',
                placeholder='You message',
                required=True,
                width='100%',
            ),
            rx.hstack(
                rx.button("Submit", type='submit'),
                rx.cond(
                    ChatState.user_did_submot,
                    rx.text("Submitted"),
                    rx.fragment(),
                )
                
            )
        ),
        on_submit=ChatState.hande_submit,
        reset_on_submit=True
    )