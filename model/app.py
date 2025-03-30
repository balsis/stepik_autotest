from model.components.auth_widget import AuthWidget
from model.components.navbar import Navbar
from model.components.profile_dropdown_menu import ProfileDropdownMenu
from model.pages.CatalogPage import CatalogPage
from model.pages.CatalogSearchPage import CatalogSearchPage
from model.pages.LearnPage import LearnPage


auth_widget = AuthWidget()
navbar = Navbar()
profile_menu = ProfileDropdownMenu()

catalog_page = CatalogPage()
catalog_search_page = CatalogSearchPage()
learn_page = LearnPage()