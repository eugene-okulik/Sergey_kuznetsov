import json
from playwright.sync_api import Page, expect, Route


def test_iphone_page(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]['familyTypes'][0]["productName"] = 'яблокофон 17 про'
        body = json.dumps(body)

        route.fulfill(
            response=response,
            body=body,
        )

    page.route("**/digital-mat**", handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role('heading', name="iPhone 17 Pro & iPhone 17 Pro Max").click()
    modal = page.get_by_role('dialog')
    expect(modal).to_be_visible()
    head_text = modal.get_by_role('heading', name='яблокофон 17 про')
    expect(head_text).to_contain_text('яблокофон 17 про')
