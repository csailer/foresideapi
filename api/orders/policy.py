from rest_access_policy import AccessPolicy


class OrderAccessPolicy(AccessPolicy):
    statements = [
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
    ]


class OrderStatusAccessPolicy(AccessPolicy):
    statements = [
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
    ]
