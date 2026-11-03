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
    },
    {
        "type": "function",
        "function": {
            "name": "test_sql_injection",
            "description": (
                "Test an HTTP parameter for SQL injection using sqlmap. "
                "Return detection results."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "Target URL including query parameters."
                    },
                    "parameter": {
                        "type": "string",
                        "description": "Parameter name to test for SQL injection."
                    }
                },
                "required": ["url", "parameter"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "crawl_with_katana",
            "description": (
                "Discover website URLs using Katana, including "
                "JavaScript and headless browser crawling. "
                "Useful for modern single-page applications."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The target website URL to crawl."
                    }
                },
                "required": ["url"],
                "additionalProperties": False
            }
        }
    }
]