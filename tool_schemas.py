TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "crawl_website",
            "description": (
                "Crawl a website using OWASP ZAP's "
                "Traditional Spider and return discovered URLs."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The website URL to crawl."
                    }
                },
                "required": ["url"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "discover_get_parameters",
            "description": (
                "Discover accepted GET query parameters "
                "on an HTTP endpoint using Arjun."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The endpoint URL to analyze."
                    }
                },
                "required": ["url"],
                "additionalProperties": False
            }
        }
    }
]