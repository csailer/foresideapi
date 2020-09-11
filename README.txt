THIS PROJECT WAS BUILT AND TESTED ON MAC OS. IT WAS NOT TESTED ON Windows.

Unzip the provided project zip file.
From a terminal, CD into the directory where the project zip file was extracted.

Create a Virtual Environment for the API (see https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html for details)
    (You can also use another Virtual Environment package but this project was tested with Virtualenvwrapper)
To install the virtualenvwrapper and create a virtual environment, from the terminal
pip install virtualenvwrapper

 -- $ mkvirtualenv -p $(which python3.7) foreside --

Make sure to specify Python 3 with the -p switch. This project was built against Python 3.7

From the terminal, Switch to the virtual environment just created:
-- $ workon forside --

Now that the virtual environment is installed and you are in the working directory (the directory in which you extracted the project .zip file)
Again, from the terminal, run

-- $ . install.sh ---

This will do the basic set up for the project and start a webserver running at http://localhost:8000

Open http://localhost:8000 in your browser.

You will land on the Swagger page for the API. This is where you can interact with the API.

Start by expanding GET /orders/
    Click on the "Try it Out" button
    Then click: Execute
    You should see a JSON representation of 2 Orders and their Status.
    These orders were created in the install.sh ran earlier.


The design, roughly

The project is a single Django Project containing the Models, the REST API, and an Admin UI for editing Users and Groups (Roles).
Obviously, a real project would separate these functional areas by concern.

The main folder structure:

 foreside/ - This is the root folder of the project
    api/ - this package is for all REST API logic including serializers, policies and views
    config/ - the package holds configuration, url, and wsgi files. The settings files are structured
              to have a base, local, and test. base has the standard, generic settings and both local and test
              include the base settings files to have access for those generic settings. local and test settings
              file extend the base settings file with settings unique to their environment.
    orders/ - this package contains Order related models, migrations for Orders, and management commands.
              There are 2 Models for Orders:
                    Order
                    OrderStatus
               the Order Model manages price, qty, ticker, etc. While the OrderStatus holds the status and reason for the order.
               The desicion to create a one-to-many with the Order/OrderStatus models was to ensure that the order could have a history
               of status changes. e.g. Who created the order, who approved the order, who rejected the order in a chronological way.
               A future feature would be to audit all changes to the order and store the audit data in a separate model/table.

               The sub folder tests contains a very simple unit test for the Order Model

    utils/ -   The utils folder holds various globally usefule information. For example, creating Orders, Users, and Roles for testing
               and initialization.

               The AuditableModel can be found in the models.py in this folder. The AuditableModel is an abstract class that has functionality
               to figure out and record who changed an Order or OrderStatus and the dates of creation and modification. Both Order and OrderStatus
               derive from an AuditableModel.


The API has Roles that limit functionality based on a user's access level.
The install.sh created 3 users:

Joe Trader    - Trader Role. He can Place a New Order, Edit an existing Order. He can edit ANY existing order.
                a needed improvement in a subsequent iteration of development may be to limit Joe Trade to only
                edit orders he created.

Joe Approver   - Approver Role. He can Approve or Reject an order but cannot create a new order.
Joe Admin      - Admin Role. He is a superuser who can create/edit orders and approve or reject orders.

Deleting orders is not allowed through the API for any Role.

Role Based Permissions

The Roles, Trade, Approver, and Admin are Django Groups. The groups (Roles) are not configured with permissions. Instead,
the Roles are controlled with Polices. This is the cleanest and most simple way I know of, probably not the only, to enforce
access while retaining flexiblity to define knew Roles and expand or contract a particular Role's access. The policies work
by mapping roles to methods.

 Order Policy

        {
            "action": ["list", "retrieve"],
            "principal": "*",
            "effect": "allow"
        },
        {
            "action": ["create"],
            "principal": ["group:Trader", "group:Admin"],
            "effect": "allow"
        },
        {
            "action": ["update"],
            "principal": ["group:Trader", "group:Admin"],
            "effect": "allow"
        }

  In this policy, everyone can list all and retrieve individual Orders. Only Traders and Admins can create orders.
  And only Traders and Admins may edit orders.

 Order Status Policy

        {
            "action": ["list", "retrieve"],
            "principal": "*",
            "effect": "allow"
        },
        {
            "action": ["create", "update"],
            "principal": ["group:Approver", "group:Admin"],
            "effect": "allow"
        }

    In this Policy, everyone can list all and retrieve individual Orders Status. Only Approvers and Admin
    may create or update an Order Status. (The Trader creates an Order Status as part of creating a new Order.
    this is done automatically as part of the logic to create an Order.)

