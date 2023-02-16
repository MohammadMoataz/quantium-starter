from dash.testing.application_runners import import_app

def test_dash_app(dash_duo):
    app = import_app("dash_test.app")
    dash_duo.start_server(app)

    # 1. Ensuring the header is present
    dash_duo.wait_for_text_to_equal(
        '#header', "Impact of pink morsel's price increase on overall sales.")
    
    # 2. Ensuring the visualiser is present
    dash_duo.percy_snapshot('test_dash_app-layout')

    # 3. Ensuring the region buttons are present
    dash_duo.wait_for_element_by_id('regions')

    # 4. Ensuring browser console doesn't contain errors
    assert dash_duo.get_logs() == []