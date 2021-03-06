# Welcome to ColdScoop's Ice Cream Store

[![Build Status](https://app.travis-ci.com/ColdScoop/ice-cream-store.svg?branch=main)](https://app.travis-ci.com/ColdScoop/ice-cream-store)

## Big Picture
Sellers: users who want to sell their ice cream on our platform

Buyers: users who want to buy their ice cream from sellers on the platform


## Requirements
- CREATE
  - Sellers can create new ice cream menu options
    - default cost of ice cream option is $0 unless specified when listing is created
  - New users (sellers and customers)
    - default account created is a Buyer/customer account
  - Logins information for users
- READ
  - Buyers read menu items, pricing, shopping cart
  - Sellers read a list of orders
- UPDATE
  - Sellers update quantity
  - Sellers update cost of ice cream listed
  - Users can add items to Shopping Cart
  - Users can edit quantity of each item in Shopping Cart
  - User billing information and address
- DELETE
  - Sellers remove their menus items from listing
  - Users remove items from Shopping Cart

## Design 

- Handle each major requirement with an API endpoint
  - /create_user parameters: Seller or Customer
  - /create_new_item
  - /update_item_status
  - /create_orders
  - /list_ice_creams
  - /update_cart parameters: itemID, quantity
  - /update_order_status

- Utilize Test-Driven-Development (TDD) to create 
- Use Swagger for initial interaction with server.
- Use Swagger, pydoc and good docstrings for documentation.

## Setup

- To build production, type `make prod`.
- To create the env for a new developer, run `make dev_env`.
