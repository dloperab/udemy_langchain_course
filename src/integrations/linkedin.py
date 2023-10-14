import os
import requests


def scrape_profile(linkedin_profile_url: str, mock_data: False):
    """Scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock_data:
        api_endpoint = "https://gist.githubusercontent.com/dloperab/e4fa62503ade5e53daa02cc44125c17f/raw/075090616ef475fc6c063afbc0a07552a2e3c93a/eden-marco-linkedin.json"
        response = requests.get(api_endpoint)
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

        response = requests.get(
            api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
        )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
