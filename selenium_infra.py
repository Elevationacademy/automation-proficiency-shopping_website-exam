from selenium.common.exceptions import NoSuchElementException
import time
class SeleniumInfra:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)  # wait up to 10 seconds when trying to find the element
        self.driver.maximize_window()
    # load the given URL
    def get_URL(self, URL):
        try:
            self.driver.get(URL)
        except Exception as e:
            print(f'Got error while trying to get the url {URL}, error is {e}')
    '''
        find an element
        from_element: finding an element from the given from_element, if from_element = None: from_element = self.driver 
    '''
    def find_element_by(self, locator_type, locator_value, from_element=None):
        try:
            if not from_element:
                from_element = self.driver
            if locator_type == "id":
                element = from_element.find_element_by_id(locator_value)
            if locator_type == "class_name":
                element = from_element.find_element_by_class_name(locator_value)
            if locator_type == "css":
                element = from_element.find_element_by_css_selector(locator_value)
            if locator_type == "name":
                element = from_element.find_element_by_name(locator_value)
            if locator_type == "xpath":
                element = from_element.find_element_by_xpath(locator_value)
            if locator_type == "tag_name":
                element = from_element.find_element_by_tag_name(locator_value)
            print(f'Find element with {locator_type} = {locator_value}')
            return element
        except Exception as e:
            print(f'Got error while trying to find the element with {locator_type} = {locator_value}, error is: {e}')
            return False
    '''
       find elements list
       from_element: finding elements from the given from_element, if from_element = None: from_element = self.driver 
   '''
    def find_element_list_by(self, locator_type, locator_value, from_element=None):
        try:
            if not from_element:
                from_element = self.driver
            if locator_type == "id":
                element = from_element.find_elements_by_id(locator_value)
            if locator_type == "class_name":
                element = from_element.find_elements_by_class_name(locator_value)
            if locator_type == "css":
                element = from_element.find_elements_by_css_selector(locator_value)
            if locator_type == "name":
                element = from_element.find_elements_by_name(locator_value)
            if locator_type == "xpath":
                element = from_element.find_elements_by_xpath(locator_value)
            if locator_type == "tag_name":
                element = from_element.find_elements_by_tag_name(locator_value)
            print(f'Find element with {locator_type} = {locator_value}')
            return element
        except Exception as e:
            print(
                f'Got error while trying to find list of elements with {locator_type} = {locator_value}, error is: {e}')
            return False
    '''
        element: if element is none - finding the element and clicking on it, else - clicking the given element
        from_element: clicking on an element from the given from_element or from the driver
    '''
    def click_element(self, locator_type, locator_value, element=None, from_element=None):
        try:
            if not element:
                if from_element:
                    element = self.find_element_by(locator_type, locator_value, from_element)
                else:
                    element = self.find_element_by(locator_type, locator_value)
            element.click()
            print(f'Clicked on element with {locator_type} = {locator_value}')
        except Exception as e:
            print(f'Got error while trying to click the element with {locator_type} = {locator_value}, error is: {e}')
    '''
        finding the wanted element and inserting the given input to it
    '''
    def write_element(self, input, locator_type, locator_value, element=None, from_element=None):
        try:
            if not element:
                if from_element:
                    element = self.find_element_by(locator_type, locator_value, from_element)
                else:
                    element = self.find_element_by(locator_type, locator_value)
            element.send_keys(input)
            print(f'Send Keys of "{input}" to element with {locator_type} = {locator_value}')
        except Exception as e:
            print(
                f'Got error while trying to send keys to element with {locator_type} = {locator_value}, error is: {e}')
    '''
        finding the wanted element and return its' text
    '''
    def get_text_from_element(self, locator_type, locator_value, element=None, from_element=None):
        try:
            if not element:
                if from_element:
                    element = self.find_element_by(locator_type, locator_value, from_element)
                else:
                    element = self.find_element_by(locator_type, locator_value)
            print(f'Get text from element with {locator_type} = {locator_value}')
            return element.text
        except Exception as e:
            print(
                f'Got error while trying to get text from element with {locator_type} = {locator_value}, error is: {e}')
            return ""
    '''
       finding the wanted element and clearing its' field 
    '''
    def clear_element_field(self, locator_type, locator_value, element=None, from_element=None):
        try:
            if not element:
                if from_element:
                    element = self.find_element_by(locator_type, locator_value, from_element)
                else:
                    element = self.find_element_by(locator_type, locator_value)
                element.clear()
                print(f'Clear text from element with {locator_type} = {locator_value}')
        except Exception as e:
            print(
                f'Got error while trying clear text from element with {locator_type} = {locator_value}, error is: {e}')
    '''
        return True if element exist or False otherwise
    '''
    def is_element_exists(self, locator_type, locator_value, from_element=None):
        try:
            if from_element:
                element = self.find_element_by(locator_type, locator_value, from_element)
            else:
                element = self.find_element_by(locator_type, locator_value)
            if element:
                return True
            else:
                return False
        except NoSuchElementException:
            return False
    def close(self):
        time.sleep(3)
        self.driver.quit()
    '''
        validate that the page name included in the current URL and return True/False accordingly
    '''
    def validate_URL(self, page_name):
        try:
            page_name = page_name.lower()
            current_url = self.driver.current_url
            if page_name in current_url:
                print(f"'{page_name}' is included in the page's URL which is '{current_url}'")
                return True
            else:
                print(f"'{page_name}' is NOT included in the page's URL which is '{current_url}'")
                return False
        except Exception as e:
            print(f'Got error while validating url, error is: {e}')