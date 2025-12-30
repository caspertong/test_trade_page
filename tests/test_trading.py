import pytest
import time
from pages.trading_page import TradingPage
from pages.notification_page import NotificationPage

# Test 1: Buy Market order without One-Click Trading function
def test_place_buy_order(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'buy'
    order_type = 'market'
    volume = 0.01
    
    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    initial_count = trading_page.get_open_positions_count()
    initial_order_id = trading_page.get_order_id()
    initial_symbol = trading_page.get_symbol_main()
    
    # Place Buy Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume)
    
    # Verify the transaction details
    time.sleep(5) 
    new_count = trading_page.get_open_positions_count()
    new_order_id = trading_page.get_order_id()
    assert new_count > initial_count, "Buy order did not result in a new open position"
    assert new_order_id != initial_order_id, "Buy order did not result in a new order ID"
    assert initial_symbol == trading_page.get_transaction_symbol(), "Symbol does not match"
    assert str(volume) == trading_page.get_transaction_volume(), "Volume does not match"

    notification_page = NotificationPage(driver)
    symbol, order_id = notification_page.get_latest_notification()
    assert symbol == initial_symbol, "Symbol does not match in notification"
    assert order_id == new_order_id, "Order ID does not match in notification"


# Test 2: Sell Market order without One-Click Trading function
def test_place_sell_order(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'sell'
    order_type = 'market'
    volume = 0.01
    
    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    initial_count = trading_page.get_open_positions_count()
    initial_order_id = trading_page.get_order_id()
    initial_symbol = trading_page.get_symbol_main()
    
    # Place Sell Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume)
    
    # Verify the transaction details
    time.sleep(5) 
    new_count = trading_page.get_open_positions_count()
    new_order_id = trading_page.get_order_id()
    assert new_count > initial_count, "Sell order did not result in a new open position"
    assert new_order_id != initial_order_id, "Sell order did not result in a new order ID"
    assert initial_symbol == trading_page.get_transaction_symbol(), "Symbol does not match"
    assert str(volume) == trading_page.get_transaction_volume(), "Volume does not match"

    notification_page = NotificationPage(driver)
    symbol, order_id = notification_page.get_latest_notification()
    assert symbol == initial_symbol, "Symbol does not match in notification"
    assert order_id == new_order_id, "Order ID does not match in notification"

# Test 3: Buy Market order with SL/TP
def test_place_buy_order_with_sl_tp(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'buy'
    order_type = 'market'
    volume = 1
    sl = 0.00005
    tp = 5
    
    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    initial_count = trading_page.get_open_positions_count()
    initial_order_id = trading_page.get_order_id()
    initial_symbol = trading_page.get_symbol_main()
    
    # Place Buy Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume, sl=sl, tp=tp)
    
    # Verify the transaction details
    time.sleep(5) 
    new_count = trading_page.get_open_positions_count()
    new_order_id = trading_page.get_order_id()
    assert new_count > initial_count, "Buy order did not result in a new open position"
    assert new_order_id != initial_order_id, "Buy order did not result in a new order ID"
    assert initial_symbol == trading_page.get_transaction_symbol(), "Symbol does not match"
    assert str(volume) == trading_page.get_transaction_volume(), "Volume does not match"
    assert str(sl) == trading_page.get_transaction_sl(), "SL does not match"
    assert str(tp) == trading_page.get_transaction_tp(), "TP does not match"

    notification_page = NotificationPage(driver)
    symbol, order_id = notification_page.get_latest_notification()
    assert symbol == initial_symbol, "Symbol does not match in notification"
    assert order_id == new_order_id, "Order ID does not match in notification"

# Test 4: Sell Market order with SL/TP
def test_place_sell_order_with_sl_tp(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'sell'
    order_type = 'market'
    volume = 1
    sl = 0.00005
    tp = 5
    
    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    initial_count = trading_page.get_open_positions_count()
    initial_order_id = trading_page.get_order_id()
    initial_symbol = trading_page.get_symbol_main()
    
    # Place Sell Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume, sl=sl, tp=tp)
    
    # Verify the transaction details
    time.sleep(5) 
    new_count = trading_page.get_open_positions_count()
    new_order_id = trading_page.get_order_id()
    assert new_count > initial_count, "Sell order did not result in a new open position"
    assert new_order_id != initial_order_id, "Sell order did not result in a new order ID"
    assert initial_symbol == trading_page.get_transaction_symbol(), "Symbol does not match"
    assert str(volume) == trading_page.get_transaction_volume(), "Volume does not match"
    assert str(sl) == trading_page.get_transaction_sl(), "SL does not match"
    assert str(tp) == trading_page.get_transaction_tp(), "TP does not match"

    notification_page = NotificationPage(driver)
    symbol, order_id = notification_page.get_latest_notification()
    assert symbol == initial_symbol, "Symbol does not match in notification"
    assert order_id == new_order_id, "Order ID does not match in notification"


# Test 5: Edit Position
def test_edit_position(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)
    
    buy_sell = 'buy'
    order_type = 'market'
    volume = 1
    sl = "{:.5f}".format(0.00005) # Format as string to avoid scientific notation
    tp = 5

    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume)
    time.sleep(3)
    trading_page.edit_position(sl=sl, tp=tp)
    time.sleep(5)
    assert trading_page.get_transaction_sl() == str(sl), "SL does not match"
    assert trading_page.get_transaction_tp() == "{:.5f}".format(tp), "TP does not match"

# Test 6: Close Open Position
def test_close_position(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'buy'
    order_type = 'market'
    volume = 2

    assert trading_page.is_loaded(), "Trading page not loaded"

    time.sleep(3)
    # Place Buy Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume)
    time.sleep(3)
    initial_order_id = trading_page.get_order_id()
    # Close Position
    trading_page.close_position()
    time.sleep(5)
    prev_order_id = trading_page.get_order_id()
    assert prev_order_id != initial_order_id, "Close position failed"

# Test 7: Partial Close Open Position
def test_partial_close_position(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'buy'
    order_type = 'market'
    volume = 2

    assert trading_page.is_loaded(), "Trading page not loaded"

    time.sleep(3)
    # Place Buy Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume)
    # Partial Close
    time.sleep(3)
    trading_page.close_position(volume=1)
    time.sleep(5)
    new_volume = trading_page.get_transaction_volume()
    assert int(new_volume) != volume, "Partial close failed"

# Test 8: Buy Limit Order Good Till Canceled
def test_buy_limit_order_gtc(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'buy'
    order_type = 'limit'
    volume = 1
    price = 0.1
    expiry = 'gtc'

    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    trading_page.click_pending_orders_tab()
    initial_count = trading_page.get_pending_orders_count()
    initial_order_id = trading_page.get_pending_orders_order_id()
    initial_symbol = trading_page.get_pending_orders_symbol()
    
    # Place Buy Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume, price=price, expiry=expiry)
    
    # Verify the transaction details
    time.sleep(5) 
    new_count = trading_page.get_pending_orders_count()
    new_order_id = trading_page.get_pending_orders_order_id()
    assert new_count > initial_count, "Buy order did not result in a new open position"
    assert new_order_id != initial_order_id, "Buy order did not result in a new order ID"
    assert initial_symbol == trading_page.get_pending_orders_symbol(), "Symbol does not match"

# Test 9: Buy Stop Order Good Till Canceled
def test_buy_stop_order_gtc(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'buy'
    order_type = 'stop'
    volume = 1
    price = 1
    expiry = 'gtc'

    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    trading_page.click_pending_orders_tab()
    initial_count = trading_page.get_pending_orders_count()
    initial_order_id = trading_page.get_pending_orders_order_id()
    initial_symbol = trading_page.get_pending_orders_symbol()
    
    # Place Buy Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume, price=price, expiry=expiry)
    
    # Verify the transaction details
    time.sleep(5) 
    new_count = trading_page.get_pending_orders_count()
    new_order_id = trading_page.get_pending_orders_order_id()
    assert new_count > initial_count, "Buy order did not result in a new open position"
    assert new_order_id != initial_order_id, "Buy order did not result in a new order ID"
    assert initial_symbol == trading_page.get_pending_orders_symbol(), "Symbol does not match"

# Test 10: Buy Limit Order Good Till Day
def test_buy_limit_order_gtd(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'buy'
    order_type = 'limit'
    volume = 1
    price = 0.1
    expiry = 'gtd'

    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    trading_page.click_pending_orders_tab()
    initial_count = trading_page.get_pending_orders_count()
    initial_order_id = trading_page.get_pending_orders_order_id()
    initial_symbol = trading_page.get_pending_orders_symbol()
    
    # Place Buy Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume, price=price, expiry=expiry)
    
    # Verify the transaction details
    time.sleep(5) 
    new_count = trading_page.get_pending_orders_count()
    new_order_id = trading_page.get_pending_orders_order_id()
    assert new_count > initial_count, "Buy order did not result in a new open position"
    assert new_order_id != initial_order_id, "Buy order did not result in a new order ID"
    assert initial_symbol == trading_page.get_pending_orders_symbol(), "Symbol does not match"

# Test 11: Buy Stop Order Good Till Day
def test_buy_stop_order_gtd(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'buy'
    order_type = 'stop'
    volume = 1
    price = 1
    expiry = 'gtd'

    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    trading_page.click_pending_orders_tab()
    initial_count = trading_page.get_pending_orders_count()
    initial_order_id = trading_page.get_pending_orders_order_id()
    initial_symbol = trading_page.get_pending_orders_symbol()
    
    # Place Buy Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume, price=price, expiry=expiry)
    
    # Verify the transaction details
    time.sleep(5) 
    new_count = trading_page.get_pending_orders_count()
    new_order_id = trading_page.get_pending_orders_order_id()
    assert new_count > initial_count, "Buy order did not result in a new open position"
    assert new_order_id != initial_order_id, "Buy order did not result in a new order ID"
    assert initial_symbol == trading_page.get_pending_orders_symbol(), "Symbol does not match"

# Test 12: Buy Limit Order Good Till Specified Date
def test_buy_limit_order_sd(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'buy'
    order_type = 'limit'
    volume = 1
    price = 0.1
    expiry = 'sd'

    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    trading_page.click_pending_orders_tab()
    initial_count = trading_page.get_pending_orders_count()
    initial_order_id = trading_page.get_pending_orders_order_id()
    initial_symbol = trading_page.get_pending_orders_symbol()
    
    # Place Buy Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume, price=price, expiry=expiry)
    
    # Verify the transaction details
    time.sleep(5) 
    new_count = trading_page.get_pending_orders_count()
    new_order_id = trading_page.get_pending_orders_order_id()
    assert new_count > initial_count, "Buy order did not result in a new open position"
    assert new_order_id != initial_order_id, "Buy order did not result in a new order ID"
    assert initial_symbol == trading_page.get_pending_orders_symbol(), "Symbol does not match"

# Test 13 Buy Stop Order Specified Date
def test_buy_stop_order_sd(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'buy'
    order_type = 'stop'
    volume = 1
    price = 1
    expiry = 'sd'

    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    trading_page.click_pending_orders_tab()
    initial_count = trading_page.get_pending_orders_count()
    initial_order_id = trading_page.get_pending_orders_order_id()
    initial_symbol = trading_page.get_pending_orders_symbol()
    
    # Place Buy Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume, price=price, expiry=expiry)
    
    # Verify the transaction details
    time.sleep(5) 
    new_count = trading_page.get_pending_orders_count()
    new_order_id = trading_page.get_pending_orders_order_id()
    assert new_count > initial_count, "Buy order did not result in a new open position"
    assert new_order_id != initial_order_id, "Buy order did not result in a new order ID"
    assert initial_symbol == trading_page.get_pending_orders_symbol(), "Symbol does not match"

# Test 14: Buy Limit Order Specified Date and Time
def test_buy_limit_order_sdt(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'buy'
    order_type = 'limit'
    volume = 1
    price = 0.1
    expiry = 'sdt'

    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    trading_page.click_pending_orders_tab()
    initial_count = trading_page.get_pending_orders_count()
    initial_order_id = trading_page.get_pending_orders_order_id()
    initial_symbol = trading_page.get_pending_orders_symbol()
    
    # Place Buy Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume, price=price, expiry=expiry)
    
    # Verify the transaction details
    time.sleep(5) 
    new_count = trading_page.get_pending_orders_count()
    new_order_id = trading_page.get_pending_orders_order_id()
    assert new_count > initial_count, "Buy order did not result in a new open position"
    assert new_order_id != initial_order_id, "Buy order did not result in a new order ID"
    assert initial_symbol == trading_page.get_pending_orders_symbol(), "Symbol does not match"

# Test 15: Buy Stop Order Specified Date and Time
def test_buy_stop_order_sdt(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    buy_sell = 'buy'
    order_type = 'stop'
    volume = 1
    price = 1
    expiry = 'sdt'

    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    trading_page.click_pending_orders_tab()
    initial_count = trading_page.get_pending_orders_count()
    initial_order_id = trading_page.get_pending_orders_order_id()
    initial_symbol = trading_page.get_pending_orders_symbol()
    
    # Place Buy Order
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume, price=price, expiry=expiry)
    
    # Verify the transaction details
    time.sleep(5) 
    new_count = trading_page.get_pending_orders_count()
    new_order_id = trading_page.get_pending_orders_order_id()
    assert new_count > initial_count, "Buy order did not result in a new open position"
    assert new_order_id != initial_order_id, "Buy order did not result in a new order ID"
    assert initial_symbol == trading_page.get_pending_orders_symbol(), "Symbol does not match"

# Test 16: Edit Buy Limit Order
def test_edit_buy_limit_order(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)
    
    buy_sell = 'buy'
    order_type = 'limit'
    volume = 1
    price = 0.1
    expiry = 'gtc'
    sl = "{:.5f}".format(0.00005) # Format as string to avoid scientific notation
    tp = 5

    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    trading_page.buy_sell_order(buy_sell=buy_sell, order_type=order_type, volume=volume, price=price, expiry=expiry)
    time.sleep(1)
    trading_page.click_pending_orders_tab()
    time.sleep(3)
    trading_page.edit_pending_order(sl=sl, tp=tp)
    time.sleep(5)
    assert trading_page.get_pending_orders_sl() == str(sl), "SL does not match"
    assert trading_page.get_pending_orders_tp() == "{:.5f}".format(tp), "TP does not match"


# Test 17: Bulk Close All Position
def test_bulk_close_all_position(login_to_trade):
    driver = login_to_trade
    trading_page = TradingPage(driver)

    position = 'position'
    option = 'all'
    
    assert trading_page.is_loaded(), "Trading page not loaded"
    
    time.sleep(3)
    trading_page.bulk_close(position, option)
    time.sleep(10)
    assert trading_page.get_open_positions_count() == 0, "Bulk close all position failed"