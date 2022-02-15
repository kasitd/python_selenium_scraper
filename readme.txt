Landing on first page, navigating with Selenium to search with:
keyword: python
job type: remote, hybrid
listing time: last 2 weeks
level: entry and junior

questions to answer:
1. What languages other than python are needed?
2. What job titles?
3. What cities?
4. Is there a salary listed?
5. What projects are recruited for?
6. What technologies are used?
7. Do I need employer names


Methodology:
Selenium for navigating website
Beautiful soup for parsing data
Cleaning data using scripts
Statictics performed with NumPy
Wisualisation with JupyterNotebook.

need to add better csv
can I speed up BS? sprzwdzić SoupStrainer
w collectData
    def strain_soup(self):
        return SoupStrainer('div', {'class': 'OfferViewgl652f'})

    def make_soup(self, res):
        return BeautifulSoup(res.content, 'lxml', parse_only=self.strain_soup())

 strain = SoupStrainer('div', {'class': 'OfferViewgl652f'})
    soup = BeautifulSoup(text, 'html.parser', parse_only=strain)
    #offer = JobOffer(DataCollection().get_offer(soup))

    offer_dict = await create_offer_dict(soup)