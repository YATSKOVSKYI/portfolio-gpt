import reflex as rx

from . import routes

class NavState(rx.State):
    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)
    
    def to_about_us(self):
        return rx.redirect(routes.ABOUTE_US_ROUTE)

    def to_publications(self):
        return rx.redirect(routes.PUBLICATIONS_ROUTE)

    def to_projects(self):
        return rx.redirect(routes.PROJECTS_ROUTE)
    
    def to_chat(self):
        return rx.redirect(routes.CHAT_ROUTE)

