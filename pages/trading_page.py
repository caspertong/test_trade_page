from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TradingPage(BasePage):
    # Main Screen
    SYMBOL = (By.CSS_SELECTOR, "div[data-testid='symbol-overview-id']")
    
    # Selectors
    BUY_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="trade-button-order-buy"]')
    SELL_BUTTON = (By.CSS_SELECTOR, 'button[data-testid="trade-button-order-sell"]')
    BUY_LIVE_PRICE = (By.CSS_SELECTOR, 'div[data-testid="trade-live-buy-price"]')
    SELL_LIVE_PRICE = (By.CSS_SELECTOR, 'div[data-testid="trade-live-sell-price"]')
    
    # Inputs
    VOLUME_INPUT = (By.CSS_SELECTOR, "input[data-testid='trade-input-volume']")
    PRICE_INPUT = (By.XPATH, "//div[contains(text(), 'One point equals')]/following::input[1]")

    # SL/TP
    SL_PRICE_INPUT = (By.CSS_SELECTOR, "input[data-testid='trade-input-stoploss-price']")
    TP_PRICE_INPUT = (By.CSS_SELECTOR, "input[data-testid='trade-input-takeprofit-price']")
    SL_POINT_INPUT = (By.CSS_SELECTOR, "input[data-testid='trade-input-stoploss-points']")
    TP_POINT_INPUT = (By.CSS_SELECTOR, "input[data-testid='trade-input-takeprofit-points']")
    
    # Order Type
    ORDER_TYPE_DROPDOWN = (By.CSS_SELECTOR, "div[data-testid='trade-dropdown-order-type']")
    ORDER_TYPE_MARKET = (By.XPATH, "//div[text()='Market']")
    ORDER_TYPE_LIMIT = (By.XPATH, "//div[text()='Limit']")
    ORDER_TYPE_STOP = (By.XPATH, "//div[text()='Stop']")
    ORDER_TYPE_STOP_LIMIT = (By.XPATH, "//div[text()='Stop Limit']")

    # Expiry Type
    EXPIRY_INPUT = (By.CSS_SELECTOR, "div[data-testid='trade-dropdown-expiry']")
    EXPIRY_TYPE_GTC = (By.XPATH, "//div[text()='Good Till Canceled']")
    EXPIRY_TYPE_GTD = (By.XPATH, "//div[text()='Good Till Day']")
    EXPIRY_TYPE_SD = (By.XPATH, "//div[text()='Specified Date']")
    EXPIRY_TYPE_SDT = (By.XPATH, "//div[text()='Specified Date and Time']")
    
    # Confirmation
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, "button[data-testid='trade-button-order']")
    CONFIRM_MODAL_BUTTON = (By.CSS_SELECTOR, "button[data-testid='trade-confirmation-button-confirm']")
    CANCEL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[data-testid='trade-confirmation-button-cancel']")

    # Tables - Use text based relative path
    # Open Positions Tab
    OPEN_POSITIONS_TAB = (By.CSS_SELECTOR, "div[data-testid='tab-asset-order-type-open-positions']")
    POSITION_DATE = (By.CSS_SELECTOR, "div[data-testid='asset-open-column-open-date']")
    POSITION_ORDER = (By.CSS_SELECTOR, "div[data-testid='asset-open-column-order-id']")
    POSITION_SYMBOL = (By.CSS_SELECTOR, "div[data-testid='asset-open-column-symbol']")
    POSITION_VOLUME = (By.CSS_SELECTOR, "div[data-testid='asset-open-column-volume']")
    POSITION_ENTRY_PRICE = (By.CSS_SELECTOR, "div[data-testid='asset-open-column-entry-price']")
    POSITION_SL = (By.CSS_SELECTOR, "div[data-testid='asset-open-column-stop-loss']")
    POSITION_TP = (By.CSS_SELECTOR, "div[data-testid='asset-open-column-take-profit']")

    POSITION_EDIT_BUTTON = (By.CSS_SELECTOR, "button[data-testid='asset-open-button-edit']")
    POSITION_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='asset-open-button-close']")

    # Pending Orders Tab
    PENDING_ORDERS_TAB = (By.CSS_SELECTOR, "div[data-testid='tab-asset-order-type-pending-orders']")
    PENDING_ORDERS_DATE = (By.CSS_SELECTOR, "div[data-testid='asset-pending-column-open-date']")
    PENDING_ORDERS_ORDER = (By.CSS_SELECTOR, "div[data-testid='asset-pending-column-order-id']")
    PENDING_ORDERS_SYMBOL = (By.CSS_SELECTOR, "div[data-testid='asset-pending-column-symbol']")
    PENDING_ORDERS_VOLUME = (By.CSS_SELECTOR, "div[data-testid='asset-pending-column-volume']")
    PENDING_ORDERS_ENTRY_PRICE = (By.CSS_SELECTOR, "div[data-testid='asset-pending-column-entry-price']")
    PENDING_ORDERS_SL = (By.CSS_SELECTOR, "div[data-testid='asset-pending-column-stop-loss']")
    PENDING_ORDERS_TP = (By.CSS_SELECTOR, "div[data-testid='asset-pending-column-take-profit']")

    # Bulk Close
    BULK_CLOSE_DROPDOWN = (By.CSS_SELECTOR, "div[data-testid='bulk-close']")
    BULK_DELETE_DROPDOWN = (By.CSS_SELECTOR, "div[data-testid='bulk-delete']")
    BULK_DROPDOWN_ALLPOSITION = (By.XPATH, "//div[text()='All Positions']")
    BULK_DROPDOWN_ALLORDER = (By.XPATH, "//div[text()='All Orders']")
    BULK_DROPDOWN_PROFITPOSITION = (By.XPATH, "//div[text()='Profitable Positions']")
    BULK_DROPDOWN_LOSSPOSITION = (By.XPATH, "//div[text()='Loss Positions']")
    BULK_DROPDOWN_LIMITORDER = (By.XPATH, "//div[text()='Limit Orders']")
    BULK_DROPDOWN_STOPORDER = (By.XPATH, "//div[text()='Stop Orders']")
    BULK_DROPDOWN_STOPLIMITORDER = (By.XPATH, "//div[text()='Stop Limit Orders']")

    # Bulk all model
    BULK_CONFIRM_ALL_BUTTON = (By.CSS_SELECTOR, "button[data-testid='bulk-close-modal-button-submit-all']")
    BULK_CANCEL_ALL_BUTTON = (By.CSS_SELECTOR, "button[data-testid='bulk-close-modal-button-cancel-all']")
    BULK_CONFIRM_PROFIT_BUTTON = (By.CSS_SELECTOR, "button[data-testid='bulk-close-modal-button-submit-profit']")
    BULK_CANCEL_PROFIT_BUTTON = (By.CSS_SELECTOR, "button[data-testid='bulk-close-modal-button-cancel-profit']")
    BULK_CONFIRM_LOSS_BUTTON = (By.CSS_SELECTOR, "button[data-testid='bulk-close-modal-button-submit-loss']")
    BULK_CANCEL_LOSS_BUTTON = (By.CSS_SELECTOR, "button[data-testid='bulk-close-modal-button-cancel-loss']")
    BULK_CONFIRM_LIMIT_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    BULK_CANCEL_LIMIT_BUTTON = (By.XPATH, "//button[text()='Cancel']")
    BULK_CONFIRM_STOP_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    BULK_CANCEL_STOP_BUTTON = (By.XPATH, "//button[text()='Cancel']")

    # Edit Popout
    # Edit Position Popout
    EDIT_POPOUT_TITLE = (By.CSS_SELECTOR, "div[data-testid='edit-confirmation-modal']")
    EDIT_POPOUT_SL_PRICE = (By.CSS_SELECTOR, "div[data-testid='edit-confirmation-modal'] input[data-testid='trade-input-stoploss-price']")
    EDIT_POPOUT_TP_PRICE = (By.CSS_SELECTOR, "div[data-testid='edit-confirmation-modal'] input[data-testid='trade-input-takeprofit-price']")
    EDIT_POPOUT_SL_POINTS = (By.CSS_SELECTOR, "div[data-testid='edit-confirmation-modal'] input[data-testid='trade-input-stoploss-points']")
    EDIT_POPOUT_TP_POINTS = (By.CSS_SELECTOR, "div[data-testid='edit-confirmation-modal'] input[data-testid='trade-input-takeprofit-points']")
    EDIT_POPOUT_UPDATE = (By.CSS_SELECTOR, "button[data-testid='edit-button-order']")
    EDIT_POPOUT_CONFIRM = (By.CSS_SELECTOR, "button[data-testid='trade-confirmation-button-confirm']")
    EDIT_POPOUT_CANCEL = (By.CSS_SELECTOR, "button[data-testid='trade-confirmation-button-close']")

    # Edit Limit Order Popout
    EDIT_LIMIT_POPOUT_TITLE = (By.CSS_SELECTOR, "div[class='sc-jxYSNo dhScmn'] div[class='sc-dTvVRJ dywwnY']")
    EDIT_LIMIT_POPOUT_SL_PRICE = (By.CSS_SELECTOR, "div[class='sc-jxYSNo dhScmn'] input[data-testid='trade-input-stoploss-price']")
    EDIT_LIMIT_POPOUT_TP_PRICE = (By.CSS_SELECTOR, "div[class='sc-jxYSNo dhScmn'] input[data-testid='trade-input-takeprofit-price']")
    EDIT_LIMIT_POPOUT_SL_POINTS = (By.CSS_SELECTOR, "div[class='sc-jxYSNo dhScmn'] input[data-testid='trade-input-stoploss-points']")
    EDIT_LIMIT_POPOUT_TP_POINTS = (By.CSS_SELECTOR, "div[class='sc-jxYSNo dhScmn'] input[data-testid='trade-input-takeprofit-points']")
    EDIT_LIMIT_POPOUT_CONFIRM = (By.XPATH, "//button[text()='Confirm']")
    EDIT_LIMIT_POPOUT_CANCEL = (By.XPATH, "//button[text()='Cancel']")

    # Close Position
    CLOSE_POSITION_TITLE = (By.XPATH, "//div[text()='Confirm To Close Position']")
    CLOSE_POSITION_CONFIRM = (By.XPATH, "//button[text()='Confirm']")
    CLOSE_POSITION_CANCEL = (By.XPATH, "//button[text()='Cancel']")
    CLOSE_POSITION_VOLUME = (By.XPATH, "//div[text()='Confirm To Close Position']/following::input[1]")



    URL = "https://aqxtrader.aquariux.com/web/trade"

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self):
        return self.is_visible(self.BUY_BUTTON)

    def select_order_type(self, order_type):
        self.click(self.ORDER_TYPE_DROPDOWN)
        match order_type.lower():
            case 'market':
                self.click(self.ORDER_TYPE_MARKET)
            case 'limit':
                self.click(self.ORDER_TYPE_LIMIT)
            case 'stop':
                self.click(self.ORDER_TYPE_STOP)
            case 'stop limit':
                self.click(self.ORDER_TYPE_STOP_LIMIT)
            case _:
                raise ValueError(f"Invalid order type: {order_type}")

    def select_expiry(self, expiry):
        self.click(self.EXPIRY_INPUT)
        match expiry.lower():
            case 'gtc':
                self.click(self.EXPIRY_TYPE_GTC)
            case 'gtd':
                self.click(self.EXPIRY_TYPE_GTD)
            case 'sd':
                self.click(self.EXPIRY_TYPE_SD)
            case 'sdt':
                self.click(self.EXPIRY_TYPE_SDT)
            case _:
                raise ValueError(f"Invalid expiry: {expiry}")

    def set_volume(self, volume):
        self.send_keys(self.VOLUME_INPUT, str(volume))
        self.driver.find_element(*self.VOLUME_INPUT).send_keys(Keys.TAB)

    def buy_sell_order(self, buy_sell, order_type, volume, price=None, sl=None, tp=None, expiry=None):
        # 1. Click Buy or Sell (Setup)
        if buy_sell.lower() == 'buy':
            self.click(self.BUY_BUTTON)
        else:
            self.click(self.SELL_BUTTON)
            
        time.sleep(1)

        # 2. Select Order Type
        self.select_order_type(order_type)

        time.sleep(1)

        # 3. Set Volume
        self.set_volume(volume)

        # 4. Set Price if provided
        if price:
            wait = WebDriverWait(self.driver, 10)
            price_input = wait.until(EC.element_to_be_clickable(self.PRICE_INPUT))
            price_input.send_keys(Keys.CONTROL + "a")
            price_input.send_keys(Keys.BACKSPACE)
            price_input.send_keys(str(price))
            time.sleep(1)
            # Click something else to trigger blur?
            self.click(self.BUY_BUTTON)
        
        # 5. Set SL/TP points if provided
        if sl:
            self.send_keys(self.SL_PRICE_INPUT, str(sl))
            self.click(self.BUY_BUTTON)
        if tp:
            self.send_keys(self.TP_PRICE_INPUT, str(tp))
            self.click(self.BUY_BUTTON)

        # 6. Set Expiry
        if expiry:
            self.select_expiry(expiry)

        # 7. Click Place Order
        time.sleep(1)
        self.click(self.PLACE_ORDER_BUTTON)
        
        # 8. Confirm if modal appears
        try:
            # Short wait for modal
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.CONFIRM_MODAL_BUTTON))
            if element.is_displayed():
                self.click(self.CONFIRM_MODAL_BUTTON)
                time.sleep(3) # Wait for processing
        except:
            Exception("Confirmation pop-out not showing") 

    def get_symbol_main(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.SYMBOL))
            symbol_text = element.text
            print(f"DEBUG: Symbol Text: '{symbol_text}'")
            return symbol_text
        except Exception as e:
            print(f"DEBUG: Error getting symbol: {e}")
            return None

    def get_live_price(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.BUY_LIVE_PRICE))
            live_price_text = element.text
            print(f"DEBUG: Live Price Text: '{live_price_text}'")
            return live_price_text
        except Exception as e:
            print(f"DEBUG: Error getting live price: {e}")
            return None

    def click_pending_orders_tab(self):
        self.click(self.PENDING_ORDERS_TAB)

    # Open Positions
    def get_open_positions_count(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.OPEN_POSITIONS_TAB))
            raw_text = element.text
            print(f"DEBUG: Raw Position Text: '{raw_text}'")
             
            # Expected format: "Open Positions (x)"
            if "(" in raw_text and ")" in raw_text:
                count_str = raw_text.split('(')[1].split(')')[0]
                print(f"DEBUG: Parsed Count: {count_str}")
                return int(count_str)
            else:
                print("DEBUG: Could not parse count, returning 0")
                return 0
        except Exception as e:
            print(f"DEBUG: Error getting count: {e}")
            return 0

    def get_order_id(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.POSITION_ORDER))
            order_id_text = element.text
            print(f"DEBUG: Order ID Text: '{order_id_text}'")
            return int(order_id_text)
        except Exception as e:
            print(f"DEBUG: Error getting order ID: {e}")
            return 0

    def get_transaction_symbol(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.POSITION_SYMBOL))
            symbol_text = element.text
            print(f"DEBUG: Transaction Symbol Text: '{symbol_text}'")
            return symbol_text
        except Exception as e:
            print(f"DEBUG: Error getting transaction symbol: {e}")
            return None

    def get_transaction_volume(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.POSITION_VOLUME))
            volume_text = element.text
            print(f"DEBUG: Transaction Volume Text: '{volume_text}'")
            return volume_text
        except Exception as e:
            print(f"DEBUG: Error getting transaction volume: {e}")
            return None

    def get_transaction_entry_price(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.POSITION_ENTRY_PRICE))
            entry_price_text = element.text
            print(f"DEBUG: Transaction Entry Price Text: '{entry_price_text}'")
            return entry_price_text
        except Exception as e:
            print(f"DEBUG: Error getting transaction entry price: {e}")
            return None

    def get_transaction_sl(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.POSITION_SL))
            sl_text = element.text
            print(f"DEBUG: Transaction SL Text: '{sl_text}'")
            return sl_text
        except Exception as e:
            print(f"DEBUG: Error getting transaction sl: {e}")
            return None

    def get_transaction_tp(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.POSITION_TP))
            tp_text = element.text
            print(f"DEBUG: Transaction TP Text: '{tp_text}'")
            return tp_text
        except Exception as e:
            print(f"DEBUG: Error getting transaction tp: {e}")
            return None
    
    def edit_position(self, sl=None, tp=None):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.POSITION_EDIT_BUTTON))
        self.click(self.POSITION_EDIT_BUTTON)
        time.sleep(1)
        element = wait.until(EC.visibility_of_element_located(self.EDIT_POPOUT_TITLE))
        if element.is_displayed():
            # Wait for any overlay to disappear
            try:
                wait.until(EC.invisibility_of_element_located((By.ID, "overlay-aqx-trader")))
            except:
                pass # Overlay might not even appear or be fleeting

            if sl:
                sl_input = wait.until(EC.element_to_be_clickable(self.EDIT_POPOUT_SL_PRICE))
                try:
                    sl_input.click()
                except:
                    self.driver.execute_script("arguments[0].click();", sl_input)
                time.sleep(1)
                # clear() is not working, using Ctrl+A + Backspace instead
                sl_input.send_keys(Keys.CONTROL + "a")
                sl_input.send_keys(Keys.BACKSPACE)
                time.sleep(1)
                sl_input.send_keys(str(sl))
                time.sleep(1)
                self.click(self.EDIT_POPOUT_TITLE)
            if tp:
                tp_input = wait.until(EC.element_to_be_clickable(self.EDIT_POPOUT_TP_PRICE))
                try:
                    tp_input.click()
                except:
                    self.driver.execute_script("arguments[0].click();", tp_input)
                time.sleep(1)
                # clear() is not working, using Ctrl+A + Backspace instead
                tp_input.send_keys(Keys.CONTROL + "a")
                tp_input.send_keys(Keys.BACKSPACE)
                time.sleep(1)
                tp_input.send_keys(str(tp))
                time.sleep(1)
                self.click(self.EDIT_POPOUT_TITLE)
            self.click(self.EDIT_POPOUT_UPDATE)
            time.sleep(1)
            element = wait.until(EC.visibility_of_element_located(self.EDIT_POPOUT_CONFIRM))
            self.click(self.EDIT_POPOUT_CONFIRM)
        
    def close_position(self, volume=None):
        wait = WebDriverWait(self.driver, 10)
        self.click(self.POSITION_CLOSE_BUTTON)
        time.sleep(1)
        wait.until(EC.visibility_of_element_located(self.CLOSE_POSITION_TITLE))
        if volume:
            volume_input = wait.until(EC.element_to_be_clickable(self.CLOSE_POSITION_VOLUME))
            volume_input.click()
            time.sleep(1)
            # clear() is not working, using Ctrl+A + Backspace instead
            volume_input.send_keys(Keys.CONTROL + "a")
            volume_input.send_keys(Keys.BACKSPACE)
            time.sleep(1)
            volume_input.send_keys(str(volume))
            time.sleep(1)
        wait.until(EC.visibility_of_element_located(self.CLOSE_POSITION_CONFIRM))
        self.click(self.CLOSE_POSITION_CONFIRM)

    # Pending Orders
    def get_pending_orders_count(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.PENDING_ORDERS_TAB))
            pending_orders_count = element.text
            print(f"DEBUG: Pending Orders Count: '{pending_orders_count}'")
            return pending_orders_count
        except Exception as e:
            print(f"DEBUG: Error getting pending orders count: {e}")
            return None
    
    def get_pending_orders_order_id(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.PENDING_ORDERS_ORDER))
            order_id_text = element.text
            print(f"DEBUG: Order ID Text: '{order_id_text}'")
            return int(order_id_text)
        except Exception as e:
            print(f"DEBUG: Error getting order ID: {e}")
            return 0

    def get_pending_orders_symbol(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.PENDING_ORDERS_SYMBOL))
            symbol_text = element.text
            print(f"DEBUG: Pending Orders Symbol Text: '{symbol_text}'")
            return symbol_text
        except Exception as e:
            print(f"DEBUG: Error getting pending orders symbol: {e}")
            return None

    def get_pending_orders_volume(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.PENDING_ORDERS_VOLUME))
            volume_text = element.text
            print(f"DEBUG: Pending Orders Volume Text: '{volume_text}'")
            return volume_text
        except Exception as e:
            print(f"DEBUG: Error getting pending orders volume: {e}")
            return None

    def get_pending_orders_entry_price(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.PENDING_ORDERS_ENTRY_PRICE))
            entry_price_text = element.text
            print(f"DEBUG: Pending Orders Entry Price Text: '{entry_price_text}'")
            return entry_price_text
        except Exception as e:
            print(f"DEBUG: Error getting pending orders entry price: {e}")
            return None

    def get_pending_orders_sl(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.PENDING_ORDERS_SL))
            sl_text = element.text
            print(f"DEBUG: Pending Orders SL Text: '{sl_text}'")
            return sl_text
        except Exception as e:
            print(f"DEBUG: Error getting pending orders sl: {e}")
            return None

    def get_pending_orders_tp(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located(self.PENDING_ORDERS_TP))
            tp_text = element.text
            print(f"DEBUG: Pending Orders TP Text: '{tp_text}'")
            return tp_text
        except Exception as e:
            print(f"DEBUG: Error getting pending orders tp: {e}")
            return None
    

    def edit_pending_order(self, sl=None, tp=None):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.POSITION_EDIT_BUTTON))
        self.click(self.POSITION_EDIT_BUTTON)
        time.sleep(1)
        element = wait.until(EC.visibility_of_element_located(self.EDIT_LIMIT_POPOUT_TITLE))
        if element.is_displayed():
            # Wait for any overlay to disappear
            try:
                wait.until(EC.invisibility_of_element_located((By.ID, "overlay-aqx-trader")))
            except:
                pass # Overlay might not even appear or be fleeting

            if sl:
                sl_input = wait.until(EC.element_to_be_clickable(self.EDIT_LIMIT_POPOUT_SL_PRICE))
                try:
                    sl_input.click()
                except:
                    self.driver.execute_script("arguments[0].click();", sl_input)
                time.sleep(1)
                # clear() is not working, using Ctrl+A + Backspace instead
                sl_input.send_keys(Keys.CONTROL + "a")
                sl_input.send_keys(Keys.BACKSPACE)
                time.sleep(1)
                sl_input.send_keys(str(sl))
                time.sleep(1)
                self.click(self.EDIT_LIMIT_POPOUT_TITLE)
            if tp:
                tp_input = wait.until(EC.element_to_be_clickable(self.EDIT_LIMIT_POPOUT_TP_PRICE))
                try:
                    tp_input.click()
                except:
                    self.driver.execute_script("arguments[0].click();", tp_input)
                time.sleep(1)
                # clear() is not working, using Ctrl+A + Backspace instead
                tp_input.send_keys(Keys.CONTROL + "a")
                tp_input.send_keys(Keys.BACKSPACE)
                time.sleep(1)
                tp_input.send_keys(str(tp))
                time.sleep(1)
                self.click(self.EDIT_LIMIT_POPOUT_TITLE)
            self.click(self.EDIT_LIMIT_POPOUT_CONFIRM)
            time.sleep(1)
            element = wait.until(EC.visibility_of_element_located(self.EDIT_POPOUT_CONFIRM))
            self.click(self.EDIT_POPOUT_CONFIRM)
        

    def select_bulk_position_pending_order(self, position, option):
        match position.lower():
            case 'position':
                self.click(self.OPEN_POSITIONS_TAB)
                time.sleep(1)
                self.select_bulk_position_option(option)
            case 'pending order':
                self.click(self.PENDING_ORDERS_TAB)
                time.sleep(1)
                self.select_bulk_pending_option(option)
            case _:
                raise ValueError(f"Invalid position: {position}")
    
    def select_bulk_position_option(self, option):
        self.click(self.BULK_CLOSE_DROPDOWN)
        match option.lower():
            case 'all':
                self.click(self.BULK_DROPDOWN_ALLPOSITION)
                time.sleep(1)
                self.click(self.BULK_CONFIRM_ALL_BUTTON)
            case 'profitable':
                self.click(self.BULK_DROPDOWN_PROFITPOSITION)
                time.sleep(1)
                self.click(self.BULK_CONFIRM_PROFIT_BUTTON)
            case 'loss':
                self.click(self.BULK_DROPDOWN_LOSSPOSITION)
                time.sleep(1)
                self.click(self.BULK_CONFIRM_LOSS_BUTTON)
            case _:
                raise ValueError(f"Invalid option: {option}")

    def select_bulk_pending_option(self, option):
        self.click(self.BULK_DELETE_DROPDOWN)
        match option.lower():
            case 'all':
                self.click(self.BULK_DROPDOWN_ALLORDER)
                time.sleep(1)
                self.click(self.BULK_CONFIRM_ALL_BUTTON)
            case 'limit':
                self.click(self.BULK_DROPDOWN_LIMITORDER)
                time.sleep(1)
                self.click(self.BULK_CONFIRM_LIMIT_BUTTON)
            case 'stop':
                self.click(self.BULK_DROPDOWN_STOPORDER)
                time.sleep(1)
                self.click(self.BULK_CONFIRM_STOP_BUTTON)
            # Function in the website not implemented yet
            case 'stoplimit':
                self.click(self.BULK_DROPDOWN_STOPLIMITORDER)
                time.sleep(1)
                self.click(self.BULK_CONFIRM_STOPLIMIT_BUTTON)
            case _:
                raise ValueError(f"Invalid option: {option}")

    def bulk_close(self, position, option):
        self.select_bulk_position_pending_order(position, option)