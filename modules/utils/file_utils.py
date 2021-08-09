from datetime import datetime
from os import path, makedirs, getcwd
from modules.tests_constants import UIConstants


def save_screenshot(page, base_path=None, file_name=None):
    """"""
    base_path = base_path or path.abspath(getcwd())
    full_path = path.join(base_path, UIConstants.SCREENSHOT_FOLDER)
    if not path.exists(full_path):
        makedirs(full_path)
    file_name = file_name or datetime.now().strftime("%d%M%Y_%H%M%S")
    if not file_name.endswith(".png"):
        file_name += ".png"
    full_path = path.join(full_path, file_name)
    page.driver.save_screenshot(full_path)