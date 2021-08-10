from datetime import datetime
from os import path, makedirs, getcwd
from modules.tests_constants import UIConstants


def save_screenshot(page, file_name, base_path=None, file_extension=".png", add_time_marker=True):
    """ Save screen shot to file

    :param page: page for screen shot
    :type page: pages.page
    :param file_name: file name without file extension
    :type file_name: str
    :param base_path: base dir for saving logs
    :type base_path: str
    :param file_extension: file extension
    :type file_extension: str
    :param add_time_marker: add time marker
    :type add_time_marker: bool
    :returns: None
    """
    base_path = base_path or path.abspath(getcwd())
    full_path = path.join(base_path, UIConstants.SCREENSHOT_FOLDER)
    if not path.exists(full_path):
        makedirs(full_path)
    if add_time_marker:
        file_name += "_" + datetime.now().strftime("%d%M%Y_%H%M%S")
    if not file_name.endswith(file_extension):
        file_name += file_extension
    full_path = path.join(full_path, file_name)
    page.driver.save_screenshot(full_path)