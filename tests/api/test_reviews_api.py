import pytest
import requests
from typing import Dict, Any

class TestSearchAPI:
    BASE_URL = "https://judge.me/search.json"
    
    @pytest.fixture
    def base_params(self) -> Dict[str, Any]:
        """Default search parameters"""
        return {
            "q": "",
            "page": 1,
            "sort_by": "reviews_count",
            "category_id": 207,
            "country": "ES",
            "store_country": "*",
            "min_rating": 0,
            "min_transparency": 80,
            "min_authenticity": 0,
            "currency": "BSD",
            "reviews_count": 0,
            "category_search": True
        }

    def make_search_request(self, params: Dict[str, Any]) -> requests.Response:
        """Helper method to make search requests"""
        return requests.get(self.BASE_URL, params=params)

    @pytest.mark.api
    def test_basic_search_response_structure(self, base_params):
        """Test the basic structure of search response"""
        response = self.make_search_request(base_params)
        
        assert response.status_code == 200
        data = response.json()
        
        # Verify response structure
        assert "meta_data" in data
        assert "data" in data
        assert "search_results" in data["data"]
        
        # Verify meta_data fields
        assert "page_title" in data["meta_data"]
        assert "page_description" in data["meta_data"]

    @pytest.mark.api
    def test_search_results_product_fields(self, base_params):
        """Test that each product in search results has required fields"""
        response = self.make_search_request(base_params)
        data = response.json()

        required_fields = [
            "title", "snippet", "user_friendly_url", "href", "shop_name",
            "image_url", "number_of_reviews", "average_rating",
            "product_metrics"
        ]

        for product in data["data"]["search_results"]:
            for field in required_fields:
                assert field in product, f"Field {field} missing in product"

            # Verify product metrics structure
            assert "transparency_score" in product["product_metrics"]
            assert "authenticity_score" in product["product_metrics"]

    @pytest.mark.api
    def test_pagination(self, base_params):
        """Test pagination functionality"""
        # Test first page
        first_page = self.make_search_request(base_params)
        first_page_data = first_page.json()

        # Test second page
        base_params["page"] = 2
        second_page = self.make_search_request(base_params)
        second_page_data = second_page.json()

        # Verify different results
        first_page_titles = [p["title"] for p in first_page_data["data"]["search_results"]]
        second_page_titles = [p["title"] for p in second_page_data["data"]["search_results"]]

        assert first_page_titles != second_page_titles, "Pagination not working - same results on different pages"

    @pytest.mark.api
    def test_sorting_by_reviews_count(self, base_params):
        """Test sorting by reviews count"""
        response = self.make_search_request(base_params)
        data = response.json()

        review_counts = [p["number_of_reviews"] for p in data["data"]["search_results"]]
        assert review_counts == sorted(review_counts, reverse=True), "Results not properly sorted by review count"

    @pytest.mark.api
    def test_min_rating_filter(self, base_params):
        """Test minimum rating filter"""
        base_params["min_rating"] = 4
        response = self.make_search_request(base_params)
        data = response.json()

        for product in data["data"]["search_results"]:
            assert product["average_rating"] >= 4, "Product rating below minimum threshold"

    @pytest.mark.api
    def test_transparency_score_filter(self, base_params):
        """Test minimum transparency score filter"""
        base_params["min_transparency"] = 85
        response = self.make_search_request(base_params)
        data = response.json()

        for product in data["data"]["search_results"]:
            transparency = product["product_metrics"]["transparency_score"] * 100
            assert transparency >= 85, "Product transparency score below minimum threshold"

    @pytest.mark.api
    def test_invalid_parameters(self):
        """Test handling of invalid parameters"""
        invalid_params = {
            "page": "invalid",
            "min_rating": "invalid",
            "category_id": "invalid"
        }

        response = self.make_search_request(invalid_params)
        assert response.status_code in [400, 422], "Invalid parameters not properly handled"

    @pytest.mark.api
    @pytest.mark.parametrize("country", ["US", "GB", "CA", "AU"])
    def test_different_countries(self, base_params, country):
        """Test search results for different countries"""
        base_params["country"] = country
        response = self.make_search_request(base_params)

        assert response.status_code == 200
        data = response.json()
        assert len(data["data"]["search_results"]) > 0, f"No results found for country {country}"
