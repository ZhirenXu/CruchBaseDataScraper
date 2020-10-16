def getRequestBody():
    requestBody ={
    "field_ids": [
        "acquirer_identifier",
        "aliases",
        "categories",
        "category_groups",
        "closed_on",
        "company_type",
        "contact_email",
        "created_at",
        "delisted_on",
        "demo_days",
        "description",
        "diversity_spotlights",
        "entity_def_id",
        "equity_funding_total",
        "exited_on",
        "facebook",
        "facet_ids",
        "founded_on",
        "founder_identifiers",
        "funding_stage",
        "funding_total",
        "funds_total",
        "hub_tags",
        "investor_identifiers",
        "investor_stage",
        "investor_type",
        "ipo_status",
        "last_equity_funding_total",
        "last_equity_funding_type",
        "last_funding_at",
        "last_funding_total",
        "last_funding_type",
        "layout_id",
        "legal_name",
        "linkedin",
        "listed_stock_symbol",
        "location_group_identifiers",
        "location_identifiers",
        "name",
        "num_acquisitions",
        "num_alumni",
        "num_articles",
        "num_current_advisor_positions",
        "num_current_positions",
        "num_diversity_spotlight_investments",
        "num_employees_enum",
        "num_enrollments",
        "num_event_appearances",
        "num_exits",
        "num_exits_ipo",
        "num_founder_alumni",
        "num_founders",
        "num_funding_rounds",
        "num_funds",
        "num_investments",
        "num_investors",
        "num_lead_investments",
        "num_lead_investors",
        "num_past_positions",
        "num_portfolio_organizations",
        "num_sub_organizations",
        "operating_status",
        "override_layout_id",
        "owner_identifier",
        "permalink",
        "permalink_aliases",
        "phone_number",
        "program_application_deadline",
        "program_duration",
        "program_type",
        "rank_delta_d30",
        "rank_delta_d7",
        "rank_delta_d90",
        "rank_org",
        "rank_principal",
        "revenue_range",
        "school_method",
        "school_program",
        "short_description",
        "status",
        "stock_exchange_symbol",
        "stock_symbol",
        "twitter",
        "updated_at",
        "uuid",
        "valuation",
        "valuation_date",
        "website",
        "website_url",
        "went_public_on"
    ],
    "order": [
        {
            "field_id": "created_at",
            "sort": "asc"
        }
    ],
    "query": [
        {
            "type": "predicate",
            "field_id": "categories",
            "operator_id": "includes_all",
            "values": ["b37dbaeb-c825-e6a0-36de-84556a5d2e1f", "c08b5441-a05b-9777-b7a6-012728caddd9"]
        },
        {
            "type": "predicate",
            "field_id": "facet_ids",
            "operator_id": "includes",
            "values": ["company"]
        },
        {
            "type": "predicate",
            "field_id": "founded_on",
            "operator_id": "gte",
            "values": ["2018"]
        }
    ],
    "limit": 1000
    }

    return requestBody

def getRequestUrl():
    url = "https://api.crunchbase.com/api/v4/searches/organizations?user_key=d1be01f70bca47e9530407e05dca75a8"

    return url
