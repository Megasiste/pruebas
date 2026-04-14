# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies

{
    "name": "Add To Cart Ajax & Multiples Quantity Option At Shop Product List",
    "author": "Softhealer Technologies",
    "support": "support@softhealer.com",
    "website": "https://www.softhealer.com",
    "category": "Website",
    "summary": "Website Multiples Product Quantity, Multiple Quantity, Multiples qty on shop, multi product qty website, Ajax Shop Cart, Add Product To Cart, Cart Without Page Reload, Add To Cart Window In Shop, Ajax Website Cart Odoo",
    "description": """Do you want the product multiples QTY option in the product list view(shop page)? This module helps the customer to add an item in the cart (Ajax) with a multiples quantity option in the product list view(shop page). Suppose you want to set multiples of quantity is 5, it will default the value of the product in the shop. If customers put manual quantity (manually = 8)of the product so it will automatically take higher No of quantity(higher = 10). Customers can decrease the number of products relative to default quantity(default is 5) in the shop or cart. If the customer click button "Add to Cart" in the shop, the product quantity automatically sets the default quantity. You can enable/disable the QTY selection option at product list view page. customers can quickly add items in the cart without loading in the cart page (AJAX).""",
    "version": "19.0.3.0.1",
    "depends": [
        "website_sale_stock", 'website_sale', "sale_management",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_views.xml",
        "views/res_config_settings_views.xml",
        "views/website_sale_templates.xml",
    ],

    "assets": {
        "web.assets_frontend": [
            "sh_qty_shop_ajax_moq/static/src/scss/sh_qty_shop_ajax_moq.scss",
            "sh_qty_shop_ajax_moq/static/src/js/website_sale.js",
            "sh_qty_shop_ajax_moq/static/src/js/cart_line.js",
            "sh_qty_shop_ajax_moq/static/src/js/product_configurator_dialog/product_configurator_dialog.js",
            "sh_qty_shop_ajax_moq/static/src/js/product/product.xml",
            "sh_qty_shop_ajax_moq/static/src/js/quantity_buttons/quantity_buttons.js",
        ],
        'website.website_builder_assets': [
            'sh_qty_shop_ajax_moq/static/src/xml/website_sale_editor_options.xml'
        ],
    },
    "images": ["static/description/background.png", ],
    "license": "OPL-1",
    "auto_install": False,
    "application": True,
    "installable": True,
    "price": 51,
    "currency": "EUR",
}
